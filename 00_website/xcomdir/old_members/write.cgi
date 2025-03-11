#!/usr/local/bin/perl

$school_starts="0828";
($s,$mi,$h,$d,$mo,$y)=localtime(time);
$mo+=1;
$today=sprintf('%02d%02d',$mo,$d);
if ($y > 99) {$y = $y-100}
$ly = $y - 1;
if ($ly > 99) {$ly = $ly-100}
$ny = $y + 1;
if ($ny > 99) {$ny = $ny-100}
if ($today > $school_starts) {$acyr=sprintf('%02d-%02d',$y,$ny);}
else {$acyr = sprintf('%02d-%02d',$ly,$y);}
$outfile = "members$acyr.dat";
                                    
&parse_form_data (*farr);

print "Content-type: text/html","\n\n";
print '<HTML><HEAD><TITLE>Parse and Write</TITLE></HEAD>',"\n";
print '<BODY BACKGROUND="http://students.washington.edu/~ukc/bits/swirl.gif" TEXT="#000000" link="0022dd" vlink="#660099">',"\n";

$day = $farr{'day'};
$month = $farr{'month'};
$year = $farr{'year'};
$date = join("", $year, $month, $day);
$new = $farr{'new'};
$n=0;
for ($i=0; $i<$new; ++$i) {
 $first[$i] = $farr{"first$i"};
 $last[$i] = $farr{"last$i"};
 $stud[$i] = $farr{"stud$i"};
 $type[$i] = $farr{"type$i"};
 $stat[$i] = $farr{"stat$i"};
 if ($first[$i] && $last[$i]) {
  $line[$i] = join(",", $last[$i], $first[$i], $stud[$i], $date,
    $type[$i], $stat[$i]);
  ++$n;
  }
 }  

print "Here's what it looks like <P><UL>";
open (FILE, ">> $outfile") || print "not written\n";
for ($i=0; $i < $n; ++$i) {
 print FILE "$line[$i] \n";
 print "<LI>$line[$i]";
}
close FILE;
chmod(0601,$outfile) || print "can't change permission for $outfile<P>";
print "</UL>";

print <<"end_html";
 <BR><P>If this doesn't look right, you will have 
 to edit the members$acyr.dat file on dante.
 <A HREF="mailto:tschaub\@u.washington.edu">Email</A> for help.
 <P>Back to the 
 <A HREF="http://students.washington.edu/~ukc/xcomdir/X-com.html">
 Xcom</A> page.</BODY></HTML>
end_html

exit(0); 

sub parse_form_data {
 local (*FORM_DATA) = @_;
 local ( $query_string, @key_value_pairs, $key_value, $key, $value);
 read (STDIN, $query_string, $ENV{'CONTENT_LENGTH'});
 @key_value_pairs = split (/&/, $query_string);
 foreach $key_value (@key_value_pairs) {
  ($key, $value) = split (/=/, $key_value);
  $value =~ tr/+/ /;
  $value =~ s/%([\dA-Fa-f][\dA-Fa-f])/pack ("C", hex ($1))/eg;
  if (defined($FORM_DATA{$key})) {
   $FORM_DATA{$key} = join("\0", $FORM_DATA{$key}, $value);
   } else {
   $FORM_DATA{$key} = $value;
   }
  }
 } 
