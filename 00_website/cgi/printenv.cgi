#!/bin/sh


# Must print out Content-type line, followed by at least one blank line,
# to have a well-formed header.
echo "Content-type: text/html\n\n"
echo "<TITLE>UKC HTML Documents</TITLE>"
echo "<H1>UKC HTML Documents</H1>"
        printenv

echo "<HR>"
echo '<A href="../UKC.html">'
echo '<img alt = "[UKC Home Page]" src = "../gif/logo.gif">'
echo 'Go to the<a href="../UKC.html">'
echo "<b>UKC Home Page</b></a>.<br>"
echo '<A href="#top"><img alt = "[TOP]" align=middle src="../gif/top.gif"></a>'
echo 'Back to the <a href="#top"> top</a> of this document.'


echo "<HR>"
echo "printenv /"
        date
echo "/ Made by <em>created on-the-fly by printenv.cgi</em>"


exit 0
