//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
//  A demo for the openXY table on Arduino with CNC Shield v3.xx with steppers
//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

/*Example sketch to control a stepper motor with A4988 stepper motor driver, AccelStepper library and Arduino: acceleration and deceleration. More info: https://www.makerguides.com */
// Include the AccelStepper library:
#include <AccelStepper.h>

//const int axes[NUM_AXES][2] = {{2, 5}, {3, 6}, {4, 7}, {12, 13}};
const int enablePin = 8;
int stepPinX = 2;
int dirPinX = 5;
int stepPinY = 4;
int dirPinY = 7;

// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
#define dirPin 5
#define stepPin 2
#define motorInterfaceType 1

// Create a new instance of the AccelStepper class:
AccelStepper stepper_x = AccelStepper(motorInterfaceType, stepPinX, dirPinX);
AccelStepper stepper_y = AccelStepper(motorInterfaceType, stepPinY, dirPinY);

void setup() {
  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW);

  // Set the maximum speed and acceleration:
  stepper_x.setMaxSpeed(1000);
  stepper_x.setAcceleration(12500);
  stepper_y.setMaxSpeed(1000);
  stepper_y.setAcceleration(12500);
}

void loop() {
  // Set the target position:
  stepper_x.moveTo(6000);
  stepper_y.moveTo(6000);
  // Run to target position with set speed and acceleration/deceleration:
  stepper_x.runToPosition();
  stepper_y.runToPosition();
  
  delay(1000);
  // Move back to zero:
  stepper_x.moveTo(0);
  stepper_y.moveTo(0);
  stepper_x.runToPosition();
  stepper_y.runToPosition();
  delay(1000);
}
