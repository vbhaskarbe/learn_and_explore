
printf "\e[1;34m%15s\e[m : \e[1m%s\e[m\n" 'Job ID' "8958"
printf "\e[1;34m%15s\e[m : %s\n" 'Start Date' "Thu Oct 12 05:07:04 IST 2017"
printf "\e[1;34m%15s\e[m : %s\n" 'Dev Branch' "hotfix-4.8.2"
printf "\e[1;34m%15s\e[m : %s\n" 'Cloud' "vmware"
printf "\e[1;34m%15s\e[m : %s\n" 'Optimus Branch' "hotfix-4.8.2"
#if status matched FAIL
printf "\e[1;34m%15s\e[m : \e[1;31m%s\e[m\n" 'Status' "Setup Failed"
#else
printf "\e[1;34m%15s\e[m : \e[1m%s\e[m\n" 'Status' "Setup In Progress"
#fi
printf "\e[1;34m%15s\e[m : %s\n" 'Suite' "sanity"
printf "\e[1;34m%15s\e[m : %s\n" 'Mode' "api"
printf "\e[1;34m%15s\e[m : %s\n" 'Duration' "00:26:12"
