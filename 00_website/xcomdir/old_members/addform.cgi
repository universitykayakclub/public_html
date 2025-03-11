#!/usr/local/bin/perl -w

$host_name = 'washington\.edu';
$remote_host = $ENV{'REMOTE_HOST'};
unless ($remote_host =~ /\.$host_name/) {
 print "Content-type: text/html","\n";
 print "Status: 403 Forbidden","\n\n";
 print "<HTML><HEAD><TITLE>GO AWAY</TITLE></HEAD>";
 print "<BODY><H1>Forbidden</H1>";
 print "<HR>This form can only be accessed from the ";
 print "washington.edu domain<HR></BODY></HTML>";
 exit (1);
 }
    
$qs=$ENV{'QUERY_STRING'};  
($junk, $new) = split(/=/, $qs);
if ($new > 30) {$new = 30;}
 elsif ($new < 1) {$new = 1;}
 
$school_starts="0828";
($s,$mi,$h,$d,$mo,$y)=localtime(time);
$mo+=1;
$today=sprintf('%02d%02d',$mo,$d);
$ly = $y - 1;
$ny = $y + 1;
if ($y > 99) {$y = $y-100}
if ($ly > 99) {$ly = $ly-100}
if ($ny > 99) {$ny = $ny-100}
if ($today > $school_starts) {$acyr=sprintf('%02d-%02d',$y,$ny);}
else {$acyr = sprintf('%02d-%02d',$ly,$y);}

print "Content-type: text/html","\n\n";
print '<HTML><HEAD><TITLE>names</TITLE></HEAD>',"\n";
print '<BODY BACKGROUND="http://students.washington.edu/~ukc/bits/swirl.gif" TEXT="#000000" link="0022dd" vlink="#660099"> <CENTER>',"\n";
print '<FORM ACTION="write.cgi" METHOD="post">',"\n";
print '<INPUT TYPE="hidden" NAME="new" VALUE=',$new,'>',"\n";
print "<font size=4>This form will add members to the data file for the <b>",$acyr,"</b> school year.<br>";
print "Please contact the web shaman if this is not the proper data file.</font><p>";


print <<'part1';
<TABLE border=1 cellspacing=0 cellpadding=2 bgcolor="#ffffff">
<TR><TD><B>Join Date:</B>

<TD>Month:
<SELECT NAME="month">
<OPTION SELECTED>01   
<OPTION>02 <OPTION>03 <OPTION>04 <OPTION>05 <OPTION>06 <OPTION>07
<OPTION>08 <OPTION>09 <OPTION>10 <OPTION>11 <OPTION>12
</SELECT>

<TD>Day:<SELECT NAME="day">
<OPTION SELECTED>01
<OPTION>02 <OPTION>03 <OPTION>04 <OPTION>05 <OPTION>06 <OPTION>07
<OPTION>08 <OPTION>09 <OPTION>10 <OPTION>11 <OPTION>12 <OPTION>13
<OPTION>14 <OPTION>15 <OPTION>16 <OPTION>17 <OPTION>18 <OPTION>19              
<OPTION>20 <OPTION>21 <OPTION>22 <OPTION>23 <OPTION>24 <OPTION>25
<OPTION>26 <OPTION>27 <OPTION>28 <OPTION>29 <OPTION>30 <OPTION>31
</SELECT>

<TD>Year:
<SELECT NAME="year">
<OPTION SELECTED>1999 <OPTION>2000 <OPTION>2001 <OPTION>2002 
<OPTION>2003 <OPTION>2004
</SELECT></TABLE><BR>
<TABLE BORDER=1 cellpadding=2 cellspacing=0 bgcolor="#ffffff">
<TH align=center>Last Name <TH align=center>First Name 
<TH align=center>Student # <TH align=center>Member Type
<TH align=center>Status
part1

for ($i=0; $i<$new; ++$i) {
 print '<TR><TD><INPUT TYPE="text" NAME="last',$i,'" size=20>';
 print '<TD><INPUT TYPE="text" NAME="first',$i,'" size=20>';
 print '<TD><INPUT TYPE="text" NAME="stud',$i,'" size=9 maxlength=9>';
 print '<TD align=center><SELECT NAME="type',$i,'"><OPTION SELECT>RS
  <OPTION>L <OPTION>I </SELECT>';
 print '<TD><SELECT NAME="stat',$i,'"><OPTION SELECT>student 
  <OPTION>faculty/staff <OPTION>spouse
  </SELECT>';
 }

print <<'part2';
</TABLE><P>
<INPUT TYPE="submit" VALUE="Submit Form">
<INPUT TYPE="reset" VALUE="Clear Form">
</FORM><HR></CENTER></BODY></HTML>
part2

 
