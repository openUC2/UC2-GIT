//Cube insert: Lens holder with clamp - for lenses with big diameter

/* [User Parameters] */
//Lens diameter - measure the diameter of your lens carefully and insert the value in millimetres. The holder can be used for lenses with a diameter from 42 mm to 50 mm.
lens_diameter = 48.55; //[40:0.01:50]
//Edge thickness - measure the thickness of your lens as close to the outer edge as possible.
lens_edge_thickness = 2.33; //[0.5:0.01:10]
// Which part would you like to print?
part = "first"; // [first:Both - Holder AND Clamp,second:Holder ONLY,third:Clamp ONLY]

/* [Hiden] */
$fn = 80;
eps = .002;
a = 49.8;
b = 33.6;
c = 6.28;
d = 53.8;
h = lens_edge_thickness < 4.1 ? 10 : lens_edge_thickness+6; //holder height
h1 = h - 1.5 - lens_edge_thickness; //clamp rims height
t = 1.5; //clamp ring thickness
IM_offset = 0.2;

print_part();

module print_part() {   //choose part to print holder/clamp/both
	if (part == "first") {
		lens_holder();
        lens_clamp();
	} else if (part == "second") {
		lens_holder();
	} else if (part == "third") {
		lens_clamp();
	} 
}
module lens_holder () {
    difference(){
        union() {   //basic insert design
            cube([a,b+2*IM_offset,h], center=true);
            cube([b+2*IM_offset,a,h], center=true);
            rotate(a=[0,0,45]){
                cube([c,d+2*IM_offset,h], center=true);
            }
            rotate(a=[0,0,-45]){
                cube([c,d+2*IM_offset,h], center=true);
            }
        }
        union() {
            cylinder(h+eps,d=lens_diameter-6, center = true); //hole
            translate([0,0,1.5]){
                scale([1,1.05,1])cylinder(h,d=lens_diameter+0.7, center = true); //rim to hold the lens
            }
        }
    } 
}

module lens_clamp() {
    translate([a/2+lens_diameter/2+7,0,-(h-t)/2]){
        difference(){   //bottom ring
            cylinder(t, d=53.5, center = true);
            cylinder(t+eps, d=lens_diameter-4, center = true);
        }
        translate([0,0,+(h1+t)/2]){
            difference(){   //rim
                scale([1,1.05,1])cylinder(h1,d=lens_diameter+0.65, center = true);
                cylinder(h1+eps,d=lens_diameter-2, center = true);
            }
            }
        }
    }