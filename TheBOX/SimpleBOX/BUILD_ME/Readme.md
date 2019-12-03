# The BOX

This is a guide for building the [SimpleBOX](../SimpleBOX). The guide for the [FullBOX can be found here.](../../STL)

## 3D Printing:

A quick printing tutorial can be found here:
[![UC2 YouSeeToo - How to print the base-cube?](./IMAGES/UC2_TutorialPrintYoutube.PNG)](https://www.youtube.com/watch?v=JswW8BexnC4&feature=youtu.be)

We have a good experience with this printer and settings:
* Prusa i3/MK3S
  * PLA 1,75 mm, for one Box: 0,455 kg = 152,53 m = 69 hours = 13 €
  * Profile Optimal 0,15 mm, infill 20%, no support, 215/60°C
  * [Hint](./IMAGES/prus_printing_SimpleBOX.pdf)

## List of parts for the SimpleBOX

### Housing

Link - name of part             |  Amount
:-------------------------:|:----------------------------:
[(01) Basic Cube 2×1](./STL/01_10_Cube_2x1_v2.stl)  |  1 piece
[(02) Basic Lid 2×1](./STL/02_10_Lid_el_2x1_v2.stl)  |  1 piece
[(03) Basic Cube 1×1](./STL/03_10_Cube_1x1_v2.stl)  |  10 pieces
[(04) Basic Lid 1×1](./STL/04_10_Lid_1x1_v2.stl)  |  10 pieces
[(18) Baseplate 4×1](./STL/18_Assembly_base_4x1.stl)  |  3 pieces
[(19) Baseplate 4×2](./STL/19_Assembly_base_4x2.stl)  |  1 piece

### Inserts

Link - name of part             |  Amount |  Comment
:-------------------------:|:-------------------------:|:-------------------------:
[(05) Z-Stage Focusing Insert](./STL/05_20_focus_inlet_triangle_spiral_v6.stl)  |  1 piece  | Rotate the part in your slicer before printing. Always print it laying on the flat side.
[(06) Z-Stage Coupling Screw M4](./STL/06_30_Coupling_Screw_28BYJ_M4.stl) |  1 piece   | This couples the gear to the screw, which moves the objective.
[(07) Z-Stage Plate](./STL/07_20_focus_inlet_plate.stl) |  1 piece   | The plate holds the gear and screw in position, allowing the only to rotate but not to wobble.
[(08) Z-Stage Gear](./STL/08_20_focus_inlet_gear.stl) |  1 piece   | Kindly borrowed from [openflexure](https://openflexure.org).
[(09) Z-Stage Sample Clamp](./STL/09_30_Sampleclamp_generic_5mmMagnets.stl)  |  1 piece | To hold the microscope slide.
[(10) Eyepiece/flashlight mount](./STL/10_20_Cube_Insert_Holder_flashlight_eyepiece_v2.stl)  |  2 pieces | Diameter fits for the listed eyepiece and flashlight.
[(11) Mirror Holder 45° 30×30mm²](./STL/11_20_Cube_Insert_Mirror_Holder_30x30Mirror_v2.stl)  |  2 pieces | Size fits for the listed mirrors.
[(12) Generic Sample Holder](./STL/12_20_Cube_insert_Sample_holder.stl)  |  1 piece | In the SimpleBOX, it is used to hold the object in the projector setup.
[(13) Generic Sample Holder Clamp](./STL/13_20_Cube_Insert_Sample_clamp.stl)  |  1 piece | To fix the sample.
[(14) Lens Holder - Thick lens](./STL/14_20_Lens_mount_thick_lens.stl)  |  1 piece | Diameter fits for the listed lenses (25 mm). The thick holder is for the diverging lens.
[(15) Lens Holder - Thin lens](./STL/15_20_Lens_mount_Thin_lens.stl)  |  4 pieces | Diameter fits for the listed lenses (25 mm). The thin holder is for the converging lenses.
[(16) Lens Holder Clamp](./STL/16_20_Lens_mount_clamp.stl)  |  5 pieces | Diameter fits for the listed lenses (25 mm).
[(17) Smartphone Holder](./STL/17_30_Smartphone_Holder.stl)  |  1 piece | Which belongs together with the eyepiece cube.

## Shopping
### What to buy

Link - name of part             |  Amount |  Comment
:-------------------------:|:----------------------------:|:-------------------------:
[Microscope objective 4×](https://de.aliexpress.com/item/32947647522.html?spm=a2g0x.search0104.3.54.6cf57a4c3DwsTO&transAbTest=ae803_3&ws_ab_test=searchweb0_0%2Csearchweb201602_6_10065_10130_10068_10890_10547_319_10546_317_10548_10545_10696_10084_453_454_10083_10618_10307_537_536_10902_10059_10884_10887_321_322_10103%2Csearchweb201603_6%2CppcSwitch_0&algo_pvid=06d972be-b176-4446-8665-56d9e61a8d2c&algo_expid=06d972be-b176-4446-8665-56d9e61a8d2c-7)  |  1 piece | It is possible to use 10× objective as well, but we recommend 4× for this setup.
[Eyepiece 20×](https://de.aliexpress.com/item/32965050204.html?spm=a2g0o.productlist.0.0.7aa657eeefLUfu&algo_pvid=cd60fca0-3fa5-4191-9ce9-303815e2afa7&algo_expid=cd60fca0-3fa5-4191-9ce9-303815e2afa7-1&btsid=76036b58-6717-4d1f-a4a0-c3d4bacd0450&ws_ab_test=searchweb0_0,searchweb201602_2,searchweb201603_52)  |  1 piece | The holder is designed for an eyepiece of this diameter.
[Lens 100 mm](https://www.comaroptics.com/components/lenses)  |  2 pieces |100 PQ 25
[Lens 50 mm](https://www.comaroptics.com/components/lenses)  |  1 piece |50 PQ 25
[Lens 40 mm](https://www.comaroptics.com/components/lenses)  |  1 piece |40 PQ 25
[Lens -50 mm](https://www.comaroptics.com/components/lenses)  |  1 piece |50 NQ 25
[Mirror](https://www.amazon.de/Rayher-14548606-Spiegelmosaik-selbstklebend-SB-Btl/dp/B008KJ8438/ref=pd_bxgy_201_img_3/258-8761405-4543762?_encoding=UTF8&pd_rd_i=B008KJ8438&pd_rd_r=80fd534c-997b-4a19-b91a-9bf38dbf4ade&pd_rd_w=4DEXV&pd_rd_wg=7SLRE&pf_rd_p=98c98f04-e797-4e4b-a352-48f7266a41af&pf_rd_r=N95R9S45MNSYNQX2BAJE&psc=1&refRID=N95R9S45MNSYNQX2BAJE)  |  2 pieces | Only 2 pieces needed.
[Flashlight](https://www.pollin.de/p/led-taschenlampe-alu-5-w-cree-led-3xmicro-schwarz-b-ware-535448)  |  1 piece | Light source for the projector and microscope.
[Magnets](https://www.magnetladen.de/kugelmagnet-5-mm-n42-nickel/)  |  84 pieces | Diameter 5 mm.
[Screws](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)  |  ~120 pieces | M3×12, galvanized steel - ~50  pieces; M3×8, galvanized steel - ~50 pieces; M3×5, galvanized steel, worm screw - 4 pieces; M3×12, galvanized dteel, worm screw - 2 pieces; M4×20, not magnetic - 1 pieces; M4 nut
