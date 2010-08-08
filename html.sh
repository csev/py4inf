# This needs netpbm and hevea from Darwin Ports

rm -rf html
mkdir html
hevea -O -e latexonly htmlonly book
# the following line is a kludge to prevent imagen from seeing
# the definitions in latexonly
grep -v latexonly book.image.tex > a; mv a book.image.tex
imagen -png book
hacha book.html
mv index.html book.css book*.html book*.png *motif.gif html
