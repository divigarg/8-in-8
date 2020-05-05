filename=ARGV.first
script =$0

puts "We're going to erase #{filename}."
puts "If you don't want that, hit CTRL-C (^C)."
puts "If you do want that, hit RETURN."

print "? "
STDIN.gets

puts "Opening the file..."
target = File.open(filename, 'w')

puts "Truncation the file.  Goodbye!"
target.truncate(target.size)

puts "Now I'm going to ask you for three lines."

print "line 1: "; line1= STDIN.gets.chomp()
print "line 2: "; line2= STDIN.gets.chomp()
print "line 3: "; line3= STDIN.gets.chomp()

puts "I'm going to write these to the file."
text=<<EDIT
#{line1}
#{line2}
#{line3}
EDIT
target.write(text)
puts "And finally, we close it."
target.close()
