
size( 900 );

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

void write_column ( string[] contents, pair start_point,
                    real row_height = 1 )
{
    for ( int i = 0 ; i < contents.length ; ++i )
        label( contents[i], start_point + (0,-i*row_height) );
}

add( dataframe( 10, 3, col_width = 2,
                col_headers = new string[]{"ID\#","Gender","Salary"} ) );
write_column( new string[]{"F","F","F","F","M","M","M","M","NaN","NaN"},
              (3,-0.5) );

label( "\Large\bf SPLIT", (7,4), red );
label( "\texttt{df.groupby('Gender')}", (7,3), red );
for ( int i = 0 ; i < 4 ; ++i )
    draw( (7,-i-0.5)--(9,2-i-0.5), red+linewidth(1), Arrow );
for ( int i = 0 ; i < 4 ; ++i )
    draw( (7,-4-i-0.5)--(9,-4-i-0.5), red+linewidth(1), Arrow );
for ( int i = 0 ; i < 2 ; ++i )
    draw( (7,-8-i-0.5)--(9,-10-i-0.5), red+linewidth(1), Arrow );

add( shift( (11,2) )
   * dataframe( 4, 3, col_width = 2,
                col_headers = new string[]{"ID\#","Gender","Salary"} ) );
write_column( new string[]{"F","F","F","F"}, (14,1.5) );
add( shift( (11,-4) )
   * dataframe( 4, 3, col_width = 2,
                col_headers = new string[]{"ID\#","Gender","Salary"} ) );
write_column( new string[]{"M","M","M","M"}, (14,-4.5) );
add( shift( (11,-10) )
   * dataframe( 2, 3, col_width = 2,
                col_headers = new string[]{"ID\#","Gender","Salary"} ) );
write_column( new string[]{"NaN","NaN"}, (14,-10.5) );

label( "\Large\bf APPLY", (19,4), blue );
label( "\texttt{['Salary']}", (19,3), blue );
for ( int i = 0 ; i < 4 ; ++i )
    draw( (18,  2-i-0.5)--(20,  2-i-0.5), blue+linewidth(1), Arrow );
for ( int i = 0 ; i < 4 ; ++i )
    draw( (18, -4-i-0.5)--(20, -4-i-0.5), blue+linewidth(1), Arrow );
for ( int i = 0 ; i < 2 ; ++i )
    draw( (18,-10-i-0.5)--(20,-10-i-0.5), blue+linewidth(1), Arrow );

add( shift( (22,2) )
   * dataframe( 4, 1, col_width = 2, col_headers = new string[]{"Salary"} ) );
add( shift( (22,-4) )
   * dataframe( 4, 1, col_width = 2, col_headers = new string[]{"Salary"} ) );
add( shift( (22,-10) )
   * dataframe( 2, 1, col_width = 2, col_headers = new string[]{"Salary"} ) );

label( "\Large\bf COMBINE", (26,4), heavygreen );
label( "\texttt{.median()}", (26,3), heavygreen );
draw( (25,2){E}..{E}(26,0) ^^ (26,0){W}..{W}(25,-2),
      heavygreen+linewidth(1) );
draw( (25,-4){E}..{E}(26,-6) ^^ (26,-6){W}..{W}(25,-8),
      heavygreen+linewidth(1) );
draw( (25,-10){E}..{E}(26,-11) ^^ (26,-11){W}..{W}(25,-12),
      heavygreen+linewidth(1) );
draw( (26,0){E}..{E}(29.5,-4.5), heavygreen+linewidth(1) );
draw( (26,-6){E}..{E}(29.5,-5.5), heavygreen+linewidth(1) );
draw( (26,-11){E}..{E}(29.5,-6.5), heavygreen+linewidth(1) );

add( shift( (31,-4) )
   * dataframe( 3, 1, col_width=2, col_headers = new string[]{"median"},
                row_headers = new string[]{"F","M","NaN"} ) );

label( "\parbox{1.25in}{\Large\bf Median Salary by Gender}", (31.5,1.5) );
label( "\texttt{df.groupby('Gender') \textbackslash}", (32,-1) );
label( "\texttt{['Salary'].median()}", (32.5,-1.75) );

