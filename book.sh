#! /bin/sh

latex book
dvipdf book.dvi book.pdf
open book.pdf
exit

latex book
makeindex book
latex book
dvips -t letter -Ppdf -o thinkpython.ps book
open thinkpython.ps
