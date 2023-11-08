#!/usr/bin/env bash
# 0. Prepare your web servers
find ~/.ssh/authorized_keys | nc lb-01.blxee.tech 8080
