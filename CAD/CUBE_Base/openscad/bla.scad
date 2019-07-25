$fn=50;
eps=.001;

a=40;
b=5;

crv=1/3;

basecube();

//strebenz();

module basecube() {
    tripod();
translate([a+2*b,0,0])rotate([0,0,90])tripod();
translate([a+2*b,a+2*b,0])rotate([0,0,180])tripod();
translate([0,a+2*b,0])rotate([0,0,270])tripod();
}

module tripod() {
    corner();
    translate([0,0,b])strebenz();
    translate([0,b,0])strebeny();
    translate([b,0,0])strebenx();
    //translate([a+2*b,0,0])rotate([0,0,90])corner();
}

// Streben
module strebenz() {
    tmp=b*crv;
    union() {
        translate([tmp,tmp,0])cylinder(r=tmp,h=a);
        translate([tmp,0,0])cube([b-tmp,b,a]);
        translate([0,tmp,0])cube([b,b-tmp,a]);
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
    union() {
        translate([tmp,tmp,tmp])sphere(r=b*crv);
        
        translate([tmp,tmp,tmp])cylinder(r=tmp,h=b-tmp);
        translate([tmp,0,tmp])cube([b-tmp,b,b-tmp]);
        translate([0,tmp,tmp])cube([b,b-tmp,b-tmp]);
        
        translate([tmp,tmp,tmp])rotate([0,90,0])cylinder(r=tmp,h=b-tmp);
        translate([tmp,tmp,tmp])rotate([-90,0,0])cylinder(r=tmp,h=b-tmp);
        translate([tmp,tmp,0])cube([b-tmp,b-tmp,b]);
    }
}