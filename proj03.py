#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:42:34 2019

"""

#MSU tuition calculator 

print("2019 MSU Undergraduate Tuition Calculator.")
print()
repeat = 'yes' #to prompt while loop

while repeat == 'yes':
    tution = 24 #ASMSU Tax + FM Radio Tax
#1 figure out where the student is from
    resident = input('Resident (yes/no): ').lower()
    if resident != 'yes' : #if not in-state, ask if international
        resident_international = input('International (yes/no): ').lower()
        
#2 Figure out what level
    level = input('Level—freshman, sophomore, junior, senior: ').lower()

    while level != 'freshman' and level != 'sophomore' \
    and level != 'junior' and level != 'senior':
    #if user types invalid input, loop until they put the right one in
        print('Invalid input. Try again.')
        level = input('Level—freshman, sophomore, junior, senior: ').lower()
        
    if level == 'freshman' or level == 'sophomore':
    #freshman/sophmore college
        CMSE = 'no' #freshman and sophmores can't be in CMSE
        
        #ask if they're in engineering
        engineering = input('Are you admitted to the College of Engineering (yes/no): ').lower()
        if engineering == 'yes':
            college = 'engineering'
            
        else: 
            #if not in engineering, can be in James Madison
            james_madison = input('Are you in the James Madison College (yes/no): ')
            if james_madison == 'yes':
                college = 'james madison'
            else:
                college = 'none' #no extra tution will be added

    if level == 'junior' or level == 'senior':
        #senior / junior college
        #ask what college they're in
        college = input('Enter college as business, engineering, health, sciences, or none: ').lower()
        
        #can be in CMSE
        CMSE = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ').lower()
        
        #if not apart of any of the colleges listed, could be in James Madison
        if college != 'business' and college != 'engineering' and \
        college != 'health' and college != 'science':
            james_madison = input('Are you in the James Madison College (yes/no): ')
            if james_madison == 'yes':
                college = 'james madison' 

#3 figure out number of credits 
    credits_str = input ('Credits: ')
    credits = 0 #to prompt while loop

    while credits == 0:
        if credits_str.isdigit() and credits_str != '0':
            #Put a valid number for credits
            credits = int(credits_str)
        else:
            #put a letters or float
            print('Invalid input. Try again.')
            credits_str = input ('Credits: ')
    
#resident tution
    if resident == 'yes':
    
        if level == 'freshman': #in state freshman (same for kids in engineering) 
            if credits <= 11:
                tution += 482 * credits
            elif 12 <= credits <= 18:
                tution += 7230
            else:
                tution += 7230 + ((credits-18) * 482)
            
        elif level == 'sophomore' : #in state sophomores (same for kids in engineering)
            if credits <= 11:
                tution += 494 * credits
            elif 12 <= credits <= 18:
                tution += 7410
            else:
                tution += 7410 + ((credits-18) * 494)
            
        elif college == 'engineering' or college == 'business' : 
            #in state junior/senior engineering/business
            if credits <= 11:
                tution += 573 * credits
            elif 12 <= credits <= 18:
                tution += 8595
            else:
                tution += 8595 + ((credits-18) * 573)
    
        else: #in state junior/senior tution
            if credits <= 11:
                tution += 555 * credits
            elif 12 <= credits <= 18:
                tution += 8325
            else:
                tution += 8325 + ((credits-18) * 555)

            
    else:
        if resident_international == 'yes':
        #how much of the international fee to put on tution
            if credits <= 4:
                tution += 375
            else:
                tution += 750
                
        if level == 'freshman' or level == 'sophomore':
        #out of state freshman & sophmore (same for kids in engineering) 
            if credits <= 11:
                tution += 1325.5 * credits
            elif 12 <= credits <= 18:
                tution += 19883
            else:
                tution += 19883 + ((credits-18) * 1325.5)
            
        elif college == 'engineering' or college == 'business' : 
            #out of state junior/senior engineering/business
            if credits <= 11:
                tution += 1385.75 * credits
            elif 12 <= credits <= 18:
                tution += 20786
            else:
                tution += 20786 + ((credits-18) * 1385.75)
    
        else: #out of state junior/senior tution
            if credits <= 11:
                tution += 1366.75 * credits
            elif 12 <= credits <= 18:
                tution += 20501
            else:
                tution += 20501 + ((credits-18) * 1366.75)
            
#Extra college costs:
    
#state news tax, only applies to students who are taking more that 6 credits
    if credits >= 6:
        tution += 5
        
#Business school fee
    if college == 'business':
        if credits <= 4:
            tution += 113
        else:
            tution +=226
            
#engineering school fee
    if college == 'engineering':
        if credits <= 4:
            tution += 402
        else:
            tution += 670

#health and science schools fee (same fees)
    if college == 'health' or college == 'sciences':
        if credits <= 4:
            tution += 50
        else:
            tution += 100
            
#James Madison College Student Senate Tax
    if college == 'james madison':
        tution += 7.50
        
#CMSE fee
    if CMSE == 'yes':
        if credits <= 4:
            tution += 402
        else:
            tution += 670
        
    print("Tuition is ${:,.2f}.".format(tution)) #print tuition
    #to prompt while loop again
    repeat = input("Do you want to do another calculation (yes/no): ").lower() 
    