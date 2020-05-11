def add(a,b)
    puts "ADDING #{a} + #{b}"
    a+b
end

def subtract(a,b)
    puts "SUBTRACTING #{a} - #{b}"
    a-b
end

def multiply(a,b)
    puts "MULTIPLYING #{a} * #{b}"
    a*b
end

def divide(a,b)
    puts "DIVIDING #{a} / #{b}"
    a/b
end

puts "Let's do some math with just function!"

age= add(10,8)
height = subtract(68,-10)
weight= multiply(12,10)
iq = divide(100,1)

puts "Age: #{age}, Height: #{height}, Weight: #{height}, IQ: #{iq}"

what = add(age, subtract(height, multiply(weight, divide(iq,1))))

puts "That becomes: #{what} Can you do it by hand?"
