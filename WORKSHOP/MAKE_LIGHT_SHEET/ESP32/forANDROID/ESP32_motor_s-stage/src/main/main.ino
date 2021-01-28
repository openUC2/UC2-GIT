// ----------- ----------- ----------- ----------- ----------- -----------
// ESP32 script to accept MQTT commands for UC2-control
// by: Rene Lachmann
// date: 11.09.2019
// based on Arduino-Interface by Rene Lachmann, Xavier Uwurukundu
// for: S-Stage
//----------- ----------- ----------- ----------- ----------- -----------

// ----------------------------------------------------------------------------------------------------------------
//                          INCLUDES
#include <WiFi.h>
#include <PubSubClient.h>
#include <string.h>
#include <vector>
#include <StepMotor.h>
#include "driver/ledc.h"
#include <ctime>
#include <sstream>
// ----------------------------------------------------------------------------------------------------------------
//                          Global Defines
#define MAX_CMD 3
#define MAX_INST 10
#define NCOMMANDS 15
#define MAX_MSG_LEN 40
#define LED_BUILTIN 11
#define LED_FLUO_PIN 26

// ----------------------------------------------------------------------------------------------------------------
//                          Parameters
// ~~~~ Device ~~~~
// create Pseudo-random number with temporal dependent input

// saved in strings, so that later (if implemented) e.g. easily changeable via Bluetooth -> to avoid connection errors
std::string SETUP = "S009";
std::string COMPONENT = "MOT02"; // LAR01 //LED01 //
std::string DEVICE = "ESP32";
std::string DEVICENAME;
std::string CLIENTNAME;
std::string SETUP_INFO;

// ~~~~  Wifi  ~~~~
const char *ssid = "UC2_wifi004";// "Blynk";       //"Blynk";"UC2";
const char *password = "_lachmannUC2"; //"12345678";"youseetoo";
WiFiClient espClient;
PubSubClient client(espClient);

// ~~~~  MQTT  ~~~~
#define BUFLEN 16
String localIP;
String gatewayIP;
//char MQTT_SERVER[BUFLEN]; //const char *MQTT_SERVER = "192.168.178.21"; // 10.9.2.116
const char *MQTT_SERVER = "21.3.2.102"; // 10.9.2.116
const char *MQTT_CLIENTID;
const char *MQTT_USER;
const char *MQTT_PASS = "23SPE";
const int MQTT_SUBS_QOS = 0;
//const int MAX_CONN = 10; // maximum tries to connect
const unsigned long period = 80000; // 80s
unsigned long time_now = 0;
// topics to listen to
std::string stopicREC = "/" + SETUP + "/" + COMPONENT + "/RECM";
std::string stopicSTATUS = "/" + SETUP + "/" + COMPONENT + "/STAT";
std::string stopicANNOUNCE = "/" + SETUP + "/" + COMPONENT + "/ANNO";
// Deliminators for CMDs (published via payload-string)
const char *delim_inst = "+";
const int delim_len = 1;

// ~~~~ MOTOR ~~~~
StepMotor stepperZ = StepMotor(1,1,1,1);//25, 26, 27, 14); // for Peter Horbert
StepMotor stepperY = StepMotor(1,1,1,1);//10, 12, 11, 13);
StepMotor stepperX = StepMotor(14,27,26,25);//27, 25, 32, 4); // never connected to same ESP32 as stepperZ -> hence: universally possible

// ~~~~ FLUO ~~~~
int led_fluo_pwm_frequency = 12000;
int led_fluo_pwm_channel = 0;
int led_fluo_pwm_resolution = 8;

// ~~~~ Commands ~~~~
const char *CMD;     //Commands like: PXL -> limited to size of 3?
int *INST[MAX_INST]; //Maximum number of possible instructions =
std::vector<int> INSTS;
std::string CMDS;

const char *COMMANDSET[NCOMMANDS] = {"DRVX", "DRVY", "DRVZ", "FLUO"};
const char *INSTRUCTS[NCOMMANDS] = {"1", "1", "1", "1"};

// ~~~~ FLUO ~~~~
int FLUO_STATUS = 0;
// ----------------------------------------------------------------------------------------------------------------
//                          Additional Functions
// Most stable and efficient way to have the ESP32 be active for input, but still wait (best for Android as well)
void uc2wait(int period)
{
    unsigned long time_now = millis();
    while (millis() < time_now + period)
    {
        //wait approx. [period] ms
    };
}
// Random-string generation from: https://stackoverflow.com/a/12468109
/*std::string random_string(size_t length)
{
    auto randchar = []() -> char {
        const char charset[] =
            "0123456789"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz";
        const size_t max_index = (sizeof(charset) - 1);
        return charset[rand() % max_index];
    };
    std::string str(length, 0);
    std::generate_n(str.begin(), length, randchar);
    return str;
}*/

void setup_device_properties()
{
    //std::time_t result = std::time(nullptr);
    //srand(result); // init randomizer with pseudo-random seed on boot
    //int randnum = rand() % 10000;
    int rand_number = random(1, 100000);
    std::stringstream srn;
    srn << rand_number;
    DEVICENAME = DEVICE + "_" + srn.str(); // random number generated up to macro MAX_RAND
    CLIENTNAME = SETUP + "_" + COMPONENT + "_" + DEVICENAME;
    SETUP_INFO = "This is:" + DEVICENAME + " on /" + SETUP + "/" + COMPONENT + ".";
    MQTT_CLIENTID = DEVICENAME.c_str(); //"S1_MOT2_ESP32"
    //Serial.print("MQTT_CLIENTID=");Serial.println(MQTT_CLIENTID);
    MQTT_USER = DEVICE.c_str();
    Serial.println(SETUP_INFO.c_str());
}

void setup_wifi()
{
    uc2wait(10);
    // We start by connecting to a WiFi network
    Serial.println();
    Serial.print("Device-MAC: ");
    Serial.println(WiFi.macAddress());
    Serial.print("Connecting to ");
    Serial.print(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        uc2wait(500);
        Serial.print(".");
    }

    localIP = WiFi.localIP().toString();
    gatewayIP = WiFi.gatewayIP().toString();
    //gatewayIP.toCharArray(MQTT_SERVER, BUFLEN);
    
    Serial.println("");
    Serial.print("WiFi connected with IP:");
    Serial.println(localIP);
    Serial.print("Default Gateway (MQTT-SERVER):\t");
    Serial.println(MQTT_SERVER);
}

int separateMessage(byte *message, unsigned int length)
{

    //Serial.println("Seperating Message.");
    //Serial.print("Message=");
    char messageSep[length];
    for (int myc = 0; myc < length; myc++)
    {
        messageSep[myc] = (char)message[myc];
        //Serial.print(messageSep[myc]);
    }
    messageSep[length] = NULL;
    //Serial.println("");
    Serial.print("Mess=");
    std::string mess(messageSep);
    Serial.println(mess.c_str());
    size_t pos = 0;
    int i = 0;
    bool found_cmd = false;
    while ((pos = mess.find(delim_inst)) != std::string::npos)
    {
        if (!found_cmd)
        {
            //Serial.print("CMD-del@");
            //Serial.println(pos);
            CMDS = mess.substr(0, pos);
            //Serial.print("CMDS=");
            CMD = CMDS.c_str();
            //Serial.println(CMD);
            found_cmd = true;
        }
        else
        {
            INSTS.push_back(atoi(mess.substr(0, pos).c_str()));
            //Serial.print("INST[");
            //Serial.print(i);
            //Serial.print("]=");
            //Serial.println(INSTS[i]);
            i++;
        }
        mess.erase(0, pos + delim_len);
    }
    if (!found_cmd)
    {
        //Serial.print("CMD-del@");
        //Serial.println(pos);
        CMDS = mess.substr(0, pos);
        //Serial.print("CMDS=");
        CMD = CMDS.c_str();
        //Serial.println(CMD);
        found_cmd = true;
    }
    else if (mess.length() > 0)
    {
        INSTS.push_back(atoi(mess.substr(0, pos).c_str()));
        //Serial.print("INST[");
        //Serial.print(i);
        //Serial.print("]=");
        //Serial.println(INSTS[i]);
        i++;
    }
    else
    {
        Serial.println("Nothing found...");
    }
    return i;
    mess.clear();
}

void callback(char *topic, byte *message, unsigned int length)
{
    Serial.println("Callback-func called.");
    // test topics
    if (std::string(topic) == stopicREC)
    {
        //Serial.println(topicREC.c_str());
        int nINST = separateMessage(message, length);
        if (strcmp(CMD, COMMANDSET[0]) == 0)
        {
            stepperX.Move((int)(INSTS[0] * 10));
        }
        else if (strcmp(CMD, COMMANDSET[1]) == 0)
        {
            stepperY.Move((int)(INSTS[0] * 10));
        }
        else if (strcmp(CMD, COMMANDSET[2]) == 0)
        {
            stepperZ.Move(INSTS[0] * 10);
        }
        else if (strcmp(CMD, COMMANDSET[3]) == 0)
        {
            //analogWrite(FLUO_PIN, INSTS[0]);
            ledcWrite(led_fluo_pwm_channel, INSTS[0]);
        }
        else
        {
            Serial.print("CMD not found.");
        }
    }
    else if (std::string(topic) == stopicSTATUS)
    {
        Serial.println(stopicSTATUS.c_str());
    }
    else if (std::string(topic) == stopicANNOUNCE)
    {
        Serial.println(stopicANNOUNCE.c_str());
    }
    else
    {
        Serial.print("Assortion Error: Nothing found for topic=");
        Serial.println(topic);
    }
    INSTS.clear();
}

void reconnect()
{
    // Loop until we're reconnected
    while (!client.connected())
    {
        Serial.print("MQTT_CLIENTID=");
        Serial.println(MQTT_CLIENTID);
        Serial.print("topicSTATUS=");
        Serial.println(stopicSTATUS.c_str());
        Serial.print("Attempting MQTT connection...");
        // Attempt to connect

        if (client.connect(MQTT_CLIENTID, stopicSTATUS.c_str(), 2, 1, "0"))
        {
            // client.connect(MQTT_CLIENTID,MQTT_USER,MQTT_PASS,"esp32/on",2,1,"off")
            Serial.println("connected");
            // Subscribe
            client.subscribe(stopicREC.c_str());
            client.publish(stopicSTATUS.c_str(), "1");
            client.publish(stopicANNOUNCE.c_str(), SETUP_INFO.c_str());
        }
        else
        {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            // Wait 5 seconds before retrying
            uc2wait(5000);
        }
    }
}

// ----------------------------------------------------------------------------------------------------------------
//                          SETUP
void setup()
{
    Serial.begin(115200);
    // check for connected motors
    //status = bme.begin();
    setup_device_properties();
    Serial.print("VOID SETUP -> topicSTATUS=");
    Serial.println(stopicSTATUS.c_str());
    setup_wifi();
    client.setServer(MQTT_SERVER, 1883);
    client.setCallback(callback);
    pinMode(LED_BUILTIN, OUTPUT);
    time_now = millis();
    //testCPP();
    // ---> pinMode(LED_BUILTIN, OUTPUT);
    // ---> pinMode(LED_FLUO_PIN, OUTPUT);
    ledcSetup(led_fluo_pwm_channel, led_fluo_pwm_frequency, led_fluo_pwm_resolution);
    ledcAttachPin(LED_FLUO_PIN, led_fluo_pwm_channel);
    ledcWrite(led_fluo_pwm_channel, 20); //analogWrite(FLUO_PIN, 20);
    uc2wait(1000);
    ledcWrite(led_fluo_pwm_channel, 0); //analogWrite(FLUO_PIN, 0,0);
    uc2wait(100);
    stepperX.SetSpeed(10);
    stepperY.SetSpeed(10);
    stepperZ.SetSpeed(10);
}
// ----------------------------------------------------------------------------------------------------------------
//                          LOOP
void loop()
{
    if (!client.connected())
    {
        reconnect();
    }
    client.loop();
    if (time_now + period < millis())
    {
        client.publish(stopicSTATUS.c_str(), "1");
        time_now = millis();
    }
}
// ----------------------------------------------------------------------------------------------------------------
