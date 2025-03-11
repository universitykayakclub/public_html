#!/usr/local/bin/perl

use CGI qw(:standard);

# This script purges the ukc email lists, then subscribes everyone again

open(MAIL, "|/usr/lib/sendmail $address");
print MAIL "To: bessette\@u.washington.edu\n";
print MAIL "From: ukc\@u.washington.edu\n";          
print MAIL "Subject:\n\n";
print MAIL "\n\n";
close(MAIL);

$school_year = param( school_year );

# Open the file for reading
open(IN, "$school_year/members") or die("Can't write to $school_year/members");

@lines = <IN>;		# Read it into an array

close(IN);

while ( <IN> ) {
	
	($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list)= split( "\t" );
  
	# everyone gets a ukc-all subscription
	$message = "add ukc-all ukc-all $email $first $last";
	if ($list == 3) {
		$message .= "\nadd ukc-ww ukc-ww $email $first $last";
	}
	if ($list == 4) {
		$message .= "\nadd ukc-sea ukc-sea $email $first $last";
	}
	if ($list == 5) {
		$message .= "\nadd ukc-ww ukc-ww $email $first $last";
		$message .= "\nadd ukc-sea ukc-sea $email $first $last";
	}

#	open(MAIL, "|/usr/lib/sendmail $address");
#	print MAIL "To: bessette\@u.washington.edu\n";
#	print MAIL "From: ukc\@u.washington.edu\n";          
#	print MAIL "Subject:\n\n";
#	print MAIL "$message\n\n";
#	close(MAIL);
}

# Print output
print header();
print '<html><head><title>UKC: Members Purged</title></head><body>';

#print '<p>ukc-all, ukc-sea, and ukc-ww have been successfully purged<p/>';
print '<p>Currently under construction<p/>';

print '<p><a href="index.cgi">Back to main page</a></body></html>';


exit(0);
