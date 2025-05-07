# name = "md EjAZ anSaRi"

#1 len() function
# print(len(name))

#2 lower() method
# print(name.lower())

#3 upper() method
# print(name.upper())

#4 title() method
# print(name.title())

#5 count() method  ///// this is case sensitive
# print(name.count("a"))

#! /////  strip method
# name = "    Ejaz    Ansari  "
# dots = "........"

# print(name)
# print(name.lstrip() + dots) #### only remove left space but not in between spaces
# print(name.rstrip() + dots) #### only remove right space but not in between spaces
# print(name.strip() + dots) #### remove both side spaces but not in between spaces
# print(name.replace(" ", "") + dots) # it replace all the space with nospace


#!  //// Replace and find method 
# sentence = "she is beautiful and she is good dancer also"

# print(sentence.replace(" ", "_"))
# print(sentence.replace("is", "was"))
# print(sentence.replace("is", "was", 1)) # how many "is" want to replace 

# print(sentence.find("is")) # it finds position of "i" in "is"
# print(sentence.find("is", 5))
# is_pos = sentence.find("is")
# print(sentence.find("is", is_pos + 1))


#! center method -> it is being used to write "*" or some other character in left and right side
# name = "Ejaz"
# print(name.center(6, "*"))
# print(name.center(5, "*")) //// it'll give only one star at last of the string

# name = input("Enter your name: ")
# print(name.center((len(name) + 8), "^"))


#! immutable strings -> means it can't be changed or replaced rather than it would creates a new string and make changes in new string

string = "string"
# string[1] = 'T' ////  TypeError: 'str' object does not support item assignment
new_string = string.replace("t", "T")

print(string)
print(new_string)