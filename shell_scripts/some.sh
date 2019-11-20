line=OUI_MAIN_HPUX.TRU64_102010
if[ `echo $line | grep HPUX.TRU64` -o `echo $line |grep LINUX.ZSERIES64` ];
then
 site="PLE"
else
 site="ADC_LINUX"
fi
