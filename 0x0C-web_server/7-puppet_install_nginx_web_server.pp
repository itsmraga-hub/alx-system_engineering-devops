# install and set up nginx

package { 'nginx':
  ensure  => 'installed',
}

file { 'var/www/html/index.html':
  require => Package['nginx'],
  content => 'Hello World!',
}

