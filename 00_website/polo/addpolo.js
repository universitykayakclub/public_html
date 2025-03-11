// Constants

        var defaultEmptyOK = false
        var mPrefix = "You did not enter a value into the "
        var mSuffix = " field. This is a required field. Please enter it now."
        var whitespace = " \t\r\n"


// Verifies that the form is filled out correctly from the client-side
function CheckForm() {

	var f = document.polo_email;

	if (f.email_action.value == 'Remove') {
		var rMsg = 'Are you sure you want to remove yourself from the kayak polo list?'
		if (!confirm(rMsg))
			return false;
	}

	var validE = checkEmail(f.email_address);
	var validN = !isEmpty(f.full_name.value);
	var msg = 'The following field(s) contain invalid data:\n\n';	

	if (!validN)
		msg += '\tName\n';
	if (!validE)
		msg += '\tEmail Address\n'
	
	if (validE && validN) {
		return true;
	}
	else {
		window.alert(msg);
		return false;
	}

	// checkEmail (TEXTFIELD theField [, BOOLEAN emptyOK==false])
	//
	// Check that string theField.value is a valid Email.
	//
	// For explanation of optional argument emptyOK,
	// see comments of function isInteger.
	
	function checkEmail (theField, emptyOK)
	{   if (checkEmail.arguments.length == 1)
			emptyOK = defaultEmptyOK;
	    if ((emptyOK == true) && (isEmpty(theField.value)))
	    	return true;
	    else
	    	if (!isEmail(theField.value, false)) 
	       		return false;
	    	else
	    		return true;
	}
	
	// Check whether string s is empty.
	
	function isEmpty(s)
	{   return ((s == null) || (s.length == 0))
	}
	
	// isEmail (STRING s [, BOOLEAN emptyOK])
	// 
	// Email address must be of form a@b.c -- in other words:
	// * there must be at least one character before the @
	// * there must be at least one character before and after the .
	// * the characters @ and . are both required
	//
	// For explanation of optional argument emptyOK,
	// see comments of function isInteger.
	
	function isEmail (s)
	{   if (isEmpty(s)) 
	       if (isEmail.arguments.length == 1) return defaultEmptyOK;
	       else return (isEmail.arguments[1] == true);
	   
	    // is s whitespace?
	    if (isWhitespace(s)) return false;
	    
	    // there must be >= 1 character before @, so we
	    // start looking at character position 1 
	    // (i.e. second character)
	    var i = 1;
	    var sLength = s.length;
	
	    // look for @
	    while ((i < sLength) && (s.charAt(i) != "@"))
	    { i++
	    }
	
	    if ((i >= sLength) || (s.charAt(i) != "@")) return false;
	    else i += 2;
	
	    // look for .
	    while ((i < sLength) && (s.charAt(i) != "."))
	    { i++
	    }
	
	    // there must be at least one character after the .
	    if ((i >= sLength - 1) || (s.charAt(i) != ".")) return false;
	    else return true;
	}
	
	// Notify user that required field theField is empty.
	// String s describes expected contents of theField.value.
	// Put focus in theField and return false.
	
	function warnEmpty (theField, s)
	{   theField.focus()
	    alert(mPrefix + s + mSuffix)
	    return false
	}
	
	// Returns true if string s is empty or 
	// whitespace characters only.
	
	function isWhitespace (s)
	
	{   var i;
	
	    // Is s empty?
	    if (isEmpty(s)) return true;
	
	    // Search through string's characters one by one
	    // until we find a non-whitespace character.
	    // When we do, return false; if we don't, return true.
	
	    for (i = 0; i < s.length; i++)
		    {   
	        // Check that current character isn't whitespace.
	        var c = s.charAt(i);
	
	        if (whitespace.indexOf(c) == -1) return false;
	    }
	
	    // All characters are whitespace.
	    return true;
	}
}