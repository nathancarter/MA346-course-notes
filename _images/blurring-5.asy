
size( 600 );

real width = 4;
real height = 4;
real hsep = 2;
transform over = shift( (width+hsep,0) );

draw( (-0.1,0)--(width,0), Arrow );
draw( (0,-0.1)--(0,height), Arrow );
draw( over * ( (-0.1,0)--(width,0) ), Arrow );
draw( over * ( (0,-0.1)--(0,height) ), Arrow );

int numpoints = 20;
int randseed = 8;
real radius = 0.5;

real rbtwn ( real a, real b ) { return unitrand()*(b-a)+a; }

pair[] points = new pair[numpoints];
srand( randseed );
pair randpt () {
    real x = rbtwn(0.15width,0.85width);
    return (x,height-x) + dir(45)*rbtwn(-1,1);
}
for ( int i = 0 ; i < numpoints ; ++i ) { points[i] = randpt(); }

real dist_from_pts ( pair p ) {
    real result = width+height;
    for ( int i = 0 ; i < numpoints ; ++i ) {
        real dist = length( p - points[i] );
        if ( dist < result ) result = dist;
    }
    return result;
}
pair edgept ( pair start, pair walk, real dist ) {
    pair step = unit( walk ) * 0.1;
    pair result = start;
    while ( dist_from_pts( result ) < dist ) { result += step; }
    return result;
}

pair center = (0,0);
for ( int i = 0 ; i < numpoints ; ++i ) center += points[i] / numpoints;
guide boundary = circle( center, 0.5width );
filldraw( over * boundary, rgb(0.8,0.8,1), blue+linewidth(1) );

for ( int i = 0 ; i < numpoints ; ++i ) {
    dot( points[i], blue+linewidth(6) );
    dot( over * points[i], blue+linewidth(3) );
}

