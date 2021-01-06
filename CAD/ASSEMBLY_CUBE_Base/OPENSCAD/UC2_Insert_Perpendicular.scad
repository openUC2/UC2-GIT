//Cube insert: Perpendicular 

/* [Hiden] */
$fn = 80;
eps = .002;
a = 49.8;
b = 33.6;
c = 6.28;
d = 53.8;
h = 5;

insert();

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
