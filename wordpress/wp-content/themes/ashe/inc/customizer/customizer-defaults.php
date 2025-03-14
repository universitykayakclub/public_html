<?php

function ashe_options( $control ) {

	$ashe_defaults = array(
		'colors_content_accent' => '#ca9b52',
		'colors_content_bg' => '#ffffff',
		'colors_header_bg' => '#ffffff',
		'general_sidebar_width' => '270',
		'general_sidebar_sticky' => true,
		'general_header_width' => 'contained',
		'general_slider_width' => 'boxed',
		'general_links_width' => 'boxed',
		'general_content_width' => 'boxed',
		'general_single_width' => 'boxed',
		'general_footer_width' => 'contained',
		'top_bar_label' => true,
		'header_image_label' => true,
		'header_image_bg_image_size' => 'cover',
		'title_tagline_logo_width' => '500',
		'main_nav_label' => true,
		'main_nav_align' => 'center',
		'main_nav_show_search' => true,
		'main_nav_show_sidebar' => true,
		'featured_slider_label' => false,
		'featured_slider_display' => 'all',
		'featured_slider_category' => 'null',
		'featured_slider_amount' => '3',
		'featured_slider_navigation' => true,
		'featured_slider_pagination' => true,
		'featured_links_label' => false,
		'featured_links_title_1' => '',
		'featured_links_url_1' => '',
		'featured_links_image_1' => '',
		'featured_links_title_2' => '',
		'featured_links_url_2' => '',
		'featured_links_image_2' => '',
		'featured_links_title_3' => '',
		'featured_links_url_3' => '',
		'featured_links_image_3' => '',
		'blog_page_post_description' => 'excerpt',
		'blog_page_post_pagination' => 'default',
		'blog_page_show_categories' => true,
		'blog_page_show_date' => true,
		'blog_page_show_comments' => true,
		'blog_page_show_dropcaps' => true,
		'blog_page_show_author' => true,
		'blog_page_related_orderby' => 'related',
		'single_page_show_categories' => true,
		'single_page_show_date' => true,
		'single_page_show_author' => true,
		'single_page_show_comments' => true,
		'single_page_show_author_desc' => true,
		'single_page_related_orderby' => 'related',
		'social_media_window' => true,
		'social_media_icon_1' => 'facebook',
		'social_media_url_1' => '',
		'social_media_icon_2' => 'twitter',
		'social_media_url_2' => '',
		'social_media_icon_3' => 'instagram',
		'social_media_url_3' => '',
		'social_media_icon_4' => 'pinterest',
		'social_media_url_4' => '',
		'page_footer_copyright' => '',
		'preloader_label' => false
	);

	// merge defaults and options
	$ashe_defaults = wp_parse_args( get_option('ashe_options'), $ashe_defaults );

	// return control
	return $ashe_defaults[ $control ];

}