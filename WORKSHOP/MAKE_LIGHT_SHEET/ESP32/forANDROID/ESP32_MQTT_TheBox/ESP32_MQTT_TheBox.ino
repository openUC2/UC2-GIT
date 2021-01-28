/* Here ESP32 will keep 2 roles:
  1/ read data from DHT11/DHT22 sensor
  2/ control led on-off
  So it willpublish temperature topic and scribe topic bulb on/off
*/

#include <WiFi.h>
#include <PubSubClient.h>
#include <Stepper.h>
#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>


// Define a unique setup number
String setup_id = "4";
#define IS_Z_STAGE 1 // either it's the s- or the z-stage


/* change it with your ssid-password */
const char* ssid = "GUEST_JRC";//"Blynk";"UC2";//
const char* password = "HHMI@Newton"; //"youseetoo";//
/* this is the IP of PC/raspberry where you installed MQTT Server
  on Wins use "ipconfig"
  on Linux use "ifconfig" to get its IP address */
const char* mqtt_server = "10.9.1.62";//"192.168.43.151";//"10.9.1.62";//"192.168.43.88";
String CLIENT_ID = "ESP32Client" + String(random(0xffff), HEX);


/* create an instance of PubSubClient client */
WiFiClient espClient;
PubSubClient client(espClient);

/* Define the pins for the components*/
int LED_MATRIX_PIN = 22;
int LED_FLUO_PIN = 26;


// don't listen to the wrong signal! 
#if IS_Z_STAGE == 1
  int z_stage_pin[] = {27, 25, 32, 4}; //
  int s_stage_pin[] = {100, 100, 100, 100};
#else
  int s_stage_pin[] = {27, 25, 32, 4}; //
  int z_stage_pin[] = {100, 100, 100, 100};
#endif


///* topics - DON'T FORGET TO REGISTER THEM! */
String TOPIC_S_STAGE_SVAL_BWD = "uc2/microscope/" + setup_id + "/sstage/bwd/sval";
String TOPIC_S_STAGE_SVAL_FWD = "uc2/microscope/" + setup_id + "/sstage/fwd/sval";
String TOPIC_LED_FLUO = "uc2/microscope/" + setup_id + "/zstage/ledval";
String TOPIC_LED_MATRIX_VAL = "uc2/microscope/" + setup_id + "/ledmatrix/ledval";
String TOPIC_Z_STAGE_ZVAL_BWD = "uc2/microscope/" + setup_id + "/zstage/bwd/zval";
String TOPIC_Z_STAGE_ZVAL_FWD = "uc2/microscope/" + setup_id + "/zstage/fwd/zval";

// default values for x/z lens' positions
int led_fluo_int = 0;
int z_stage_val = 0;
int led_matrix_na = 0;
int s_stage_val = 0;

// Motor related
int highSpeed = 1000;

// PWM Stuff
int pwm_resolution = 15;
int pwm_frequency = 800000;//19000; //12000

// lens x-channel
int PWM_CHANNEL_LED_FLUO = 0;

// MQTT Stuff
long lastMsg = 0;
char msg[20];

// Matrix Related
Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, LED_MATRIX_PIN,
                            NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
                            NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
                            NEO_GRB            + NEO_KHZ400);
int max_intensity_matrix = 125;


void setup() {

  // MOTOR
  pinMode(s_stage_pin[0], OUTPUT);
  pinMode(s_stage_pin[1], OUTPUT);
  pinMode(s_stage_pin[2], OUTPUT);
  pinMode(s_stage_pin[3], OUTPUT);

  pinMode(z_stage_pin[0], OUTPUT);
  pinMode(z_stage_pin[1], OUTPUT);
  pinMode(z_stage_pin[2], OUTPUT);
  pinMode(z_stage_pin[3], OUTPUT);

  /* set led and laser as output to control led on-off */
  pinMode(LED_MATRIX_PIN, OUTPUT);
  pinMode(LED_FLUO_PIN, OUTPUT);
  matrix.begin();


  /* setup the PWM ports and reset them to 0*/
  ledcSetup(PWM_CHANNEL_LED_FLUO, pwm_frequency, pwm_resolution);
  ledcAttachPin(LED_FLUO_PIN, PWM_CHANNEL_LED_FLUO);
  ledcWrite(PWM_CHANNEL_LED_FLUO, 0);

  // Debug Matrix
  LED_NA3();
  delay(1000);
  LED_NA0();

  // Visualize, that ESP is on!
  ledcWrite(PWM_CHANNEL_LED_FLUO, 1000);
  //digitalWrite(LED_FLUO_PIN, HIGH);
  delay(1000);
  ledcWrite(PWM_CHANNEL_LED_FLUO, 0);
  //digitalWrite(LED_FLUO_PIN, LOW);



  Serial.begin(115200);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  Serial.print("I am setup #: ");
  Serial.println(setup_id);


  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }


  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("MAC address:");
  Serial.println(WiFi.macAddress());

  /* configure the MQTT server with IPaddress and port */
  client.setServer(mqtt_server, 1883);
  /* this receivedCallback function will be invoked
    when client received subscribed topic */
  client.setCallback(receivedCallback);


}

void loop() {
  /* if client was disconnected then try to reconnect again */
  if (!client.connected()) {
    mqttconnect();
  }
  /* this function will listen for incomming
    subscribed topic-process-invoke receivedCallback */
  client.loop();

}




void receivedCallback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received: ");
  Serial.println(topic);

  // Convert pointer to int
  int payload_int = 0;
  for (int i = 0; i < length; i++) {
    char c = payload[i];
    if (c >= '0' && c <= '9')
      payload_int = payload_int * 10 + c - '0'; //einzelne Ziffern zu einem Integer zusammenfügen
    else {
      Serial.print ((int)c);
      Serial.println(" war so nicht erwartet");
    }
  }

  Serial.print("Value is : [");
  Serial.print(payload_int);
  Serial.println("]");


  // Catch the value for movement of lens in X-direction (right)
  if (String(topic) == TOPIC_LED_FLUO) {
    //dacWrite(25, (int)payload_int);
    led_fluo_int = abs((int)round(payload_int / 10));
    ledcWrite(PWM_CHANNEL_LED_FLUO, led_fluo_int);
    Serial.print("Fluo Intensity is set to: ");
    Serial.print(led_fluo_int);
    Serial.println();
  }

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == TOPIC_Z_STAGE_ZVAL_BWD) {
    // Drive motor X in positive direction
    z_stage_val = ((int)payload_int);
    drive_left(highSpeed, z_stage_pin, abs(z_stage_val) * 10);
    stop(z_stage_pin);
    Serial.print("Z-Stage Motor is running for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }


  // Catch the value for stepment of lens in X-direction
  if (String(topic) == TOPIC_Z_STAGE_ZVAL_FWD) {
    // Drive motor X in positive direction
    z_stage_val = ((int)payload_int);
    drive_right(highSpeed, z_stage_pin, abs(z_stage_val) * 10);
    stop(z_stage_pin);
    Serial.print("Z-Stage Motor is running for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }




  // Catch the value for stepment of lens in X-direction
  if (String(topic) == TOPIC_S_STAGE_SVAL_FWD) {
    // Drive motor X in positive direction
    s_stage_val = ((int)payload_int);

    drive_left(highSpeed, s_stage_pin, abs(s_stage_val) * 10);
    stop(s_stage_pin);
    Serial.print("S-Stage Motor is running for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == TOPIC_S_STAGE_SVAL_BWD) {
    // Drive motor X in positive direction
    s_stage_val = ((int)payload_int);

    drive_right(highSpeed, s_stage_pin, abs(s_stage_val) * 10);
    stop(s_stage_pin);
    Serial.print("S-Stage Motor is running for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }


  // Catch the value for movement of lens in X-direction (right)
  if (String(topic) == TOPIC_LED_MATRIX_VAL) {
    //dacWrite(25, (int)payload_int);
    led_matrix_na = abs((int)payload_int);
    if (led_matrix_na == 0) LED_NA0();
    if (led_matrix_na == 1) LED_NA1();
    if (led_matrix_na == 2) LED_NA2();
    if (led_matrix_na == 3) LED_NA3();
    if (led_matrix_na == 4) LED_NA4();

    Serial.print("NA is set to: ");
    Serial.print(led_matrix_na);
    Serial.println();
  }


}

void mqttconnect() {
  /* Loop until reconnected */
  while (!client.connected()) {
    Serial.print("MQTT connecting ...");

    /* connect now */
    if (client.connect(CLIENT_ID.c_str())) {//if (client.connect(clientId.c_str(), "username", "pi")) {
      Serial.println("connected");
      /* subscribe topic with default QoS 0*/
      client.subscribe(TOPIC_S_STAGE_SVAL_FWD.c_str());
      client.subscribe(TOPIC_S_STAGE_SVAL_BWD.c_str());
      client.subscribe(TOPIC_LED_FLUO.c_str());
      client.subscribe(TOPIC_LED_MATRIX_VAL.c_str());
      client.subscribe(TOPIC_Z_STAGE_ZVAL_FWD.c_str());
      client.subscribe(TOPIC_Z_STAGE_ZVAL_BWD.c_str());

    } else {
      Serial.print("faiLED_MATRIX_PIN, status code =");
      Serial.print(client.state());
      Serial.println("try again in 5 seconds");
      /* Wait 5 seconds before retrying */
      delay(5000);
    }
  }
}








void drive_right(unsigned int motorSpeed, int motorPin[], int steps)
{ // 1

  int motorPin1 = motorPin[0];
  int motorPin2 = motorPin[1];
  int motorPin3 = motorPin[2];
  int motorPin4 = motorPin[3];

  for (int i = 0; i < steps; i++)
  {
    digitalWrite(motorPin4, HIGH);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin1, LOW);
    delayMicroseconds(motorSpeed);

    // 2
    digitalWrite(motorPin4, HIGH);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin1, LOW);
    delayMicroseconds(motorSpeed);

    // 3
    digitalWrite(motorPin4, LOW);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin1, LOW);
    delayMicroseconds(motorSpeed);

    // 4
    digitalWrite(motorPin4, LOW);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin1, LOW);
    delayMicroseconds(motorSpeed);

    // 5
    digitalWrite(motorPin4, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin1, LOW);
    delayMicroseconds(motorSpeed);

    // 6
    digitalWrite(motorPin4, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin1, HIGH);
    delayMicroseconds(motorSpeed);

    // 7
    digitalWrite(motorPin4, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin1, HIGH);
    delayMicroseconds(motorSpeed);

    // 8
    digitalWrite(motorPin4, HIGH);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin1, HIGH);
    delayMicroseconds(motorSpeed);
  }
}

void drive_left(unsigned int motorSpeed, int motorPin[], int steps)
{ // 1

  int motorPin1 = motorPin[0];
  int motorPin2 = motorPin[1];
  int motorPin3 = motorPin[2];
  int motorPin4 = motorPin[3];

  for (int i = 0; i < steps; i++)
  {
    // 1
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    delayMicroseconds(motorSpeed);

    // 2
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    delayMicroseconds(motorSpeed);

    // 3
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    delayMicroseconds(motorSpeed);

    // 4
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, LOW);
    delayMicroseconds(motorSpeed);

    // 5
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, LOW);
    delayMicroseconds(motorSpeed);

    // 6
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, HIGH);
    delayMicroseconds(motorSpeed);

    // 7
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, HIGH);
    delayMicroseconds(motorSpeed);

    // 8
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, HIGH);
    delayMicroseconds(motorSpeed);
  }
}


void stop(int motorPin[])
{
  int motorPin1 = motorPin[0];
  int motorPin2 = motorPin[1];
  int motorPin3 = motorPin[2];
  int motorPin4 = motorPin[3];

  digitalWrite(motorPin4, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin1, LOW);
}


void LED_NA0() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };

  drawPattern(logo);
}

void LED_NA1() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 1, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };

  drawPattern(logo);
}

void LED_NA2() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 1, 0, 0, 0},
    {0, 0, 0, 1, 1, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };

  drawPattern(logo);
}


void LED_NA3() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 1, 1, 1, 0, 0},
    {0, 0, 1, 1, 1, 1, 0, 0},
    {0, 0, 1, 1, 1, 1, 0, 0},
    {0, 0, 1, 1, 1, 1, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };

  drawPattern(logo);
}


void LED_NA4() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 1, 1, 1, 1, 1, 1, 0},
    {0, 1, 1, 1, 1, 1, 1, 0},
    {0, 1, 1, 1, 1, 1, 1, 0},
    {0, 1, 1, 1, 1, 1, 1, 0},
    {0, 1, 1, 1, 1, 1, 1, 0},
    {0, 1, 1, 1, 1, 1, 1, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
  };

  drawPattern(logo);
}

void drawPattern(int logo[8][8]) {
  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(max_intensity_matrix, max_intensity_matrix, max_intensity_matrix));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }
      //delay(50);

    }
  }
  matrix.show();
}


