
echo "Examining .ipynb files in _slides/ folder..."
cd _slides
for file in *-slides.ipynb
do
    if test -f $file
    then
        no_ext="${file%.*}"
        echo "Converting $no_ext.ipynb to $no_ext.html..."
        jupyter nbconvert $no_ext.ipynb --to=slides
        echo "Renaming to $no_ext.html..."
        mv $no_ext.slides.html $no_ext.html
    fi
done
cd ..
echo "Done."

