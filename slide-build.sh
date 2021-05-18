
echo "Examining .ipynb files in _slides/ folder..."
cd _slides
for file in *-slides.ipynb
do
    if test -f $file
    then
        no_ext="${file%.*}"
        echo "Converting $no_ext.ipynb to $no_ext.html..."
        jupyter nbconvert $no_ext.ipynb --to=slides
        mv $no_ext.slides.html $no_ext.html
        echo "Also creating printable version..."
        jupyter nbconvert $no_ext.ipynb --to=html --output=$no_ext-printable.html
    fi
done
cd ..
echo "Done."

