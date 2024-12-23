// MultiStepper.pde
// -*- mode: C++ -*-
// Use MultiStepper class to manage multiple steppers and make them all move to
// the same position at the same time for linear 2d (or 3d) motion.

#include <AccelStepper.h>
#include <MultiStepper.h>

// create an instance of the stepper class, specifying
// the number of steps of the motor and the pins it's
// attached to
int n_substeps = 1;
  int myspeed = 1000;
  int mynsteps = 800;

AccelStepper stepperX(AccelStepper::HALF4WIRE, 12,13,2,15); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepperX(AccelStepper::HALF4WIRE, 14,27,26,25); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepperX(AccelStepper::HALF4WIRE, 0,4,16,17); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5

// Up to 10 steppers can be handled as a group by MultiStepper
MultiStepper steppers;


void setup() {
  Serial.begin(115200);
  // set the speed at 600 rpm:
  stepperX.setMaxSpeed(600);
  stepperX.setAcceleration(300);
  stepperX.setCurrentPosition(10000);
  stepperY.setMaxSpeed(600);
  stepperY.setAcceleration(300);
  stepperY.setCurrentPosition(10000);
  stepperZ.setMaxSpeed(600);
  stepperZ.setAcceleration(300);
  stepperZ.setCurrentPosition(10000);

    // Then give them to MultiStepper to manage
    steppers.addStepper(stepperX);
  steppers.addStepper(stepperY);
  steppers.addStepper(stepperZ);
  
}

void loop() {

  Serial.println("Z+");

  drive_z(mynsteps, myspeed, 1);
  delay(1000);

  Serial.println("Z-");
  drive_z(mynsteps, myspeed, -1);
  delay(1000);

//  Serial.println("X+");
//  drive_x(1000, 1);
//  delay(1000);
//
//  Serial.println("X-");
//  drive_x(1000, -1);
//  delay(1000);
//
//  Serial.println("Y+");
//  drive_y(1000, 1);
//  delay(1000);
//
//  Serial.println("Y-");
//  drive_y(1000, -1);
//  delay(1000);





}


void drive_z(int nsteps, unsigned int motorSpeed, int mydirection) {
int i_iter = nsteps/n_substeps;
  if (mydirection>0){
    for(int i=0; i<i_iter; i++){
    drive_right(motorSpeed, motorPin_X, n_substeps);
    drive_right(motorSpeed, motorPin_Y, n_substeps);
    drive_right(motorSpeed, motorPin_Z, n_substeps);  
    }
  }
  else{
    for(int i=0; i<i_iter; i++){
    drive_left(motorSpeed, motorPin_X, n_substeps);
    drive_left(motorSpeed, motorPin_Y, n_substeps);
    drive_left(motorSpeed, motorPin_Z, n_substeps);  
    }
  }

  stop(motorPin_X);
  stop(motorPin_Y);
  stop(motorPin_Z);
 
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
