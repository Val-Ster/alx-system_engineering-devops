# This Puppet manifest changes the OS configuration to increase the open file limit for the holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/echo "* soft nofile 4096\n* hard nofile 4096" >> /etc/security/limits.conf && ' +
  '/bin/echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  path    => ['/bin', '/usr/bin'],
}
