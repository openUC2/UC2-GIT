// Copyright UC2
// this drives 2 Stepper-Motors (28BYJ) over an ESP32
// It is a test for the later MQTT software
// Install Pyserial!
// https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame


// Pins for the Motor X and Y
int motorPin_X[] = {10, 11, 12, 13}; //{13, 12, 14, 27};
int motorPin_Y[] = {6, 7, 8, 9}; //26, 25, 23, 32};

// Define speeds
unsigned int highSpeed =  2500;
unsigned int  nsteps = 1;

// Set registers
void setup() {
  Serial.begin(9600);

  pinMode(motorPin_X[0], OUTPUT);
  pinMode(motorPin_X[1], OUTPUT);
  pinMode(motorPin_X[2], OUTPUT);
  pinMode(motorPin_X[3], OUTPUT);

  pinMode(motorPin_Y[0], OUTPUT);
  pinMode(motorPin_Y[1], OUTPUT);
  pinMode(motorPin_Y[2], OUTPUT);
  pinMode(motorPin_Y[3], OUTPUT);


  // Move stage to origin position
        // Drive motor X in positive direction
        drive_right(highSpeed, motorPin_X, nsteps);
        stop(motorPin_X);

        // Drive motor X in negative direction
        drive_right(highSpeed, motorPin_Y, nsteps);
        stop(motorPin_X);

        // Drive motor X in positive direction
        drive_left(highSpeed, motorPin_X, nsteps);
        stop(motorPin_X);

        // Drive motor X in negative direction
        drive_left(highSpeed, motorPin_Y, nsteps);
        stop(motorPin_X);




}

void loop()
{
  char data[2];


  if (Serial.available() > 0) {
    char cmd = Serial.read();
    switch (cmd) {


      case 'X': // Drive motor in positive X-direction
        nsteps = Serial.parseInt();

        // Drive motor X in positive direction
        drive_right(highSpeed, motorPin_X, nsteps);
        stop(motorPin_X);
        break;

      case 'x': // Drive motor in negative X-direction
        nsteps = Serial.parseInt();
        Serial.println(nsteps);
        // Drive motor X in positive direction
        drive_left(highSpeed, motorPin_X, nsteps);
        stop(motorPin_X);
        break;

      case 'Y': // Drive motor in positive Y-direction
        nsteps = Serial.parseInt();
        Serial.println(nsteps);
        // Drive motor Y in positive direction
        drive_right(highSpeed, motorPin_Y, nsteps);
        stop(motorPin_Y);
        break;

      case 'y': // Drive motor in negative Y-direction
        nsteps = Serial.parseInt();
        Serial.println(nsteps);
        // Drive motor X in positive direction
        drive_left(highSpeed, motorPin_Y, nsteps);
        stop(motorPin_Y);
        break;




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
