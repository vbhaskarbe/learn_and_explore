#!/usr/bin/ruby 

5.times { print "Welcome, to the world of Ruby!\n" }
['toast','cheese','wine','pizza'].each { |food| print food.capitalize,"\n" }
(1..10).each { |it| print it," " }
print "\n"
(1..10).each { |it| print it*it," " }
print "\n"
begin
	raise "This is a message"
rescue Exception => e
	print "Exception Handler: ", e,"\n"
end

