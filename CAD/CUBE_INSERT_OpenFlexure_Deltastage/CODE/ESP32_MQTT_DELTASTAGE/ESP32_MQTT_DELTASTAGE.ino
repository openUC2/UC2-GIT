/* Here ESP32 will keep 2 roles:
  1/ read data from DHT11/DHT22 sensor
  2/ control led on-off
  So it willpublish temperature topic and scribe topic bulb on/off
*/

#include <WiFi.h>
#include <PubSubClient.h>
#include <AccelStepper.h>
#include <MultiStepper.h>


// EG X-Y position bed driven by 2 steppers
// Alas its not possible to build an array of these with different pins for each :-(
AccelStepper stepper1(AccelStepper::HALF4WIRE, 2, 4, 3, 5);
AccelStepper stepper2(AccelStepper::HALF4WIRE, 6, 8, 7, 9);
AccelStepper stepper3(AccelStepper::HALF4WIRE, 10, 12, 11, 13);

/* change it with your ssid-password */
const char* ssid = "Blynk";
const char* password = "12345678";
/* this is the IP of PC/raspberry where you installed MQTT Server
  on Wins use "ipconfig"
  on Linux use "ifconfig" to get its IP address */
const char* mqtt_server = "192.168.43.88";

/* create an instance of PubSubClient client */
WiFiClient espClient;
PubSubClient client(espClient);

///* topics - DON'T FORGET TO REGISTER THEM! */
#define STEPPER_X_FWD     "stepper/x/fwd"
#define STEPPER_X_BWD     "stepper/x/bwd"
#define STEPPER_Y_FWD     "stepper/y/fwd"
#define STEPPER_Y_BWD     "stepper/y/bwd"
#define STEPPER_Z_FWD     "stepper/z/fwd"
#define STEPPER_Z_BWD     "stepper/z/bwd"

#define CLIENT_ID "ESP32Client_deltastage";


void setup() {

  // Configure each stepper
  stepper1.setMaxSpeed(1000);
  stepper2.setMaxSpeed(1000);
  stepper3.setMaxSpeed(1000);
  // Then give them to MultiStepper to manage
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
  steppers.addStepper(stepper3);

  Serial.begin(115200);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

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
  Serial.print("]");

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == STEPPER_X_FWD) {
    // Drive motor X in positive direction
    int n_steps_x = (int)payload_int;
    drive_x(n_steps_x, true);
    Serial.print("Motor is running in x for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == STEPPER_X_BWD) {
    // Drive motor X in positive direction
    int n_steps_x = (int)payload_int;
    drive_x(n_steps_x, false);
    Serial.print("Motor is running in x for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }
  // Catch the value for stepment of lens in X-direction
  if (String(topic) == STEPPER_Y_FWD) {
    // Drive motor X in positive direction
    int n_steps_x = (int)payload_int;
    drive_y(n_steps_x, true);
    Serial.print("Motor is running in x for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == STEPPER_Y_BWD) {
    // Drive motor X in positive direction
    int n_steps_x = (int)payload_int;
    drive_y(n_steps_x, false);
    Serial.print("Motor is running in x for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == STEPPER_Z_FWD) {
    // Drive motor X in positive direction
    int n_steps_x = (int)payload_int;
    drive_z(n_steps_x, true);
    Serial.print("Motor is running in x for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }

  // Catch the value for stepment of lens in X-direction
  if (String(topic) == STEPPER_Z_BWD) {
    // Drive motor X in positive direction
    int n_steps_x = (int)payload_int;
    drive_z(n_steps_x, false);
    Serial.print("Motor is running in x for: ");
    Serial.print((int)payload_int);
    Serial.println();
  }
}

void mqttconnect() {
  /* Loop until reconnected */
  while (!client.connected()) {
    Serial.print("MQTT connecting ...");
    /* client ID */
    String clientId = CLIENT_ID;
    /* connect now */
    if (client.connect(clientId.c_str(), "username", "pi")) {
      Serial.println("connected");
      /* subscribe topic with default QoS 0*/
      client.subscribe(STEPPER_Z_BWD);
      client.subscribe(STEPPER_Z_FWD);
      client.subscribe(STEPPER_X_BWD);
      client.subscribe(STEPPER_X_FWD);
      client.subscribe(STEPPER_Y_BWD);
      client.subscribe(STEPPER_Y_FWD);

    } else {
      Serial.print("faiLED_PIN, status code =");
      Serial.print(client.state());
      Serial.println("try again in 5 seconds");
      /* Wait 5 seconds before retrying */
      delay(5000);
    }
  }
}


void drive_x(int nsteps, int mydirection){
  long positions[3]; // Array of desired stepper positions
  positions[0] = mydirection*nsteps;
  positions[1] = mydirectionnsteps;
  positions[2] = -nsteps;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position 
}
