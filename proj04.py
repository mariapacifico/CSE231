#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:44:53 2019

"""

#Create functions to preform specific math functions
#Create function to ask user which function to be used
#Loop until user enters x
#Print result(s)

import math
EPSILON = 1e-7

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the value of the sum of the first N natural numbers. 
             B. Display the approximate value of e.
             C. Display the approximate value of the hyperbolic sine of X.
             D. Display the approximate value of the hyperbolic cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)

# sum_natural
def sum_natural (n):
    '''This function takes the sum of a natural number '''
    
    if n.isdigit(): #to see if number is actually natural
        n = int(n) #create int
        if n == 0:
            return None
        sum = 0
        while n != 0: #loop to keep adding itself until reaches 0
            sum += n
            n -= 1
        return sum
    else:
        return None
    
# approximate_euler()
def approximate_euler():
    ''' This function calculates the approximate Euler number '''
    
    euler = 0
    n = 0 #what n is intially
    term = 1 #what term is at n = 0
    bottom = 1 
    while abs(term) > EPSILON: #keep adding until absolute value less than Epsilon
        euler += term 
        n += 1 
        b = n #create new variable to avoid messing with n value
        while (b-1) != 0: #to find the denominator
            bottom *= b
            b -= 1
        term = 1/bottom
        bottom = 1 #reset for next calculation 
    return round(euler, 10) #round to ten places
        
# approximate_sinh(x)
def approximate_sinh(x):
    ''' This function calculates the approximate sinh of any float '''
    
    try: #make sure input can convert to a float
        float(x)
    except ValueError:
        return None
    x = float(x) #convert string to float
    n = 0 #what n is intially
    sinh = 0
    term = x #what the result is when n=0
    bottom = 1
    while abs(term) > EPSILON: #keep adding until absolute value less than Epsilon
        sinh += term 
        n += 1
        b = 2 * n + 1 #what is inside the factorial parentheses
        while (b-1) > 0:
            bottom *= b #find the denominator
            b -= 1
        term = (x ** (2 * n + 1)) / bottom #equation
        bottom = 1
    return round(sinh, 10) #round to ten places
        
# approximate_cosh(x)
def approximate_cosh(x):
    ''' This function calculates the approximate cosh of any float '''
    
    try: #make sure input can convert to float
        float(x)
    except ValueError:
        return None
    x = float(x) #convert string to float
    n = 0 #what n is initally
    cosh = 0
    term = 1 #what is the result at n = 0
    bottom = 1
    while abs(term) > EPSILON: #keep adding until absolute value less than Epsilon
        cosh += term 
        n += 1
        b = 2 * n #what is inside the factorial parentheses
        while (b-1) > 0:
            bottom *= b #find denominator
            b -= 1
        term = (x ** (2*n)) / bottom #equation
        bottom = 1 #reset denominator
    return round(cosh, 10) #round to 10 places
        
def main():
    ''' Where all functions will be printed'''

    display_options() #print options
        
    option = input("Enter option: ").lower() #to prompt while loop
        
    while option != 'x':
        
        if option == 'a': #sum_natural
            n_str = input("Enter N: ")
            if n_str == '0': #error when n = 0 since it's not a natural number
               print("Error: N was not a valid natural number. [{:s}]".format(n_str))
               option = input("Enter option: ").lower() #prompt loop
               continue 
            elif n_str.isdigit():
                #prompt sum_natural if there was given a natural number
                print("The sum: {:>1d}".format(sum_natural(n_str))) 
                option = input("Enter option: ").lower() #prompt loop
                continue
            else:
                #when natural number isn't given
                print("Error: N was not a valid natural number. [{:s}]".format(n_str))
                option = input("Enter option: ") #prompt loop
                continue
            
        elif option == 'b': #approximate_euler
            print("Approximation: {:.10f}".format(approximate_euler()))
            print("Math module: {:>3.10f}".format(math.e)) #actual number
            print("difference: {:>4.10f}".format(abs(approximate_euler()-math.e)))
            option = input("Enter option: ").lower() #prompt loop
            continue
        
        elif option == 'c': #approximate_sinh(x)
            x = input("Enter X: ")
            try: #to see if input could be a float
                float(x)
                y = approximate_sinh(x)
                z = math.sinh(float(x)) #actual number
                difference = abs(y-z)
                print("Approximation: {:.10f}".format(y)) 
                print("Math module: {:>3.10f}".format(z))
                print("difference: {:>4.10f}".format(difference))
            except ValueError: #if not given, print error
                print("Error: X was not a valid float. [{:s}]".format(x))
            option = input("Enter option: ").lower() #prompt loop
            continue
        
        elif option == 'd': #approximate_cosh(x)
            x = input("Enter X: ")
            try: #see if input could be a float
                float(x)
                y = approximate_cosh(x)
                z = math.cosh(float(x)) #actual number
                difference = abs(y-z)
                print("Approximation: {:.10f}".format(y)) 
                print("Math module: {:>3.10f}".format(z))
                print("difference: {:>4.10f}".format(difference))
            except ValueError: #if cannot be a float, print error
                print("Error: X was not a valid float. [{:s}]".format(x))
            option = input("Enter option: ").lower() #prompt loop
            continue
        
        elif option == 'm': #display options
            display_options()
            option = input("Enter option: ").lower() #prompt loop
            continue
        
        elif option != 'a' and option != 'b' and option != 'c' and option != 'd' \
        and option != 'm' and option != 'x':
            #if user inputs something that is not an optin, print error and 
            #display items again
            print("Error:  unrecognized option [{:s}]".format(option.upper()))
            display_options()
            option = input("Enter option: ").lower() #prompt loop
            continue
        
    else:
        return print("Hope to see you again.") #when user option = 'x', ends loop
        
            
if __name__ == "__main__": #prints main
    main()
 
