<!-- Main Container -->
<div class="main-container">
	
	<?php

	// Blog Grid
	echo '<ul class="blog-grid">';
	
	if ( have_posts() ) :

		// Loop Start
		while ( have_posts() ) :

			the_post();

			echo '<li>';

			?>
			<article id="post-<?php the_ID(); ?>" <?php post_class('blog-post'); ?>>
				
				<div class="post-media">
					<a href="<?php echo esc_url( get_permalink() ); ?>"></a>
					<?php the_post_thumbnail('ashe-full-thumbnail'); ?>
				</div>

				<header class="post-header">

			 		<?php

					$category_list = get_the_category_list( ',&nbsp;&nbsp;' );

					if ( ashe_options( 'blog_page_show_categories' ) === true && $category_list ) {
						echo '<div class="post-categories">' . $category_list . ' </div>';
					}

					?>

					<?php if ( get_the_title() ) : ?>
					<h1 class="post-title">
						<a href="<?php esc_url( the_permalink() ); ?>"><?php the_title(); ?></a>
					</h1>
					<?php endif; ?>

					<?php if ( ashe_options( 'blog_page_show_date' ) === true ) : ?>
					<div class="post-meta clear-fix">
						<span class="post-date"><?php the_time( get_option( 'date_format' ) ); ?></span>
					</div>
					<?php endif; ?>
					
				</header>

				<?php if ( ashe_options( 'blog_page_post_description' ) !== 'none' ) : ?>

				<div class="post-content">
					<?php
					if ( ashe_options( 'blog_page_post_description' ) === 'content' ) {
						the_content('');
					} elseif ( ashe_options( 'blog_page_post_description' ) === 'excerpt' ) {
						ashe_excerpt( 110 );												
					}
					?>
				</div>

				<?php endif; ?>

				<div class="read-more">
					<a href="<?php echo esc_url( get_permalink() ); ?>"><?php esc_html_e( 'read more','ashe' ); ?></a>
				</div>
				
				<footer class="post-footer">

					<?php if ( ashe_options( 'blog_page_show_author' ) === true ) : ?>
					<span class="post-author">
						<a href="<?php echo esc_url(get_author_posts_url( get_the_author_meta( 'ID' ), get_the_author_meta( 'user_nicename' ) )); ?>">
							<?php echo get_avatar( get_the_author_meta( 'ID' ), 30 ); ?>
						</a>
						<?php the_author_posts_link(); ?>	
					</span>
					<?php endif; ?>

					<?php
					if ( ashe_options( 'blog_page_show_comments' ) === true ) {
						comments_popup_link( esc_html__( 'No Comments', 'ashe' ), esc_html__( '1 Comment', 'ashe' ), '% '. esc_html__( 'Comments', 'ashe' ), 'post-comments');
					}
					?>
					
				</footer>

				<!-- Related Posts -->
				<?php
				ashe_related_posts( esc_html__( 'You May Also Like','ashe' ), ashe_options( 'blog_page_related_orderby' ) );
				?>

			</article>
		
			<?php

			echo '</li>';

		endwhile; // Loop End

	else:

	?>

	<div class="no-result-found">
		<h3><?php esc_html_e( 'Nothing Found!', 'ashe' ); ?></h3>
		<p><?php esc_html_e( 'Sorry, but nothing matched your search terms. Please try again with some different keywords.', 'ashe' ); ?></p>
		<div class="ashe-widget widget_search">
			<?php get_search_form(); ?>
		</div> 
		
	</div>

	<?php
	
	endif; // have_posts()

	echo '</ul>';

	?>

	<?php get_template_part( 'templates/grid/blog', 'pagination' ); ?>

</div><!-- .main-container -->