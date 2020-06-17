//Cube insert: Lens holder with clamp 

/* [User Parameters] */
//Lens diameter - measure the diameter of your lens carefully and insert the value in millimetres. The holder can be used for lenses with a diameter from 9 mm to 42 mm.
lens_diameter = 25.4; //[9:0.01:42]
//Edge thickness - measure the thickness of your lens as close to the outer edge as possible.
lens_edge_thickness = 1.5; //[0.5:0.01:8]
// Which part would you like to print?
part = "first"; // [first:Both - Holder AND Clamp,second:Holder ONLY,third:Clamp ONLY]

/* [Hiden] */
$fn = 80;
eps = .002;
a = 49.8;
b = 33.6;
c = 6.28;
d = 53.8;
angle = 45;
h = lens_edge_thickness < 4.1 ? 5 : 5+(lens_edge_thickness-3); //holder height
h1 = 3; //clamp rims height
t = 1.5; //clamp ring thickness

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
            cube([a,b,h], center=true);
            cube([b,a,h], center=true);
            rotate(a=[0,0,angle]){
                cube([c,d,h], center=true);
            }
            rotate(a=[0,0,-angle]){
                cube([c,d,h], center=true);
            }
        }
        union() {
            cylinder(h+eps,d=lens_diameter-2, center = true); //hole
            translate([0,0,(h-lens_edge_thickness)/2]){
                cylinder(lens_edge_thickness+eps,d=lens_diameter+0.7, center = true); //rim to hold the lens
            }
        }
    }
    translate([0,0,(h+h1-0.1)/2]){  //rim for the clamp
        difference(){
                cylinder(h1+0.1,d1=lens_diameter+2.7, d2=lens_diameter+1.5, center = true);
                cylinder(h1+0.1+eps,d=lens_diameter+0.7, center = true);
        }
    }
}

module lens_clamp() {
    translate([a/2+lens_diameter/2+7,0,-(h-t)/2]){
        difference(){   //bottom ring
            cylinder(t, d=lens_diameter+4.9, center = true);
            cylinder(t+eps, d=lens_diameter-1, center = true);
        }
        translate([0,0,+(h1+t)/2]){
            difference(){   //outer rim
                cylinder(h1,d=lens_diameter+4.9, center = true);
                cylinder(h1+eps,d=lens_diameter+2.9, center = true);
            }
            difference(){   //inner rim
                cylinder(h1,d=lens_diameter+0.5, center = true);
                cylinder(h1+eps,d=lens_diameter-1, center = true);
                }
            }
        }
    }


