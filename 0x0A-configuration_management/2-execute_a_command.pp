# Exec resource to kill the process
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep -x killmenow',
}

