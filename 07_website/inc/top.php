<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
	<base href="http://students.washington.edu/ukc/07_website/"/>
	<!-- <base href="http://localhost:8000/"/> -->
	<link rel="stylesheet" type="text/css" href="ukc_style.css" />
		        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
		        <meta name = "description" content = "Whitewater and Sea Kayaking for Students, Faculty, and Staff at the University of Washington" />
	<title>University Kayak Club - @ the University of Washington</title>
</head>
<body>

<div id="wrap">
	<div id="top_banner">
		<div id="title">
			<div class="line1">University Kayak Club</div>
			<div class="line2">@ the University of Washington</div>
		</div><!--title-->
		<div id="top_nav">
			<ul id="nav">
				<li><a href="index.php" title="UKC Home">Home</a></li>
				<li><img class="nav_line" src="imagelib/light_purple_dot.gif" width="1" height="30" /></li>
				<li><a href="/ukc/blog" title="UKC Blog">Blog</a></li>
				<li><img class="nav_line" src="imagelib/light_purple_dot.gif" width="1" height="30" /></li>
				<li><a href="seakayaking" title="Sea Kayaking">Sea</a></li>
				<li><img class="nav_line" src="imagelib/light_purple_dot.gif" width="1" height="30" /></li>
				<li><a href="whitewater" title="Whitewater">Whitewater</a></li>
				<li><img class="nav_line" src="imagelib/light_purple_dot.gif" width="1" height="30" /></li>
				<li><a href="lake_polo" title="Lake Polo">Lake/Polo</a></li>
				<li><img class="nav_line" src="imagelib/light_purple_dot.gif" width="1" height="30" /></li>
				<li><a href="contact_us.php" title="">Contact</a></li>
			</ul><!--nav-->
		</div><!--top_nav-->
	</div><!--top_banner-->
	<div id="border_begin">
	<?
	$cur_second = date("s");
	$num_pics = 4;
	$rand_img = $cur_second % $num_pics;
	?>
		<div id="header">
			<img src="imagelib/landscape_masthead<?echo $rand_img?>.jpg" alt="University Kayak Club" />
		</div>	
		
