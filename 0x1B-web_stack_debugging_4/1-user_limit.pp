# Change the hard limit for the 'nofile' resource in the '/etc/security/limits.conf' file
exec { 'change hard limit':
  command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf',
  provider => shell,
}
