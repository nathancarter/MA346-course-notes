
import os
import os.path
import time

times = {}
while True:
    output = []
    for file in os.listdir('.'):
        if file.endswith('.py') or file.endswith('.ipynb'):
            new_time = os.path.getmtime(file)
            new_output = ''
            if file not in times:
                output += [f"Noticed new file: {file}"]
            elif times[file] != new_time:
                output += [f"Noticed file update: {file}"]
            times[file] = new_time
    if len(output) > 0:
        print('\n\n')
        print('-'*70)
        print('\n'.join(output))
        print('-'*70)
        os.system('./build.sh')
    time.sleep(1)

