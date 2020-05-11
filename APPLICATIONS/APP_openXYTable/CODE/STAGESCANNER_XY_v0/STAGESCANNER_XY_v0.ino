//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
//  A demo for the openXY table on Arduino with CNC Shield v3.xx with steppers 
//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

const int axes[NUM_AXES][2] = {{2, 5}, {3, 6}, {4, 7}, {12, 13}};
const int enablePin = 8;
int stepPinX = 2;
int dirPinX = 5;
int stepPinY = 4;
int dirPinY = 7;

const int INPUT_BUFLEN = 200;
String inputString = "";         // a string to hold incoming serial data
boolean stringComplete = false;  // whether the string is complete
boolean inputBufferTruncated = false;  // whether the string got truncated
boolean steppersEnabled = false;
boolean runTest = false;

int numSteps = 2500;
int stepDelayUs_L2H = 600; // about the lowest reliable value for my setup
int stepDelayUs_H2L = stepDelayUs_L2H; // about the lowest reliable value for my setup
int dirChangeDelayMs = 100;



void setup() {
  inputString.reserve(INPUT_BUFLEN);
  inputString = "";
  Serial.begin(9600);
  Serial.println("Stepper exerciser for CNC Shield v3.xx");

  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW);

  pinMode(stepPinX, OUTPUT);
  pinMode(stepPinY, OUTPUT);
  pinMode(dirPinX, OUTPUT);
  pinMode(dirPinY, OUTPUT);

  digitalWrite(stepPinX, LOW);
  digitalWrite(stepPinY, LOW);
  digitalWrite(dirPinX, LOW);
  digitalWrite(dirPinY, LOW);

}


void loop() {

  // Drive in X
  Serial.println("Drive in X");
  digitalWrite(dirPinX, HIGH);
  digitalWrite(dirPinY, HIGH);
  driveSteps(numSteps);
  delay(dirChangeDelayMs);


  // Drive in Y
  Serial.println("Drive in Y");
  digitalWrite(dirPinX, HIGH);
  digitalWrite(dirPinY, LOW);
  driveSteps(numSteps);
  delay(dirChangeDelayMs);

  // Drive in -X
  Serial.println("Drive in -X");
  digitalWrite(dirPinX, LOW);
  digitalWrite(dirPinY, LOW);
  driveSteps(numSteps);
  delay(dirChangeDelayMs);

  // Drive in -Y
  Serial.println("Drive in -Y");
  digitalWrite(dirPinX, LOW);
  digitalWrite(dirPinY, HIGH);
  driveSteps(numSteps);
  delay(dirChangeDelayMs);

}

void driveSteps(int numSteps) {
  for (int stepCnt = 0; stepCnt < numSteps; stepCnt++) {
    digitalWrite(stepPinX, HIGH);
    digitalWrite(stepPinY, HIGH);
    delayMicroseconds(stepDelayUs_H2L);
    digitalWrite(stepPinX, LOW);
    digitalWrite(stepPinY, LOW);
    delayMicroseconds(stepDelayUs_L2H);
  }
}
