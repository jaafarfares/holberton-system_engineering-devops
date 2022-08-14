# connect to a server without typing a password using puppet
file_line { 'ssh_config':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => "PasswordAuthentication no",
    match  => 'PasswordAuthentication yes'
}
ssh_connect { 'ssh_config':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => "IdentityFile ~/.ssh/school",
    match  => 'IdentityFile ~/.ssh/school'
}
