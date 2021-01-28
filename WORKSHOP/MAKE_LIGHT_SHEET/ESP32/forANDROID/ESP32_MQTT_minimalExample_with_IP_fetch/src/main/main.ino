#include <Arduino.h>
#include <WiFi.h>
#include <HardwareSerial.h>
#include <PubSubClient.h>
#include <time.h>

#define GMT_OFFSET_CET 3600
#define CEST_OFFSET 3600
#define BAUDRATE 115200
#define BUFLEN 16
#define MQTT_USER "UC2_USER"
#define MQTT_PASSWORD "YOUSEETOO_PASSWORD"
#define LED_BUILTIN 2

const char* SSID = "Blynk";
const char* PASSWORD = "12345678";
const char* NTP_SERVER = "de.pool.ntp.org";
const int MQTT_PORT = 1883;
unsigned long RECONNECT_DELAY = 2000;

int n_blinks = 1;
unsigned long delta_t = 0;
unsigned long reconnectTimer = 0;
unsigned long confirmTimer = 0;

String localIP;
String gatewayIP;
struct tm timeinfo;

WiFiClient espClient;
PubSubClient mqttClient(espClient);

String clientID = "ESP32";
char MQTT_SERVER[BUFLEN];
long lastMsg = 0;
char msg[50];
int value = 0;

bool updateTime(){
  return getLocalTime(&timeinfo);
}

void printLocalTime()
{
  if(updateTime()){
    Serial.print(&timeinfo, "\n%d-%m-%Y %H:%M:%S\t\t");
  }
}

void callback(char* topic, byte* message, unsigned int length) {
  printLocalTime();
  Serial.print(topic);
  Serial.print(":\t");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
}

bool WiFiConnected(){ 
  bool connect = (WiFi.status() == WL_CONNECTED);
  if (!connect){
    digitalWrite(LED_BUILTIN, LOW);
    printLocalTime();
    Serial.print("Lost connection! Reconnecting in ");
    Serial.print(RECONNECT_DELAY/1000);
    Serial.print(" seconds...");
    delay(RECONNECT_DELAY);
  }
  return connect;
}

void setupMQTT(){
  mqttClient.setServer(MQTT_SERVER, 1883);
  mqttClient.setCallback(callback);
}

void reconnectMQTT(){
  if (WiFiConnected())
  {
    printLocalTime();
    if (mqttClient.connect(clientID.c_str(), MQTT_USER, MQTT_PASSWORD))
    {
      Serial.print("Connected to MQTT-Server.");
      mqttClient.subscribe("esp32/output");
      confirmTimer = millis();
    } 
    else {
      Serial.print("\t\t\t\tFailed to connect to MQTT-Server ");
      Serial.print("(rc=");
      Serial.print(mqttClient.state());
      Serial.print("). Trying again in 5 seconds...");
      reconnectTimer = millis();
    }
  }
}

void setupWiFi(){
  Serial.print("\nConnecting to WiFi-network ");
  Serial.print(SSID);
  WiFi.begin(SSID, PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  digitalWrite(LED_BUILTIN, HIGH); 
  configTime(GMT_OFFSET_CET, CEST_OFFSET, NTP_SERVER);

  localIP = WiFi.localIP().toString();
  gatewayIP = WiFi.gatewayIP().toString();
  gatewayIP.toCharArray(MQTT_SERVER, BUFLEN);

  printLocalTime();
  Serial.println("Connection established!");
  Serial.print("IP Address:\t\t\t");
  Serial.println(localIP);
  Serial.print("Default Gateway (MQTT-SERVER):\t");
  Serial.println(MQTT_SERVER);

}

void setup() {
  Serial.begin(BAUDRATE);
  pinMode(LED_BUILTIN, OUTPUT);
  setupWiFi();
  setupMQTT();
}

void loop() {

  if (!WiFiConnected()){
    esp_restart();
  }
  else{
    delta_t = millis() - reconnectTimer;
    if (!mqttClient.connected() && (delta_t > RECONNECT_DELAY))
    {
      Serial.print("\nConnecting to MQTT-Server...");
      reconnectMQTT();
    }
    mqttClient.loop();
  }

  delta_t = millis() - confirmTimer;
  if(delta_t < RECONNECT_DELAY){
    n_blinks = delta_t / 250;
    digitalWrite(LED_BUILTIN, (n_blinks % 2 == 0));
  }
  else if(n_blinks != 0)
  {
    digitalWrite(LED_BUILTIN, WiFi.status() == WL_CONNECTED);
    n_blinks = 0;
  }
}
