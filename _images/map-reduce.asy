
size( 800 );

picture dataframe ( int num_rows, int num_cols,
                    real row_height = 1, real col_width = 1.5,
                    bool row_header = true, bool col_header = true,
                    string[] row_headers = {}, string[] col_headers = {} ) {
    pair dfpt ( real x, real y ) {
        return row_header ? (min(x,1)+(x-min(x,1))*col_width,-y*row_height)
                          : (x*col_width,-y*row_height);
    }
    picture result = new picture;
    int start_x = row_header ? 1 : 0;
    int start_y = col_header ? 1 : 0;
    for ( int i = 0 ; i <= num_rows + start_y ; ++i ) {
        draw( result, dfpt(0,i)--dfpt(num_cols+start_x,i) );
        if ( row_header && i < num_rows + start_y - 1 ) {
            string header = i < row_headers.length ? row_headers[i]
                                                   : format( "%d", i );
            label( result, header, dfpt(0.5,i+1.5) );
        }
    }
    for ( int i = 0 ; i <= num_cols + start_x ; ++i ) {
        draw( result, dfpt(i,0)--dfpt(i,num_rows+start_y) );
        if ( col_header && i < num_cols + start_x - 1 ) {
            string header = i < col_headers.length ? col_headers[i]
                                                   : format( "Col %d", i );
            label( result, header, dfpt(i+1.5,0.5) );
        }
    }
    fill( result, box( dfpt(0,start_y),
                       dfpt(num_cols+start_x,num_rows+start_y) ),
          opacity(0.2) );
    fill( result, box( dfpt(start_x,0),
                       dfpt(num_cols+start_x,num_rows+start_y) ),
          opacity(0.2) );
    return shift( -dfpt(start_x,start_y) ) * result;
}

int nrows = 10;

add( dataframe( nrows, 3, col_width = 2,
                col_headers = new string[]{
                    "Semester","\# Students","\# Teachers"} ) );

label( "\Large\bf MAP", (8,2), red );
label( "\parbox{1.6in}{\texttt{df['\# Students'] /}\\ "
     + "\texttt{\phantom{x}df['\# Teachers']}}",
       (8,1), red );
for ( int i = 0 ; i < nrows ; ++i )
    draw( (7,-i-0.5)--(9,-i-0.5), red+linewidth(1), Arrow );

add( shift( 11, 0 )
   * dataframe( nrows, 1, col_width = 2,
                col_headers = new string[]{"S/T Ratio"} ) );

label( "\Large\bf REDUCE", (15,2), blue );
label( "\texttt{.max()}", (15,1), blue );
draw( (14,0){E}..{E}(16,-5) ^^ (16,-5){W}..{W}(14,-10), blue+linewidth(1) );

label( "\parbox{2.5in}{\raggedright\Large\bf Maximum Student/ Teacher Ratio}",
       (18,-2), purple );
label( "\parbox{2.5in}{\texttt{( df['\# Students'] /}\\ "
     + "\texttt{\phantom{xx}df['\# Teachers'] ).max()}}",
       (18,-3.5), purple );
add( shift( (17,-4.5) ) * dataframe( 1, 1, false, false, col_width=2 ) );

