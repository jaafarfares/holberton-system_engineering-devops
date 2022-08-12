# kill a process with puppet and you must use pkill and exec

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}