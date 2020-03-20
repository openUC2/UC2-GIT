## <img src="./IMAGES/L.png" width=40>Electronics
Here you'll find the schematics for the wiring parts of the UC2 parts.

---
# If all the wiring scares you, click here [<img src="./IMAGES/lightbulb.svg" width="60">](./ELECTRONICS_FOR_DUMMIES)
---

    This section needs an update!

## Wire Diagrams/Schematics
All schemes are put together with the Open-Source Software [Fritzing](http://fritzing.org/).

Most connections can be established with pin-connection (male/female). For durable connection, please solder everything! You're not expected to have perfect soldering skills though. Look up some youtube-tutorials on "How to solder wires" and alike. Be careful not to mixing up +/- to prevent any shortcuts which would very likely fry the Pi or the Arduinos.

## General Wiring (Arduino)
For the I2C Bus we use a 4-wire colour-code as follows:

- **5V** - White
- **GND** - Yellow
- **Data** - Green
- **CLK** - Brown

The junctions are connected with [WaGo Snapping Clamps, Compact Wago 2273-203 -> Amazon](https://www.amazon.de/Wago-VERBINDUNGSKLEMME-3POL-2273-203/dp/B075ZRQCGZ):
<p align="center">
<img src="./IMAGES/UC2_WiringColourCode.JPG" width="500">
</p>


## Projects
- [XY-Stage](./XY-Stage)
- [LED-Matrix](./LED-Matrix)
- [FLUO-LED](./FLUO-LED)
- [Magnetic Connectors](./Magnetic-Connectors)
- [Raspberry Pi](./RASPBERRY-PI)

# Done with the wiring? Then it's time for [software<img src="./IMAGES/W.png" width=40>](https://github.com/bionanoimaging/UC2-Software-GIT)!
