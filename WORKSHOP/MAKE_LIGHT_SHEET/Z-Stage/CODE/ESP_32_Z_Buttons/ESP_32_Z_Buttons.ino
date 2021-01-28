// Copyright UC2
// this drives 2 Stepper-Motors (28BYJ) over an ESP32
// It is a test for the later MQTT software
// Install Pyserial!
// https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame


// Pins for the Motor X and Y
int motorPin_Z[] = {27, 26, 25, 33}; //{13, 12, 14, 27};
int PIN_button_left = 18;
int PIN_button_right = 19;

boolean buttonstate_left = false;
boolean buttonstate_right = false;

// Define speeds
unsigned int MotorSpeed =  4500;
unsigned int  nsteps = 2;
unsigned int speedincrement = 0; 

// Set registers
void setup() {
  Serial.begin(9600);

  pinMode(motorPin_Z[0], OUTPUT);
  pinMode(motorPin_Z[1], OUTPUT);
  pinMode(motorPin_Z[2], OUTPUT);
  pinMode(motorPin_Z[3], OUTPUT);

  // initialize the pushbutton pin as an input:
  pinMode(PIN_button_left, INPUT_PULLUP);
  pinMode(PIN_button_right, INPUT_PULLUP);       // turn on pullup resistors




}

void loop()
{
  // read the state of the pushbutton value:
  buttonstate_left = digitalRead(PIN_button_left);
  buttonstate_right = digitalRead(PIN_button_right);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonstate_left == LOW) {
    drive_left(MotorSpeed-speedincrement, motorPin_Z, nsteps);
    if (speedincrement<2500) speedincrement = speedincrement +100;
  }
    else if(buttonstate_right == LOW) {
    drive_right(MotorSpeed-speedincrement, motorPin_Z, nsteps);
    if (speedincrement<2500) speedincrement = speedincrement +100;
    
  } 
  else {
    stop(motorPin_Z);
    speedincrement = 0;
  }

Serial.println(MotorSpeed-speedincrement);


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
