# ISM alignment tutorial

This tutorial is aming to align the openISM module to the microscope. The required components and setup steps are similar to the openSIM module which is in the Github repository.

  - openISM module
  - optical components
  - UC2 cubes and inserts
  - target sample
  - magical hand
## Introduction of the openISM module

In the openISM module, the illumination source is a commercially available laser video projector (Sony/Anybeam HAT). Both of them have integrated different colored laser diodes and the desired image is displayed with the help of a MEMS mirror. In this project, we have built a openSIM/ISM setup, which the imaging and sample modules of the setup are shared. The illumination of the openISM module is shown in Fig. 1. 
<p align="center">
<img src="./IMAGES/Setup_ISM.png" width="600">
</p>
***Fig. 1*** *The openISM illumination module based on our UC2 CAD design. Comparing to the openSIM module, the ISM part is relative simply thanks to the projector, which has integrated laser diodes and MEMS mirror. The laser beam is directed twice with the help of two mirrors and focus on the back focal plane of the objective.*

The spectra of both projectors are illustrated in Fig. 2
<p align="center">
<img src="./IMAGES/Spectra.png" width="600">
</p>
***Fig. 2*** *Spectra of Sony/Anybeam laser projector.Both projectors used the laser diodes which have similar spectra. They can used to excite fluorescent such as GFP, mCherry and Alexa Flour 647.*

## Alignmen of the telescope
After collimate the beam with first lens, the beam is directed by two mirrors to the second 165 mm lens. After the second lens, the beam should refocus at the back focal plane (BFP) of the objective and reimage the MEMS mirror.

<p align="center">
<img src="./IMAGES/CollimatedBeam.png" width="500">
</p>
***Fig. 2*** *The collimated illumination beam after the first lens of the telescope with the both projectors. The beam should keep the same size irrelevantly to the distance. Blow shows the detail of the beam at the wall. The beam shape from the Sony projector is not only a round spot due to the freeform lens in front of the DMD.*

## Alignment of the
<p align="center">
<img src="./IMAGES/" width="500">
</p>
***Fig. 3*** **