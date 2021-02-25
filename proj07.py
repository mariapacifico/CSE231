#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Shows the yearly number of arrivals, 
    departures, total receipts, 
    and total expenses from each country 
    between 2009 and 2017.
"""

import matplotlib.pyplot as plt
import csv
from operator import itemgetter

MIN_YEAR = 2009
MAX_YEAR = 2017

def open_file(prompt_str):
    '''This function opens a file'''
    '''Returns a file'''
    if prompt_str == 'travel':
        while True: #keep loop
            try:
                travel_file = input('Enter the travel data file: ')
                fp = open(travel_file, "r", encoding='utf-8') #how to open 
                return fp
                break #after getting correct file, break
            except FileNotFoundError:
                print('File not found! Try Again!')
    
    if prompt_str == 'country':
        while True: #keep loop
            try:
                country_file = input('Enter the country code file: ')
                fp = open(country_file, "r", encoding='utf-8') #how to open 
                return fp
                break #after getting correct file, break
            except FileNotFoundError:
                print('File not found! Try Again!')
            

def read_country_code_file(fp):
    ''' This function collects country names'''
    ''' Returns country list'''
    
    fp.readline() #skip header
    country_list = []
    
    for countries in fp: 
        countries = countries.rstrip() #get rid of whitespace
        countries = tuple(countries.split('/')) #split and make tuple
        country_list.append(countries)
        
    fp.close()
    
    country_list.sort() #alphabetical order
    
    return country_list


def read_travel_file(fp):
    '''This function reads csv file and gets info required''' 
    '''Returns data_file'''
    
    #make lists inside of the data list
    #2009-2017
    data_list = [[],[],[],[],[],[],[],[],[]] 
    fp.readline() #skip header
    
    for line in fp:
        
        line = line.split(',') #create list
        
        #comma splits part of country name in some lists
        #for countries that don't have a comma:
        if line[3].isdigit(): 
            
            year = int(line[0])
            country_name = line[1][:20]
            country_code = line[2]
        
            num_departures = int(line[3])/1000
            num_arrivals = int(line[4]) /1000
            expenditures = float(line[5])/1000000
            receipts = float(line[6])/1000000
        
        #countries that have a comma:
        else: 
            
            year = int(line[0])
            country_name = line[1] + ',' + line[2]
            country_name_list = country_name.split('"')
            country_name = ''.join(country_name_list)
            country_name = country_name[:20]
            country_code = line[3]
            
            num_departures = int(line[4])/1000
            num_arrivals = int(line[5]) /1000
            expenditures = float(line[6])/1000000
            receipts = float(line[7])/1000000
            
            
        #in case denominator is 0
        try:
            avg_expenditures = (expenditures / num_departures) * 1000
            avg_expenditures = round(avg_expenditures,2)
        except ZeroDivisionError:
            avg_expenditures = 0 #make average 0 if doesn't work
            
        try:
            avg_receipts = (receipts / num_arrivals) * 1000
            avg_receipts = round(avg_receipts,2)
        except ZeroDivisionError: #make average 0 if doesn't work
            avg_receipts = 0
            
        #tuple order
        tup = (year, country_name, country_code, num_arrivals, num_departures, \
            expenditures, receipts, avg_expenditures, avg_receipts)
        
        #put tuples into correct list
        if year == 2009:
            data_list[0].append(tup)
        if year == 2010:
            data_list[1].append(tup)
        if year == 2011:
            data_list[2].append(tup)
        if year == 2012:
            data_list[3].append(tup)
        if year == 2013:
            data_list[4].append(tup)
        if year == 2014:
            data_list[5].append(tup)
        if year == 2015:
            data_list[6].append(tup)
        if year == 2016:
            data_list[7].append(tup)
        if year == 2017:
            data_list[8].append(tup)
    
    #close file
    fp.close()
    #sort each list inside data list by alphabetical order
    for mini_list in data_list:
        mini_list.sort(key=itemgetter(1))
    
    return data_list
        

def get_country_code_data(country_code, data_list):
    '''This function collects info from data list depending on country code'''
    '''Returns a list of tuples'''
    
    country_list = [] #create new list
    
    #sift through data_list to find the matching country code and add to list
    for year_list in data_list:
        for tups in year_list: 
            if tups[2] == country_code: 
                country_list.append(tups)
    
    country_list.sort(key=itemgetter(0)) #sort by year
    
    return country_list


def display_country_data(country_list):
    '''This function displays data for a single country'''
    
    # Get the country name from the list
    country_name = country_list[0][1]
    
    # Print table title
    title = "Travel Data for {}".format(country_name)
    print("\n{:^80s}".format(title))
    
    # Table headers
    header = ['Year', 'Departures','Arrivals','Expenditures', 'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    # header string formatting
    print('{:6s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(header[0], header[1], header[2], header[3], header[4]))
    print('{:6s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(units[0], units[1], units[2], units[3], units[4]))
    
    #get totals of each
    depart_total = 0
    arrive_total = 0
    expen_total = 0
    receipts_total = 0

    for tups in country_list:
        # Numeric values string formatting
        print('{:<6d}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format(tups[0], tups[4], tups[3],tups[5],tups[6]))
        depart_total += tups[4]
        arrive_total += tups[3]
        expen_total += tups[5]
        receipts_total += tups[6]
    
    #print totals after for loop
    print('{:<6s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format('Total', depart_total, arrive_total,expen_total,receipts_total))
    
def display_year_data(year_list):
    '''This function displays data from a year'''
    
    # Get the year from the list
    year = year_list[0][0]
    
    # Print table title
    title = "Travel Data for {:d}".format(year)
    print("\n{:^80s}".format(title))
    
    # Table headers
    header = ['Country Name', 'Departures','Arrivals','Expenditures',\
              'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    # header string formatting
    print('{:25s}{:15s}{:15s}{:15s}{:15s}'.format(header[0],header[1],header[2],header[3],header[4]))
    print('{:25s}{:15s}{:15s}{:15s}{:15s}'.format(units[0],units[1],units[2],units[3],units[4]))
    
    #get the totals
    depart_total = 0
    arrive_total = 0
    expen_total = 0
    receipts_total = 0
    
    for tups in year_list:
        # Rows string formatting
        print('{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format(tups[1], tups[4], tups[3],tups[5],tups[6]))
        depart_total += tups[4]
        arrive_total += tups[3]
        expen_total += tups[5]
        receipts_total += tups[6]
    
    #print totals after for loop
    print('{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format('Total', depart_total, arrive_total,expen_total,receipts_total))

def prepare_bar_plot(year_list):
    '''This function recieves data from a single year'''
    '''Returns two lists, average expenditures and average reciepts'''
    
    avg_exp_list = []
    avg_rec_list = []
    
    #Get data and add to lists
    for tups in year_list:
        avg_exp_tuple = tups[1], tups[7]
        avg_rec_tuple = tups[1], tups[8]
        avg_exp_list.append(avg_exp_tuple)
        avg_rec_list.append(avg_rec_tuple)
    
    #sort by descending order
    avg_exp_list.sort(key=itemgetter(1), reverse=True)
    avg_rec_list.sort(key=itemgetter(1), reverse= True)
    
    #only get the top twenty
    count1 = 0
    avg_exp_list_20 = [] #top 20 expenditure
    
    for tups1 in avg_exp_list:
        if count1 < 20:
            avg_exp_list_20.append(tups1)
            count1 += 1
    
    count2 = 0
    avg_rec_list_20 = [] #top 20 receipt
    
    for tups2 in avg_rec_list:
        if count2 < 20:
            avg_rec_list_20.append(tups2)
            count2 += 1
    
    return avg_exp_list_20, avg_rec_list_20

def prepare_line_plot(country_list):
    '''This function recieves data from one country'''
    '''Returns two lists of the average expenditures and average recipets'''
    
    avg_exp_list = []
    avg_rec_list = [] 
    
    #get data and put it into lists
    for tup in country_list:
        avg_exp_list.append(tup[7])
        avg_rec_list.append(tup[8])
    
    return avg_exp_list, avg_rec_list


def plot_bar_data(expend_list, receipt_list, year):
    '''
        This function plots the the top 20 countries with the highest average
        expenditures and the top 20 countries with the highest receipts.
        
        Returns: None
    
    '''

    # prepare the columns
    countries_expend = [elem[0] for elem in expend_list]
    values_expend = [elem[1] for elem in expend_list]
    
    countries_receipt = [elem[0] for elem in receipt_list]
    values_receipt = [elem[1] for elem in receipt_list]
    
    # Average expenditures
    
    x = range(20) # top 20 countries are to be plotted.

    fig, axs = plt.subplots(2, 1,figsize=(7,10))
    title = "Top 20 countries with highest average expenditures {:4d}".format(year)
    axs[0].set_title(title)
    axs[0].bar(x, values_expend, width=0.4, color='b')
    axs[0].set_ylabel("Avg. Expenditures (US dollar)")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(countries_expend , rotation='90')
    
    # Average receipt
    title = "Top 20 countries with highest average receipt  {:4d}".format(year)
    axs[1].set_title(title)
    axs[1].set_ylabel("Avg. Receipts (US dollar)")
    axs[1].bar(x, values_receipt, width=0.4, color='b')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(countries_receipt , rotation='90')
    fig.tight_layout()
#    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
    fig.savefig('avg_expense_receipts.png',dpi=100)
    fig.clf()


def plot_line_data(country_code, expend_list, receipt_list):
    '''
        Plot the line plot for the expenditures and receipts for the
        country between 2009 and 2017
        
        Returns: None
    '''
    
    
    title = "Average expenditures and receipts for {} between 2009 and 2017".format(country_code)
    years = range(MIN_YEAR, MAX_YEAR+1)
    fig, axs = plt.subplots(figsize=(7,5))
    axs.set_title(title)
    axs.set_ylabel("Cost (US dollar)")
    axs.plot(years, expend_list, years, receipt_list)
    axs.legend(['Expenditures','Receipt'])

#    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
    fig.savefig('line.png',dpi=100)
    fig.clf()

def main():
    '''
        WRITE DOCSTRING HERE!!!
    '''
    
    BANNER = "International Travel Data Viewer\
    \n\nThis program reads and displays departures, arrivals, expenditures,"\
    " and receipts for international travels made between 2009 and 2017."
    
    # Prompt for option
    OPTION = "Menu\
    \n\t1: Display data by year\
    \n\t2: Display data by country\
    \n\t3: Display country codes\
    \n\t4: Stop the Program"
    
    print(BANNER)
    
    #open and read travel file
    travel_str = 'travel'
    fp = open_file(travel_str)
    data_list = read_travel_file(fp)
    
    #open and read country code file
    country_str = 'country'
    fp = open_file(country_str)
    country_list = read_country_code_file(fp)
    
    #print option
    print(OPTION)
    #prompt while loop
    option = input('\t\tEnter option number: ')
    
    # '4' will end loop
    while option != '4':
        
        if option == '1': #Display data by year
            
            #year must be between 2009 and 2017 and an int
            while True:
                try:
                    year = int(input("Enter year: ")) #make year an int
                    while year < 2009 or year > 2017: #year within range
                        print('Year needs to be between 2009 and 2017. Try Again!')
                        year = int(input("Enter year: "))
                    break #an int and in the correct range, break loop
                except ValueError:
                    print('Year needs to be between 2009 and 2017. Try Again!')
            
            #which part of data_file you need depends on year
            if year == 2009:
                year_list = data_list[0]
            elif year == 2010:
                year_list = data_list[1]
            elif year == 2011:
                year_list = data_list[2]
            elif year == 2012:
                year_list = data_list[3]
            elif year == 2013:
                year_list = data_list[4]
            elif year == 2014:
                year_list = data_list[5]
            elif year == 2015:
                year_list = data_list[6]
            elif year == 2016:
                year_list = data_list[7]
            elif year == 2017:
                year_list = data_list[8]
            
            #display
            display_year_data(year_list)
            
            #ask to plot
            plot_str = input('Do you want to plot (yes/no)? ').lower() 
            
            #get data needed to plot 
            if plot_str == 'yes':
        
                expend_list, receipt_list = prepare_bar_plot(year_list)
                plot_bar_data(expend_list, receipt_list, year)
            
            #prompt while loop
            print(OPTION)
            option = input('\t\tEnter option number: ')
                
        elif option == '2': #display data by country
            
            country_code = input("Enter country code: ").upper() #all country codes are upper case
            
            #check if country code is in data_list
            count = 0
            while True:
                for list in data_list:
                    for tup in list:
                        if country_code in tup[2]:
                            count += 1 
                            
                if count == 0: #if count doesn't go up, country code isn't in list
                    print('Country code is not found! Try Again!')
                    country_code = input("Enter country code: ").upper()
                else:
                    break 
            
            #display country code data
            country_code_list = get_country_code_data(country_code, data_list)
            display_country_data(country_code_list)
            
            #ask to plot
            plot_str = input('Do you want to plot (yes/no)? ').lower()
            
            #line graph 
            if plot_str == 'yes':
                expend_list, receipt_list = prepare_line_plot(country_code_list)
                plot_line_data(country_code,expend_list,receipt_list)
                
            #prompt while loop
            print(OPTION)
            option = input('\t\tEnter option number: ')
                
        elif option == '3':
            
            #header
            print('Country Code Reference')
            print('{:<15s}{:<25s}'.format('Country Code','Country Name'))
            
            #get country and country code from country_list
            for tup in country_list:
                print('{:<15s}{:<25s}'.format(tup[0],tup[1]))
            
            #prompt while loop
            print(OPTION)
            option = input('\t\tEnter option number: ')
        
        #if user inputs the wrong option
        elif option != '1' or option != '2' or option != '3':
            print('Invalid option. Try Again!')
            print(OPTION)
            option = input('\t\tEnter option number: ')
     
    #when user inputs '4'
    else:
        print("\nThanks for using this program!")
        
if __name__ == "__main__":
    main()