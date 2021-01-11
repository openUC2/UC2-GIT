# Circular Aperture Cube
This is the repository for a circular aperture incorporated into the basic Cube.

To acquire the STL-files use the [UC2-Configurator](). The files themselves are in the [RAW](../RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes.

## Purpose
The aperture diaphragm is typically used in the case of critical or Köhler illumination, where it allows for controlling the intensity and/or diameter of the illuminated area.

<p align="center">
<img src="./IMAGES/Assembly_Cube_CircularAperture_v3.png" width="300">
</p>

### Properties
* the diameter of the aperture goes from 25 mm to approximately 2 mm
* design is inspired by [mechanical aperture](https://www.thingiverse.com/thing:2796724) but adapted to the Cube size and for the purpose of microscopy

## Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

#### Default:
* **IM Cube** which houses the insert and adapts it into a UC2 setup.
* **The Aperture Guide** which controls the movement of the leaves ([20_Cube_Insert_CirAp_Guide_v3.stl](../RAW/STL))
* **The Aperture Wheel** which opens and closes the aperture when rotated ([20_Cube_Insert_CirAp_Wheel.stl](../RAW/STL))
* **The Aperture Leaf** which moves when the wheel is rotated. Print ALL the leaves in the STL folder ([20_Cube_Insert_CirAp_Leaf.stl](../RAW/STL))
* **The Aperture Lid** which holds the wheel in position by pressing it against the guiding part ([20_Cube_Insert_CirAp_Lid_v3.stl](../RAW/STL))

#### Alternatives:
* **3DP Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([10_Cube_1x1_v3.stl](../RAW/STL)) and **3DP Lid** which closes the Cube ([10_Lid_1x1_v3.stl](../RAW/STL)) - find the details in [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base)


### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 2× M2×16 screw with nuts (non-magnetic)

## <img src="./IMAGES/A.png" height="40"> Assembly
* Assemble the aperture
* Add the insert to the Cube
* Close the cube accordingly (IM/3DP)
* Done!

### <img src="./IMAGES/A.png" height="40"> Assembly Tutorial with images
:grey_exclamation: This tutorial shows a UC2_v2 cube but the assembly of the insert is still the same. For assembly of the cube (IM/3DP) check the [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base).

1. All parts for this model: Make sure to print SEVEN leaves!
<p align="center">
<img src="./IMAGES/CirAp01.jpg" width="300">
</p>

2. Start with putting all the leaves on the pins of the wheel. Don't worry if they seem too loose, they will be held in place once the aperture is assembled.
<p align="center">
<img src="./IMAGES/CirAp02.jpg" width="300">
<img src="./IMAGES/CirAp03.jpg" width="300">
</p>

3. Next, smooth into overlapping pattern. Hold the leaf on the pin of the wheel when moving it, so it doesn't fall off.
<p align="center">
<img src="./IMAGES/CirAp04.jpg" width="300">
<img src="./IMAGES/CirAp05.jpg" width="300">
</p>

4. Put the wheel carrying the leaves together with the leave-guide. The pins of each leaf has to fall into the rail on the guide. When done correctly, the wheel and guide end up being parallel. See pictures:
<p align="center">
<img src="./IMAGES/CirAp06.jpg" width="300">
<img src="./IMAGES/CirAp07.jpg" width="300">
</p>

5. Close the assembly with the aperture-lid. The lid holds the wheel centered.
<p align="center">
<img src="./IMAGES/CirAp08.jpg" width="300">
<img src="./IMAGES/CirAp09.jpg" width="300">
</p>

6. Add the assembled aperture to the cube and close the cube with the lid, using four M3×12 screws. Make sure the guide and the lid are close enough, so the leaves can't move anywhere else that following the rails in the guide.
<p align="center">
<img src="./IMAGES/CirAp10.jpg" width="300">
<img src="./IMAGES/CirAp11.jpg" width="300">
</p>

7. Assembled Aperture cube allows for opening and closing the aperture from the outside. Fully open aperture has the diameter of 25 mm, fully closed is approximately 2 mm in diameter.
<p align="center">
<img src="./IMAGES/CirAp12.jpg" height="300">
<img src="./IMAGES/CirAp13.jpg" height="300">
<img src="./IMAGES/CirAp14.jpg" height="300">
</p>

<p align="center">
<img src="./IMAGES/CirAp-closing.gif" height="300">
</p>

8. In the latest version on this module, we added two holes for M2 screws to hold the aperture together and make the movement of it inside the cube more convenient.  
When you assemble the aperture, make sure that the holes in the Lid and Guide part are matching. Then put the M2 screws into the holes and fix the aperture by putting nuts on the screws.
<p align="center">
<img src="./IMAGES/CirAp15.jpg" width="300">
<img src="./IMAGES/CirAp16.jpg" width="300">
</p>
