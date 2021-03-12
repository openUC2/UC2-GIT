//Cube insert: Perpendicular 
/* [User] */
eyepiece_diameter = 30; //[10:0.01:42]

/* [Hiden] */
$fn = 80;
eps = .002;
a = 49.8;
b = 33.6;
c = 6.28;
d = 53.8;
h = 5;
IM_offset = 0.2;

insert();

module insert() {
    difference() {
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
        cylinder(h+eps,d=eyepiece_diameter, center = true);
    }
}