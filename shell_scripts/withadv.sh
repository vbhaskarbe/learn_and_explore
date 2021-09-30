#!/bin/bash
read -p "Enter Ur favorite vegetable? " -t 5 resp && echo "Ur response is $resp" || echo -e "\nTIMEOUT" && echo "Done"
