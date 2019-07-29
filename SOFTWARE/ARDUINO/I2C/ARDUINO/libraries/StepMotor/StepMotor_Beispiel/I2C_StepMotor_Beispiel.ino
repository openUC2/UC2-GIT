#include <I2C_StepMotor.h>

I2C_StepMotor STP_X = I2C_StepMotor(12, 11, 10, 9, 9600);
I2C_StepMotor STP_Y = I2C_StepMotor(4, 3, 2, 13, 14400);

void setup()
{    
    STP_Y.SetSpeed(8);
}
void loop()
{
    STP_X.Move(2048);
    STP_Y.Move(-1024);
}
