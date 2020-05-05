name= 'Divyansh Garg'
age=18
height= 72 #inches
weight= 120
eyes= 'Black'
teeth = 'White'
hair= 'Black'

puts "Let's talk about %s." % name
puts "He's %d inches tall." % height
puts "He's %d pounds heavy." % weight
puts "Actually that's not too heavy."
puts "He's got %s eyes and %s hair." %[eyes, hair]
puts "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
puts "If I add %d, %d, and %d I get %d." % [age,height,weight, age+height+weight]
