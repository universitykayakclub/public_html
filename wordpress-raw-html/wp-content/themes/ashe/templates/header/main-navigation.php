<?php if ( ashe_options( 'main_nav_label' ) === true ) : ?>
<div id="main-nav" class="clear-fix">

	<div <?php echo esc_attr(ashe_options( 'general_header_width' )) === 'contained' ? 'class="boxed-wrapper"': ''; ?>>	
		
		<!-- Alt Sidebar Icon -->
		<?php if ( ashe_options( 'main_nav_show_sidebar' ) === true ) : ?>
		<div class="main-nav-sidebar">
			<div>
				<span></span>
				<span></span>
				<span></span>
			</div>
		</div>
		<?php endif; ?>


		<!-- Icons -->
		<div class="main-nav-icons">
			<?php if ( ashe_options( 'main_nav_show_search' ) === true ) : ?>
			<div class="main-nav-search">
				<i class="fa fa-search"></i>
				<i class="fa fa-times"></i>
				<?php get_search_form(); ?>
			</div>
			<?php endif; ?>
		</div>


		<!-- Menu -->
		<span class="mobile-menu-btn">
			<i class="fa fa-chevron-down"></i>
		</span>

		<?php // Navigation Menus

		wp_nav_menu( array(
			'theme_location' 	=> 'main',
			'menu_id'        	=> 'main-menu',
			'menu_class' 		=> '',
			'container' 	 	=> 'nav',
			'container_class'	=> 'main-menu-container',
			'fallback_cb' 		=> 'ashe_main_menu_fallback'
		) );

		wp_nav_menu( array(
			'theme_location' 	=> 'main',
			'menu_id'        	=> 'mobile-menu',
			'menu_class' 		=> '',
			'container' 	 	=> 'nav',
			'container_class'	=> 'mobile-menu-container',
			'fallback_cb' 		=> false
		) );

		?>

	</div>

</div><!-- #main-nav -->
<?php endif; ?>