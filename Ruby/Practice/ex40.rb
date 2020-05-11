cities = {'CA' => 'San Francisco',
    'MI' => 'Detroit',
    'FL' => 'Jacksonville'}
    
cities['NY'] ='New York'
cities['OR']='Portland'

def find_city(map,state)
    if map.include? state
        return map[state]
    else
        return "Not found."
    end
end
#the below step creates a key with name :find and the value is the function (method) :find_city
cities[:find] = method(:find_city)

while true
    print "State? (ENTER to quit) "
    state = gets.chomp
    
    break if state.empty?
    
    #cities[:find] restore the method object and call calls the function with params    
    puts cities[:find].call(cities,state)
end 
