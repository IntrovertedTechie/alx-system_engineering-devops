# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  content => "
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;

  index index.html;

  server_name _;

  location / {
    # Return Hello World! string
    add_header Content-Type text/plain;
    return 200 'Hello World!\n';
  }

  location /redirect_me {
    # Perform 301 redirect
    return 301 https://talenthive.tech/;
  }
}
",
}

# Enable Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service
service { 'nginx':
  ensure => 'running',
  enable => 'true',
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}

