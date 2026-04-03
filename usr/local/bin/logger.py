#!/usr/bin/python3

f = open('/var/log/postfix/current', 'r')
while True:
    with open('/proc/1/fd/1', 'w') as fdfile:
        fdfile.write(f.readline())
