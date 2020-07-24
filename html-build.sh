
echo "Removing _build/ folder..."
rm -rf _build/html
echo "Running build..."
jupyter-book build .
echo "Done."

