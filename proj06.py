#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Reading csv files

Making a list of country rank, website, traffic rank, 
average daily pageviews, and country

Creating functions to manipulate list

Prompt user to select what data they want displayed

'''

import csv
from operator import itemgetter 

#prompts for main()
PROMPT = ''' 
Choose
         (1) Top sites by country
         (2) Search by web site name
         (3) Top sites by views
         (q) Quit         
'''

         
def open_file():
    '''This function prompts the user to input a file.'''
    '''returns fp'''
    
    while True: #keep loop
        try:
            file_name = input("Input a filename: ") 
            fp = open(file_name, encoding='ISO-8859-1') #how to open 
            return fp
            break #after getting correct file, break
        except FileNotFoundError:
            print('Error: file not found.')

def read_file(fp):
    '''This function converts the file to a list.'''
    '''returns a list'''
    
    L_of_L = [] #empty list
    for row in fp: #to read every line
        
        row = row.split(',') #turn to list first
        
        traffic_rank = row[14] #get rid of spaces
        traffic_rank = traffic_rank.split()
        traffic_rank = ''.join(traffic_rank)
        
        avg_daily_pageviews = row[5] #get rid of spaces
        avg_daily_pageviews = avg_daily_pageviews.split()
        avg_daily_pageviews = ''.join(avg_daily_pageviews)
        
        try: #try to turn into int
            row[0] = int(row[0])
            row[14] = int(traffic_rank)
            row[5] = int(avg_daily_pageviews)
        except ValueError:
            continue #restarts for loop, n/a data
        
        country = row[-1]
        country = country.rstrip() #get rid of white space
        
        row = row[0], row[1], row[14], row[5], country #creates tuple
        L_of_L.append(row) #list of tuples
    
    fp.close()
    L_of_L.sort(key=itemgetter(0,4)) #sort
        
    return L_of_L   

def remove_duplicate_sites(L_of_L):
    '''This function goes through list and removes duplicate sites.'''
    '''Returns a list'''
    
    website_list = [] #what websites were listed
    remove_list = [] #list to return, all data
    
    for row in L_of_L:
        
        website = row[1].split('.')
        website = website[1] #don't want endings (ex: .com, .it ,etc)
        
        if website not in website_list: #website already not listed
            website_list.append(website)
            remove_list.append(row)
            
    remove_list.sort(key=itemgetter(0,1)) #sort
    
    return remove_list

def top_sites_per_country(L_of_L,country):
    '''This function reutns the top 20 ranked sites for a certain country.'''
    '''Returns a list'''
    
    top_list = [] #final list
    count = 0 #only want 20
    
    for row in L_of_L:
        
        if row[4] == country and count < 20:
            top_list.append(row)
            count += 1
            
    top_list.sort(key=itemgetter(0)) #sort
    
    return top_list

def top_sites_per_views(L_of_L):
    '''This function will return the top 20 sites ranked by page views.'''
    '''Returns a list'''
    
    top_view_list = [] #final list
    count = 0 #only want 20
    
    L_of_L.sort(key=itemgetter(3), reverse=True) #want the greatest page views 
    
    top_remove_list = remove_duplicate_sites(L_of_L) #don't want to same sites
    top_remove_list.sort(key=itemgetter(3), reverse=True)
    
    for row in top_remove_list:
        
        if count < 20:
            top_view_list.append(row)
            count += 1
            
    top_view_list.sort(key=itemgetter(3),reverse=True) #want the highest page views
    
    return top_view_list


def main():
    ''''This function is used to display results, depending on user's input.'''
    
    print('----- Web Data -----')
    L_of_L = read_file(open_file()) #get list from file
    print(PROMPT) #display options
    prompt = input("Choice: ").lower() #ask user
    
    while prompt != 'q': #q quits
    
        if prompt == '1': #top sites of country
            
            print('--------- Top 20 by Country -----------')
            
            country = input("Country: ")
            top_sites_list = top_sites_per_country(L_of_L,country) #get top 20 list using function
            
            print("{:30s} {:>15s}{:>30s}".format('Website','Traffic Rank','Average Daily Page Views'))

            for line in top_sites_list: #get website, traffic rank, and avg daily in list
                website = line[1]
                traffic_rank = line[2]
                avg_daily = line[3]
            
                print("{:30s} {:>15d}{:>30,d}".format(website,traffic_rank,avg_daily)) #print

            print(PROMPT)
            prompt = input("Choice: ").lower() #prompt while loop
            
        elif prompt == '2': #Search by web site name
            
            search = input("Search: ").lower() 
            results = []
    
            for line in L_of_L:
                websites = line[1] #full website name
                
                website_search = line[1]
                website_search = website_search.split('.')
                website_search = website_search[1] #remove www. and ending
            
                if search in website_search: #search in cut web, add website to results
                    results.append(websites)
                
            if results == []: #if there are no results
                print("{:^50s}".format("Websites Matching Query"))
                print('None found')
            else:
                print("{:^50s}".format("Websites Matching Query"))
                for final_website in results: #print individual website
                    print("{:<10s}".format(final_website))
            
            print(PROMPT)
            prompt = input("Choice: ").lower() #prompt while loop
                
        elif prompt == '3': #Top sites by views
            
            print('--------- Top 20 by Page View -----------')
            
            top_list = top_sites_per_views(L_of_L) #top 20 view page
            print("{:30s} {:>15s}".format('Website','Ave Daily Page Views'))
            
            for line in top_list:
                website = line[1] #only want website and avg views
                avg_daily = line[3]
                
                print("{:30s} {:>20,d}".format(website,avg_daily)) #print in every line
                
            print(PROMPT)
            prompt = input("Choice: ") #prompt while loop
            
        elif prompt != '1' or prompt != '2' or prompt != '3': #incorrect output
            print('Incorrect input. Try again.')
            print(PROMPT)
            prompt = input("Choice: ").lower() #prompt while loop
            
if __name__ == "__main__":
     main()