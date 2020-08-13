
size( 300 );

typedef real realfn ( real );

real width = 4;
real height = 4;

transform over ( real howmany ) { return shift((howmany*1.25width,0)); }

real signal ( real x ) {
    return -(x-width/2)^2/12 + (x-width/2)/2 + 0.3height;
}
srand(2);
pair[] points = new pair[]{ };
real noise ( real x ) {
    real y = 0.8sin((100+unitrand()*20)*x);
    points.push( (x,y+signal(x)) );
    return y;
}
real both ( real x ) {
    return signal(x) + noise(x);
}

real silly_fit ( real x ) {
    real[] coeffs = new real[]{
           0.02261193,    -0.62712512,     7.82359827,   -58.02517542,
         284.75176102,  -972.91537698,  2368.32931305, -4124.66923213,
        5075.11241517, -4273.9038744 ,  2323.30761677,  -735.47297485,
         112.30169321,    -5.08953621,    -0.01309237
    };
    real result = 0;
    real term = 1;
    for ( int i = 0 ; i < coeffs.length ; ++i ) {
        result += coeffs[coeffs.length-1-i] * term;
        term = x ^ ( i + 1 );
    }
    return result;
}

picture graph_of ( realfn f, pen color, string title ) {
    picture result = new picture;
    real margin = 0.1;
    int num_points = 70;
    draw( result, (-margin,0)--(width+margin,0), Arrow );
    draw( result, (0,-1-margin)--(0,height-1.5+margin), Arrow );
    guide curve;
    //draw( result, graph( f, 0, width, num_points ), color );
    for ( int i = 0 ; i < num_points ; ++i ) {
        real x = interp( 0, width, i*1.0/(num_points-1) );
        real y = f(x);
        dot( result, (x,y), color );
        curve = curve -- (x,y);
        //write( (x,y) );
    }
    draw( result, curve, color+linewidth(0) );
    label( result, title, (width/2,height-1), N, color );
    clip( result, box((-margin,-1-margin),(width+margin,height-1.5+margin)) );
    return result;
}

//draw( graph( both, 0, width ), black );
//draw( graph( signal, 0, width ), red );
//add( graph_of( signal, blue, "\Large Signal" ) );
//add( over(1) * graph_of( noise, red, "\Large Noise" ) );
//add( over(2) * graph_of( both, black, "\Large Data" ) );
//pair top = (width/2,height-1);
//label( "\Large +", interp( top, over(1)*top, 0.5 ), N );
//label( "\Large =", interp( over(1)*top, over(2)*top, 0.5 ), N );
add( graph_of( both, black, "" ) );
add( graph_of( silly_fit, blue, "" ) );
//draw( wiggle, blue+linewidth(1) );

