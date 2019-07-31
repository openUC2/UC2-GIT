$fn=500;
L=50; //Länge
R=18.8*0.5; // Radius Linse
HL = 3.2; // Höhe Linse
E=0.01;
H=3; //Höhe Platte
difference(){
    translate([0,0,0])cube([L,L,H]);
    translate([0.5*L,0.5*L,-E])cylinder(h=4,r=R-0.5);
    translate([10,10,-E])cylinder(h=4,r1=2.5,r2=2.25);
    translate([10,40,-E])cylinder(h=4,r1=2.5,r2=2.25);
    translate([40,40,-E])cylinder(h=4,r1=2.5,r2=2.25);
    translate([40,10,-E])cylinder(h=4,r1=2.5,r2=2.25);
    translate([L,L,-E])cylinder(h=4,r=11);
    translate([L,0,-E])cylinder(h=4,r=11);
    translate([0,L,-E])cylinder(h=4,r=11);
    translate([0,0,-E])cylinder(h=4,r=11);
    }
    
difference(){
    translate([0.5*L,0.5*L,H])cylinder(h=HL,r=R+0.5);
    translate([0.5*L,0.5*L,H-E])cylinder(h=HL+2*E,r=R+0.1);
    }
    
    
