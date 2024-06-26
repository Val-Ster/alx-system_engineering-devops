# This Puppet manifest configures Nginx to handle higher loads
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections 768;/worker_connections 1024;/" /etc/nginx/nginx.conf && service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
