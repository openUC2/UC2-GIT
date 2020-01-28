## Experiment – 3 (Incubator Microscope)
Assemble and setup the incubator microscope 

This experiment sets up a compound microscope in order to get familiar with the GUI running on the Raspberry Pi. 
The experiment involves multiple MQTT-able components such as the ```LED-Array``` and the ```Z-stage```. 

The microscope is based on the design found [here](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/APP_Incubator_Microscope_fluorescence)


## Steps

1. Setup the microscope using one BOX and the description given in the link above 
2. First try to get an image using the ```raspistill -k``` command in combination with your cellphone torch 
3. Setup the WiFi-connection:
	- Optional: Install the UC2 Wifi-APP for controling the components from [here](https://github.com/bionanoimaging/UC2-Software-GIT/tree/master/GUI/Android/UC2-TheBox)
4. Setup the Raspberry Pi with the Camera and start the GUI by double-clicking on the UC2-icon which appears on the desktiop 
5. Get familar with basic functions inside the GUI 
6. Try to change the LED-Matrix pattern using the customized settings
7. Try to get a focussed microscope image by coarsly aligning the lens and stepping it up-and-down using the GUI
8. Try to set up a time-series using the GUI 
9. Place a sample in the tray and study how the contrast varies when the light-source changes


### Long-Time Experiment

Prepare a "living" sample and observe it over-night:

#### DOG-sample

Ask Edna ;-) 


#### YEAST-sample 

***Ingredients*** 
- 10 g/L Yeast extract (powder)
- 20 g/L peptone
- 20 g/L glucose

*alternatively*
- 4 g/L NH4H2PO4 = N source
- 10 g/L glucose
- 2 g/L Yeast extract
- 4 g/L peptone

*alternatively*
- ready Medium YNB
- 10 g/L Glucose

*alternatively*
- Fruit juice with N-source 
- or nutrient salts for wine production you can get this in the pharmacy or health food store or drugstore. 

**Tips:**

- pH-value should be between 5 and 7 - instead of glucose you can also take sucrose.
- Yeast forms ethanol - gas development
- Yeast cannot metabolize starch (flour) and starch grains are visible under the microscope.
