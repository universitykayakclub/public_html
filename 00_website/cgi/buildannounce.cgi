#!/usr/local/bin/perl

################################################################
#
# buildannounce.pl - used to build an announcement for the UKC
# Announcements page.  Referred by announceform.html.
#
# parts stolen from Ben Johnson's mailform.pl.
# 
# copyright 1996, Mark Wilber
#
################################################################

################################################################
# Configuration parameters
################################################################

# today
$date = `date`;

chop($date);

# begin CGI output 
print("Content-type: text/html\n\n<html>\n");
print("<head><title>Announcement Format:</title></head>\n");
print("<body>\n");

################################################################
# Process Query
################################################################

# Decide whether GET or POST method:

$request_method = $ENV{'REQUEST_METHOD'};

if ($request_method eq "GET")
{
    $query_string = $ENV{'QUERY_STRING'};
}
elsif ($request_method eq "POST")
{
    read (STDIN, $query_string, $ENV{'CONTENT_LENGTH'});
}
else
{
    print ("Request method not supported.  Please inform web master");
    print ("for referring document that GET or POST method is required.\n");
    print ("</body></html>");
    exit;
}

print ("");

print("$query_string");

print("<h2>Announcement Format:</h2>\n");
print("\n");
print("<ul>\n");

@cgiPairs = split("&",$query_string);
foreach $pair ( @cgiPairs ) {
    ($var,$val) = split("=",$pair);

    $val =~ s/\+/ /g;
#   $val =~ s/%(..)/pack("c",hex($1))/ge;
    $val =~ s/%([\dA-Fa-f][\dA-Fa-f])/pack ("C", hex ($1))/ge;
#
#   Translate new lines to <br> tags:
#
    $val =~ s/[\n]/<br>/g;
    $cgiVals{"$var"} = "$val";
    if ( $var eq "Announcement" )
    {
	print ("<li> $var: $val\n");
    }
    else
    {
	print ("<li> $var: $val\n");
    }
}

print ("</ul>");


################################################################
# construct the body
################################################################

foreach $key ( keys(%cgiVals) ) {
    if ( $key eq "firstname" || $key eq "lastname" )
    {
        next;
    } 
    print( "$key: $cgiVals{$key}<p>\n");
}

# if ( ! $first_name || ! $last_name ) {
    # Gotta identify yourself.
#    &error("No postings without sender identified.");
# }

################################################################
# Get ready to send mail 
################################################################

# get ready to send the mail
# if ( ! open(MAIL,"| $sendmail $recipient") ) {
#     &error("Could not start mail program");
# }

################################################################
# construct the headers
################################################################
# print(MAIL "To: recipient\n");
# if ( ! $cgiVals{'subject'} ) {
#     $cgiVals{'subject'} = "(no subject)";
# }
# print(MAIL "Subject: $cgiVals{subject}\n");
# if ( ! $cgiVals{'from'} ) {
#    $cgiVals{'from'} = "nobody";
# }
# print( MAIL "From: $cgiVals{from}\n");
# done with the headers.  Add the blank line.
# print( MAIL "\n");
################################################################
# All done.  Clean up.
################################################################
# close(MAIL);
# the response.
print("Form submitted successfully.  Thanks!");
exit(0);

# define an error routine:
sub error {
    ($message) = @_;
    print("<b>ERROR:<b>",
          $message,
          "<p>Contact the author of the previous page for assistance\n");
    exit(0);
}
