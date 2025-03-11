#!/usr/local/bin/perl

use CGI qw(:standard);

# check to see that form data was entered correctly
$new=param(new);
if ($new < 1) {
 print header();
 print '<html><head><title>serious problem</title></head><body>';
 print '<center>Membership data not written.';
 print '<p><a href="index.cgi">Try again</a></center></body></html>';
 exit(0);
}

$year=param(year);
$month=param(month);
$day=param(day);
$join=sprintf("%2.2d/%2.2d/%4.4d",$month,$day,$year);

$school_year=param(school_year);
open(OUT, ">>$school_year/members") or die("Can't write to $school_year/members");
$count = 0;
$new_subs=0;
for ($i=1; $i<=$new; ++$i) {
 # get form data and replace unentered data with empty string
 $last=param("last$i"); ($last) or ($last="");
 $first=param("first$i"); ($first) or ($first="");
 $gender=param("gender$i"); ($gender) or ($gender="");
 $stud=param("stud$i"); ($stud) or ($stud="");
 $type=param("type$i"); ($type) or ($type="");
 $wac=param("wac$i"); ($wac) or ($wac="");
 $stat=param("stat$i"); ($stat) or ($stat="");
 $email=param("email$i"); ($email) or ($email="");
 $list=param("list$i"); ($list) or ($list="");
 $address=param("address$i"); ($address) or ($address="");
 $aca=param("aca$i"); ($aca) or ($aca="");
 $line=join("\t",$join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list,$address,$aca);

 if ($last and $first) {
  if ($email and $list>=2 and $list<=5) {
   subscribe($list,$email,$first,$last);
   $new_subs += 1;
  }
  $count += 1;
  print OUT "$line\n";
 }
}
close(OUT);

print header();
print '<html><head><title>UKC: Members Added</title></head><body>';
print '<p>&nbsp;<p>&nbsp;<p>&nbsp;';
print "<center>$count members added to $school_year list.";
print "<br>$new_subs members added to mailing list.";
print '<p><a href="index.cgi">Back to main page</a></center></body></html>';

exit(0);

sub subscribe {
    # everyone gets a ukc-all subscription
    $message = "subscribe kayaker nodigest address=$email";
    if ($list == 2) {
	$to = "ukc-all-request\@mailman.u.washington.edu";
    }
    if ($list == 3) {
       $to = "ukc-all-request\@mailman.u.washington.edu, ukc-ww-request\@mailman.u.washington.edu";
    }
    if ($list == 4) {
	$to = "ukc-all-request\@mailman.u.washington.edu, ukc-sea-request\@mailman.u.washington.edu";
    }
    if ($list == 5) {
	$to = "ukc-all-request\@mailman.u.washington.edu, ukc-sea-request\@mailman.u.washington.edu, ukc-ww-request\@mailman.u.washington.edu";
    }
    
    open(MAIL, "|/usr/lib/sendmail $to\n");
    print MAIL "To: $to\n";
    print MAIL "From: ukc\@u.washington.edu\n";          
    print MAIL "Subject:\n\n";
    print MAIL "$message\n\n";

    close(MAIL);
}








