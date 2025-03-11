#!/usr/local/bin/perl

use CGI qw(:standard);

# get http parameters
$school_year=param( school_year );
$date = param( date );
$email_address = param ( email );

# what this script did?
if ( $email_address eq "" ) {
    $action = "Created";
}
else {
    $action = "Sent";
}

# read properties from aca.inc
open( IN, "aca.inc" )
    or die ( "can't open aca.inc\n" );

$props = ();
while ( <IN> ) {
    chomp;
    ( $key, $value ) = split( /\s?=>\s?/ );
    $props{ $key } = $value;
}
close( IN );

# get today's date
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$mon += 1;
$year += 1900;

$body = $props{ body_header } . "\n\n";

# read in from member list
open(IN, "sort -t/ -k3n -k1n -k2n $school_year/members |")
    or die("can't open $school_year/members\n");
@members=<IN>;
close(IN);

foreach ( @members ) {
    chomp;
    ($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list,$address,$aca)=split("\t");

    if ( datecmp( $join, $date ) >= 0 ) {
	$body .= "Name: $first $last\nAddress: $address\nACA \#: $aca\n\n";
    }
}

# send email
$result = "";
if ( $email_address ne "" ) {
    open( MAIL, "|/usr/lib/sendmail $email_address" );
    print MAIL "To: $email_address\n";
    print MAIL "From: ukc\@u.washington.edu\n";
    print MAIL "Subject: $props{ subject }\n";
    print MAIL "$body\n\n";
    close(MAIL);

    $result = "Email sent successfully.";
}
else {
    $result = "No email sent.";
}


print header();
print <<"end_html";
<html>
<head>
    <title>UKC: $action ACA List</title>
</head>
<body>
    <center>
      <p/>
      <h2>University Kayak Club</h2>
      All members who joined from $date to $mon/$mday/$year
    </center>

    <P>$result</P>

    <PRE>
To: $email_address
Subject: $props{ subject }
Body:

$body
    </PRE>

</body>
</html>
end_html

exit(0);

sub datecmp {

    my ( $datel, $dater ) = @_;

    my @datel_list = split( /\//, $datel );
    my @dater_list = split( /\//, $dater );

    $datel = "$datel_list[2]$datel_list[1]$datel_list[0]";
    $dater = "$dater_list[2]$dater_list[1]$dater_list[0]";  

    if ( $datel < $dater ) {
	return -1;
    }
    elsif ( datel > $dater ) {
	return 1;
    }
    else {
	return 0;
    }
} 
