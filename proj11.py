"""
    PROJECT 11: Pokemon Game
    Creates a move and pokemon list by reading csv files
    Player 1 and player 2 pick a pokemon
    Play turns until either quits or wins
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
        Uses a csv.reader and creates a list of move objects
        Returns a list
    '''
    #csv reader
    reader = csv.reader(fp)
    next(reader,None)
    
    #create list and go through line to find parameters for move class
    #remember to int type_id, accuracy, and damage_class_id
    moves_list = []
    for line in reader:
        
        name = line[1]
        type_id = int(line[3])
        
        if type_id >= 19:
            continue
        
        element = element_id_list[type_id]
        power = line[4]
        if power == '':
            continue
        else:
            power = int(power)
        accuracy = line[6]
        if accuracy == '':
            continue
        else:
            accuracy = int(accuracy)
        damage_class_id = int(line[9]) #attack
        if damage_class_id == 1:
            continue
        generation_type = line[2]
        if generation_type != '1':
            continue
        
        #put in move class then add to list
        move_function = Move(name, element, power, accuracy, damage_class_id)
       
        moves_list.append(move_function)
        
    return moves_list
    


def read_file_pokemon(fp):
    '''
        Uses a csv.reader and creates a list of pokemon objects
        Returns a list
    '''
    #csv reader
    reader = csv.reader(fp)
    next(reader,None)
    
    poke_list = []
    column_list = []
    
    #go thorugh csv file and find parameters for pokemon class
    #int hp, patt, pdef, satt, sdef
    #none for moves
    for line in reader:
        generation_column = line[11]
        if generation_column != '1':
            continue
        
        column_num = int(line[0])
        #if there are multiple columns, keep the first skip the rest
        if column_num in column_list:
            continue
        else:
            column_list.append(column_num)
        
        name = line[1].lower()
        element1 = line[2].lower()
        element2 = line[3].lower()
        hp = int(line[5])
        patt = int(line[6])
        pdef = int(line[7])
        satt = int(line[8])
        sdef = int(line[9])
        moves = None
        
        pokemon_function = Pokemon(name, element1, element2, moves, hp, patt,
                                   pdef, satt, sdef)
        #add to list
        poke_list.append(pokemon_function)
    
    return poke_list

def choose_pokemon(choice,pokemon_list):
    '''
        This function finds the pokemon in pokemon list with either
        an index or a string
        Returns pokemon object or None
    '''
    copy_poke_list = deepcopy(pokemon_list)
    
    #if choice is an index, subtract one from choice
    #return index from the copied list
    try:
        choice = int(choice)
        index = choice - 1
        try:
            return copy_poke_list.pop(index)
        except IndexError:
            return None
    except ValueError:
        pass
    
    #if type is a string, find in list and return it
    if type(choice) is str:
        for element in pokemon_list:
            element_str = str(element)
            element_list = element_str.split()
            if choice == element_list[0]:
                return element
    
    return None

def add_moves(pokemon,moves_list):
    '''
        Adds one random move and then adds three more 
        if possible
        Returns a Boolean
    '''
    copy_moves_list = deepcopy(moves_list)
    
    index = -1
    #find how many index in copy list
    for move in copy_moves_list:
        index += 1
    
    #random move
    random_num = randint(0,index)
    move = copy_moves_list[random_num]
    pokemon.add_move(move)
    
    #add only 3 moves
    #check 200 times before returning false
    count = 0
    for i in range(200):
       random_num = randint(0,index)
       move = copy_moves_list[random_num]
       
       #if the pokemon already has that move then skip
       if move in pokemon.get_moves():
           continue

       get_element = move.get_element()
       
       #add move if element is the same as one of the pokemon's elements
       if get_element == pokemon.get_element1():
           pokemon.add_move(move)
           count += 1
           if count == 3:
               return True
       elif get_element == pokemon.get_element2():
           pokemon.add_move(move)
           count += 1
           if count == 3:
               return True
           
    return False


def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        This function is how the players take their turns
        Returns a boolean
    '''
    #print the player and the pokemon
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    
    if player_num == 1:
        opponent_num = 2
    elif player_num == 2:
        opponent_num = 1
    
    #show prompt
    prompt = input("""Show options: 'show ele', 'show pow', 'show acc'
Select an attack between 1 and 4 or show option or 'q': """).lower()
    
    while prompt != 'q' and prompt != 'n':
        
        #show_move_element
        if prompt == 'show ele':
            player_pokemon.show_move_elements()
            prompt = input("""Show options: 'show ele', 'show pow', 'show acc'
Select an attack between 1 and 4 or show option or 'q': """).lower()
        
        #show_move_power
        elif prompt == 'show pow':
            player_pokemon.show_move_power()
            prompt = input("""Show options: 'show ele', 'show pow', 'show acc'
Select an attack between 1 and 4 or show option or 'q': """).lower()
    
        #show_move_accuracy
        elif prompt == 'show acc':
            player_pokemon.show_move_accuracy()
            prompt = input("""Show options: 'show ele', 'show pow', 'show acc'
Select an attack between 1 and 4 or show option or 'q': """).lower()
        
        #if they pick an index
        elif prompt == '1' or prompt == '2' or prompt == '3' or prompt == '4':
            
            print('selected move:',player_pokemon.choose(int(prompt) - 1))
            print('{} hp before:{}'.format(opponent_pokemon.get_name(),opponent_pokemon.get_hp()))
            
            #display move and attack
            move = player_pokemon.choose(int(prompt) - 1)
            player_pokemon.attack(move, opponent_pokemon)
            
            #show the hp
            print('{} hp after:{}'.format(opponent_pokemon.get_name(),opponent_pokemon.get_hp()))
            
            #if someone wins the hp is <= 0, then return False
            if opponent_pokemon.get_hp() <= 0:
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(opponent_num, player_num))
                return False
            elif player_pokemon.get_hp() <= 0:
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(player_num, opponent_num))
                
                return False
            break
        else:
            prompt = input("Invalid option! Please enter a valid choice: ").lower()
            
    #when they hit q
    else:
        print('Player {} quits, Player {} has won the pokemon battle!'.format(player_num, opponent_num))
        return False

def main():
    """The main function which displays how to play the game"""
    
    #get the move and pokemon lists
    fp_move = open('moves.csv')
    fp_poke = open('pokemon.csv')
    
    moves_list = read_file_moves(fp_move)
    poke_list = read_file_pokemon(fp_poke)
    
    #prompt user
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
   
    #loop until hit q or n
    while usr_inp != 'q':
        
        #battle
        if usr_inp == 'y':
            
            choice1 = input('Player 1, choose a pokemon by name or index: ').lower()
            pokemon1 = choose_pokemon(choice1,poke_list)
            
            #player 1
            pokemon1 = choose_pokemon(choice1,poke_list)
            print('pokemon1:')
            print(pokemon1)
            
            choice2 = input('Player 2, choose a pokemon by name or index: ').lower()
            
            #player 2
            pokemon2 = choose_pokemon(choice2,poke_list)
            print('pokemon2:')
            print(pokemon2)
            
            #add moves
            add_moves(pokemon1,moves_list)
            add_moves(pokemon2,moves_list)
            
            #take turns with player 1 going first
            turn1 = turn(1, pokemon1, pokemon2)
                    
            if pokemon2.get_hp() != 0:
                turn2 = turn(2, pokemon2, pokemon1)
            
            #keep going until turn() == False
            while turn1 != False and turn2 != False:
                
                print('Player 1 hp after: {}'.format(pokemon1.get_hp()))
                print('Player 2 hp after: {}'.format(pokemon2.get_hp()))
                
                turn1 = turn(1, pokemon1, pokemon2)
                    
                if pokemon2.get_hp() != 0 and turn1 != False:
                    turn2 = turn(2, pokemon2, pokemon1)
            
            
            #prompt while loop
            usr_inp = input('Battle over, would you like to have another? ').lower()
        
        #break while loop
        elif usr_inp == 'n':
            print("Well that's a shame, goodbye")
            break
        
        #user inputs some thing wrog
        else:
            usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
    
    #when user enters q
    else:
        print("Well that's a shame, goodbye")
    
if __name__ == "__main__":
    main()