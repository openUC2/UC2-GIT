# Dichroic Beam splitter Cube
This is the repository for the Dichroic Beam splitter Cube.

To acquire the STL-files use the [UC2-Configurator](https://uc2configurator.netlify.app/). The files themselves are in the [RAW](../RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes.

## Purpose
This is meant to be used for fluorescence microscopic imaging setups. The cube can hold an emission and excitation filter as well as a dichroic mirror. The idea is to low-pass filter light e.g. coming from an LED which gets reflected onto the sample plane by a bandpass dichroic mirror. The emitted fluorescent signal is shifted towards the lower frequencies and gets filtered by the emission filter.

<p align="center">
<img src="./IMAGES/Assembly_Cube_Dichroic_Beamsplitter_25x35_v3.png" width="300">
</p>

### Properties
* design is derived from the base-cube

## Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

#### Default:
* **IM Cube** which houses the insert and adapts it into a UC2 setup.
* **The Dichroic Beam splitter Insert** which holds the three different filters ([20_Cube_Insert_Beamsplittercube_Base_25x35_v3.stl](../RAW/STL))
* 2x **The Retain Rings** which fixes the emission and excitation filters ([20_Cube_Insert_Beamsplittercube_Retainring_25mm.stl](../RAW/STL))
* 1x **The Retain Plate** which holds the dichroic filter ([20_Cube_Insert_Beamsplittercube_Dichroicmirror_Retainplate_25_36.stl](../RAW/STL))

#### Alternatives:
* **3DP Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([10_Cube_1x1_v3.stl](../RAW/STL)) and **3DP Lid** which closes the Cube ([10_Lid_1x1_v3.stl](../RAW/STL)) - find the details in [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base)


### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 2× DIN912 M3*12 screws (non stainless steel)
* 1× Dichroic Mirror (16mmx25mm, rectangular, e.g. COMAR optics)
* 1× Excitation filter (25mm Diameter, e.g. COMAR optics)
* 1× Emission filter (25mm Diameter, e.g. COMAR optics)

## <img src="./IMAGES/A.png" height="40"> Assembly
* Remove any support and clean the part
* Insert the dichroic filter inside its place
* Mount the Retain Plate with 2x M3 Screws
* Insert the excitation filter inside its place
* Mount the Retain Ring so that the filter is fixed
* Insert the emission filter inside its place
* Mount the Retain Ring so that the filter is fixed
* Slide the dichroic beam splitter holder into the Cube Body
* Close the cube accordingly (IM/3DP)
* Done!


### Tutorial with images
:grey_exclamation: This tutorial shows a UC2_v2 cube but the assembly of the insert is still the same. For assembly of the cube (IM/3DP) check the [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base).

1. All parts for this model
<p align="center">
<img src="./IMAGES/CUBE_DICHROIC_0.jpg" width="300">
</p>

2. Mount the dichroic + retain plate
<p align="center">
<img src="./IMAGES/CUBE_DICHROIC_1.jpg" width="300">
</p>

3. Add the excitation/emission filter + retain rings
<p align="center">
<img src="./IMAGES/CUBE_DICHROIC_2.jpg" width="300">
</p>

4. Fix everything
<p align="center">
<img src="./IMAGES/CUBE_DICHROIC_3.jpg" width="300">
</p>

5. Place the Insert into the Cube and add all screws
<p align="center">
<img src="./IMAGES/CUBE_DICHROIC_4.jpg" width="300">
</p>

6. Done!


## Safety
Don't touch the smooth glass surfaces, only the opaque ones!
