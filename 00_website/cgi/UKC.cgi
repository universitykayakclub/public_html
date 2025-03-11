#!/usr/local/bin/perl
#
# Much borrowed from the Web Engineer's Toolbox at Metronet:
#
#      http://www59.metronet.com/cgi/#lk5
#
# Determines browser type and domain of client, and then sends back a page
# appropriate for that browser.  If client is from outside .washington.edu
# domain, user is first shown a page with extra information.
#
#
#$UKCtxt = "http://weber.u.washington.edu/~ukc/html/UKCtxt.html";
#$UKCgraph = "http://weber.u.washington.edu/~ukc/html/UKCmenu.html";
#
#read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
#
#if ($ENV{'HTTP_USER_AGENT'} =~ /^Lynx.*/ || $ENV{'HTTP_USER_AGENT'} =~ /^NCSA_Mosaic.*/) {
#    print "Location:$UKCtxt\n\n";
#}
#else {
#    print "Location:$UKCgraph\n\n";
#}
print "Location:http://weber.u.washington.edu/~ukc/main/UKCmain.cgi\n\n";
