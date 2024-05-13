#!/usr/bin/env bash
#automation to create a custom iTTP header response, but with Puppet.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        
        server_name _;
        
        location / {
            try_files $uri $uri/ =404;
            add_header X-Served-By $hostname;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Restart Nginx service if configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
