# find out why the 500 error and fix the issue
exec {'fix_wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}