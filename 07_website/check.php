<?php

require 'CaptchasDotNet.php';

// See query.php for documentation

$captchas = new CaptchasDotNet ('demo', 'secret',
                                '/tmp/captchasnet-random-strings','3600',
                                'abcdefghkmnopqrstuvwxyz','6',
                                '240','80');

// Read the form values
$message       = $_REQUEST['message'];
$password      = $_REQUEST['password'];
$random_string = $_REQUEST['random'];
?>

<html>
  <head>
    <title>Sample PHP CAPTCHA Query</title>
  </head>
  <h1>Sample PHP CAPTCHA Query</h1>

<?php
  // Check the random string to be valid and return an error message
  // otherwise.
  if (!$captchas->validate ($random_string))
  {
    echo 'Every CAPTCHA can only be used once. The current CAPTCHA has already been used. Try again.';
  }
  // Check, that the right CAPTCHA password has been entered and
  // return an error message otherwise.
  elseif (!$captchas->verify ($password))
  {
    echo 'You entered the wrong password. Aren\'t you human? Please use back button and reload.';
  }
  // Return a success message
  else
  {

	$to = "york.matt@gmail.com, myork@cs.washington.edu, mattmanpower@comcast.net, myork@u.washington.edu";
	$subject = "Hi!";
	$body = $message;
	if (mail($to, $subject, $body)) {
  echo("<p>Message successfully sent!</p>");
 } else {
  echo("<p>Message delivery failed...</p>");
 }
    echo 'Your message was verified to be entered by a human and is "' . $message . '"';
  }
?>

</html>
