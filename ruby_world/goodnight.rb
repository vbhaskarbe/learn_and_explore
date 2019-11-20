#!/usr/bin/ruby

def sayGoodNight( name)
   result = "Good night, " + name
   return result
end

def sayGoodNight1( name)
    result = "Good night, #{name}\n";
    return result
end

puts sayGoodNight("Bhaskar!")
puts sayGoodNight1("Bhaskar!")


3.times  { print "X" }
print "\n"
1.upto(5) { |i| print i, " " }
print "\n"
99.downto(95) { |i| print i, " " }
print "\n"
50.step(80, 5) { |i| print i, " " } 
print "\n"

digits = 0..9
puts digits.include?(5)
puts digits.min
puts digits.max
puts digits.reject { |i| i < 5 }
print "\n"
print [ 5, 3, 4, 1, 6, 2].sort
print [ 5, 3, 4, 1, 6, 2].sort.reverse

