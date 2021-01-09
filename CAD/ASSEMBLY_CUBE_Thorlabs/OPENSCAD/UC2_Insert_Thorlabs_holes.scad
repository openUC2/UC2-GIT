//Cube Insert: Thorlabs Cage System Rods 

/* [User Parameters] */
//If the holes of this insert are too loose or too tight for the Thorlabs rods, adjust their diameter by changing the offset (in millimetres)
off_dr = 0; //[-1:0.1:1]

/* [Hiden] */
//basic insert design
$fn = 80;
eps = .002;
a = 49.8;
b = 33.6;
c = 6.28;
d = 53.8;
h = 6;
//specific for this insert
dh = 35; //center hole diameter
dr = 6.02; //rod hole diameter
rp = 15; //rod pitch - half

insert_thorlabs();

module insert_thorlabs(){
    difference(){
        difference(){
            insert();
            cylinder(d = dh,h = h+eps,center = true);
        }
        translate([rp,rp,0]) cylinder(d = dr+off_dr,h = h+eps,center = true);
        translate([rp,-rp,0]) cylinder(d = dr+off_dr,h = h+eps,center = true);
        translate([-rp,rp,0]) cylinder(d = dr+off_dr,h = h+eps,center = true);
        translate([-rp,-rp,0]) cylinder(d = dr+off_dr,h = h+eps,center = true);
    }
}

module insert() {
    union() {   //basic insert design
            cube([a,b,h], center=true);
            cube([b,a,h], center=true);
            rotate(a=[0,0,45]){
                cube([c,d,h], center=true);
            }
            rotate(a=[0,0,-45]){
                cube([c,d,h], center=true);
            }
        }
}