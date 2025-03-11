#!/usr/local/bin/perl

# Makes sure the the script was called from the correct page
if ($ENV{'HTTP_REFERER'} eq "http://students.washington.edu/~ukc/polo/polo.html") {

#   Read in the data from the form
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	
#       Replaces all the pluses with spaces
	$value =~ tr/+/ /;
	
#       Restores all charactors to ascii
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
    }
    
    $name = $FORM{"full_name"};
    $address = $FORM{"email_address"};
    $action = $FORM{"email_action"};

    print "Content-type:text/html\n\n";

    print <<MyHead;
<html>
<head><title>Kayak Polo Email List Receipt</title></head>
<body background="../bits/swirl.gif">
<H1>UKC Kayak Polo</H1>
<table border="0" cellpadding="0">
  <tr>
    <td>
      <IMG height=115 src="polologo.gif" width=236 align=middle>
    </td>
    <td>
        &nbsp; Return to <a href="polo.html">UKC Polo</a>
            <p>&nbsp; Go to <A href="../main/UKCmain.cgi">UKC Index</A>
    </td>
  </tr>
</table>

MyHead
    
#   Checks to make sure it's a valid email address and the name is not empty
    if ($address =~ /[\w\-]+\@[\w\-]+\.[\w\-]+/ && $name ne "") {
	
	open(MAIL, "|/usr/lib/sendmail -t");
	print MAIL "To: listproc\@u.washington.edu\n";
	print MAIL "From: $address\n";
	print MAIL "Subject:\n\n";
	
#       Add or remove as desired
	if ($action eq "Remove") {
	    print MAIL "un";
	}
	
	print MAIL "subscribe ukc-polo $name\n\n";
	
	close(MAIL);
    }
    else {
#       Print error if input is invalid	
	print <<ToError;
<h4>Either you email address, <font color="#FF0000">$address</font>, or your name, <font color="#FF0000">$address</font>, is invalid.  Please try again.</h4>
<h4>Yours in paddling,<br>Kayak Polo Sultan</h4> 

ToError

    }

#   Print the correct message based on email action
    if ($action eq "Add") {
	print <<ToAdd;
<h4>Your request for <font color="#FF0000">$address</font> to be added to the University Kayak Club's Kayak Polo email list has been sent.&nbsp; You will receive a confirmation email from <font color="#FF0000">University of Washington ListProcessor</font> within 24 hours, although they are usually sent within a few minutes.</h4>
<h4>This email will have a subject like <font color="#FF0000">ListProc Command Confirmation. Conf-Cookie:899362633-111880-5</font> and will ask you to reply if you really do want to add yourself to the Kayak Polo email list.&nbsp; After you reply, you will receive another email stating the the subscription was successful.&nbsp; You are now added to the list and will begin to receive messages.</h4>
<h4>If, for some reason, you do not receive a confirmation email within 24 hours, you most likely misspelled your email address.&nbsp; Check the address at the beginning of this page, and make sure it is correct.  If it is not correct, return to the main polo page and try again.&nbsp; If you would like to remove yourself from the list again in the future, return to the main polo page and fill out the email list form.</h4>
<h4>Thank you for joining the Kayak Polo email list, now it's time to have fun and play kayak polo.</h4>
<h4>Yours in paddling,<br>Kayak Polo Sultan</h4>

ToAdd
}
    else {
	print <<ToRemove;
<h4>Your request for <font color="#FF0000">$address</font> to be removed from the University Kayak Club's Kayak Polo email list has been sent.&nbsp; You will receive a confirmation email from <font color="#FF0000">University of Washington ListProcessor</font> within 24 hours, although they usually are sent within a few minutes.</h4>
<h4>This email will have a subject like <font color="#FF0000">ListProc Command Confirmation. Conf-Cookie:899362633-111880-5</font> and will ask you to reply if you really do want to remove yourself from the Kayak Polo email list.&nbsp; After you reply, you will receive another email stating the the removal was successful.&nbsp; You are now removed from the list and will not receive any more messages.</h4>
<h4>If, for some reason, you do not receive a confirmation email within 24 hours, you most likely misspelled your email address.&nbsp; Check the address at the beginning of this page, and make sure it is correct.  If it is not correct, return to the main polo page and try again.&nbsp; If you would like to add yourself to the list again in the future, return to the main polo page and fill out the email list form.</h4>
<h4>Thank you for being a part of the Kayak Polo email list, you are still welcome to come and play kayak polo anytime.</h4>
<h4>Yours in paddling,<br>Kayak Polo Sultan</h4>

ToRemove
}

    print <<EndOfHtml;
</body>
</html>

EndOfHtml

}
else {
    print "Location:polo.html\n\n";
}
