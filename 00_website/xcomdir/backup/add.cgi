#!/usr/local/bin/perl

use CGI qw(:standard);

# check to see that form data was entered correctly
$new=param(new);
if ($new < 1) {
 print header();
 print '<html><head><title>bad entry</title></head><body>';
 print '<p>&nbsp;<p>&nbsp;<p>&nbsp;';
 print '<center>Enter the number of new members for the form';
 print '<br>(between 1 and 30).  One form per join date.';
 print '<p><a href="index.cgi">Try again</a></center></body></html>';
 exit(0);
}
if ($new > 30) {$new=30;}

# create pulldown options for join day
$day=param(day);
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
$month = param(month);
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
$year=param(year);			# current year
$school_year=param(school_year);	# current academic year
($start_year,$end_year)=split('-', $school_year);
if ($year eq $start_year) {
 $year_options = "<option selected>$start_year<option>$end_year";
}
else {
 $year_options = "<option>$start_year<option selected>$end_year";
}

###################################################
# this part goes to the browser

print header();
print <<"end_html1";
 <html><head><title>UKC: New Members Form</title>
 <body><center>
 <form action="added.cgi" method="post">
 Enter join date<br>
 <select name="month">$month_options</select>
 <select name="day">$day_options</select>
 <select name="year">$year_options</select>
 <p><table border=1 cellspacing=2 cellpadding=2>
 <tr><th>Last Name<th>First Name<th>M/F<th>Student #<th>Member<br>Type
 <th>WAC<br>Fee<th>University<br>Status<th>Email<br>address<th>Email list</tr>
end_html1

for ($i=1; $i<=$new; ++$i) {
 print qq(<tr><td align=center><input type="text" name="last$i" maxlength=18 size=10>\n);
 print qq(<td align=center><input type="text" name="first$i" maxlength=18 size=10>\n);
 print qq(<td align=center><select name="gender$i"><option>M<option>F</select>\n);
 print qq(<td align=center><input type="text" name="stud$i" maxlength=7 size=8>\n);
 print qq(<td align=center><select name="type$i"><option select>RS<option>L<option>I</select>\n);
 print qq(<td align=center><select name="wac$i"><option select>no<option>paid</select>\n);
 print qq(<td align=center><select name="stat$i"><option select>Student<option>Faculty/Staff<option>Spouse</select>\n);
 print qq(<td align=center><input type="text" name="email$i" maxlength=30 size=10>\n);
 print qq(<td align=center><select name="list$i"><option select>ukc-all<option>ukc-ww<option>ukc-sea</select>);
 print "</tr>\n";
}

print<<"end_html2";
 </table>
 <input type="hidden" name="school_year" value="$school_year">
 <input type="hidden" name="new" value="$new">
 <p><input type="reset"
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="clear form">
 <input type="submit" 
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="write to list">
 </form>
 <p>First and last names are required fields.  Others may be left blank.
 </center></body></html>
end_html2

###################################################


exit(0);
