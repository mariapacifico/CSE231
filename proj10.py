
"""
    Project 10
    ACES UP GAME
    1. initialize game by adding cards to tableau and shuffling deck
    using the Deck and Card class
    2. move cards into foundation or add to tableau until user
    quits or wins
"""


import cards 

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    
    '''
        This function starts the game by setting up the 
        frist four cards in the tableau and shuffles deck
        Returns stock, tableau, and foundation
    '''
    #get deck and shuffle
    stock = cards.Deck()
    stock.shuffle()
    
    #foundation is an empty list
    foundation = []
    
    #put 4 cards into tableau that are lists
    tableau = []
    
    for i in range(4):
        tableau.append( [stock.deal()] )
        
 
    return (stock, tableau, foundation)
    
def deal_to_tableau( stock, tableau ): 
        
    '''
        This function adds a card to each list in tableau
        Doesn't return anything
    '''
 
    #add card from stock into tableau lists
    tableau[0].append(stock.deal())
    tableau[1].append(stock.deal())
    tableau[2].append(stock.deal())
    tableau[3].append(stock.deal())


def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    
    # determine the number of rows to be printed -- determined by the most
    #           cards in any tableau column
    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):
        # display stock (only in first row)
        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char),end='')
        else:
            print("{:<8s}".format(""),end='')

        # display tableau
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format( str(col[i]) ), end='' )

        # display foundation (only in first row)
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()

def get_option():
    
    '''
        This function prompts user input and checks to see if it's valid
        Returns None or user input
    '''
    
    #ask user 
    user_input_pre_list = input('Input an option (DFTRHQ): ')
    #make all letters upper
    user_input_pre_list_upper = user_input_pre_list.upper()
    #make into a list
    user_input = user_input_pre_list_upper.split()
    
    #D has no other numbers needed
    if 'D' in user_input:
        if len(user_input) > 1:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        else:
            return user_input
    
    #F has an integer paired with it
    elif 'F' in user_input:
        if len(user_input) != 2:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        
        #make sure second input is an int
        try:
            user_input[1] = int(user_input[1])
            return user_input
        
        except ValueError:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
    
    # T has two integers paired with it
    elif 'T' in user_input:
        if len(user_input) != 3:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        
        #check to see if second and third input are numbers
        try:
            user_input[1] = int(user_input[1])
        except ValueError:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        
        try:
            user_input[2] = int(user_input[2])
            return user_input
        except ValueError:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
    
    # R doesn't have any integers paired with it
    elif 'R' in user_input:
        if len(user_input) > 1:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        else:
            return user_input
    
    # H doesn't have any integers paired with it
    elif 'H' in user_input:
        if len(user_input) > 1:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        else:
            return user_input
        
    # Q doesn't have any integers paired   
    elif 'Q' in user_input:
        if len(user_input) > 1:
            print('Error in option: {}'.format(user_input_pre_list))
            return None
        else:
            return user_input
   
    # if other input put in, then error     
    else:
        print('Error in option: {}'.format(user_input_pre_list))
        return None
            
def validate_move_to_foundation( tableau, from_col ):
    
    '''
        This function checks if card can go into foundation
        Another card must have a higher value and have the same suit
        Returns boolean
    '''
 #number must be in between 1 and 4
    if 1 <= from_col <= 4:
        
        index = from_col - 1
        
        cards_list= []
        count = -1
        
        #get card
        #if there is an empty list in column, then invalid
        try:
            card = tableau[index][-1]

        except IndexError:
            print('Error, no card')
            return False
        
        # add cards in last row to a list to compare card to
        while count < 4:
            count += 1
            try:
                if index != count:
                    cards_list.append(tableau[count][-1])
            
            except IndexError:
                pass
        
        index_count = -1
        
        #count how many cards in list
        for elements in cards_list:
            index_count += 1
            
        card_suit = card.suit()
        
        #loop thorugh list
        while index_count >= 0:
            
            #if they have the same suit, compare card values
            if card_suit == cards_list[index_count].suit():
                
                #aces have greater value and cannot be moved to foundation
                if card.value() == 1:
                    print('Error, cannot move {}.'.format(card))
                    return False
                
                #can't have greater value, unless other card is an ace
                elif card.value() > cards_list[index_count].value():
                    if cards_list[index_count].value() == 1:
                        return True
                    #break if true
                        break
                    
                #if card isn't greater than any suits, then true
                else:
                    return True
                    break
                
            index_count -= 1
        
        #if no other card has same suit, then false
        else:
            print('Error, cannot move {}.'.format(card))
            return False
    
    #put in wrong column number
    else:
        print('Error, not in range')
        return False

    
def move_to_foundation( tableau, foundation, from_col ):
    
    '''
        The funciton moves card to foundation
        Returns nothing
    '''
    
    #check if valid
    #the find card in column and add to foundation
    if validate_move_to_foundation(tableau, from_col):
        the_col = tableau[from_col-1]
        card1 = the_col.pop()
        foundation.append(card1)  


def validate_move_within_tableau( tableau, from_col, to_col ):
    
    '''
        This function checks if cards can move within tableau
        Returns boolean
    '''
    # from_col and to_col must be in between 1 and 4
    if 1 <= from_col <=4:
        
        if 1 <= to_col <= 4:
            index = to_col - 1
            
            #must be an empty to move card
            if tableau[index] == []:
                return True
            else:
                print('Invalid move')
                return False
        
        else:
            print('Invalid move')
            return False
        
    else:
        print('Invalid move')
        return False 


def move_within_tableau( tableau, from_col, to_col ):
    
    '''
        This function moves card with in tableau list
        Returns nothing
    '''
 
    #checks if move is valid
    #then moves card from from_col to to_col
    if validate_move_within_tableau(tableau, from_col, to_col):
        card = tableau[from_col-1].pop()
        tableau[to_col-1].append(card) 

        
def check_for_win( stock, tableau ):
    
    '''
        This funciton checks if the player won the game
        Returns boolean
    '''
 
    #stock must be empty
    if stock.is_empty():
        
        #there can only be on card in each column
        #and those cards can only be aces (rank == 1)
        #otherwise, False
        if len(tableau[0]) == 1:
        
            if tableau[0][0].rank() == 1:
                if tableau[1][0].rank() ==1 and len(tableau[1]) == 1:
                    if tableau[2][0].rank() == 1 and len(tableau[2]) == 1:
                        if tableau[3][0].rank() == 1 and len(tableau[3]) == 1:
                            print("You won!")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        return False

        
def main():
        
    '''
       This funciton follows the user inputs and displays the game
    '''
    
    #initilize game
    stock, tableau, foundation = init_game()
    print( MENU )
    display( stock, tableau, foundation )
    
    user_input = get_option()
    
    #stops loop when user wins
    #ask for option
    #display tableau, stock, and foundation
    while check_for_win(stock,tableau) == False:
        
        #if invalid input, ask again
        if user_input == None:
            print("Invalid option.")
            display( stock, tableau, foundation )
            user_input = get_option()
        
        #D adds cards to the tableau
        elif 'D' in user_input:
            deal_to_tableau( stock, tableau )
            display( stock, tableau, foundation )
            user_input = get_option()
        
        #F checks to see and moves card from tableau to foundation
        elif 'F' in user_input:
            move_to_foundation( tableau, foundation, user_input[1] )
            #if move causes win, then break
            if check_for_win(stock,tableau):
                break
            display( stock, tableau, foundation )
            user_input = get_option()
        
        #T moves cards within tableau
        elif 'T' in user_input:
            move_within_tableau( tableau, user_input[1], user_input[2] )
            if check_for_win(stock,tableau):
                break
            display( stock, tableau, foundation )
            user_input = get_option()
        
        #R restarts the game
        elif 'R' in user_input:
            stock, tableau, foundation = init_game()
            print('=========== Restarting: new game ============')
            print(RULES)
            print(MENU)
            display( stock, tableau, foundation )
            user_input = get_option()
        
        #H displays the menu
        elif 'H' in user_input:
            print( MENU )
            display( stock, tableau, foundation )
            user_input = get_option()
    
        #Q quits the game
        elif 'Q' in user_input:
            print('You have chosen to quit.')
            user_input = False
            break
        
        

if __name__ == "__main__":
    main()