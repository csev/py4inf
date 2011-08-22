#! /bin/sh

latex cfbook
makeindex cfbook
latex cfbook
dvipdf cfbook.dvi book.pdf
open book.pdf
echo Removed temporary files
rm -f cfbook.aux cfbook.ind cfbook.ilg cfbook.log cfbook.dvi cfbook.idx cfbook.toc cfbook.haux cfbook.hind cfbook.image.tex
