
echo "Removing build/ folder..."
rm -rf build
echo "Running build..."
jupyter-book build .
echo "Done."

