// Adafruit_NeoMatrix example for single NeoPixel Shield.
// Scrolls 'Howdy' across the matrix in a portrait (vertical) orientation.

#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>

#ifndef PSTR
#define PSTR // Make Arduino Due happy
#endif

#define PIN 23



// MATRIX DECLARATION:
// Parameter 1 = width of NeoPixel matrix
// Parameter 2 = height of matrix
// Parameter 3 = pin number (most are valid)
// Parameter 4 = matrix layout flags, add together as needed:
//   NEO_MATRIX_TOP, NEO_MATRIX_BOTTOM, NEO_MATRIX_LEFT, NEO_MATRIX_RIGHT:
//     Position of the FIRST LED in the matrix; pick two, e.g.
//     NEO_MATRIX_TOP + NEO_MATRIX_LEFT for the top-left corner.
//   NEO_MATRIX_ROWS, NEO_MATRIX_COLUMNS: LEDs are arranged in horizontal
//     rows or in vertical columns, respectively; pick one or the other.
//   NEO_MATRIX_PROGRESSIVE, NEO_MATRIX_ZIGZAG: all rows/columns proceed
//     in the same order, or alternate lines reverse direction; pick one.
//   See example below for these values in action.
// Parameter 5 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)


// Example for NeoPixel Shield.  In this application we'd like to use it
// as a 5x8 tall matrix, with the USB port positioned at the top of the
// Arduino.  When held that way, the first pixel is at the top right, and
// lines are arranged in columns, progressive order.  The shield uses
// 800 KHz (v2) pixels that expect GRB color data.
Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, PIN,
                            NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
                            NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
                            NEO_GRB            + NEO_KHZ800);
struct RGB {
  byte r;
  byte g;
  byte b;
};


// Define some colors we'll use frequently
int myintensity_R = 50; 
int myintensity_G = 50; 
int myintensity_B = 50; 
RGB white = { myintensity_R, myintensity_G, myintensity_B};
RGB red = { myintensity_R, myintensity_G, myintensity_B};
RGB off = { 0, 0, 0 };




void setup() {
  matrix.begin();
  matrix.setTextWrap(false);
  matrix.setBrightness(150);

}





int x    = matrix.width();
int pass = 0;



// let's create a boolean variable to save the direction of our rotation
boolean moveClockwise = true;


int tdelay = 4000;
int tdelay_short = 1000;
void loop() {

  drawLeft();
  matrix.show();
  delay(tdelay);

  drawRight();
  matrix.show();
  delay(tdelay);

  drawUp();
  matrix.show();
  delay(tdelay);

  drawDown();
  matrix.show();
  delay(tdelay);

  drawDark();
  matrix.show();
  delay(tdelay);

if(1){
  matrix.fillScreen(matrix.Color(white.r, white.g, white.b));
  matrix.show();
  delay(tdelay);

  drawNA1();
  matrix.show();
  delay(tdelay);

  drawNA2();
  matrix.show();
  delay(tdelay);

  drawNA3();
  matrix.show();
  delay(tdelay);

  drawDark();
  matrix.show();
  delay(tdelay);

  drawDF();
  matrix.show();
  delay(tdelay);

  drawDark();
  matrix.show();
  delay(tdelay);

  drawFPM();

}
}






void drawLeft() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0, 0, 0}
  };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}


void drawUp() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0}
  };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}

void drawDown() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1}
  };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}



void drawDark() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0}
  };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}

void drawRight() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1},
    { 0, 0, 0, 1, 1, 1, 1, 1}
  };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}

void drawFPM() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {

      matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      matrix.show();
      delay(500);
      matrix.drawPixel(column, row, matrix.Color(0, 0, 0));


    }
  }
}


void drawNA1() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 1, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0}
    };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}



void drawNA2() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 1, 1, 0, 0, 0},
    { 0, 0, 0, 1, 1, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0}
    };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}



void drawNA3() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    { 0, 0, 1, 1, 1, 1, 0, 0},
    { 0, 0, 0, 1, 1, 1, 0, 0},
    { 0, 0, 1, 1, 1, 1, 0, 0},
    { 0, 0, 1, 1, 1, 1, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0},
    { 0, 0, 0, 0, 0, 0, 0, 0}
    };

  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}

void drawDF() {
  // This 8x8 array represents the LED matrix pixels.
  // A value of 1 means we’ll fade the pixel to white
  int logo[8][8] = {
    { 1, 1, 1, 1, 1, 1, 1, 1},
    { 1, 0, 0, 0, 0, 0, 0, 1},
    { 1, 0, 0, 0, 0, 0, 0, 1},
    { 1, 0, 0, 0, 0, 0, 0, 1},
    { 1, 0, 0, 0, 0, 0, 0, 1},
    { 1, 0, 0, 0, 0, 0, 0, 1},
    { 1, 0, 0, 0, 0, 0, 0, 1},
    { 1, 1, 1, 1, 1, 1, 1, 1}
    };


  for (int row = 0; row < 8; row++) {
    for (int column = 0; column < 8; column++) {
      if (logo[row][column] == 1) {
        matrix.drawPixel(column, row, matrix.Color(myintensity_R, myintensity_G, myintensity_B));
      }
      else {
        matrix.drawPixel(column, row, matrix.Color(0, 0, 0));
      }

    }
  }
}

