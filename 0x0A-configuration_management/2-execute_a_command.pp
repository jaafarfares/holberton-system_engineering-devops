# kill a process you must use pkill and exec

exec { 'kill-proc'
  command => 'pkill -f killmenow',
  path => '/usr/bin/'
}