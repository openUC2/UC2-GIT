#include <StepMotor.h>

StepMotor STP_X = StepMotor(6,8,7,9,9600);
StepMotor STP_Y = StepMotor(10,12,11,13,9600);
StepMotor STP_Z = StepMotor(2,3,4,5,9600);

void setup()
{
  STP_X.SetSpeed(4);
  STP_Y.SetSpeed(4);
   STP_Z.SetSpeed(15);
}
void loop()
{
  STP_X.Move(450);
  delay(100);
  STP_X.Move(-450);
  delay(100);

  STP_Y.Move(450);
  delay(100);
  STP_Y.Move(-450);
  delay(100);

   STP_Z.Move(2000);
  delay(100);
  STP_Z.Move(-2000);
  delay(100);
  
}
