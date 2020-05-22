//UC2 Cube and Lid 

/* [User Parameters] */
// Which part would you like to print?
part = "first"; // [first:Both - Cube Body AND Lid,second:Cube Body ONLY,third:Lid ONLY]

/* [Hiden] */
$fn=80;
eps=.002;

a=33.8; //Edge length
b=8; //Edge width
c=3.55; //Chamfer

crv=2; //Curvature
scoff=4.9; //Screw offset from outside (cube width (49,8)-screw pitch(40))/2
scr_d=2.8; // Screw hole diameter (M3)
scr_l=8; // Screw length (hole length)
scr_hd=5.5; // Screw head diameter (M3)
scr_hl=3.1; // Screw head length (M3)

print_part();

module print_part() {   //choose part to print cube body/lid/both
	if (part == "first") {
		basecube();
        lid();
	} else if (part == "second") {
		basecube();
	} else if (part == "third") {
		lid();
	} 
}

module basecube() {
    union() {
        tripod();
        translate([a+2*b,0,0])rotate([0,0,90])tripod();
        translate([a+2*b,a+2*b,0])rotate([0,0,180])tripod();
        translate([0,a+2*b,0])rotate([0,0,270])tripod();
    }
}

module lid() {
    translate([55,0,0]){
        translate([0,0,b])mirror([0,0,1]) {
            union() {
                corner();
                translate([0,b,0])edge_y();
                translate([b,0,0])edge_x();
                translate([a+2*b,0,0])rotate([0,0,90]) {
                    corner();
                    translate([b,0,0])edge_x();
                }
                translate([a+2*b,a+2*b,0])rotate([0,0,180]) {
                    corner();
                    translate([b,0,0])edge_x();
                }
                translate([0,a+2*b,0])rotate([0,0,270])corner();
            }
        }
    }
}

module tripod() {
    union() {
        corner();
        translate([0,0,b])edge_z();
        translate([0,b,0])edge_y();
        translate([b,0,0])edge_x();
    }
}

//Edge
module edge_z() {
    difference() {
        union() {
            translate([crv,crv,0])cylinder(r=crv,h=a);
            translate([crv,0,0])cube([b-crv,b,a]);
            translate([0,crv,0])cube([b,b-crv,a]);
        }
        //Inner chamfer
        translate([b,c,-eps])rotate([0,0,45])cube([1.5*b,1.5*b,a+2*eps]);
        //Holes for screws
        translate([scoff,scoff,-eps])cylinder(d=scr_d,h=scr_l); //bottom
        translate([scoff,scoff,a-scr_l+eps])cylinder(d=scr_d,h=scr_l); //top
    }
}

module edge_x() {
    rotate([0,0,90])rotate([90,0,0])edge_z();
}

module edge_y() {
    translate([0,a,0])rotate([90,0,0])edge_z();
}

//Corner
module corner() {
    difference() {
        union() {
            translate([crv,crv,crv])sphere(r=crv);
            translate([crv,crv,crv])cylinder(r=crv,h=b-crv);
            translate([crv,0,crv])cube([b-crv,b,b-crv]);
            translate([0,crv,crv])cube([b,b-crv,b-crv]);
            translate([crv,crv,crv])rotate([0,90,0])cylinder(r=crv,h=b-crv);
            translate([crv,crv,crv])rotate([-90,0,0])cylinder(r=crv,h=b-crv);
            translate([crv,crv,0])cube([b-crv,b-crv,b]);
        } 
        //Holes for Screws
        translate([scoff,scoff,-eps])cylinder(d=scr_d,h=b+2*eps); //z direction
        rotate([90,0,0])translate([scoff,scoff,-b-eps])cylinder(d=scr_d,h=b+2*eps); //y direction
        rotate([0,90,0])translate([-scoff,scoff,-eps])cylinder(d=scr_d,h=b+2*eps); //x direction
        
        //Screw heads
        translate([scoff,scoff,-eps])cylinder(d=scr_hd,h=scr_hl);
    }
}