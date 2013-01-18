# This needs netpbm and hevea from Darwin Ports

rm -rf html
mkdir html
hevea -O -e latexonly png.hva htmlonly cfbook
# the following line is a kludge to prevent imagen from seeing
# the definitions in latexonly
grep -v latexonly cfbook.image.tex > a; mv a cfbook.image.tex
imagen -png cfbook
hacha cfbook.html
mv index.html cfbook.css cfbook*.html cfbook*.png cfbook*.gif *motif.gif html
