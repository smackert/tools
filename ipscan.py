#!/usr/bin/env python
# Slow single thread scan of the /24
# address is hardcoded

import os

addr = []
for i in range(0,256):
	ip = "10.11.1.%s" % i
	result = os.system("ping -c 1 %s" % ip)
	if (result == 0):
		addr.append(ip)

print("Live hosts:")
for i in addr:
	print i + "\r"
