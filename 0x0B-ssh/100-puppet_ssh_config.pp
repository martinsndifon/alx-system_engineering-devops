# Use puppet to make changes to our server configuration file

file_line {'no-password':
path    => '/etc/ssh/ssh_config',
line    => '    PasswordAuthentication no',
replace => true
}


file_line {'private-key':
path    => '/etc/ssh/ssh_config',
line    => '    IdentityFile ~/.ssh/school',
replace => true
}
