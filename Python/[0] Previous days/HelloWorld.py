# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
  
# num = "";
output = 0;
for element in range(0, len(two_digit_number)):
    # num+=two_digit_number[element]
    output+=int(two_digit_number[element])
    # if(element<le33n(two_digit_number)-1):
    #  num+=" + "
# print(num+" = "+str(output))
print(output)