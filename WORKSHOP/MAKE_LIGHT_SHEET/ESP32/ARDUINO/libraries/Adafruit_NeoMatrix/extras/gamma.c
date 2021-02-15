// THIS IS NOT ARDUINO CODE -- DON'T INCLUDE IN YOUR SKETCH.  It's a
// command-line tool that outputs a gamma correction table to stdout;
// redirect or copy and paste the results into header file for the
// NeoMatrix library code.
// Optional 1 parameter: bit depth (default=5, for 32 output levels).

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define GAMMA 2.6

int planes = 5;

int main(int argc, char *argv[])
{
	int i, maxval;

	if(argc > 1) planes = atoi(argv[1]);

	maxval = (1 << planes) - 1;

	(void)printf(
	  "#ifndef _GAMMA_H_\n"
	  "#define _GAMMA_H_\n"
	  "\n"
	  "#ifdef __AVR\n"
	  " #include <avr/pgmspace.h>\n"
	  "#else\n"
	  " #ifndef PROGMEM\n"
	  "  #define PROGMEM\n"
	  " #endif\n"
	  "#endif\n"
	  "\n"
	  "static const uint8_t PROGMEM\n"
	  "  gamma%d[] = {\n"
	  "    ", planes);

	for(i=0; i<=maxval; i++) {
		(void)printf("%3d",
		  (int)(pow((float)i / (float)maxval, GAMMA) *
		  (float)255.0 + 0.5));
		if(i < maxval) (void)printf(((i & 15) == 15) ? ",\n    " : ",");
	}

	(void)puts(
	  "\n};\n\n"
	  "#endif // _GAMMA_H_");

	return 0;
}
