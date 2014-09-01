#!/bin/bash
clear
EXCLUDED="asciinet,cybloom,asyncrpc,cysparql,cyqplanner,avalanche_jvm,cytokyotygr,msgpackutil"
extract_requirements setup.py --excludes=${EXCLUDED} > requirements.txt