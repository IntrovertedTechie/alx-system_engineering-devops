# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Add X-Served-By header
file_line { 'add_x_served_by_header':
  path  => '/etc/nginx/sites-available/default',
  line  => "add_header X-Served-By ${facts['hostname']};",
  match => "^\\s*server\\s*{",
  after => "^\\s*listen\\s*\\[\\:\\:\\]\\:80\\s*default_server\\s*\\;\\s*$",
  notify => Service['nginx'],
}

# Enable Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [
    Package['nginx'],
    File['/etc/nginx/sites-enabled/default'],
  ],
}

