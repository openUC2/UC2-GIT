$fn=100;
L=50; //Länge
R=18.8*0.5; // Radius Linse
HL = 3.2; // Höhe Linse
E=0.01;
H=3; //Höhe Platte
    
    
difference(){
    translate([0.5*L,0.5*L,HL+5])cylinder(h=HL,r=R+2.5);
    translate([0.5*L,0.5*L,HL+5-E])cylinder(h=HL+2*E,r1=R+1.65,r2=R+1.55);
    }
difference(){
    translate([0.5*L,0.5*L,2*HL+5])cylinder(h=1,r=R+3.5);
    translate([0.5*L,0.5*L,2*HL+5-E])cylinder(h=2,r=R-0.5);
    }    