# kill a process you must use pkill and exec

exec { 'killmenow'
  command => 'pkill -f killmenow',
  path => '/usr/bin/:/user/bin/'
}