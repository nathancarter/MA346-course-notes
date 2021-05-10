
import os
import os.path
import time

times = {}

def scan(folder, extensions, description, command):
    global times
    output = []
    for file in os.listdir(folder):
        if any([file.endswith(ext) for ext in extensions]):
            full_file = os.path.join(folder, file)
            new_time = os.path.getmtime(full_file)
            if full_file not in times:
                output += [f"Noticed new {description}: {full_file}"]
            elif times[full_file] != new_time:
                output += [f"Noticed {description} update: {full_file}"]
            times[full_file] = new_time
    if len(output) > 0:
        print('\n\n')
        print('-'*70)
        print('\n'.join(output))
        print('-'*70)
        os.system(command)

while True:
    scan('_slides', ['.ipynb'],        'slides', './slide-build.sh')
    scan('.',       ['.py', '.ipynb'], 'page',   './book-build.sh' )
    time.sleep(1)

