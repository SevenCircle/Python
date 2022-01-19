for i in range(1,101):
    ## IDEA 1    
    # output = ""
    # if(i%3==0):
    #     output="Fizz"
    # if(i%5 == 0):
    #     output+="Buzz"
    # if(len(output)==0):
    #     print(i)
    # else: print(output)
    
    ## IDEA 2
    # if(i%5 == 0 and i%3 == 0):
    #     print('FizzBuzz');
    # elif (i%5 == 0):
    #     print('Buzz');
    # elif (i%3 == 0):
    #     print('Fizz');
    # else: print(i)

    #IDEA 3
    print(str(i) if i%5 != 0 and i%3 != 0 else "" "Fizz" if(i%3==0) else "" + "Buzz" if(i%5==0) else "")
    