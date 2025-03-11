#!/usr/local/bin/perl

# This script generates academic quarter start dates,
# figures out what academic year it is, writes start
# dates to a file (if this is the year's first visit),
# and creates a series of html forms to deal with
# member lists.

# get current date
($month, $day, $year) = split('/', `date +"%m/%d/%Y"`);
chomp($year);		# get rid of newline
# use full_date (YYYYMMDD) in absolute comparisons
$full_date = sprintf("%4.4d%2.2d%2.2d", $year, $month, $day) + 0;

# get school year start date of current calendar year
($start_month,$start_day) = start_date(1, $year);
$full_start_date = sprintf("%4.4d%2.2d%2.2d", $year, $start_month, $start_day) + 0;

# figure out academic year
if ($full_date < $full_start_date) {
 $school_year = sprintf("%4d-%4d", $year-1, $year);
}
else {
 $school_year = sprintf("%4d-%4d", $year, $year+1);
}

unless (-d $school_year) {
 mkdir($school_year,0777) or die("can't create directory $school_year\n");
 open(MEMBERS, ">$school_year/members") or die("can't create $MEMBERS\n");
 close(MEMBERS);
}

$DATEFILE = "$school_year/start_dates";

# get quarter start dates (if they have been generated)
if (-e $DATEFILE) {
 open(DATEFILE) or die("can't read from $DATEFILE\n");
 @all_dates=<DATEFILE>;
 close(DATEFILE);
 foreach (@all_dates) {chomp;}
 ($autumn_month, $autumn_day) = split('/', $all_dates[0]);
 ($winter_month, $winter_day) = split('/', $all_dates[1]);
 ($spring_month, $spring_day) = split('/', $all_dates[2]);
 ($summer_month, $summer_day) = split('/', $all_dates[3]);
}
# or create them (if it's the start of a new year)
else {
 ($start_year, $finish_year) = split('-', $school_year);
 ($autumn_month, $autumn_day) = start_date(1, $start_year);
 ($winter_month, $winter_day) = start_date(2, $finish_year);
 ($spring_month, $spring_day) = start_date(3, $finish_year);
 ($summer_month, $summer_day) = start_date(4, $finish_year);
 open(OUT, ">$DATEFILE") or die("can't create $DATEFILE\n");
 print OUT "$autumn_month/$autumn_day\n";
 print OUT "$winter_month/$winter_day\n";
 print OUT "$spring_month/$spring_day\n";
 print OUT "$summer_month/$summer_day\n";
 close(OUT);
}

# generate school year options
@school_year_list = <????-????>;	# matches anything like 1999-2000
foreach (@school_year_list) {
 if ($_ eq $school_year) {$selected="selected";}
 else {$selected="";}
 $school_year_options .= "<option $selected>$_";
}


#############################################
# here's the part that goes to the browser

print "Content-Type: text/html\n\n<html>";
print <<"end_html";

 <head><title>UKC Members</title></head>
 <body><center>

 <hr size=2 noshade width="80%">
 <b>Membership Lists</b>
 <br><form action="list.cgi" method="post">
 List members for the
 <select name="school_year">$school_year_options</select>
 academic year, sorted by
 <select name="by">
 <option>last name
 <option>join date
 </select>
 &nbsp;<input type="submit" 
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="list">
 </form>

 <hr size=2 noshade width="80%">
 <b>Quarterly Reports</b>
 <br><form action="stats.cgi" method="post">
 Generate membership statistics for the 
 <select name="school_year">$school_year_options </select>academic year
 &nbsp;<input type="submit" name="submit"
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="stats">
 </form>

 <hr size=2 noshade width="80%">
 <b>Add New Members</b>
 <br><form action="add.cgi" method="post">
 Enter number of new members (one form per join date)
 <input type="text" name="new" maxlength=2 size=3>
 <input type="hidden" name="school_year" value="$school_year">
 <input type="hidden" name="year" value="$year">
 <input type="hidden" name="month" value="$month">
 <input type="hidden" name="day" value="$day">
 &nbsp;<input type="submit" 
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="add">
 </form>

 <hr size=2 noshade width="80%">
 <b>Edit Membership List</b>
 <br>This only needs to be done to correct mistyped
 <br>information, add email addresses, remove members, etc.
 <br> To add new members, use the new member form.
 <br><form action="edit.cgi" method="post">
  Edit the $school_year membership list, sorted by
 <select name="by">
 <option>last name
 <option>join date
 </select>
 <input type="hidden" name="school_year" value="$school_year">
 &nbsp;<input type="submit" 
 style="background: #5588ff; color: #ffffff; font-weight: bold"
 value="edit">
 <br><font size="-1">Warning:  Long forms may hang browsers on Windows98</font>
 </form>

 <hr size=2 noshade width="80%">

 </center></body></html>

end_html

#############################################

exit(0);

sub start_date {

 my($quarter, $year) = @_;	# local quarter number and year
 my(@lines, $week);
 my($start_month, $start_day);	# local values to return

 if ($quarter==1) {$start_month=9;}	# autumn
 if ($quarter==2) {$start_month=1;}	# winter
 if ($quarter==3) {$start_month=3;}	# spring
 if ($quarter==4) {$start_month=6;}	# summer

 # The unix cal command returns dates for specified
 # month and year.  The first line returned is the month
 # and year.  The second line is the days of the week
 # The remaining lines ( $lines[2] through $lines[7] )
 # are the dates on the calendar.
  
 open(CAL, "cal $start_month $year|");
 @lines=<CAL>;
 close(CAL);

 # autumn starts last Monday of September
 if ($quarter==1) {
  $week=$lines[6];
  $start_day = substr($week, 4, 2)+0;	# date of quarter start
  if ($start_day == 24) {			
   $start_month=10;			# if no Mon in last week
   $start_day=1;
  }
 }

 # winter starts 1st Monday of January
 if ($quarter==2) {
  $week=$lines[2];
  $start_day = substr($week, 4, 2)+0;	# date of quarter start
  if ($start_day < 1) {
   $week=$lines[3];			# if no Mon in 1st week
   $start_day = substr($week, 4, 2)+0;
  }
  if ($start_day == 1) {$start_day = 2;}	# hangover accomodation
 }

 # spring starts last Monday of March
 if ($quarter==3) {
  $week=$lines[6];
  $start_day = substr($week, 4, 2)+0;	# date of quarter start
  if ($start_day == 24) {			
   $start_month=3;			# if no Mon in last week
   $start_day=31;
  }
  if ($start_day == 25) {			
   $start_month=4;			# if no Mon in last week
   $start_day=1;
  }
 }

 # summer starts 2nd to last week of June
 if ($quarter==4) {
  $week=$lines[5];
  $start_day = substr($week, 4, 2)+0;	# date of quarter start
  if ($start_day == 17) {
   $start_day=24;			# if no Mon in last week
  }
 }

 return($start_month,$start_day);

}
