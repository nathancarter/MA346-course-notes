
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
for ( int i = 0 ; i < numpoints ; ++i ) {
    real x = rbtwn(0.15width,0.85width);
    points[i] = (x,height-x);
    points[i] += dir(45)*rbtwn(-1,1);
}

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

int num_edge_pts = 5;
int num_cap_pts = 5;
int num_circle_pts = 20;
guide boundary;
for ( int i = 0 ; i < num_circle_pts ; ++i ) {
    real angle = i * 360.0 / num_circle_pts;
    pair next = edgept( (width/2,height/2), dir(angle), 0.5 );
    boundary = boundary .. next;
}
boundary = boundary .. cycle;
filldraw( over * boundary, rgb(0.8,0.8,1), blue+linewidth(1) );

for ( int i = 0 ; i < numpoints ; ++i ) {
    dot( points[i], blue+linewidth(6) );
    dot( over * points[i], blue+linewidth(3) );
}

