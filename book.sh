#! /bin/bash

rm *.tmp *.aux
latex cfbook
makeindex cfbook
latex cfbook
dvipdf cfbook.dvi book.pdf
if [[ "$OSTYPE" == "darwin"* ]]; then
  open book.pdf
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
  xdg-open book.pdf
else
  echo "Output on book.pdf"
fi
echo Removed temporary files
rm -f cfbook.aux cfbook.ind cfbook.ilg cfbook.log cfbook.dvi cfbook.idx cfbook.toc cfbook.haux cfbook.hind cfbook.image.tex cfbook.tmp cfbook.idv cfbook.4tc cfbook.lg cfbook.xref
