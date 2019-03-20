## Simple Telescope 

We developed a very easy-to-use setup to let people understand how a telescope works. It guides you through  different varieties of optical designs all with the goal: magnifying of far-away objects (e.g. Stars). 

In the end the setup should look like this here:
![](./IMAGES/Assembly_simple_Telescope.png)

We created a [Workshop-Document](UC2_Telescope.pdf) which goes into details of assembling the Telescope and comes with a quiz to test your knowledge about telescopes. Are you able to answer all of them? 

### Keppler Telescope 
![](./IMAGES/UC2_Kepler.png)

It consists of two lenses with positive focal-length, where the focal lengths (f_1) of the first falls into the focal length (f_2) of the latter one. The magnification is thus given by the ratio of m=f_1/f_2. 

The core idea is to form an image of (red spot) from an object which is infinitely far away, thus having ~plane wave as input. The entrance pupil - namely the diameter of L1 - limits the plane wave. The second lens L2 reimages the red-spot again to infinity, where the outgoing diameter of the rays parallel to the optical axis are (de-)magnified by the ratio m. The eye can then conveniently form an image on the retina.

### Galileo Telescope 
![](./IMAGES/UC2_Galileo.png)
The core idea of the Galileo-Telescope is to magnify objects from far away - suprise! The main difference as you might guess from the two images are the components selected in order to build this setup. Compared to the Keppler telescope, whe have a positive and a negative lens. The concept, that the focal lenght of the first lens falls into the focal length of the latter one is still met, but now the entire setup shrinks because you add a positive f_1 to a negative f_2 which defines the entire length of this instrument: d=f_1+f_2.

Another major difference is, that the image is not flipped compared to the Kepler Telescope! 


## Components 
The CAD parts can also be found [here](../../CAD/SIMPLE-Telescope).

In particular you need the following parts:

####3D-printed components
* 1x [Base Frame](../../CAD/SIMPLE-Telescope/INLINE_HOLOGRAM_00_Base_4x1_v0.stl)
* 2x [Cube Lid](../../CAD/SIMPLE-Telescope/INLINE_HOLOGRAM_10_Lid_el_v0.stl)
* 2x [Cube Lid](../../CAD/SIMPLE-Telescope/INLINE_HOLOGRAM_10_Cube_v0.stl)
* 2x [Lens Holder](../../CAD/SIMPLE-Telescope/Assembly_Custom_Lens_Adapter_11_Lens_Thorlabs_Mount_Customized_B_1.stl)
* 2x [Lens Holder Ring](../../CAD/SIMPLE-Telescope/Assembly_Custom_Lens_Adapter_11_Lens_Thorlabs_Mount_Ring_B_2.stl)

####Lenses (Kepler+Galileo)
* 1x biconvex lens, Diameter=20mm, 50mm
* 1x plano-concave lens, Diameter=20mm, -50mm 
* 1x biconvex lens, Diameter=20mm, 150mm 

####Miscellaneous 
* 4x [Aluminium Rods, Diameter=6mm, length=50mm, EBAY](https://www.ebay.de/itm/Aluminium-rund-6mm-Lange-wahlbar-Rundstange-Alu-AlCuMgPb-Rundmaterial-Stab/142225734720?hash=item211d507c40:m:mAppPewY6qYHfgAQt2GatDg)
* 8x [Ball-Magnets - 5mm, Neo-Dym, AMAZON](https://www.amazon.de/Unbekannt-100-Neodym-Kugelmagnete-5-mm/dp/B00HXLBH6K/ref=pd_sbs_196_4/261-4292290-0235846?_encoding=UTF8&pd_rd_i=B00HXLBH6K&pd_rd_r=985b1a67-4b1e-11e9-b3ce-5b3ae6a6812b&pd_rd_w=Yei4i&pd_rd_wg=eETBx&pf_rd_p=74d946ea-18de-4443-bed6-d8837f922070&pf_rd_r=Z3BJWK5PJB16K7PF8ENR&psc=1&refRID=Z3BJWK5PJB16K7PF8ENR)
* 8x [M3 srews, DIN 912, magnetic (!), 18mm long, AMAZON](https://www.amazon.de/Edelstahl-Innensechskant-Schrauben-Sortiment-250-tlg/dp/B0065GSI34)


##Assembly of the cube
Putting the parts together is as simple as that: 
<p align="center">
<img src="./IMAGES/UC2_assembly.png" width="300">
</p>

##Assembly of the lenses
Putting the parts together is as simple as that: 
<p align="center">
<img src="./IMAGES/Assembly_Custom_Lens_Adapter.png" width="300">
</p>
Put the lens into the inner hole of the adapter, add the retaining ring and you're done. If you have a specifc lens shape, let us know, we can customize the inner diameter in order to make it work! This part goes on the 6mm rod which goes inside cube. 






## Suggestions
If you have any problems or suggestions, please file an issue. Thank you! 