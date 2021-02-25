
"""
    Game of Scrabble
    1. Open a file and read it
    2. Get all of the letters in user's rack and letters
     placed on board
    3. Find all possible words the letters can create and 
    calculate their scores
    4. Display the words with longest length and score
"""

import itertools
from operator import itemgetter

SCORE_DICT = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,
              'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,
              's':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

def open_file():
    """
    This function opens a file that's inputed by user
    Returns file
    """
    while True: #create loop
        try:
            open_fp = input('Input word file: ') #input file name
            fp = open(open_fp, "r")
            return fp
            break
        except FileNotFoundError:
            print('File not found! Try Again!')

def read_file(fp): 
    """
    This function reads the file 
    Returns a dictionary 
    """
    scrabble_words_dict = {} 
    
    for line in fp:
        line = line.lower().rstrip() #lower and strip spaces
        
        if len(line) < 3: #don't want words less than 3
            continue
        elif "'" in line: #no ' or -
            continue
        elif "-" in line:
            continue
        elif line in scrabble_words_dict:
            scrabble_words_dict[line] += 1
            
        else:
            scrabble_words_dict[line] = 1 #add to dict
    
    fp.close()
    
    return scrabble_words_dict

def calculate_score(rack,word): 
    """
    The function calculates how many points a word is
    Returns the score (int)
    """
    
    score = 0
    count = 0
    
    for letter in word: #get score from SCORE_DICT
        score += SCORE_DICT[letter]
    
    for char in rack: #count how many letters used in rack
        if char in word:
            count += 1
            word = word.replace(char,'',1)
    
    if count == 7: #if uses all 7 letters in rack
        score += 50
    
    return score

def generate_combinations(rack,placed_tile): 
    """
    This function finds all combinations of string 
    Returns a set 
    """
    words_set = set() #create a set
    letters_str = rack + placed_tile #combine
    
    for words_tup8 in itertools.combinations(letters_str, 8): #find combos
        if placed_tile =='': #if no tiles on board
            words_set.add(words_tup8)
        if placed_tile in words_tup8:  #must include placed_tile
            words_set.add(words_tup8) #add tuples
        
        #repeat above up until the length of 3
    for words_tup7 in itertools.combinations(letters_str, 7): 
        if placed_tile =='':
            words_set.add(words_tup7)
        if placed_tile in words_tup7: 
            words_set.add(words_tup7)
        
    for words_tup6 in itertools.combinations(letters_str, 6):
        if placed_tile =='':
            words_set.add(words_tup6)
        if placed_tile in words_tup6: 
            words_set.add(words_tup6)
        
    for words_tup5 in itertools.combinations(letters_str, 5):
        if placed_tile =='':
            words_set.add(words_tup5)
        if placed_tile in words_tup5: 
            words_set.add(words_tup5)
        
    for words_tup4 in itertools.combinations(letters_str, 4):
        if placed_tile =='':
            words_set.add(words_tup4)
        if placed_tile in words_tup4: 
            words_set.add(words_tup4)
        
    for words_tup3 in itertools.combinations(letters_str, 3): 
        if placed_tile =='':
            words_set.add(words_tup3)
        if placed_tile in words_tup3: 
            words_set.add(words_tup3)
    
    return words_set

def generate_words(combo,scrabble_words_dict):   
    """
    This function finds all the permutations of a list of characters
    Returns a set 
    """
    word_set = set() #create new set
    
    for word in itertools.permutations(combo):
        word = ''.join(word) #make word
        if word in scrabble_words_dict: #if in dict, add to set
            word_set.add(word)
    
    return word_set

def generate_words_with_scores(rack,placed_tile,scrabble_words_dict): 
    """
    This function creates a dict with all of the possible words and scores
    Returns a dict
    """
    words_score_dict = {} #create new dict
    
    #get all of the combinations
    combinations = generate_combinations(rack,placed_tile) #returns a set
    for element in combinations:
        #get all of the words would of combinations
        words_set = generate_words(element,scrabble_words_dict) #returns a set
        for words in words_set:
            score = calculate_score(rack,words)
            words_score_dict[words] = score
    
    return words_score_dict
    

def sort_words(word_dic): 
    """
    This function sorts dict into two lists based on each words length and score
    Returns two lists. One sorted by score and other by length
    """
    #create new list
    word_score_len = []
    
    #Get word and score from dict
    for word,score in word_dic.items():
        #create tuples based on word, score, and length
        word_score_len_tup = word, score, len(word)
        word_score_len.append(word_score_len_tup)
    #sort alphabetically
    word_score_len.sort()
    
    #create sorted score list
    score_sort = word_score_len[:]
    score_sort.sort(key=itemgetter(1,2),reverse=True)
    
    #create sorted length list
    len_sort = word_score_len[:]
    len_sort.sort(key=itemgetter(2,1), reverse=True)
    
    return score_sort,len_sort

def display_words(word_list,specifier): 
    """
    This function displays the top 5 words in length and score
    No return
    """
    specifier = specifier.lower()
    
    # DISPLAY TOP 5 LENGTH
    if specifier == 'length':
        #headers
        print('Word choices sorted by Length')
        print("{:>6s}  -  {:s}".format('Length','Word'))

        #only 5
        if len(word_list) > 5:
            print("{:>6d}  -  {:s}".format(word_list[0][2],word_list[0][0]))
            print("{:>6d}  -  {:s}".format(word_list[1][2],word_list[1][0]))
            print("{:>6d}  -  {:s}".format(word_list[2][2],word_list[2][0]))
            print("{:>6d}  -  {:s}".format(word_list[3][2],word_list[3][0]))
            print("{:>6d}  -  {:s}".format(word_list[4][2],word_list[4][0]))
            
        #if there are less than 5 words, display all of them
        else:
            for tup in word_list:
                print("{:>6d}  -  {:s}".format(tup[2],tup[0]))
    
    # DISPLAY TOP 5 SCORE    
    if specifier == 'score':
        #headers
        print('Word choices sorted by Score')
        print("{:>6s}  -  {:s}".format('Score','Word'))
        
        #only 5
        if len(word_list) > 5:
            print("{:>6d}  -  {:s}".format(word_list[0][1],word_list[0][0]))
            print("{:>6d}  -  {:s}".format(word_list[1][1],word_list[1][0]))
            print("{:>6d}  -  {:s}".format(word_list[2][1],word_list[2][0]))
            print("{:>6d}  -  {:s}".format(word_list[3][1],word_list[3][0]))
            print("{:>6d}  -  {:s}".format(word_list[4][1],word_list[4][0]))
            
        #if there are less than 5 words, display all of them    
        else:
            for tup in word_list:
                print("{:>6d}  -  {:s}".format(tup[1],tup[0]))
            

def main(): #weekend
    """
    This function is used to display results, depending on user's input.
    """
    #header
    print('Scrabble Tool')
    user_input = input('Would you like to enter an example (y/n): ').lower()
       
    #if user wants to continue, loop until they say no
    while user_input == 'y':
        
        #open file and read it
        fp = open_file()
        scrabble_words_dict = read_file(fp)
        
        #get the users rack
        rack = input('Input the rack (2-7chars): ')
        #rack has to be in between 2 and 7
        if 2 > len(rack):
            continue
        elif 7 < len(rack):
            continue
        #rack has to have only letters
        if not rack.isalpha():
            continue
        
        #get placed tiles
        while True: 
            placed_tiles = input('Input tiles on board (enter for none): ')
            #can be an empty string
            if placed_tiles == '':
                break
            #only has letters
            elif not placed_tiles.isalpha():
                continue
            else:
                break
        
        #no tiles placed, only print possible combos with rack
        if placed_tiles == '':
            final_dict = generate_words_with_scores(rack,placed_tiles,scrabble_words_dict)
            
            score_sort, len_sort = sort_words(final_dict)
        
            display_words(score_sort,'score')
            display_words(len_sort,'length')
        
        #tiles placed
        else:
            final_dict = {}
            index = -1
            
            #get the number of indecies in placed_tiles
            for char in placed_tiles:
                index += 1
            
            #get possible words for each placed tile and put into final list
            while index != -1:
                D1 = generate_words_with_scores(rack,placed_tiles[index],scrabble_words_dict)
                for key, value in D1.items():
                    final_dict[key] = value
            
                index -= 1
            
            #sort
            score_sort, len_sort = sort_words(final_dict)
        
            #display
            display_words(score_sort,'score')
            display_words(len_sort,'length')
        
        #promput loop again or break it
        user_input = input('Do you want to enter another example (y/n): ').lower()
        
    else:
        print("Thank you for playing the game")
        
if __name__ == "__main__":
    main()