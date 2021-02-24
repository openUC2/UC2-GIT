#define SCHRITTEPROUMDREHUNG 2048 

#include "Stepper.h"  // Bibliothek

int buttonStateUp = 0; //Variable für Taste nach oben
int buttonStateDown = 0; //Variable für Taste nach unten

Stepper Schrittmotor(SCHRITTEPROUMDREHUNG, 25, 27, 26, 14); // Anbindung Schrittmotor über diese Pins an Arduino

void setup() {
  Serial.begin(115200); // Baud-Rate für Logging

  
  pinMode(23, INPUT_PULLUP); // Taster Eingang hoch definieren (pin 23)

  
  pinMode(19, INPUT_PULLUP); // Taster Eingang runter definieren (pin 19)
}

void loop() {

  buttonStateUp = digitalRead (23);  // lese von pin 23 die Info für den Button
  Serial.print("Status button down: "); // Gib den Text für seriellen Monitor
  Serial.println(buttonStateDown); //Status der Variable für Seriellen Monitor
  

  buttonStateDown = digitalRead (19);  // lese von pin 19 die Info für den Button
  Serial.print("Status button up: "); // Gib den Text für seriellen Monitor
  Serial.println(buttonStateUp); //Status der Variable für Seriellen Monitor
 


  if (buttonStateUp == LOW) { //wenn button gedrückt (logisch low weil gedrückt)
    Serial.println("Tastehoch"); //serieller Monitor Information
    Schrittmotor.setSpeed(15); //Geschwindigkeit Drehung
    Schrittmotor.step(5); //Anzahl Schritte auf einmal

  }

  if (buttonStateDown == LOW) { //wenn button gedrückt (logisch low weil gedrückt)
    Serial.println("Tasterunter"); //serieller Monitor Information
    Schrittmotor.setSpeed(15); //Geschwindigkeit Drehung
    Schrittmotor.step(-5); //Anzahl Schritte auf einmal aber in andere Richtung

  }

}
