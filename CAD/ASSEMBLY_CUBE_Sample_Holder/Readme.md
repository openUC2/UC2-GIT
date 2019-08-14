# Generic Sample Holder
This is the repository for the design of the sample holder that can hold microscope slides ad other flat object inside the Cube. The stl-files can be found in the folder [STL](./STL).



## Purpose
This holder can be used for microscope slides, filters and other flat objects. Both vertical and horizontal position is possible. The holder can be slid through the cube and the sample can be moved through the field of view in X and Y.

<p align="center">
<img src="./IMAGES/Assembly_Cube_Sample_holder_v2.png"
width="1000">
</p>


## Properties
* design is derived from the Base Cube

## Parts

### 3D printing parts

The Part consists of the following components.

1. **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/ASSEMBLY_CUBE_Sample_Holder_10_Cube_Lid.stl))
2. **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/ASSEMBLY_CUBE_Sample_Holder_10_Cube_Base.stl))
3. **The Sample holder Insert** that can hold the pinhole in front of the LED ([Sample holder](./STL/ASSEMBLY_CUBE_Sample_Holder_20_Cube_insert_Sample_holder.stl))
4. **The Sample holder clamp** that fixes the pinhole in its position ([Sample clamp](./STL/ASSEMBLY_CUBE_Sample_Holder_20_Cube_Insert_Sample_clamp.stl))

### Additional parts
* 8x DIN912 M3*12 screws (non stainless steel)

## Remarks and Tips

### 3D Printing
* No support required in all designs
* Carefully remove all support structures (if applicable)


## Assembly
* Remove any support and clean the part
* Press the Clamp on the sample holder, slide the holder into the Cube Body in front of the LED
* Add the lid and fix it using a set of M3 screws
* Done!
