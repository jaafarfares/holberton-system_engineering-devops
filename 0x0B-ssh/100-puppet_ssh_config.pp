# connect to a server without typing a password using puppet
ssh_connect { 'ssh_config':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'PasswordAuthentication no',
    multiple => 'true'
}
ssh_connect { 'ssh_config_2':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'IdentityFile ~/.ssh/school',
    multiple => 'true'
}
