<?php

if ( ! is_active_sidebar( 'footer-widgets' ) && ! ashe_is_preview() ) {
	return;
}

?>

<div class="footer-widgets clear-fix">
	<?php

	if ( ashe_is_preview() ) {
		ashe_preview_footer_sidebar();
	} else {
		dynamic_sidebar( 'footer-widgets' );
	}

	?>
</div>