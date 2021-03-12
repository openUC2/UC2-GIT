# UC2 Configurator Helper Doc

## Add a module to the Excel sheet

1. Add the `STL` file to the folder `CAD/RAW/STL` with the name from Inventor plus prefix `UC2_` and the suffix `_v3.stl` which means for a file named `20_Cube_Insert_CirAp_Wheel.stl` => `UC2_20_Cube_Insert_CirAp_Wheel_v3.stl`
2. Similiarily add a new folder for the module in the folder `/CAD/` with the same given in the column 2 (e.g. `ASSEMBLY_CUBE_AlliedVision_Alvium`)  

3. Open the Excel sheet and add a new module on the very left hand side which has the following structure: 

| ASSEMBLY_CUBE_AlliedVision_Alvium |                                                  |   |   |                                                                                                                           | 250,1 |
|-----------------------------------|--------------------------------------------------|---|---|---------------------------------------------------------------------------------------------------------------------------|-------|
|                                   | ASSEMBLY_CUBE_Base                               |   | 1 | Module#2                                                                                                                  | 0     |
| 250,10 €                          | 20_Cube_insert_AlliedVision_Alvium_v3            | 1 | 1 | https://github.com/bionanoimaging/UC2-GIT/blob/v3/CAD/RAW/STL/UC2_v3_20_Cube_insert_AlliedVision_Alvium_v3_1.stl          | 0,1   |
|                                   | 20_Cube_insert_AlliedVision_Alvium_adjustable_v3 | 1 | 1 | https://github.com/bionanoimaging/UC2-GIT/blob/v3/CAD/RAW/STL/UC2_v3_20_Cube_insert_AlliedVision_Alvium_adjustable_83.stl | 0,1   |
|                                   | Allied Vision Camera                             | 0 | 1 | https://www.alliedvision.com/en/digital-industrial-camera-solutions.html                                                  | 250   |

### Explanation: 

1. `ASSEMBLY_CUBE_Base` always refer to the standard base cube and will be automatically inserted by the UC2-configurator 
2. Inserts from a module e.g. `20_Cube_insert_AlliedVision_Alvium_v3` have to be inside the RAW/STL folder; it can be as many as you want
3. The running number in collum 1 is dictating the start/end point of a module
4. `Printable` if `0` it is not meant to be used for downloading; `1` refers to the STL file accordingly 
5. `Amount` gives the integer (!) number of files you want to have in one module
6. `Source` link is obsolete for printed files since the download link is generated from the Name (1)
7. `Price` is the price for the printed/bought part in €


## Add a module to an `APPLICATION`

1. Add an integer (!) number to the application in the respective column; The configurator will automatically recognize it


## Add a `Application` to the list

1. Add a new column to the end of the list with the following features:

3. `NAME`: Represents the exact folder Name of the `APPLICATION`in the folder `/APPLICATIONS` e.g. `APP_Abbe_Setup`
4. `Link to Github`: is obsolet (in future could be the image link) 
5. `Link to Image`: is obsolet (right now it takes `conver.png` or `conver.jpg` by default)
6. `Brief Description`: Write a short comment about what the application can do; It shows in the configurator (it can have HTML commands).

## Add a `BOX` to the list

Follow steps from *Add a `Application` to the list*

## Add Cover images to the Applications 

1. Place a file in `/APPLICATIONS/APP_***/IMAGES/conver.jpg`

## Remarks:

- It only works if the spelling of the filename is exactly as given by the Excel sheet! 
- If you add a new module/application/make changes to the excel sheet: you need to run the Python converter script in `/DOCUMENTS/UC2-Configurator/generate_config_from_database.py`
- The converter script will add new `config.json` files in all folders and will delete those which became obsolete
- MOVE the `END` tag to the very end such that the script recognizes the END
