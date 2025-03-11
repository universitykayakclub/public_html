<br />
<form action="" method="post">
	<table style="margin: 0 auto">
		<tr>
				   <td width="275px" style="padding-right: 15px; vertical-align: top;">
				   <h3 style="text-align: center; padding: 0; margin: 0">Email List!</h3>
		   Want UKC announcements and the likes? Add yourself to our email list! The 
image validation thingamajiggy is to ensure you're not a robot. There's a 
refresh button in there in case you're not human enough to read the picture
they gave you. Note: only current club members can go on trips and use equipment.
		   </td>
			<td>
			<?php
			
			require_once('recaptchalib.php');
			$publickey = "6Ld6VQEAAAAAAFlziLV5wvIOaeK5qRLuF51igR87";
			$privatekey = "6Ld6VQEAAAAAAE8XzfmQsQFcftudDA4ZEEBuBwxr";
			
			# the response from reCAPTCHA
			$resp = null;
			# the error code from reCAPTCHA, if any
			$error = null;
			
			# are we submitting the page?
			if ($_POST["submit"]) {
			  $resp = recaptcha_check_answer ($privatekey,
			                                  $_SERVER["REMOTE_ADDR"],
			                                  $_POST["recaptcha_challenge_field"],
			                                  $_POST["recaptcha_response_field"]);
			
			  if ($resp->is_valid) {
				    $to = "myork@u.washington.edu, ukc-all-request@mailman.u.washington.edu";
					$subject = "";
					$body = "subscribe kayaker nodigest address=".$_REQUEST['address'];
					$headers = "From: ukc@u.washington.edu";
					echo('<br /><span style="color: red;">');
					if (mail($to, $subject, $body, $headers)) {
				 		echo("Email added");
				 	} else {
				  		echo("Something failed - email Matt");
				 	}
				 	echo('</span>');
			  } else {
			    $error = $resp->error;
			  }
			}
			echo recaptcha_get_html($publickey, $error);
			?>
		   <input type="submit" name="submit" value="submit" style="float: right"/>
			<label for="address">Email:</label>
			<input type="text" id="address" name="address" />		   
		   </td>
   	</tr>
	</table>
</form>
<br />
