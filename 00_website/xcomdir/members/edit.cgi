#!/usr/local/bin/perl

use CGI qw(:standard);

$school_year=param(school_year);

# either sort by last name or join date
$by = param(by);
if ($by eq "join date") {
 $by_what = "-t/ -k3n -k1n -k2n";	# first by year, then month, then day
}
else {
 $by = "last name";
 $by_what = "-d -k2f -k3f";	# first by LastName, then FirstName (ignore case)
}

open(IN, "sort $by_what $school_year/members |") 
	or die("can't open $school_year/members\n");

# read in from member list
@members=<IN>;
close(IN);


$line_number=param(line_number);

# if line_number is selected, only edit that member
if (defined $line_number) {
 chomp($edit=$members[$line_number]);
 ($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list,$address,$aca)=split("\t",$edit);
 ($month,$day,$year)=split("/",$join);

 # create pulldown options for join day
 for ($i=1; $i<=31; ++$i) {
  if ($i == $day) {
   $selected = "selected";
  }
  else {
   $selected = "";
  }
  $day_options .= "<option $selected>$i";
 }
 
 # create pulldown options for join month
 @month_names = qw(zero Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
 for ($i=1; $i<=12; ++$i) {
  if ($i == $month) {
   $selected = "selected";
  }
  else {
   $selected = "";
  }
  $month_options .= "<option value=$i $selected>$month_names[$i]";
 }

 # create pulldown options for join year
 ($start_year,$end_year)=split('-', $school_year);
 if ($year eq $start_year) {
  $year_options = "<option selected>$start_year<option>$end_year";
 }
 else {
  $year_options = "<option>$start_year<option selected>$end_year";
 }

 # determine options for other pulldown menus

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

 # this part goes to the browser
 print header();
 print <<"end_html1";
  <html><head><title>UKC: Edit Member List</title></head>
  <body><center><p><b>Membership list for $school_year</b>
  <form action="edited.cgi" method="post">
  <p><table border=1 cellspacing=2 cellpadding=2>
  <tr><th colspan=3>Join Date<th>Last Name<th>First Name<th>Gender<th>Student #
  <th>Member<br>Type<th>WAC<br>Fee<th>University<br>Status
  <th>Email<br>address<th>Email list
  <th>Address<th>ACA #
</tr>
  <tr><td align=center><select name="month">$month_options</select>
  <td align=center><select name="day">$day_options</select>
  <td align=center><select name="year">$year_options</select>
  <td align=center><input type="text" name="last" maxlength=18 size=10 value="$last">
  <td align=center><input type="text" name="first" maxlength=18 size=10 value="$first">
  <td align=center><select name="gender"><option $M_select>M<option $F_select>F</select>
  <td align=center><input type="text" name="stud" maxlength=7 size=8 value="$stud">
  <td align=center><select name="type"><option $RS_select>RS<option $L_select>L<option $I_select>I</select>
  <td align=center><select name="wac"><option $no_select>no<option $paid_select>paid</select>
  <td align=center><select name="stat"><option $stu_select>Student<option $fac_select>Faculty/Staff<option $spo_select>Spouse</select>
  <td align=center><input type="text" name="email" maxlength=30 size=10 value="$email">
  <td align=center><select name="list"><option value=1 $list1_select>no mail<option value=2 $list2_select>ukc-all<option value=3 $list3_select>ukc-all & ukc-ww<option value=4 $list4_select>ukc-all & ukc-sea<option value=5 $list5_select>ukc-all, ukc-ww, & ukc-sea</select>
  <td align=center><input type="text" name="address" maxlength=100 size=30 value="$address"/>
  <td align=center><input type="text" name="aca" maxlength=30 size=7 value="$aca"/>
</tr>
</table>
  <p><input type="hidden" name="school_year" value="$school_year">
  <input type="hidden" name="line_number" value="$line_number">
  <input type="hidden" name="by" value="$by">
  <input type="submit"
  style="background: #5588ff; color: #ffffff; font-weight: bold"
  value="save changes">
  </form>
  <p>Last Name, and First Name are required fields.  Others may be left blank.
  <p>To remove a member, delete their first or last name and save changes.
  </center></body></html>
end_html1
}
# if no line_number is given, show the whole list
else {
 print header();
 print <<"end_html2";
  <html><head><title>UKC: Edit Member List</title></head>
  <body><center><p><b>Membership list for $school_year</b>
  <br>Select member to edit by clicking on the button in the first column
  <form action="edit.cgi" method="post">
  <p><table border=1 cellspacing=2 cellpadding=2>
  <tr><th>Edit<th>Join Date<th>Last Name<th>First Name<th>Gender<th>Student #
  <th>Member<br>Type<th>WAC<br>Fee<th>University<br>Status
  <th>Email<br>address<th>Email list
  <th>Address<th>ACA #
</tr>
end_html2
 $i=0; 
 foreach (@members) {
  ++$i; chomp; $line_number=sprintf("%3.3d",$i-1);
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
  print <<"end_html3";
   <tr><td align=center><input type="submit" name="line_number" value="$line_number"
   style="background: #5588ff; color: #5588ff">
   <td>$join
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
end_html3
 }
 print <<"end_html4";
  <input type="hidden" name="school_year" value="$school_year">
  <input type="hidden" name="by" value="$by">
  </table></body></html>
end_html4
}

exit(0);
