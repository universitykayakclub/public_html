<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'skykomish');

/** MySQL hostname */
define('DB_HOST', 'ukc.vergil.u.washington.edu:10378');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '}(Ye<{4:t97j%9v<Kr4[uwLe43=>PwK=NyC|i(ii{VlVvNfdj7&7+mp:khi+F~+%');
define('SECURE_AUTH_KEY',  '9hw.uK7u-=O</Sk|mMA#zYHcC#ts?SjxL!~9}pH2ti8 -PC$m&14)N$Di#O[p*>F');
define('LOGGED_IN_KEY',    'ybi68jkH7mB%aRRG_P{_HK53b`kDQZHGq2A_YtX~}fG1a=O1M8; ]Do*lsY+0H=+');
define('NONCE_KEY',        'UFX{-xzm&k0QeMmaZg{J}hDch?Z5F3r,=9Zu*#h+bEfu&a|t/&`iNXq!(E%_m{ie');
define('AUTH_SALT',        ']?E^t$~WvX|IquxQ>7;,8A)CIdV9}?YGU~`Gq2e/d kiekDrZ=*n7WR&QuxHFHx(');
define('SECURE_AUTH_SALT', 'vpS}|3Hh|^eJ |m|$faz3iU;Q{7Uql}^]b!`Pn_t]Gu :7+V3n+<W]dVvJ|7._c]');
define('LOGGED_IN_SALT',   'LMULfeSx}dDgSI8[BsOz(mhu$P0Wl2mwT&>RI8X~-Z)E5-Y8xo*<v_**1Zu0V]q ');
define('NONCE_SALT',       'kA%h0/SF>+evTqt_&v^#PP`/OUq*r^i[yp;h/hQ|-eV?D(bM!.Bq{]N YT-&XPZg');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * WordPress Localized Language, defaults to English.
 *
 * Change this to localize WordPress.  A corresponding MO file for the chosen
 * language must be installed to wp-content/languages. For example, install
 * de.mo to wp-content/languages and set WPLANG to 'de' to enable German
 * language support.
 */
define ('WPLANG', '');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');

