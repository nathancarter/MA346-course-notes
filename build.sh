
echo "Removing build/ folder..."
rm -rf build/
echo "Running build..."
jupyter-book build .
echo "Renaming _build/_static/_sources to remove underscores..."
mv _build build
mv build/_static build/static
mv build/_sources build/sources
echo "Updating all links to remove underscores..."
for file in build/html/*.html
do
    echo "    $file"
    sed 's/_static\//build\/html\/static\//g' $file > $file.tmp
    rm $file
    mv $file.tmp $file
    sed 's/_sources\//build\/html\/sources\//g' $file > $file.tmp
    rm $file
    mv $file.tmp $file
done
echo "Done."

