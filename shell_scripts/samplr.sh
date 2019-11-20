#!/bin/bash
host=stadu56.us.oracle.com
echo ${host%%\.*}
host=stadu56
echo ${host%%\.*}
host=stadu56.us
echo ${host%%\.*}
