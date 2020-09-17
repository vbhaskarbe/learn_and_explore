
# importing module 
import platform 
  
# dictionary 
info = {} 
  
# platform details 
platform_details = platform.platform() 
  
# adding it to dictionary 
info["platform details"] = platform_details 
  
# system name 
system_name = platform.system() 
  
# adding it to dictionary 
info["system name"] = system_name 
  
# processor name 
processor_name = platform.processor() 
  
# adding it to dictionary 
info["processor name"] = processor_name 
  
# architectural detail 
architecture_details = platform.architecture() 
  
# adding it to dictionary 
info["architectural detail"] = architecture_details 
  
# printing the details 
for i, j in info.items(): 
    print(i, " - ", j) 


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

my_system = platform.uname()

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

