Python for Informatics: Exploring Information
=============================================

This is the source code for "Python for Informatics: Exploring Information"
the web site for this book is http://www.pythonlearn.com/

LaTeX Files
-----------

The source file for the book is *book.tex* - this file includes the 
per-chapter files *00-cover.tex* through *AD-copyright.tex*

Workflow
--------

Once you have LaTeX and HeVeA installed properly the workflow is simple. 
To produce the PDF version of the book you type:

    bash book.sh

This leaves the output on *book.pdf* and if you are on a Mac or Linux, it
even attempts to open the PDF viewer for your system.

To produce the HTML version of the book you type:

    bash html.sh

This produces files in the *html* folder.  This folder contains the book, chapters in
HTML and the images for the book.  

To make EPUB or MOBI files I use the Caliper software.  The steps that I tak in Caliper
are here:

* [Importing HTML into Caliper](CALIPER.md)

I also have a server that builds the latest version from this repository at this URL:

    http://do1.dr-chuck.com/py4inf/EN-us/

I don't yet have the files that make up the build server checked in because it is 
still a bit of a hack.  If you want to set up your own build server - I will check
the files in.

Software Installation - Macintosh
---------------------------------

Running the script to produce the PDF is really easy and convenent on the Mac.  Simply
install this software:

https://tug.org/mactex/

Make sure to install the extras as well.   If you have a recent Mac you **cannot** make
the binary download of *hevea* work as it is a PowerPC binary.  If you want to do the HTML
generation, you need a variant of Linux.

Software Installation - Ubuntu
------------------------------

This is the rough set of steps I use on ubuntu:

    sudo apt-get install texlive-latex-base
    sudo apt-get install texlive-latex-recommended
    sudo apt-get install texlive-fonts-recommended 
    sudo apt-get install texlive-latex-extra
    sudo apt-get install hevea
    sudo apt-get install imagemagick

You could put them all on one long apt-get, but I like to see if they work :)

Once this is done, the *book.sh* and *html.sh* should both work just fine.  For
my own sanity, I have Parallels with an ubuntu image that I can use to generate
HTML.  It was easier than keeping a four-year-old MacBook running with Rosetta
support.

TO DO
-----

I need to document and check in the code to run a build server.  The build server
is another way for a MacBook without HeVeA to develop.  Edit locally, check the PDF
and then check in the changes wait a tick and then the HTML is made in the build 
server.

I also need to work up documentation as to how to fork this repo for a language 
translation effort on this book.   I have refactored the source to make it
easier to edit the book using git and my build server can handle any number of 
languages.  If you are interested in starting a language translation project
for this book - please read the Appendix on copyright and contact me.

Chuck Severance - 
Fri Jul 25 20:25:16 EDT 2014




