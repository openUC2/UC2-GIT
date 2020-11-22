# UC2 configurator 

The process to prepare the files for the [UC2 configurator](https://github.com/bionanoimaging/uc2-configurator) are the following. 

**1. Add new modules/applications**

Inside the Excel Datasheet: [UC2_ReadyToUse_Boxes_Modules_Parts.xlsx](UC2_ReadyToUse_Boxes_Modules_Parts.xlsx) you need to add a module or application by copying one of the existing ones and adjust it such that it has all STL files and extra files. Make sure, that the names in the column "Source" match the filename of the file which should be linked e.g. ```Assembly_base_4x1.stl```

**2. Add the file to the repository**

You need to copy the file you need into the folder of this repository: ```./CAD/RAW/STL``` -> [here](./CAD/RAW/STL). 

***3. Compile the Config-files***

Call the python script which creates all the ```json```-files in each module/application folder by doing the following in this folder:

```py
generate_config_from_database.py
```

***4. Push to the Master branch***

With all changes, you can push the changes to the master branch. 