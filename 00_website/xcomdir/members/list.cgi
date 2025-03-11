#!/usr/local/bin/perl

use CGI qw(:standard);

$school_year=param(school_year);

# either sort by last name or join date
if (param(by) eq "join date") {
 $by_what = "-t/ -k3n -k1n -k2n";	# first by year, then month, then day
}
else {
 $by_what = "-d -k2f -k3f";	# first by LastName, then FirstName (ignore case)
}

open(IN, "sort $by_what $school_year/members |") 
	or die("can't open $school_year/members\n");

$f_time=(stat("$school_year/members"))[9];
($f_day,$f_month,$f_year)=(localtime($f_time))[3,4,5];
$f_month+=1;
$f_year=substr($f_year,-2,2);
$when=sprintf('%2.2d/%2.2d/%2.2d',$f_month,$f_day,$f_year);

print header();
print <<"end_html1";
 <html><head><title>UKC: $school_year Members</title></head>
 <body><center><p><h2>University Kayak Club</h2>
 Membership list for $school_year
 <p><table border=1 cellspacing=0 cellpadding=4>
 <tr><th>Join Date<th>Last Name<th>First Name<th>M/F<th>Student #
 <th>Member<br>Type<th>WAC<br>Fee<th>University<br>Status
 <th>Email<br>address<th>Email list<th>Address<th>ACA #</tr>
end_html1

# read in from member list
@members=<IN>;
close(IN);

$i=0;
foreach (@members) {
 ++$i; chomp;
 ($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list,$address,$aca)=split("\t");
 if ($list == 2) {$list_name = "ukc-all";}
 elsif ($list == 3) {$list_name = "ukc-all & ukc-ww";}
 elsif ($list == 4) {$list_name = "ukc-all & ukc-sea";}
 elsif ($list == 5) {$list_name = "ukc-all, ukc-ww, & ukc-sea";}
 else {$list_name = "no mail";}
 ($stud) or ($stud = "&nbsp;");
 ($email) or ($email = "&nbsp;");
 ($address) or ($address = "&nbsp;");
 ($aca) or ($aca = "&nbsp;");
 print <<"end_html2";
  <tr><td>$join
  <td>$last
  <td>$first
  <td align=center>$gender
  <td>$stud
  <td align=center>$type
  <td align=center>$wac
  <td align=center>$stat
  <td>$email
  <td align=center>$list_name
  <td>$address
  <td>$aca
  </tr>
end_html2
}


print<<"end_html3";
 </table>
 <p>Last modified $when
 </center></body></html>
end_html3

exit(0);
