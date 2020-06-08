
echo "Removing _build/ folder..."
rm -rf _build
echo "Running build..."
jupyter-book build .
echo "Done."

