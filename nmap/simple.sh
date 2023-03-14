#!/bin/env bash

# simple nmap scan
	# -p0- 	-- scan every possible TCP port
	# -v 		-- verbose
	# -A 		-- Aggressive; OS, service, version... decection
	# -T4 	-- aggressive timing policy; increased speed

nmap -p0- -v -A -T4 scanme.nmap.org
