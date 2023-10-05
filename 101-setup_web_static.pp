file { '/data/web_static/shared/':
  ensure  => directory,
  recurse => true,
}
file { '/data/web_static/releases/test/':
  ensure  => directory,
  recurse => true,
}
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  recurse => true,
  content => '<html>\n<body>\n<h1>Hello World!</h1>\n</body>\n</html>',
}
exec { 'ln -sf /data/web_static/releases/test/ /data/web_static/current':
  provider => shell,
}
exec { 'chown -R ubuntu:ubuntu /data/':
  provider => shell,
}
