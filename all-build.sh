#!/bin/bash

# do these in sequence so they don't clobber one another's compute cache:
./html-build.sh && ./pdf-build.sh &
# do this one in parallel because it's totally independent of those:
./slides-build.sh &
# wait for all background processes to complete:
wait
# say so:
echo "All processes completed: HTML, PDF, slides."

