# connect to a server without typing a password using puppet
file_line { 'ssh_config':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => "PasswordAuthentication no",
    match  => 'PasswordAuthentication yes',
    multiple => 'true'
}
ssh_connect { 'ssh_config1':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => "IdentityFile ~/.ssh/school",
    match  => 'IdentityFile ~/.ssh/school',
    multiple => 'true'
}
