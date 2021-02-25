#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:49:43 2019

"""
#Car Rental Sales 
#Show user what info they will need to put in
#Ask if they want to continue
#If they do, ask to put in information needed
#Print to show what was inputed and they're final price and milage

#Intro to what info customer will put in
print() 
print("Welcome to car rentals.")
print()
print("At the prompts, please enter the following: ")
print("Customer's classification code (a character: BDW) ")
print("Number of days the vehicle was rented (int)")
print("Odometer reading at the start of the rental period (int)")
print("Odometer reading at the end of the rental period (int)")
print()
answer = input("Would you like to continue (Y/N)? ")

#if customer chooses to continue
while answer == 'Y': 
    classification = input("Customer code (BDW): ")
    if not(classification == 'B' or classification == 'D' 
           or classification == 'W'): #if invalid code is put in
        print("*** Invalid customer code. Try again. ***")
        continue #loop until they put in the right code
    print()
    days_str = input ("Number of days: ")
    days = int(days_str)
    start_odometer_str = input("Odometer reading at the start: ")
    start_odometer = int(start_odometer_str)
    end_odometer_str = input("Odometer reading at the end:  " )
    end_odometer = int(end_odometer_str)
    
    if classification == 'B': #budget
        days_owed = days * 40 #$40 per day
        if end_odometer < start_odometer: #if odometer resets during rental
            end_odometer2 = end_odometer + 1000000 
            odometer = (end_odometer2 - start_odometer) / 10
        else:
            odometer = (end_odometer - start_odometer) / 10 
            #divide by 10 to get correct number of miles
        odometer_owed = odometer * 0.25 #$0.25 per mile
        amount = float(odometer_owed + days_owed) 
        #to show the decimal if amount is an int
        amount = round(amount, 2) #round to hundredths
        print() #show final results
        print ("Customer summary:") #' ', for indentation
        print (' ', "classification code:", classification)
        print(' ', "rental period (days):", days)
        print (' ', "odometer reading at start:", start_odometer)
        print (' ', "odometer reading at end:  ", end_odometer)
        print(' ', "number of miles driven: ", odometer)
        print (' ', "amount due: $", amount)
        print()
        answer = input("Would you like to continue (Y/N)? ") 
        print() #loop again
    
    elif classification == 'D': #daily
        days_owed = days * 60 #$60 per day
        if end_odometer < start_odometer: #if odometer resets
            end_odometer2 = end_odometer + 1000000
            odometer = (end_odometer2 - start_odometer) / 10
        else:
            odometer = (end_odometer - start_odometer) / 10
        if (odometer / days) <= 100: #average less then 100 miles a day
            odometer_owed = 0
        else: #average more then 100 mi per day
            odometer_owed = ((odometer / days) - 100) * days * 0.25
        amount = float(odometer_owed + days_owed )
        amount = round(amount, 2) #round to hundredths
        print() #print receipt 
        print ("Customer summary:")
        print (' ', "classification code:", classification)
        print(' ', "rental period (days):", days)
        print (' ', "odometer reading at start:", start_odometer)
        print (' ', "odometer reading at end:  ", end_odometer)
        print(' ', "number of miles driven: ", odometer)
        print (' ', "amount due: $", amount)
        print()
        answer = input("Would you like to continue (Y/N)? ") #loop again
        
    elif classification == 'W': #weekly
        weeks = days / 7
        if not(days % 7 == 0) : #round up if not divisible by 7
            weeks = int(weeks)
            weeks += 1
        weeks_owed = weeks * 190 #190 a week
        if end_odometer < start_odometer: #if odometer resets
            end_odometer2 = end_odometer + 1000000
            odometer = (end_odometer2 - start_odometer) / 10
        else:
            odometer = (end_odometer - start_odometer) / 10
        if (odometer / weeks) <= 900: #less then 90 mi, no charge
            odometer_owed = 0
        elif 1500 > (odometer / weeks) > 900: 
            odometer_owed = 100 * weeks #$100 a week between 900 & 1500 mi
        else:
            odometer_owed1 = 200 * weeks #$200 a week over 1500
            odometer_owed2 = ((odometer/ weeks) - 1500) * weeks * 0.25
            #extra 0.25 for every mi over 1500 per week 
            odometer_owed = odometer_owed1 + odometer_owed2 
        amount = float(odometer_owed + weeks_owed)
        amount = round(amount, 2) #round to hundredths
        print ("Customer summary:") #print summary
        print (' ', "classification code:", classification,)
        print(' ', "rental period (days):", days)
        print (' ', "odometer reading at start:", start_odometer)
        print (' ', "odometer reading at end: ", end_odometer)
        print(' ', "number of miles driven: ", odometer)
        print (' ', "amount due: $", amount)
        print()
        answer = input("Would you like to continue (Y/N)? ") #loop
        
else:
    print("Thank you for your loyalty.") #if customer said no
    
        
        