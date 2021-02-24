//Cube insert: Perpendicular 
// Is this insert for a 3D printed cube or for a cube produced by injection molding?
3D_printed_cube = "IM"; // [IM, 3Dprint]

/* [Hiden] */
$fn = 80;
eps = .002;
a = 49.8;
b = 33.6;
c = 6.28;
d = 53.8;
h = 5;
IM_offset = 3D_printed_cube == "3Dprint" ? 0 : 0.2;

insert();

module insert() {
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
}
