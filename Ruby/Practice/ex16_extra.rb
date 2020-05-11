filename= ARGV.first
txt=File.open(filename)
puts txt.read()
txt.close()
