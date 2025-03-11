#!/usr/local/bin/perl

$qs=$ENV{'QUERY_STRING'};  
($junk, $fselect) = split(/=/, $qs);
if ($fselect > 1) {$fselect = 1;}
 elsif ($fselect < 0) {$fselect = 0;}

$school_starts="0828";
($s,$mi,$h,$d,$mo,$y)=localtime(time);
$mo+=1;
$today=sprintf('%02d%02d',$mo,$d);
$ly = $y - 1;
$lly = $y - 2;
$ny = $y + 1;
if ($y > 99) {$y = $y-100}
if ($ly > 99) {$ly = $ly-100}
if ($lly > 99) {$lly = $lly-100}
if ($ny > 99) {$ny = $ny-100}
if ($fselect == 1)  {
    if ($today > $school_starts) {$acyr=sprintf('%02d-%02d',$y,$ny);}
    else {$acyr = sprintf('%02d-%02d',$ly,$y);}
} else {
    if ($today > $school_starts) {$acyr=sprintf('%02d-%02d',$ly,$y);}
    else {$acyr = sprintf('%02d-%02d',$lly,$ly);}
}

$MEMBERS = "members$acyr.dat";
open (BYDATE, "sort -t , -k 4nr -k 1 -k 2 $MEMBERS |");
@bydate = <BYDATE>;
close BYDATE;

open MEMBERS;
while (<MEMBERS>) {
 (/,RS,/) && (++$riversea);
 (/,L,/) && (++$lake);
 (/,I,/) && (++$independent);
 (/student/) && (++$student);
 (/faculty/) && (++$faculty);
 (/spouse/) && (++$spouse);
 ++$total;
 }
($total) || ($total=0);
($riversea) || ($riversea=0);
($lake) || ($lake=0);
($independent) || ($independent=0);
($student) || ($student=0);
($faculty) || ($faculty=0);
($spouse) || ($spouse=0);
@stats = stat MEMBERS;
close MEMBERS;

($sec,$min,$hr,$day,$month,$year)=localtime($stats[9]);
$month+=1;
$when=sprintf('%02d/%02d/%02d',$month,$day,$year);

print "Content-type: text/html","\n\n";
print <<"enddates";
 <HTML><HEAD><TITLE>Members by Date</TITLE></HEAD>
 <BODY BACKGROUND="http://students.washington.edu/~ukc/bits/swirl.gif"><CENTER>
 <H2>UKC Membership List for $acyr School Year</H2>
 The club has $total members as of $when, broken down as follows:<P>
 <TABLE border=1 cellpadding=1 cellspacing=0>
 <TR><TH colspan=3>Membership Level
 <TH colspan=3>University Status
 <TR><TH>River/Sea<TH>Lake<TH>Independent
 <TH>Student<TH>Faculty/Staff<TH>Spouse
 <TR><TD align=center>$riversea<TD align=center>$lake
 <TD align=center>$independent
 <TD align=center>$student<TD align=center>$faculty
 <TD align=center>$spouse</TABLE>
 <P><TABLE border=1 cellpadding=1>
 <TH align=center>Join Date <TH align=center>Last Name
 <TH align=center>First Name <TH align=center>Student #
 <TH align=center>Member Type <TH align=center>University Status
enddates

foreach (@bydate) {
 @item = split(',' , $_);
 $yr = substr($item[3], 2, 2);
 $mo = substr($item[3], 4, 2);
 $da = substr($item[3], 6, 2);
 $date = join('/', $mo, $da, $yr);
 print "<TR><TD align=center>$date <TD>$item[0] <TD>$item[1]
  <TD align=center>$item[2] <TD align=center>$item[4]
  <TD align=center>$item[5] </TR> \n";
 }

print "</TABLE></BODY></HTML>\n";
exit(0);
