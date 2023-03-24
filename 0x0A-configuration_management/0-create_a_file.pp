# create a file with permissions using puppet

file{'create file':
path    => '/tmp/school',
mode    => '0744',
owner   => www-data,
group   => www-data,
content => 'I love Puppet'
}
