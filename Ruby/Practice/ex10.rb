tabby_cat = "\tI'm tabbed in."
persian_cat= "I'm split\non a line."
backslash_cat= "I'm \\ a \\ cat."

fat_cat= <<USE_ANY_NAME
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
USE_ANY_NAME

alert="this will bell\a"

backspacing="appear one but two are  \bthere."
puts tabby_cat
puts persian_cat
puts backslash_cat
puts fat_cat
puts alert
puts backspacing
