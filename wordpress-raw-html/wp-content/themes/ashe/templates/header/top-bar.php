<?php if ( ashe_options( 'top_bar_label' ) === true ) : ?>

<div id="top-bar" class="clear-fix">
	<div <?php echo esc_attr(ashe_options( 'general_header_width' )) === 'contained' ? 'class="boxed-wrapper"': ''; ?>>
		
		<?php

		// Menu
		wp_nav_menu( array(
			'theme_location' 	=> 'top',
			'menu_id' 		 	=> 'top-menu',
			'menu_class' 		=> '',
			'container' 	 	=> 'nav',
			'container_class'	=> 'top-menu-container',
			'fallback_cb' 		=> 'top_menu_fallback'
		) );
		
		// Social Icons
		ashe_social_media( 'top-bar-socials' );

		?>

	</div>
</div><!-- #top-bar -->

<?php endif; ?>