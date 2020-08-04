
// ----------- ----------- ----------- ----------- ----------- -----------
// ESP32 script for UC2-control
// by: student of the KLGymansium Erfurt
// date: 11.09.2019 
// part: LEDarray with a button 
// application: simple smartphone microscope
//----------- ----------- ----------- ----------- ----------- -----------

// ----------------------------------------------------------------------------------------------------------------
#include "FastLED.h"


#define NUM_LEDS 64
#define DATA_PIN 5

CRGB leds[NUM_LEDS];

int buttonPushCounter = 4;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button

void setup() {
  // put your setup code here, to run once:
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  Serial.begin(115200);

  // Define buttor input
  pinMode(21, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:

  buttonState = digitalRead(21);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button goes from off to on:
      buttonPushCounter++;
      Serial.println("on");
      Serial.print("number of button pushes: ");
      Serial.println(buttonPushCounter);
    } else {
      // if the current state is LOW then the button goes from on to off:
      Serial.println("off");
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state, for next time through the loop
  lastButtonState = buttonState;
  if (buttonPushCounter == 5)
    buttonPushCounter = 1;

  // Set 3 x White with 3 x brightness and off

  Serial.println(buttonPushCounter);
  if (buttonPushCounter == 1)
  {
    fill_solid( &(leds[0]), 64 /*number of leds*/, CRGB::Black );
    FastLED.setBrightness(0);
  }

  if (buttonPushCounter == 2)
  {
    fill_solid( &(leds[0]), 64 /*number of leds*/, CRGB::White );
    FastLED.setBrightness(16);
  }

  if (buttonPushCounter == 3)
  {
    fill_solid( &(leds[0]), 64 /*number of leds*/, CRGB::White );
    FastLED.setBrightness(64);
  }

  if (buttonPushCounter == 4)
  {
    fill_solid( &(leds[0]), 64 /*number of leds*/, CRGB::White );
    FastLED.setBrightness(255);
  }

 
  // Ausgeben
  FastLED.show();
}
