#!/usr/bin/python3

import time
import bluetooth


if __name__ == '__main__':
	my_devs = ['78:88:6D:3A:EA:E3'] # iPhone

	print("Performing device inquiry...")
	nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
	print("Found {} devices".format(len(nearby_devices)))
	for addr, name in nearby_devices:
		try:
			print("ADDR = %s DEV = %s" % (addr, name))
		except UnicodeEncodeError:
			print("ADDR = %s DEV = %s" % (addr, name.encode("utf-8", "replace")))

	print("Checking connection stability...")
	while True:
		print("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
		result = bluetooth.lookup_name(my_devs[0], timeout=5)
		if result:
			print("Connected.")
		else:
			print("Connection lost!")

		time.sleep(10)
	
