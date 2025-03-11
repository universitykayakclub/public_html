#!/usr/local/bin/perl

use CGI qw(:standard);

$school_year=param(school_year);
# either sort by last name or join date
$by = param(by);
if ($by eq "join date") {
 $by_what = "-t/ -k3n -k1n -k2n";       # first by year, then month, then day
}
else {
 $by = "last name";
 $by_what = "-d -k2f -k3f";     # first by LastName, then FirstName (ignore case)
} 
 
open(IN, "sort $by_what $school_year/members |")
        or die("can't open $school_year/members\n");
  
# read in from member list
@members=<IN>;
close(IN);
  
$line_number=param(line_number);
unless ($line_number <= $#members) {die("Membership lists not edited!\n");}

# replace old data with new data
$month=param("month");
$day=param("day");
$year=param("year");
$join=sprintf("%2.2d/%2.2d/%4.4d",$month,$day,$year);
$last=param("last"); ($last) or ($last="");
$first=param("first"); ($first) or ($first="");
$gender=param("gender"); ($gender) or ($gender="");
$stud=param("stud"); ($stud) or ($stud="");
$type=param("type"); ($type) or ($type="");
$wac=param("wac"); ($wac) or ($wac="");
$stat=param("stat"); ($stat) or ($stat="");
$email=param("email"); ($email) or ($email="");
$list=param("list"); ($list) or ($list="");
$address=param("address"); ($address) or ($address="");
$aca=param("aca"); ($aca) or ($aca="");
$new_data=join("\t",$join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list,$address,$aca);
$members[$line_number]="$new_data\n";
 
# figure out if there is a new subscriber
$new_subs=0;
if ($last and $first and $email and $list>=2 and $list<=5) {
 open(IN, "grep $email $school_year/members |");
 $old_data=<IN>;
 close(IN);
 # if the email address wasn't on the old list
 if (!($old_data)) {
  subscribe($list,$email,$first,$last);
  $new_subs += 1;
 }
 else {
  chomp($old_data);
  ($old_join,$old_last,$old_first,$old_gender,$old_stud,$old_type,$old_wac,$old_stat,$old_email,$old_list)=split("\t",$old_data);
  # or if the list name has changed
  if ($list ne $old_list) {
   subscribe($list,$email,$first,$last);
   $new_subs += 1;
  }
 }
}

# write edited data to membership file
open(OUT, ">$school_year/members") or die("can't write to $school_year/members");
$write_count = 0;
for ($i=0; $i<=$#members; ++$i) {
 # get membership data and replace unentered data with empty string
 chomp($line=$members[$i]);
 ($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list)=split("\t",$line);
 if ($last and $first) {
  $write_count += 1;
  print OUT "$line\n";
 }
}
close(OUT);

print header();
print '<html><head><title>UKC: Member List Edited</title></head><body>';
print '<p>&nbsp;<p>&nbsp;<p>&nbsp;';
print "<center>$write_count members written to $school_year list.";
print "<br>1 member added to mailing list." if $new_subs;
print '<p><a href="index.cgi">Back to main page</a></center></body></html>';

exit(0);

sub subscribe {
    $address = "listproc\@u.washington.edu";
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
    open(MAIL, "|/usr/lib/sendmail $address");
    print MAIL "To: $address\n";
    print MAIL "From: ukc\@u.washington.edu\n";
    print MAIL "Subject:\n\n";
    print MAIL "$message\n\n";
    close(MAIL);
}
