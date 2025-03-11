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

print header();
print <<"end_html1";
 <html><head><title>UKC: Edit Member List</title></head>
 <body><center><p><b>Membership list for $school_year</b>
 <form action="edited.cgi" method="post">
 <p><table border=1 cellspacing=2 cellpadding=2>
 <tr><th>Join Date<th>Last Name<th>First Name<th>Gender<th>Student #
 <th>Member<br>Type<th>WAC<br>Fee<th>University<br>Status
 <th>Email<br>address<th>Email list</tr>
end_html1

# read in from member list
@members=<IN>;
close(IN);

$i=0;
foreach (@members) {
 ++$i; chomp;
 ($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list)=split("\t");

 # determine options for pulldown menus

 $M_select=""; $F_select="";
 if ($gender =~ /m/i) {$M_select="selected";}
 else {$F_select="selected";}
 
 $RS_select=""; $L_select=""; $I_select="";
 if ($type =~ /l/i) {$L_select="selected";}
 elsif ($type =~ /i/i) {$I_select="selected";}
 else {$RS_select="selected";}

 $no_select=""; $paid_select="";
 if ($wac =~ /paid/i) {$paid_select="selected";}
 else {$no_select="selected";}

 $stu_select=""; $fac_select=""; $spo_select="";
 if ($stat =~ /spouse/i) {$spo_select="selected";}
 elsif ($stat =~ /faculty/i) {$fac_select="selected";}
 else {$stu_select="selected";}

 $list1_select=""; $list2_select=""; $list3_select=""; $list4_select=""; $list5_select="";
 if ($list =~ /2/) {$list2_select="selected";}
 elsif ($list =~ /3/) {$list3_select="selected";}
 elsif ($list =~ /4/) {$list4_select="selected";}
 elsif ($list =~ /5/) {$list5_select="selected";}
 else {$list1_select="selected";}

 unless ($email) {$email="";}

 print <<"end_html2";
  <tr><td align=center><input type="text" name="join$i" maxlength=10 size=10 value="$join">
  <td align=center><input type="text" name="last$i" maxlength=18 size=10 value="$last">
  <td align=center><input type="text" name="first$i" maxlength=18 size=10 value="$first">
  <td align=center><select name="gender$i"><option $M_select>M<option $F_select>F</select>
  <td align=center><input type="text" name="stud$i" maxlength=7 size=8 value="$stud">
  <td align=center><select name="type$i"><option $RS_select>RS<option $L_select>L<option $I_select>I</select>
  <td align=center><select name="wac$i"><option $no_select>no<option $paid_select>paid</select>
  <td align=center><select name="stat$i"><option $stu_select>Student<option $fac_select>Faculty/Staff<option $spo_select>Spouse</select>
  <td align=center><input type="text" name="email$i" maxlength=30 size=10 value="$email">
  <td align=center><select name="list$i"><option value=1 $list1_select>no mail<option value=2 $list2_select>ukc-all<option value=3 $list3_select>ukc-all & ukc-ww<option value=4 $list4_select>ukc-all & ukc-sea<option value=5 $list5_select>ukc-all, ukc-ww, & ukc-sea</select>
  </tr>
end_html2
}

print<<"end_html3";
 </table>
 <p><input type="hidden" name="school_year" value="$school_year">
 <input type="hidden" name="count" value="$i">
 <input type="submit"
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="save changes">
 </form>
 <p>Join Date, Last Name, and First Name are required fields.  Others may be left blank.
 <br>Dates should be entered as MM/DD/YYYY.
 <p>To remove a member, delete their first or last name and save changes.
 </center></body></html>
end_html3

exit(0);
