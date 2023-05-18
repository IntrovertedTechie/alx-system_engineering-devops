# Increase the open file limit for nginx to prevent failed requests

exec { 'increase nginx limit':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
