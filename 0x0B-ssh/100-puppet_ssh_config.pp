# connect to a server without typing a password using puppet
file_line { 'ssh_config':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'PasswordAuthentication no',
    multiple => 'true'
}
ssh_connect { 'ssh_config1':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'IdentityFile ~/.ssh/school',
    multiple => 'true'
}
