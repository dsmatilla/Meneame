#!/usr/bin/python

import sys
import datetime
import argparse
from watchdata import WatchData

def main():
	global configuration

	data = WatchData()
	data.connect(configuration.group)
	data.get_instances_info()

	""" Check if we must change the desired instances """
	if configuration.instances > 1:
		desired = configuration.instances
		if desired > 0 and abs(data.instances - desired) < 3:
			data.set_desired(desired)
		else:
			print "You can specify up to +-2 instances more of currently running (%d)" % (data.instances,)

		exit(0)

	data.get_CPU_loads()

	print "Group values: instances: %d min: %d max: %d desired: %d Launch config: %s" % (data.instances, data.group.min_size, data.group.max_size, data.group.desired_capacity, data.group.launch_config_name)

	for instance in data.instances_info:
		print "%s %5.2f%%	%-15s %s" % (instance.id, data.loads[instance.id], instance.private_ip_address, instance.dns_name)

	print "Average load: %5.2f%%" % (data.avg_load,)

	if data.instances > 1:
		print "Average load with %d instances: %5.2f%%" % (data.instances-1, data.total_load/(data.instances-1))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--group", "-g", default="web", help="AutoScaler group")
	parser.add_argument("--instances", "-i", type=int, help="Set the number of desired instances")
	configuration = parser.parse_args()
	main()

