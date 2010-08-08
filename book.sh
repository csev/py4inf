#! /bin/sh

latex book
makeindex book
latex book
dvipdf book.dvi book.pdf
open book.pdf
echo Removed temporary files
rm book.aux book.ind book.ilg book.log book.dvi book.idx book.toc
exit

latex book
makeindex book
latex book
dvips -t letter -Ppdf -o thinkpython.ps book
open thinkpython.ps
