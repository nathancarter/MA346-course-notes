
size( 200 );

real cw = 2;
real rh = 1;
int nc = 3;
int nr = 7;
int ri = 2;
real hofs = 10;
pen light = rgb(0.8,0.8,0.8);
pen emph = linewidth(2);

void box_at ( real i, real j, pen p = black, real hofs = 0, string text = "" ) {
    draw( shift(hofs,0) * box( (i*cw,j*rh), ((i+1)*cw,(j+1)*rh) ), p );
    label( text, shift(hofs,0) * ((i+0.5)*cw,(j+0.5)*rh) );
}

for ( int i = 0 ; i < nc ; ++i )
    for ( int j = 0 ; j < nr ; ++j )
        box_at( i, j, light );
box_at( 0, ri, emph, text="$i$" );
box_at( 1, ri, emph, text="$c$" );
box_at( 2, ri, emph, text="$v$" );

for ( int i = 0 ; i < nc-1 ; ++i )
    for ( int j = 0 ; j < nr ; ++j )
        box_at( i, j, light, hofs );
box_at( 0, ri, emph, hofs, "$i$" );
box_at( 1, nr-1, emph, hofs, "$c$" );
box_at( 1, ri, emph, hofs, "$v$" );

draw( ((nc+0.5)*cw,nr/2*rh)--(-0.5cw+hofs,nr/2*rh), Arrow );

