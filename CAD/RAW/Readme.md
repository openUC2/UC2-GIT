# RAW CAD Files

In this folder we provide all design (```.ipt```) and exported (```.stl```)-files.

## IPT files
All designs are created in Autodesk Inventor 2019, with the exception of the openSCAD files.

To work with the files, download the ```IPT``` folder or pull the repository and open the project file ```UC2_v3.ipj```.  

If you wish to contribute with your own designs, please have a look at our [Contributing guidelines](../../CONTRIBUTING.md) and [Code of Conduct](../../CODE_OF_CONDUCT.md). To contribute with a new design, add your assembly files ```.iam``` and part files ```.ipt``` to the IPT folder and create a pull request.


## STL files
In order to print parts, modules and applications, we recommend using the [UC2 Configurator](https://uc2configurator.netlify.app/). In case your searching for alternatives to the main parts, the ```STL``` folder should have them all.

### Export files from Inventor
IPT: Save as -> Pack 'n go -> save somewhere and copy the ```.ipt``` files in the [IPT](.\IPT)-folder).
STL: Export -> export as STL and hit options -> individual files. All STL files have to be called UC2_***_v3.stl

#### Renaming
On Windows:
```
python convertname2.py
```
