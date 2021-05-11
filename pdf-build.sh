
echo "Removing _build/ folder..."
rm -rf _build/latex
echo "Running build..."
jupyter-book build . --builder pdflatex
echo "Done."
cp _build/latex/book.pdf _static/MA346-course-notes.pdf
# open _static/MA346-course-notes.pdf

