
class Arrays < Array
        attr_accessor :myarray

        def initialize(narray)
                p narray
                @myarray = narray
        end
end

ar_obj = Arrays.new([ 0, 'Bhaskar', 'Cisco', 4.33, 'Cisco India'])
puts ar_obj.myarray.first
puts ar_obj.myarray.last
puts ar_obj.myarray[1]
p ar_obj.myarray
puts ar_obj.myarray.pop
p ar_obj.myarray
ar_obj.myarray.push('Cisco India Pvt. Ltd.')
p ar_obj.myarray
ar_obj.myarray << 'Bangalore'
p ar_obj.myarray
myarray1 = [1, 2, 3, 4]
p myarray1
p myarray1.map { |num| num**2 }
p myarray1
p myarray1.collect { |num| num**2 }
p myarray1



