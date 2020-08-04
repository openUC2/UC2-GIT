#include <Stepper.h>

const int step_360 = 2058;// 360 number of steps per/rev  
const int nsteps = 1000;                            
// initialize the stepper library on pins 2-5 n 8-11
Stepper myStepper1(step_360,2,4,3,5);
Stepper myStepper2(step_360,6,8,7,9);      
Stepper myStepper3(step_360,10,12,11,13);      

void setup()
{
 // set the speed at 60 rpm:
 myStepper1.setSpeed(8);//left
 myStepper2.setSpeed(8);//right
 myStepper3.setSpeed(8);//right
 // initialize the serial port:
 Serial.begin(9600);
}
void loop()
{

// step one revolution  in one direction:
 Serial.println("clockwise");
 
for(int s=0; s<nsteps; s++)
{
  myStepper1.step(1);
  myStepper2.step(1);
  myStepper3.step(1);
}

 for(int s=0; s<step_360; s++)
{
  myStepper1.step(-1);
  myStepper2.step(-1);
  myStepper3.step(-1);
}
 
}
