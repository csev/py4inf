#! /bin/sh

latex book
makeindex book
latex book
dvips -t letter -Ppdf -o thinkpython.ps book
open thinkpython.ps
