# 5. Puppet for setup
file { 'shared':
  path    =>  '/data/web_static/shared/',
  ensure  => 'directory',
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
file { 'test':
  path    =>  '/data/web_static/releases/test/',
  ensure  => 'directory',
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['shared'],
}
file { 'index':
  path    =>  '/data/web_static/releases/test/index.html',
  ensure  => 'file',
  recurse => true,
  content => '<html>\n<body>\n<h1>Hello World!</h1>\n</body>\n</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['test'],
}
exec { 'ln':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  require  => File['index'],
}
exec { 'chown -R ubuntu:ubuntu /data/':
  provider => shell,
  require  => Exec['ln'],
}
