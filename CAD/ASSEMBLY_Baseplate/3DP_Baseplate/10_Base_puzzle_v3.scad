//Cube insert: Baseplate puzzle piece 

/* [User Parameters] */
//screw offset
scr_offset = 0; //[-0.1:0.1:0.35]
//magnet offset
mag_offset = 0; //[-0.1:0.1:0.35]
//male puzzle offset
puzzle_m_offset = 0; //[0:0.1:0.4]
//female puzzle offset
puzzle_f_offset = 0; //[0:0.1:0.4]


/* [Hiden] */
$fn = 80;
eps = .002;
a = 50; //UC2 unit size
h = 5; //height of the baseplate
b = 34; //size of the inner empty space
mag = 4.85; //magnet hole diameter default
scr = 5.3; //screw hole diameter default
s1 = 10.5; //screw hole to side distance 1 (x,y)
s2 = 4.2; //screw hole to side distance 2 (x,y)
r1 = 2; //radius of fillets
m6_1 = 5; //hole for M6 screw diameter
m6_2 = 8; //hole for M6 screw head diameter
m6_3 = 3; //hole for M6 screw head depth
m6_4 = 4; //hole for M6 screw to side distance
puzz1 = 10; //puzzle protrusion neck thickness
puzz2 = 1.5; //puzzle protrusion neck length
puzz3 = 0.5; //puzzle protrusion distance 3
puzz4 = 0.075; //male to female puzzle protrusion offset 
puzz5 = 0.41; //puzzle protrusion radius of fillets

baseplate_puzzle ();

module baseplate_puzzle () {
    difference () {
    union () { //four corners together
        corner();
        translate([a,0,0]){rotate([0,0,90]){corner();}}
        translate([0,a,0]){rotate([0,0,270]){corner();}}
        translate([a,a,0]){rotate([0,0,180]){corner();}}
        translate([a/2-puzz1/2,-(r1+puzz2),0]){puzzle_m();} //male puzzle
        translate([-(r1+puzz2),a/2+puzz1/2,0]){rotate([0,0,270]){puzzle_m();}} //male puzzle
    }
    translate([a/2,m6_4,-eps/2]){m6_hole();} //M6 screw hole
    translate([m6_4,a/2,-eps/2]){m6_hole();} //M6 screw hole
    translate([a/2-puzz1/2,a-r1-puzz2,0]){puzzle_f();} //female puzzle
    translate([a-r1-puzz2,a/2+puzz1/2,0]){rotate([0,0,270]){puzzle_f();}} //female puzzle
    }
}
module corner () {
    union () {
        difference () {
            cube([a/2,a/2,h]);
            difference () { //outer corner fillet
                translate([-eps,-eps,-eps/2]){cube([r1,r1,h+eps]);}
                translate([r1,r1,-eps/2]){cylinder(h+2*eps,r=r1);}
            }
            translate([(a-b)/2,(a-b)/2,-eps/2]){cube([b/2+eps,b/2+eps,h+eps]);}
            translate([h,h,-eps/2]){cylinder(h+eps,d=mag+mag_offset);} //hole for magnet
            translate([s1,s2,-eps/2]){cylinder(h+eps,d=scr+scr_offset);} //hole for snap fit
            translate([s2,s1,-eps/2]){cylinder(h+eps,d=scr+scr_offset);} //hole for snap fit
        }
        translate([(a-b)/2,(a-b)/2,0]){ //inner corner fillet
            difference () {
                translate([-eps,-eps,]){cube([r1,r1,h+eps]);}
                translate([r1,r1,-eps/2]){cylinder(h+2*eps,r=r1);}
            }
        }
    }
}
module m6_hole () {
    union () {
        cylinder(h+eps,d=m6_1);
        translate([0,0,h-m6_3]){cylinder(m6_3+eps,d=m6_2);}
    }
}
module puzzle_m () {
    union () {
        cylinder(h+eps,r=r1-puzzle_m_offset);
        translate([puzz1,0,0,]){cylinder(h,r=r1-puzzle_m_offset);}
        translate([0,-r1+puzzle_m_offset,0]){cube([puzz1,2*(r1-puzzle_m_offset),h]);}
        translate([puzzle_m_offset,r1-puzzle_m_offset,0]){cube([puzz1-2*puzzle_m_offset,puzz2+puzzle_m_offset,h]);}
        translate([puzz1-puzzle_m_offset,r1-puzzle_m_offset,0]){difference () {
                translate([-eps,-eps,0]){cube([puzz3,puzz3,h]);}
                translate([puzz3,puzz3,-eps/2]){cylinder(h+eps,r=puzz3);}
            }}
        translate([puzzle_m_offset,r1-puzzle_m_offset,0]){rotate([0,0,90]){difference () {
                translate([-eps,-eps,0]){cube([puzz3,puzz3,h]);}
                translate([puzz3,puzz3,-eps/2]){cylinder(h+eps,r=puzz3);}
            }}}
    }
}
module puzzle_f () {
    union () {
        cylinder(h+eps,r=r1+puzz4+puzzle_f_offset);
        translate([puzz1,0,-eps/2]){cylinder(h+eps,r=r1+puzz4+puzzle_f_offset);}
        translate([0,-r1-puzz4-puzzle_f_offset,-eps/2]){cube([puzz1,2*(r1+puzz4+puzzle_f_offset),h+eps]);}
        translate([-1.25*puzzle_f_offset,r1+puzz4+puzzle_f_offset,-eps/2]){cube([puzz1+2*puzz4+2*puzzle_f_offset,puzz2,h+eps]);}
        translate([puzz1+2*puzz4+0.75*puzzle_f_offset,r1+0.5*puzz4+0.75*puzzle_f_offset,0]){difference () {
                translate([-eps,-eps,-eps/2]){cube([puzz5,puzz5,h+eps]);}
                translate([puzz5,puzz5,-eps/2]){cylinder(h+2*eps,r=puzz5);}
            }}
        translate([puzz4-1.5*puzzle_f_offset,r1-puzz4+1.25*puzzle_f_offset,0]){rotate([0,0,90]){difference () {
                translate([-eps,-eps,-eps/2]){cube([puzz5,puzz5,h+eps]);}
                translate([puzz5,puzz5,-eps/2]){cylinder(h+2*eps,r=puzz5);}
            }}}
    }
}