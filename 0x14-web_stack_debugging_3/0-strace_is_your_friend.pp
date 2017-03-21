# Fix a typeo in a .php file to run WordPress
exec { 'sed':
  path    => '/usr/bin/:/bin/:/user/sbin/:/sbin/',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
