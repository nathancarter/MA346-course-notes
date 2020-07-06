
void boxed ( string main, string subtitle, pair topleft, pair botright,
             pen color, picture pic )
{
    real margin = 0.02;
    filldraw( pic,
              box( topleft+(margin,-margin), botright+(-margin,margin) ),
              color, linewidth(1) );
    pair center = interp( topleft, botright, 0.5 );
    if ( subtitle == "" ) {
        label( pic, "{\Large "+main+"}", center );
    } else {
        label( pic, "{\Large "+main+"}", center, N );
        label( pic, "{\small "+subtitle+"}", center, S );
    }
}

pen my_gray = rgb(221/255,221/255,221/255);
pen my_blue = rgb(221/255,221/255,255/255);
pen my_green = rgb(221/255,255/255,221/255);

picture pivot = new picture;
size( pivot, 600 );
boxed( "index", "", (0,0), (1,-2), my_gray, pivot );
boxed( "columns",
       "\parbox{1in}{\centering (no repeats within one index entry)}",
       (1,0), (2,-2), my_blue, pivot );
boxed( "values", "", (2,0), (3,-2), my_green, pivot );
draw( pivot, (3.5,-1)--(4.5,-1), Arrow );
boxed( "index", "", (5,0), (6,-2), my_gray, pivot );
boxed( "columns", "", (6,0.3), (8,0), my_blue, pivot );
boxed( "values", "", (6,0), (8,-2), my_green, pivot );
shipout( "table-verb-pivot", pivot, format="pdf" );
// then from prompt, do: convert -density 150 table-verb-pivot.{pdf,png}

picture pivot_table = new picture;
size( pivot_table, 600 );
boxed( "index", "", (0,0), (1,-2), my_gray, pivot_table );
boxed( "columns", "", (1,0), (2,-2), my_blue, pivot_table );
boxed( "values", "", (2,0), (3,-2), my_green, pivot_table );
draw( pivot_table, (3.5,-1)--(4.5,-1), Arrow );
boxed( "index", "", (5,0), (6,-2), my_gray, pivot_table );
boxed( "columns", "", (6,0.3), (8,0), my_blue, pivot_table );
boxed( "values", "aggregated", (6,0), (8,-2), my_green, pivot_table );
shipout( "table-verb-pivot-table", pivot_table, format="pdf" );
// then from prompt, do: convert -density 150 table-verb-pivot-table.{pdf,png}

picture melt = new picture;
size( melt, 600 );
boxed( "id\_vars", "", (0,0), (1,-2), my_gray, melt );
boxed( "value\_vars", "", (1,0.3), (3,0), my_blue, melt );
boxed( "values", "(not an input parameter)", (1,0), (3,-2), my_green, melt );
draw( melt, (3.5,-1)--(4.5,-1), Arrow );
boxed( "id\_vars", "", (5,0), (6,-2), my_gray, melt );
boxed( "value\_vars", "", (6,0), (7,-2), my_blue, melt );
boxed( "values", "", (7,0), (8,-2), my_green, melt );
shipout( "table-verb-melt", melt, format="pdf" );
// then from prompt, do: convert -density 150 table-verb-melt.{pdf,png}

