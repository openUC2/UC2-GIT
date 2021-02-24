#include <Arduino.h>
#include "Adafruit_GFX.h"
#include "Adafruit_NeoMatrix.h"
#include "Adafruit_NeoPixel.h"
#include <SPI.h>

#define LEDARR_PIN 26
#define SWITCH 21

int brightlvl = 0;
volatile int showMode = 0;
volatile bool done = false;
//Arduino devices
// StepMotor stepperX = StepMotor(12, 13, 2, 3);
// StepMotor stepperY = StepMotor(8, 9, 10, 11);
// StepMotor stepperZ = StepMotor(4, 5, 6, 7);
Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, LEDARR_PIN, 
    NEO_MATRIX_TOP + NEO_MATRIX_RIGHT + NEO_MATRIX_COLUMNS + 
    NEO_MATRIX_PROGRESSIVE, NEO_GRB + NEO_KHZ800);

const int nrows = 8;
const int ncols = 8;
const int npixels = ncols * nrows;
int ledNA = 4;

struct RGB {
  byte r;
  byte g;
  byte b;
};

struct RGB rgb;

void pin_ISR(){
  showMode = 1 - showMode;
}

void setup()
{
  matrix.begin();
  matrix.fillScreen(0);
  rgb.r = 0;
  rgb.g = 0;
  rgb.b = 255;
  pinMode(SWITCH, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(SWITCH), pin_ISR, FALLING);
}

void drawRect(int x, int y, int w, int h, bool fill)
{
  int offset_x = (ncols - ledNA*2) * 0.5;  
  int offset_y = (nrows - ledNA*2) * 0.5;
  if(x < offset_x) x = offset_x;
  if(y < offset_y) y = offset_y;
  if(x > ncols-offset_x) x = ncols-offset_x;
  if(y > nrows-offset_y) y = nrows-offset_y;
  if((x+w) > (ncols - offset_y)) w = ncols - offset_y - x;
  if((y+h) > (nrows - offset_x)) h = nrows - offset_x - y;

  if(fill) 
    matrix.fillRect(x, y, w, h, matrix.Color(rgb.r, rgb.g, rgb.b));
  else
    matrix.drawRect(x, y, w, h, matrix.Color(rgb.r, rgb.g, rgb.b));
  
  matrix.show();
}

void setNA(int select)
{
	if (select > 4)
	{
		select = 4;
	}
	if (select < 1)
	{
    select = 1;
		matrix.fillScreen(0);
	}
	ledNA = select;
}

void updateColor()
{
  uint8_t r_old = rgb.r;
  uint8_t g_old = rgb.g;
  uint8_t b_old = rgb.b;
  rgb.r = g_old;
  rgb.g = b_old;
  rgb.b = r_old;
}

void loop()
{
  if (showMode == 1){
    brightlvl += 1;
    matrix.setBrightness(brightlvl);
    delay(10);
    brightlvl = brightlvl % 255;
    matrix.fillRect(0, 0, 8, 8, matrix.Color(rgb.r, rgb.g, rgb.b));
    if (brightlvl == 0){
      updateColor();
      for (int i=0; i < 5; i++){
        matrix.fillRect(0, 0, 4, 4, matrix.Color(255, 255,   0));
        matrix.show();
        delay(100);
        matrix.fillRect(4, 4, 4, 4, matrix.Color(255,   0,   0));
        matrix.show();
        delay(100);
        matrix.fillRect(0, 4, 4, 4, matrix.Color(  0, 255,   0));
        matrix.show();
        delay(100);
        matrix.fillRect(4, 0, 4, 4, matrix.Color(  0,   0, 255));
        matrix.show();
        delay(100);
        matrix.fillScreen(0);
        matrix.show();
        delay(100);
      }
    }
    matrix.show();
    done = false;
  }
  else{
    if (!done){
      matrix.fillRect(0, 0, 8, 8, matrix.Color(255, 255, 255));
      matrix.show();
      done = true;
    }
  }
}


