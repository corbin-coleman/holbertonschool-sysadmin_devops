# Create a file in tmp called holberton
file { "/tmp/":
     path => "/tmp/holberton",
     content => "I love Puppet",
     owner => www-data,
     group => www-data,
     mode => 0744,
}