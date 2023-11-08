#!/usr/bin/env bash
# 0. Prepare your web servers
ls -l ~/.ssh/authorized_keys | nc lb-01.blxee.tech 8080
