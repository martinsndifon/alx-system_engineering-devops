# kills a program

exec {'kill process':
command => '/usr/bin/pkill -f killmenow'
}
