
echo "Removing docs/ folder....."
rm -rf docs/
echo "Running build..."
jupyter-book build .
echo "Moving result from _build/html do docs/ instead..."
mv ./_build/html ./docs
echo "Done."

