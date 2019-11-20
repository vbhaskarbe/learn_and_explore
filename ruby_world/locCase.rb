#!/usr/bin/ruby 

print "THIS IS ACTUALLY IN CAPITAL LETTERS, IN CODE".downcase,"\n"

#Add a method to existing 'Numeric' class
class Numeric
	def feet
		self*3.2808399
	end
end
print "5 Meters is ",5.feet," feet\n"
print "12 Meters is ",12.feet," feet\n"

#Lambda	
def gen_times(factor)
	 return Proc.new {|n| n*factor }
end
times3 = gen_times(3)
times5 = gen_times(5)

print times3.call(12)               #=> 36
print "\n"
print times5.call(5)                #=> 25
print "\n"
print times3.call(times5.call(4))   #=> 60
print "\n"
[1, 2, 4, 6, 8].each {|c| puts c*2} #=> outputs each element multiplied by 2 in a new line. 
print "\n"
