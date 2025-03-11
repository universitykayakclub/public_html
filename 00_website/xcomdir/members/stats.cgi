#!/usr/local/bin/perl

use CGI qw(:standard);

$school_year=param("school_year");	# always get this
unless ($school_year) {html_error();exit(0);}

$submit=param("submit");		# either change dates, report stats
					# or show calendar
if ($submit eq "change dates") {
 change_dates();
}

# get quarter start dates
open(DATES, "cat $school_year/start_dates |") or die("can't open $school_year/start_dates\n");
@dates=<DATES>;
close(DATES);
foreach (@dates) {chomp;}
($start_year, $finish_year)=split('-',$school_year);
($autumn_month,$autumn_day)=split('/',$dates[0]);
($winter_month,$winter_day)=split('/',$dates[1]);
($spring_month,$spring_day)=split('/',$dates[2]);
($summer_month,$summer_day)=split('/',$dates[3]);
$autumn_start=sprintf("%4.4d%2.2d%2.2d",$start_year,$autumn_month,$autumn_day)+0;
$winter_start=sprintf("%4.4d%2.2d%2.2d",$finish_year,$winter_month,$winter_day)+0;
$spring_start=sprintf("%4.4d%2.2d%2.2d",$finish_year,$spring_month,$spring_day)+0;
$summer_start=sprintf("%4.4d%2.2d%2.2d",$finish_year,$summer_month,$summer_day)+0;

if ($submit eq "stats") {

 $today = `date +"%m/%d/%Y"`;
 chomp($today);

 @quarters=qw(autumn winter spring summer);
 foreach (@quarters) {
  %{"$_\_stats"}=();	# clear hash for each quarter
  ${"$_\_stats"}{Student}=0;
  ${"$_\_stats"}{M_Student}=0;
  ${"$_\_stats"}{F_Student}=0;
  ${"$_\_stats"}{Faculty}=0;
  ${"$_\_stats"}{M_Faculty}=0;
  ${"$_\_stats"}{F_Faculty}=0;
  ${"$_\_stats"}{Spouse}=0;
  ${"$_\_stats"}{M_Spouse}=0;
  ${"$_\_stats"}{F_Spouse}=0;
  ${"$_\_stats"}{paid_wac}=0;
  ${"$_\_stats"}{RS}=0;
  ${"$_\_stats"}{L}=0;
  ${"$_\_stats"}{I}=0;
  ${"$_\_stats"}{total}=0;
 }
 %annual_stats=();
 $annual_stats{total}=0;

 open(IN, "$school_year/members") or die("can't open $school_year/members\n");
 # go throught the entire membership list
 while (<IN>) {
  ++$annual_stats{total}; chomp;
  ($join,$last,$first,$gender,$stud,$type,$wac,$stat,$email,$list,$address,$aca)=split("\t");

  (($gender =~ /m/i) and ($gender = "M")) or ($gender ="F");
  
  if ($type =~ /l/i) {$type = "L";}   
  elsif ($type =~ /i/i) {$type = "I";}
  else {$type = "RS";}
  
  if ($stat =~ /faculty/i) {$stat = "Faculty/Staff";}
  elsif ($stat =~ /spouse/i) {$stat = "Spouse";}
  else {$stat = "Student";}
  
  ($join_month,$join_day,$join_year)=split('/',$join);
  $full_join_date=sprintf("%4.4d%2.2d%2.2d",$join_year,$join_month,$join_day) + 0;
  # figure out what quarter the person joined
  foreach (@quarters) {
   $quarter_start = ${"$_\_start"};
   if ($full_join_date >= $quarter_start) {$quarter=$_;}
  }
  # tally up WAC fees
  if ($wac eq "paid") {
   ++${"$quarter\_stats"}{paid_wac};
   ++$annual_stats{paid_wac};
  }
  # tally up all other stats
  ($stat,$junk)=split('/',$stat);
  ++${"$quarter\_stats"}{"$gender\_$stat"};
  ++${"$quarter\_stats"}{$stat};
  ++${"$quarter\_stats"}{"$gender\_$type"};
  ++${"$quarter\_stats"}{$type};
  ++${"$quarter\_stats"}{total};
  ++$annual_stats{$stat};
  ++$annual_stats{$type};
 }
 close(IN);

 # send this to the browser
 print header();
 print <<"part_1";
  <html><head><title>UKC: Quarterly Statistics</title></head>
  <body><center><p><h2>University Kayak Club</h2>
  Membership Statistics for $school_year
  <br>as of $today
  <p><table border=1 cellpadding=5 cellspacing=0>
  <tr><th>&nbsp;<th>Student<th>Faculty/Staff<th>Spouse
  <th>RS<th>&nbsp;L&nbsp;<th>&nbsp;I&nbsp;
  <th>Total Members<th>Paid WAC</tr>
part_1
 
 foreach $quarter (@quarters) {
  $quarter_name = $quarter;
  substr($quarter_name,0,1) =~ tr/[a-z]/[A-Z]/;
  print "<tr><td colspan=9 align=center><b>$quarter_name</b></tr>\n";
  print qq(<tr><td>Men<td align=center>${"$quarter\_stats"}{M_Student});
  print qq(<td align=center>${"$quarter\_stats"}{M_Faculty});
  print qq(<td align=center>${"$quarter\_stats"}{M_Spouse});
  print "<td>&nbsp;<td>&nbsp;<td>&nbsp<td>&nbsp;<td>&nbsp;</tr>\n";
  print qq(<tr><td>Women<td align=center>${"$quarter\_stats"}{F_Student});
  print qq(<td align=center>${"$quarter\_stats"}{F_Faculty});
  print qq(<td align=center>${"$quarter\_stats"}{F_Spouse});
  print "<td>&nbsp;<td>&nbsp;<td>&nbsp<td>&nbsp;<td>&nbsp;</tr>\n";
  print "<tr><td><b>$quarter_name Totals</b>";
  print qq(<td align=center><b>${"$quarter\_stats"}{Student}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{Faculty}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{Spouse}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{RS}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{L}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{I}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{total}</b>);
  print qq(<td align=center><b>${"$quarter\_stats"}{paid_wac}</tr>\n);
 }

 print <<"part_2";
  <tr><td colspan=9>&nbsp;</tr>
  <tr><th>&nbsp;<th>Student<th>Faculty/Staff<th>Spouse
  <th>RS<th>&nbsp;L&nbsp;<th>&nbsp;I&nbsp;
  <th>Total Members<th>Paid WAC</tr>
  <tr><td><b>Annual Totals</b>
  <td align=center><b>$annual_stats{Student}</b>
  <td align=center><b>$annual_stats{Faculty}</b>
  <td align=center><b>$annual_stats{Spouse}</b>
  <td align=center><b>$annual_stats{RS}</b>
  <td align=center><b>$annual_stats{L}</b>
  <td align=center><b>$annual_stats{I}</b>
  <td align=center><b>$annual_stats{total}</b>
  <td align=center><b>$annual_stats{paid_wac}</b></tr>
  </table>
  </center></body></html>
part_2

 exit(0);
}

else {
 annual_calendar();
}

exit(0);

sub change_dates {
 return 0;
}

sub html_error {
 print header();
 print "<html>oops</html>\n";
}

sub annual_calendar {
 # generate school year options
 @school_year_list = <????-????>;	# matches anything like 1999-2000 
 foreach (@school_year_list) {
  if ($_ eq $school_year) {$selected="selected";}
  else {$selected="";}
  $school_year_options .= "<option $selected>$_";
 }
 # generate month options
 @months = qw(zero January February March April May June July August September October November December);
 for ($i=1; $i<=12; ++$i) {
  (($autumn_month == $i) && ($select_autumn="selected")) || ($select_autumn="");
  (($winter_month == $i) && ($select_winter="selected")) || ($select_winter="");
  (($spring_month == $i) && ($select_spring="selected")) || ($select_spring="");
  (($summer_month == $i) && ($select_summer="selected")) || ($select_summer="");
  $autumn_month_options .= "<option $select_autumn value=$i>$months[$i]";
  $winter_month_options .= "<option $select_winter value=$i>$months[$i]";
  $spring_month_options .= "<option $select_spring value=$i>$months[$i]";
  $summer_month_options .= "<option $select_summer value=$i>$months[$i]";
 }
 # generate day options
 for ($i=1; $i<=31; ++$i) {
  (($autumn_day == $i) && ($select_autumn="selected")) || ($select_autumn="");
  (($winter_day == $i) && ($select_winter="selected")) || ($select_winter="");
  (($spring_day == $i) && ($select_spring="selected")) || ($select_spring="");
  (($summer_day == $i) && ($select_summer="selected")) || ($select_summer="");
  $autumn_day_options .= "<option $select_autumn>$i";
  $winter_day_options .= "<option $select_winter>$i";
  $spring_day_options .= "<option $select_spring>$i";
  $summer_day_options .= "<option $select_summer>$i";
 }
 # send this to the browser
 print header();
 print <<"end_html1";
  <html><head><title>UKC: Quarterly Statistics</title></head>
  <body><center>
  <form action="stats.cgi" method="post">
  <p>&nbsp;
  <hr size=2 noshade width="80%">
  <p><b>Report Membership Stats</b>
  <p>Show membership statistics for all quarters
  <br> of the <select name="school_year">$school_year_options</select>
  academic year
  <input type="submit" name="submit"
  style="background: #5588ff; color: #ffffff; font-weight: bold"
  value="stats">
  <p>&nbsp;
  <hr size=2 noshade width="80%">
  <p>&nbsp;<b>$school_year Academic Calendar</b>
  <p><table border=1 cellspacing=0 cellpadding=4>
  <tr><th>Quarter<th>Begins</tr>
  <tr><td align="center">Autumn<td align=center><select name="autumn_month">$autumn_month_options</select>
  <select name="autumn_day">$autumn_day_options</select></tr>
  <tr><td align="center">Winter<td align=center><select name="winter_month">$winter_month_options</select>
  <select name="winter_day">$winter_day_options</select></tr>
  <tr><td align="center">Spring<td align=center><select name="spring_month">$spring_month_options</select>
  <select name="spring_day">$spring_day_options</select></tr>
  <tr><td align="center">Summer<td align=center><select name="summer_month">$summer_month_options</select>
  <select name="summer_day">$summer_day_options</select></tr>
  <tr><td align="center" colspan=2>These dates are automatically generated.  If they are incorrect,
  <br>make changes in the table above, and 
  <input type="hidden" name="school_year" value="$school_year">
  <input type="submit" name="submit"
  style="background: #5588ff; color: #ffffff; font-weight: bold"
  value="change dates"></tr>
  </table>
  </form>
  <p>&nbsp;
  <hr size=2 noshade width="80%">
  </center></body></html>
end_html1

}

