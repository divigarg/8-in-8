#this accepts the argument provided
filename= ARGV.first
prompt= ">"
# this opens the file handle with the name txt
txt=File.open(filename)
puts "Here's your file: #{filename}"
#this is a method for the class file which reads all the material in it
puts txt.read()
txt.close()
puts "I'll also ask you to type it again:"
print prompt
#Takes user input
file_again=STDIN.gets.chomp()
#again open the file handle
txt_again=File.open(file_again)
#repeat same
puts txt_again.read()
txt_again.close()
