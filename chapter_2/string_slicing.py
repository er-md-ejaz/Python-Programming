name = "mdejazansari"

# syntax:- name[start argument : stop argument + 1]

# print(name[2:5])
# print(name[:])
# print(name[4:])
# print(name[:6])
# print("ejazansari"[2:5])


#! step_argument_slicing 
print(name[2:5:2])
print("ansari"[1:3:-1]) # it will not be give any outcomes because step argument is negative and slice is in increasing order
# if (step argument is positive) then (slice argument should be in increasing(left to right) order) //// vice versa is also true
print("ansari"[-1::-1]) # this is trick to reverse a string
print("ansari"[-1::-2])