
import os, re

markdown_results = '\n# All Learning On Your Own Opportunities\n'
folder = os.path.abspath( os.path.dirname( __file__ ) )
files = [ file for file in os.listdir( folder ) \
          if file[-6:] == '.ipynb' and file[:8] == 'chapter-' ]
def chapnum ( filename ):
    m = re.match( 'chapter-([0-9]+)-(.*)\\.ipynb', filename )
    return int( m.group( 1 ) )
files.sort( key=chapnum )
for file in files:
    with open( file, 'r' ) as f:
        lines = f.readlines()
    title = None
    num_found = 0
    for line in lines:
        if title is None and '"# ' in line:
            m = re.search( '"# (.*)\\\\n"', line )
            if m is not None:
                title = m.group(1)
                markdown_results += f'\n## From [Chapter {chapnum(file)} - {title}]({file[:-6]})\n\n'
        if 'admonition' in line:
            m = re.search( 'Learning On Your Own - (.*)\\\\n"', line, re.I )
            if m is not None:
                markdown_results += f' * {m.group(1)}\n'
                num_found += 1
    if num_found == 0:
        markdown_results += '(None)\n'
with open( os.path.join( folder, 'loyo-list.md' ), 'w' ) as f:
    f.write( markdown_results )
