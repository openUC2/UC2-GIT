$fn=50;
eps=.001;

a=34; // Strebenlänge
b=7.9; // Strebenbreite
c=3.5; // Gerade Strecke Streben

crv=1/3; // Curvature
scoff=.65; // Screw offset from outside
scr=1.43; // Screw radius
sch=7; // Screw length (height)

basecube();

//lid();
//corner();

//strebenz();

module basecube() {
    union() {
        tripod();
        translate([a+2*b,0,0])rotate([0,0,90])tripod();
        translate([a+2*b,a+2*b,0])rotate([0,0,180])tripod();
        translate([0,a+2*b,0])rotate([0,0,270])tripod();
    }
}

module lid() {
    translate([0,0,b])mirror([0,0,1]) {
        union() {
            corner();
            translate([0,b,0])strebeny();
            translate([b,0,0])strebenx();
            translate([a+2*b,0,0])rotate([0,0,90]) {
                corner();
                translate([b,0,0])strebenx();
            }
            translate([a+2*b,a+2*b,0])rotate([0,0,180]) {
                corner();
                translate([b,0,0])strebenx();
            }
            translate([0,a+2*b,0])rotate([0,0,270])corner();
        }
    }
}

module tripod() {
    union() {
        corner();
        translate([0,0,b])strebenz();
        translate([0,b,0])strebeny();
        translate([b,0,0])strebenx();
        //translate([a+2*b,0,0])rotate([0,0,90])corner();
    }
}

// Streben
module strebenz() {
    tmp=b*crv;
    difference() {
        union() {
            translate([tmp,tmp,0])cylinder(r=tmp,h=a);
            translate([tmp,0,0])cube([b-tmp,b,a]);
            translate([0,tmp,0])cube([b,b-tmp,a]);
        }
        
        // Schräge im Innern
        translate([b,c,-eps])rotate([0,0,45])cube([1.5*b,1.5*b,a+2*eps]);
        
        // Schraubenlöcher
        translate([scoff*b,scoff*b,-eps])cylinder(r=scr,h=sch);
        translate([scoff*b,scoff*b,a-sch+eps])cylinder(r=scr,h=sch);
    }
}

module strebenx() {
    rotate([0,0,90])rotate([90,0,0])strebenz();
}

module strebeny() {
    translate([0,a,0])rotate([90,0,0])strebenz();
}

// Ecke
module corner() {
    tmp=b*crv;
    difference() {
        union() {
            translate([tmp,tmp,tmp])sphere(r=b*crv);
            
            translate([tmp,tmp,tmp])cylinder(r=tmp,h=b-tmp);
            translate([tmp,0,tmp])cube([b-tmp,b,b-tmp]);
            translate([0,tmp,tmp])cube([b,b-tmp,b-tmp]);
            
            translate([tmp,tmp,tmp])rotate([0,90,0])cylinder(r=tmp,h=b-tmp);
            translate([tmp,tmp,tmp])rotate([-90,0,0])cylinder(r=tmp,h=b-tmp);
            translate([tmp,tmp,0])cube([b-tmp,b-tmp,b]);
        }
        
        // Schraubenlöcher
        translate([scoff*b,scoff*b,-eps])cylinder(r=scr,h=b+2*eps);
        rotate([90,0,0])translate([scoff*b,scoff*b,-b-eps])cylinder(r=scr,h=b+2*eps);
        rotate([0,90,0])translate([-scoff*b,scoff*b,-eps])cylinder(r=scr,h=b+2*eps);
    }
}