#!/usr/local/bin/perl

use CGI qw(:standard);

$count=param(count);
unless ($count > 0) {
 print header();
 print '<html><head><title>not written</title><head>',"\n";
 print '<body><center>Membership file not edited!</center></body></html>',"\n";
 exit(0);
}

$school_year=param(school_year);

# figure out if there are any new subscribers
$new_subs=0;
for ($i=1; $i<=$count; ++$i) {
 $last=param("last$i");
 $first=param("first$i");
 $email=param("email$i");
 $list=param("list$i");
 if ($last and $first and $email and $list) {
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
}

open(OUT, ">$school_year/members") or die("can't write to $school_year/members");
$write_count = 0;
for ($i=1; $i<=$count; ++$i) {
 # get form data and replace unentered data with empty string
 $join=param("join$i"); ($join) or ($join="");
 $last=param("last$i"); ($last) or ($last="");
 $first=param("first$i"); ($first) or ($first="");
 $gender=param("gender$i"); ($gender) or ($gender="");
 $stud=param("stud$i"); ($stud) or ($stud="");
 $type=param("type$i"); ($type) or ($type="");
 $wac=param("wac$i"); ($wac) or ($wac="");
 $stat=param("stat$i"); ($stat) or ($stat="");
 $email=param("email$i"); ($email) or ($email="");
 $list=param("list$i"); ($list) or ($list="");
 $line=join("\t",$join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list);
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
print "<br>$new_subs members added to mailing list.";
print '<p><a href="index.cgi">Back to main page</a></center></body></html>';

exit(0);

sub subscribe {
    $address = "listproc\@u.washington.edu";
    $message = "subscribe $list $first $last";
    open(MAIL, "|/usr/lib/sendmail $address");
    print MAIL "To: $address\n";
    print MAIL "From: $email\n";
    print MAIL "Subject:\n\n";
    print MAIL "$message\n\n";
    close(MAIL);
}
