#Using Puppet to install flask from pip3.

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
}

file { '/usr/local/bin/flask':
  ensure => link,
  target => '/usr/local/bin/flask2',
}
