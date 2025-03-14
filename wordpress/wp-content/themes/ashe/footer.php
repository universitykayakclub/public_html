		</div><!-- #page-content -->

		<!-- Page Footer -->
		<footer id="page-footer" class="<?php echo esc_attr(ashe_options( 'general_footer_width' )) === 'boxed' ? 'boxed-wrapper ': ''; ?>clear-fix">
			
			<!-- Scroll Top Button -->
			<span class="scrolltop">
				<i class="fa fa fa-angle-up"></i>
			</span>

			<div class="page-footer-inner <?php echo ashe_options( 'general_footer_width' ) === 'contained' ? 'boxed-wrapper': ''; ?>">

			<!-- Footer Widgets -->
			<?php echo get_template_part( 'templates/sidebars/footer', 'widgets' ); ?>

			<div class="footer-copyright">
				<div class="copyright-info">
				<?php

				$copyright = ashe_options( 'page_footer_copyright' );
				$copyright = str_replace( '$year', date_i18n( __('Y','ashe') ), $copyright );
				$copyright = str_replace( '$copy', '&copy;', $copyright );

				if ( ashe_is_preview() ) {
					echo esc_html__( '&copy; 2018 - All Rights Reserved.', 'ashe' );
				} else {
					echo wp_kses_post( $copyright );
				}

				?>
				</div>
				
				<div class="credit">
					<?php esc_html_e( 'Ashe Theme by ', 'ashe' ); ?>
					<a href="<?php echo esc_url( 'http://wp-royal.com/' ); ?>">
					<?php esc_html_e( 'Royal-Flush', 'ashe' ); ?>
					</a>
				</div>

			</div>

			</div><!-- .boxed-wrapper -->

		</footer><!-- #page-footer -->

	</div><!-- #page-wrap -->

<?php wp_footer(); ?>

</body>
</html>