
"""
    PROJECT 9
    1. Read through csv file
    2. Make master dict that has all info required for other functions
    3. Use master dict to get specific in diff functions
    4. Display in main()
"""

import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def open_file(message='breachdata.csv'):
    
    '''
        This function open and reads a file
        Returns a file
    '''
    while True: #keep loop
        
        try:
            fp = open(message, encoding='utf8') #how to open 
            return fp
            break #after getting correct file, break
            
        #if file not found, repeat until a file is found
        except FileNotFoundError:
            print('Error: file not found.')
            message = input("Input a filename: ")
    
    
def build_dict(reader):
    '''
        This function reads CSV file to gain all info needed
        for other functions
        Returns a dict
    '''
    
    next(reader,None) #skip header
    big_dict = {}
    
    #read CSV lines
    for line in reader:
        

        entity = line[0]
        
        records_lost = line[2].split(',')
        records_lost = ''.join(records_lost)

        #check if records_lost is an int, skip if not
        try:
            records_lost = int(records_lost)
        except ValueError:
            continue
        
        #check if year is an int, skip if not
        try:
            year = int(line[3])
        except ValueError:
            continue
        
        story = line[4]
        if story == '':
            continue
        sector = line[5]
        if sector == '':
            continue
        method = line[6]
        if method == '':
            continue
        new_sources = line[11]
        if new_sources == '':
            continue
        else:
            new_sources = new_sources.split(',')
        
        #put in two diff dicts
        D1 = {entity :(records_lost, year, story, new_sources)}
        D2 = {year: (sector,method)}
    
        #make into tups
        tup_dicts = D1, D2
        
        #put into big_dict
        if entity in big_dict:
            big_dict[entity] += [tup_dicts]
        else:
            big_dict[entity] = [tup_dicts]

    return big_dict

def top_rec_lost_by_entity(dictionary):
    '''
        This function goes through dict and finds the top 10 entities that
        lost the most records
        Returns a list
    '''
    
    rec_lost_dict = {}
    
    #get the records_lost in dict
    for keys, values in dictionary.items():
        #entity is the key in original dict
        entity = keys
        for tups in values:
            for small_dicts in tups:
                for items in small_dicts.values():
                    #either an int or a str, get rid of strs 
                    try:
                        records_lost = int(items[0])
                        #if in dict, add the records_lost
                        if entity in rec_lost_dict:
                            rec_lost_dict[entity] += records_lost
                        #add to dict
                        else:
                            rec_lost_dict[entity] = records_lost
                    
                    except ValueError:
                        continue
    
    #create tuples and add to a list and sort so that the largest recrods lost
    #is at the beginning
    rec_lost_total_list = [tuple(x) for x in rec_lost_dict.items()]
    rec_lost_total_list.sort(key=itemgetter(1, 0), reverse=True)
    
    #get only the top ten
    if len(rec_lost_total_list) > 10:
        
       count = 0
       index = 0
       rec_lost_list_10 = [] #create a new list to add elements
    
       while count < 10:
           rec_lost_list_10.append(rec_lost_total_list[index])
           index += 1
           count += 1
    else:
        rec_lost_list_10 = rec_lost_total_list

    return rec_lost_list_10


def records_lost_by_year(dictionary):
    '''
        This function adds the total records lost per year
        Returns a list
    '''
    
    total_year_rec_dict = {}
    
    for keys, values in dictionary.items():
        #only want values, don't care about entities
        for tups in values:
            #tuples
            for small_dicts in tups:
                #dict
                for items in small_dicts.values():
                    #here you can get the year and records_lost
                    try:
                        year = int(items[1])
                        records_lost = int(items[0])
                        
                        #add to dict and add the records_lost up
                        if year in total_year_rec_dict:
                            total_year_rec_dict[year] += records_lost
                        else:
                            total_year_rec_dict[year] = records_lost
                            
                    
                    except ValueError:
                        continue
    
    #make tuples and add to list, then sort
    total_list = [tuple(x) for x in total_year_rec_dict.items()]
    total_list.sort(key=itemgetter(1, 0), reverse=True)
    
    return total_list

def top_methods_by_sector(dictionary):
    '''
        This function counts how many instances a method had occured in 
        each sector
        Returns a dict
    '''
    
    master_dict = {}
    
    #get sector and method from original dict
    for keys, values in dictionary.items():
        for lists in values:
            sector_dicts = lists[1]
            for values in sector_dicts.values():
                
                sector = values[0]
                method = values[1]
                
                #put sector and method in nested dict
                #count how many times the method occurs
                if sector in master_dict:
                    
                    if method in master_dict[sector]:
                        master_dict[sector][method] += 1
                    else:
                        master_dict[sector][method] = 1
                            
                else:
                    master_dict[sector] = {}
                    master_dict[sector][method] = 1
                    
    #sort the sectors in alaphabetical order and add to a different dict
    #keeping the same values with each key             
    top_methods_dict = {}
    sector_list = []
    
    for keys in master_dict:
        sector_list.append(keys)
    
    sector_list.sort()
    
    for sector in sector_list:
        top_methods_dict[sector] = master_dict[sector]
    
    return top_methods_dict

        
def top_rec_lost_plot(names,records):
    ''' Plots a bargraph pertaining to
        the cybersecurity breaches data '''
        
    y_pos = np.arange(len(names))

    plt.bar(y_pos, records, align='center', alpha=0.5,
            color='blue',edgecolor='black')
    plt.xticks(y_pos, names, rotation=90)
    plt.ylabel('#Records lost')
    plt.title('Cybersecurity Breaches',fontsize=20)
    plt.show()
    
def top_methods_by_sector_plot(methods_list):
    ''' Plots the top methods used to compromise
        the security of a sector '''
    methods = [] ; quantities = []
    for tup in methods_list:
        methods.append(tup[0])
        quantities.append(tup[1])
    labels = methods
    sizes = quantities
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors = colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.show()
    
def main():
    BANNER = '''
    
                 _,.-------.,_
             ,;~'             '~;, 
           ,;                     ;,
          ;                         ;
         ,'                         ',
        ,;                           ;,
        ; ;      .           .      ; ;
        | ;   ______       ______   ; | 
        |  `/~"     ~" . "~     "~\'  |
        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
         |   |        }:{        |   | 
         |   l       / | \       !   |
         .~  (__,.--" .^. "--.,__)  ~. 
         |     ---;' / | \ `;---     |  
          \__.       \/^\/       .__/  
           V| \                 / |V  
            | |T~\___!___!___/~T| |  
            | |`IIII_I_I_I_IIII'| |  
            |  \,III I I I III,/  |  
             \   `~~~~~~~~~~'    /
               \   .       .   /
                 \.    ^    ./   
                   ^~~~^~~~^ 
                   
           
           ~~Cybersecurity Breaches~~        
                   @amirootyet    
                
    '''
    
    print(BANNER)
    
    MENU = '''  
[ 1 ] Most records lost by entities
[ 2 ] Records lost by year
[ 3 ] Top methods per sector
[ 4 ] Search stories
[ 5 ] Exit'''
    
    print(MENU)
    #to prompt while loop
    MENU_INPUT = input('''[ ? ] Choice: ''')
    
    #if correct input, then open a file
    if MENU_INPUT == '1' or MENU_INPUT == '2' or MENU_INPUT == '3' or MENU_INPUT == '4':
        message = input('[ ? ] Enter the file name: ')
        
        # '' = 'breachdata.csv', already in open_file parameter
        if message == '':
            fp = open_file()
        else:
            fp = open_file(message)
        
        #need to reader to get dict
        reader = csv.reader(fp)
        big_dict = build_dict(reader)
    
    while MENU_INPUT != '5':
        
        #prints top_rec_lost_by_entity()
        if MENU_INPUT == '1':
            
            #header
            print('[ + ] Most records lost by entities...')
            
            entity_rec_list = top_rec_lost_by_entity(big_dict)
            
            #print entity and records lost
            count = 1
            for tup in entity_rec_list:
                print('-'*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format(count, tup[0], tup[1]))
                count += 1
                
            #ask if user wants to plot
            user_plot = input('[ ? ] Plot (y/n)? ')
            
            #get names and records from tup in entity_rec_list
            #add to a new list
            #use top_rec_lost_plot
            if user_plot == 'y':
                
                names = []
                records = []
                
                for tup in entity_rec_list:
                    names.append(tup[0])
                    records.append(tup[1])
                
                top_rec_lost_plot(names, records)
            
            #prompt while loop
            print(MENU)
            MENU_INPUT = input('''[ ? ] Choice: ''')
            
        #print records_lost_by_year()    
        elif MENU_INPUT == '2':
            
            #header
            print('[ + ] Most records lost in a year...')
            
            rec_year_list = records_lost_by_year(big_dict)
            
            #print year and records lost
            count = 1
            for tup in rec_year_list:
                print('-'*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format(count,str(tup[0]),tup[1]))
                count += 1
            
            #ask if user wants to plot
            user_plot = input('[ ? ] Plot (y/n)? ')
            
            #put year and records in new lists
            #use top_rec_lost_plot() to plot
            if user_plot == 'y':
                
                years = []
                records = []
                
                for tup in rec_year_list:
                    years.append(tup[0])
                    records.append(tup[1])
                
                top_rec_lost_plot(years, records)
            
            #prompt while loop
            print(MENU)
            MENU_INPUT = input('''[ ? ] Choice: ''')
        
        #print top_methods_by_sector()
        if MENU_INPUT == '3':
            
            #header
            print('[ + ] Loaded sector data.')
            
            sector_methods_dict = top_methods_by_sector(big_dict)
            
            #print sector
            for keys in sector_methods_dict:
                print(keys, end=' ')
            
            #make sure correct sector was inputed
            while True:
                input_sector = input('[ ? ] Sector (case sensitive)? ')
                if input_sector in sector_methods_dict:
                    break
                else:
                    print('[ - ] Incorrect input. Try again.')
                    
            #print what sector was chosen
            print('[ + ] Top methods in sector {}'.format(input_sector))
        
            methods_list = []
            print_dict = {}
            
            #get the methods and sort to get alaphabetical order
            for methods, values in sector_methods_dict[input_sector].items():
                methods_list.append(methods)
            methods_list.sort()
            
            #get correct values with methods
            for methods in methods_list:
                print_dict[methods] = sector_methods_dict[input_sector][methods]
            
            #print methods and values
            count = 1
            for methods, values in print_dict.items():
                print('-'*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format(count, methods, values))
                count += 1
            
            #ask user to plot
            user_plot = input('[ ? ] Plot (y/n)? ')
            
            #create a master_list by appending tups from sector_methods_dict
            #use top_methods_by_sector_plot to display
            if user_plot == 'y':
                
                master_list = []
                
                for dicts in sector_methods_dict[input_sector].items():
                    master_list.append(dicts)
                
                top_methods_by_sector_plot(master_list)
            
            #prompt while loop
            print(MENU)
            MENU_INPUT = input('''[ ? ] Choice: ''')
        
        #use big_dict to print each story one entity
        elif MENU_INPUT == '4':
            
            #get correct entity
            while True:
                entity = input('[ ? ] Name of the entity (case sensitive)? ')
                if entity in big_dict:
                    break
                else:
                    print('[ - ] Entity not found. Try again.')
            
            count = 0
            story_list = []
            
            #get story from big_dict
            for entity_list in big_dict[entity]:
                get_story = entity_list[0]
                for values in get_story.values():
                    story = values[2]
                    #add to list
                    story_list.append(story)
                    #count how many stories
                    count += 1
            
            #print how many stories
            print('[ + ] Found {} stories:'.format(count))
            
            #count how many stories were displayed, can't exceed count
            num_of_story = 1
            #to get story out of list
            index = 0
            
            #print
            while num_of_story <= count:
                print('[ + ] Story {}: {}'.format(num_of_story, story_list[index]))
                index += 1
                num_of_story += 1
            
            #prompt while loop
            print(MENU)
            MENU_INPUT = input('''[ ? ] Choice: ''')
         
        #if wrong input
        elif MENU_INPUT != '1' and MENU_INPUT != '2' and MENU_INPUT != '3' and MENU_INPUT != '4' and MENU_INPUT != '5':
            print('[ - ] Incorrect input. Try again.')
            
            #prompt loop again
            print(MENU)
            MENU_INPUT = input('''[ ? ] Choice: ''')
            
    #end program    
    else:
        print('[ + ] Done. Exiting now...')
        
        
if __name__ == "__main__":
     main()