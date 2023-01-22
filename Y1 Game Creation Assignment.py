#-----------------------------------------
#Mandy Tang Min Yee
#S10218941C | P09
#Programming 1 assignment (Final draft)
#-----------------------------------------
#Simp City Game
#Draft 7
#9 August 2021 11:15pm
#-----------------------------------------

#main menu
def main_menu():
    write_blank_game()
    print('Welcome, mayor of Simp City!')
    print('----------------------------')
    print('1. Start new game')
    print('2. Load saved game')
    print()
    print('0. Exit')

#get 2 random building to display
def choose_buildings():
    global building_list
    #get random no. to be the index of item u take frm the list
    index = random.randint(0, len(building_list) - 1)
    
    #label that building
    building1 = building_list.pop(index)

    #append it to the choice list
    choice_list.append(building1)

    #repeat for building 2
    index = random.randint(0, len(building_list) - 1)
    building2 = building_list.pop(index)
    choice_list.append(building2)

#show game
def show_game():
    print()
    
    global board, turn

    #see if game end alr or not
    if turn <=16:
        print('Turn', turn)
    
    else:
        print('Final layout of Simp City:')

    #print out board decor thingie, so it looks like an actual board
    print('    A     B     C     D')
    print(' +-----+-----+-----+-----+')

    for row in range(1, 5):
        print('{}'.format(row), end = '')

        for column in range(1, 5):
            print('| {:3} '.format(board[row][column]), end = '')

        print('|')

        print(' +-----+-----+-----+-----+')


#show game menu (the choices u can make when playing the game)
def game_menu():
    print('1. Build a {}'.format(choice_list[0]))
    print('2. Build a {}'.format(choice_list[1]))
    print('3. See remaining buildings')
    print('4. See current score')
    print('5. Save game')
    print()
    print('0. Exit to main menu')
    
#start a new game
def new_game():
    global turn, building_list
    quit = False
    while not quit:
        #choose buildings to put in the choice list to choose frm later
        choose_buildings()

        #print out game board thing
        show_game()

        #while the turn is equal/less than 16, i.e. game nvr end
        if turn <= 16:
            
            #show the game choices menu, cause technically u still playing game
            game_menu()

            #choose what u wanna do
            choice = input('Your choice?')

            #when u not choosing the location to put stuff down, return the taken buildings frm the choose list to the building list
            #if not that means pool size decrease even tho u nvr play anything, personally i'll feel pissed if im the one playing
            if choice != '1' and choice!= '2':
                building_list.append(choice_list[0])
                building_list.append(choice_list[1])
                choice_list.clear()
                
            #if building 1 is chosen
            if choice == '1':
                location = input('enter the location')

                #check if location is letter-number combo
                if len(location) == 2 and location[0].isalpha() and location[1].isdigit():
                    
                    row = int(location[1])
                    col = ord((location[0]).upper()) - ord('A') + 1

                    #check if location is within the board size
                    if col in range(1, len(board[0]) - 1) and row in range(1, len(board) - 1):

                        #check see if you are over-riding any buildings
                        #i think can be removed if wanted
                        if board[row][col] == '   ':

                            #check if its adjacent any building
                            if turn != 1 and ((col != (len(board[0]) - 1) and row != (len(board) - 1) and board[row][col + 1] == '   ' and board[row][col - 1] == '   ' and board[row + 1][col] == '   ' and board[row - 1][col] == '   ')):
                                building_list.append(choice_list[0])
                                building_list.append(choice_list[1])
                                choice_list.clear()
                                print()
                                print('Invalid input.')
                                print('Please check if you are building next to an existing building.')

                            #if all ok, then place
                            else:
                                board[row][col] = choice_list[0]
                                building_list.append(choice_list[1])
                                building_left[choice_list[0]] -=1
                                choice_list.clear()
                                turn += 1
                                
                        #error msg for over-ride building, can remove with some changes  
                        else:
                            building_list.append(choice_list[0])
                            building_list.append(choice_list[1])
                            choice_list.clear()
                            print()
                            print('Invalid input.')
                            print('Please check if you are building on an empty plot.')
                            
                    else:
                        building_list.append(choice_list[0])
                        building_list.append(choice_list[1])
                        choice_list.clear()
                        print()
                        print('Invalid input.')
                        print('Please check if your input contains only 1 letter and 1 number within the parameters of the board.')
                    
                else:
                    building_list.append(choice_list[0])
                    building_list.append(choice_list[1])
                    choice_list.clear()
                    print()
                    print('Invalid input.')
                    print('Please check if your input is a letter-number combo. e.g. A2')

            #repeat frm 1
            elif choice == '2':
                location = input('enter the location')
                
                if len(location) == 2 and location[0].isalpha() and location[1].isdigit():
                    
                    row = int(location[1])
                    col = ord((location[0]).upper()) - ord('A') + 1

                    if col in range(1, len(board[0])) and row in range(1, len(board)):

                        if board[row][col] == '   ':
                            
                            if turn != 1 and ((col != (len(board[0]) - 1) and row != (len(board) - 1) and board[row][col + 1] == '   ' and board[row][col - 1] == '   ' and board[row + 1][col] == '   ' and board[row - 1][col] == '   ')):
                                building_list.append(choice_list[0])
                                building_list.append(choice_list[1])
                                choice_list.clear()
                                print()
                                print('Invalid input.')
                                print('Please check if you are building next to an existing building.')

                            else:
                                board[row][col] = choice_list[1]
                                building_list.append(choice_list[0])
                                building_left[choice_list[1]] -=1
                                choice_list.clear()
                                turn += 1
                        else:
                            building_list.append(choice_list[0])
                            building_list.append(choice_list[1])
                            choice_list.clear()
                            print()
                            print('Invalid input.')
                            print('Please check if you are building on an empty plot.')
                    else:
                        building_list.append(choice_list[0])
                        building_list.append(choice_list[1])
                        choice_list.clear()
                        print()
                        print('Invalid input.')
                        print('Please check if your input contains only 1 letter and 1 number within the parameters of the board.')
                    
                else:
                    building_list.append(choice_list[0])
                    building_list.append(choice_list[1])
                    choice_list.clear()
                    print()
                    print('Invalid input.')
                    print('Please check if your input is a letter-number combo. e.g. A2')

            #if choice is 3, print remaining buildings in the pool
            elif choice == '3':
                print()
                print('--------------------')
                print('remaining buildings')
                print('--------------------')
                for key, value in building_left.items():
                    print('{:4}: {}'.format(key, value))

                print('--------------------')
                print()

            #if choice is 4, show current score
            elif choice == '4':
                total_score()

            #if choice is 5, save game
            elif choice == '5':
                save_game()
                
                
            #if choice is 0, exit to main menu
            elif choice == '0':

                #ask if they wanna save game first
                #cause i think if u leave and forget to save accidentally, its abit sad
                save_exit_choice = input('Do you want to save your game? (Y/N)')
                save_exit_choice = save_exit_choice.upper()

                #yes save game
                if save_exit_choice == 'Y':
                    print()
                    save_game()
                    print('Quiting to main menu...')
                    print()
                    

                #no then break out to main menu
                elif save_exit_choice == 'N':
                    print()
                    print('Quiting to main menu...')
                    print()
                    print()

                else:
                    print('Invalid input')
                    
                #the main menu loop thing
                break

            #error msg to check if the choices they choose when playing the game is correct or not
            else:
                print('Invalid input')
                print('Please check if your choice is a single digit')
                print('and that it is part of the given choices.')

        #this is when the turn is more than 16, meaning game end. it auto quits to main menu
        else:
            total_score()

            print()
            print()
            print('End of game')
            print('Thanks for playing!')
            print('Quiting to main menu...')
            print()
            print()
            quit = True

#counts and displays total score
def total_score():
    bch_score()
    fac_score()
    hse_score()
    shp_score()
    hwy_score()

    #total score menu header thing
    print()
    print('-----------')
    print('Total Score')
    print('-----------')
    
    #list to put total scores of all areas
    total_list = []
    
    #make list of appended score in the 'value' area of the key
    for key in building_score:
        score_list = building_score[key]

        #header for score calc at the back
        print(key, end=' : ')

        #here to give a base starting + make the thing look nice + ensure no format errors
        score = '0'
        
        #for each item in the score list, searched via index thing,
        #string "adding" giving a '0, frm above score, + etc'
        for score_index in range(0, len(score_list)):
            score = score + ' + {}'.format(score_list[score_index])

        #print the thingie out to make the addition line thing
        print(score, '=', sum(score_list))
        
        #append the sum of the 1 item in the dict calculated here, to total list, to calc total
        total_list.append(sum(score_list))
        t_score = sum(total_list)
    #formatting + calc out total score
    print('Total score: {}'.format(t_score))

    #buffer line
    print()

#count score of bch
def bch_score():
    for row in range(1, len(board)):

        for col in range(1, len(board[0])):

            #check if bch in col A or col D
            #if yes, give 3 pts per beach
            #if not, give 1 pt per beach
            #procede to append score to dict of scores
            if 'BCH' in board[row][col]:
                if col == 1 or col == 4:
                  building_score['BCH'].append(3)

                else:
                  building_score['BCH'].append(1)

#count score of fac      
def fac_score():
    
    #counts total no. of fac in the coard
    #if the count is 0, fac score is 0
    if ((board[1].count('FAC')) + (board[2].count('FAC')) + (board[3].count('FAC')) + (board[4].count('FAC'))) == 0:
        building_score['FAC'].append(0)

    #if the count is less/equal to 4, appends the count no as the score to the dict
    #score is appended as many times as the no. of fac count here
    #for loop is used to do so
    elif ((board[1].count('FAC')) + (board[2].count('FAC')) + (board[3].count('FAC')) + (board[4].count('FAC'))) <= 4:
        for i in range(1, ((board[1].count('FAC')) + (board[2].count('FAC')) + (board[3].count('FAC')) + (board[4].count('FAC')) + 1)):
            building_score['FAC'].append(((board[1].count('FAC')) + (board[2].count('FAC')) + (board[3].count('FAC')) + (board[4].count('FAC'))))

    #if count is else
    #aka not 0
    #aka not less than/equal to 4
    #aka more than 4
    #using for loop, 4 is appended 4 times, then 1 is appended as many times as the remaining fac after u -4 frm the total
       
    else:
        for x in range(1, 5):
            building_score['FAC'].append(4)

        for y in range(1, (((board[1].count('FAC')) + (board[2].count('FAC')) + (board[3].count('FAC')) + (board[4].count('FAC'))) - 4) + 1):
            building_score['FAC'].append(1)
                
#count score for hse
def hse_score():            
  for row in range(1, len(board)):
    for col in range(1, len(board[0])):
        if board[row][col] == 'HSE':

            #first assign variables to count no. of buildings beside
            h_bch = 0
            h_shp = 0
            h_hse = 0

            #list of adj buildings
            adj_list = []

            #append building adj to the hse
            adj_list.append(board[row + 1][col])
            adj_list.append(board[row - 1][col])
            adj_list.append(board[row][col + 1])
            adj_list.append(board[row][col - 1])

            #remove '   ' to avoid errors later on
            if '   ' in adj_list:
                adj_list.remove('   ')

            #check if fac is adj to a hse
            #if yes, give the hse 1 pt
            if 'FAC' in adj_list:
                building_score['HSE'].append(1)
                
            #for each item in the adj list
            #check what item it is
            #then add score accordingly
            #+2 per bch
            #+1 per shp/hse
            else:
                for b in adj_list:
                    
                    if b == 'BCH':
                        h_bch += 2

                    if b == 'SHP':
                        h_shp += 1

                    if b == 'HSE':
                        h_hse += 1
                        
                #add up the scores and append it to dict
                h_score = h_bch + h_shp + h_hse
                building_score['HSE'].append(h_score)
                        
#count score for shp
def shp_score():            
  for row in range(1, len(board)):
    for col in range(1, len(board[0])):
        if board[row][col] == 'SHP':

            #same as hse, assign variables per building type
            #and adj list etc
            s_bch = 0
            s_fac = 0
            s_hse = 0
            s_shp = 0
            s_hwy = 0

            adj_list = []
            
            adj_list.append(board[row + 1][col])
            adj_list.append(board[row - 1][col])
            adj_list.append(board[row][col + 1])
            adj_list.append(board[row][col - 1])

            if '   ' in adj_list:
                adj_list.remove('   ')

            for b in adj_list:
                    
                if b == 'BCH':
                    s_bch += 1

                if b == 'FAC':
                    s_fac += 1

                if b == 'HSE':
                    s_hse += 1

                if b == 'SHP':
                    s_shp += 1

                if b == 'HWY':
                    s_hwy += 1
                    
            #since its +1 pt per UNIQUE building adj to it
            #if the count above it more than 1, make it into 1
            #this is the score thing
            if s_bch >= 1:
                s_bch = 1

            if s_fac >= 1:
                s_fac = 1

            if s_hse >= 1:
                s_hse = 1

            if s_shp >= 1:
                s_shp = 1

            if s_hwy >= 1:
                s_hwy = 1

            #shp score is the addition of presence of
            #all unique buildings present in adj list
            #add up score and append to dict
            s_score = s_bch + s_fac + s_hse + s_shp + s_hwy
            building_score['SHP'].append(s_score)

#count hwy score
def hwy_score():            
  for row in range(1, len(board)):
    for col in range(1, len(board[0])):
        if board[row][col] == 'HWY':

            #building to left is hwy
            #skip cause counted alr
            if board[row][col - 1] == 'HWY':
                continue

            score = 0

            #check if next col (the tile next to it) is a hwy
            #if yes, score + 1pt cause hwy 1 tile score depend on the linking
            while board[row][col] == 'HWY':
                score += 1
                col += 1

            #for each tile in the range of the score,
            #append the score per tile
            for squares in range(score):
                building_score['HWY'].append(score)

#menu loop, to satisfy the exit frm game thing
#where if u press 0, exit to main menu, not entirely stop game
def main_option():
    
    #constantly running as loop, until exit
    while True:
        main_menu()
        opt = (input('Enter your choice'))

        #if option is 1, start new game
        if opt == '1':

            #ask user if they wanna check for a previous save file
            print('You may have a previously saved game')
            load = input('Do you wish to load it? (Y/N)')

            #check if they want load,
            #if load is yes, Y,
            #then try to open the text file
            #however, if there is no file and it returns an error
            #say got no save file
            #then start new game
            load = load.upper()
            if load =='Y':
                
                try:
                    open('game.txt', 'r')
                    load_game()

                except FileNotFoundError:
                    print('No saved game found')
                    print()
                    print('Starting new game')
                    print()

            #if no
            #write a blank game file
            #and load it
            elif load == 'N':
                write_blank_game()
                load_blank_game()

            new_game()

        #if option is 2, load saved game
        #then start game
        #error exception as seen above
        elif opt == '2':
            
            try:
                open('game.txt', 'r')
                load_game()
                new_game()

            except FileNotFoundError:
                print('No saved game found')
                print()
                print('Starting new game')
                print()
                new_game()

        #if option is 0, exit game
        elif opt == '0':

            #ask for sure, just in case
            sure = str(input('Are you sure you want to quit? (Y/N)'))

            sure = sure.upper()
            
            if sure == 'Y':
                break

            #if input neither Y or N, for exit
            #give error
            elif sure != 'Y' and sure != 'N':
                print('Invalid input')
                
            #buffer line
            print()

        #if input for main menu choice is not 1, 2, or 0
        #give error
        else:
            print('Invalid input.')

#function to save game
#all items ONLY seperated by comma (',')
def save_game():
    file = open('game.txt', 'w')

    #read and save turn as string
    file.write(str(turn) + '\n')

    #read and save board as items, no fancy stuff inside
    #format as a 6x6 save thing
    #board size is 6x6
    for row in range(0, len(board)):
        data = ""
        for col in range(0, len(board[0])):
            data = data + board[row][col] + ','
        file.write(data + '\n')

    #similar to board, save remaing building list/pool thing
    #as a list seperated by commas
    #no need formatting unlike board
    b_data = ''

    for b in building_list:
        b_data = b_data + b + ','

    file.write(b_data + '\n')

    #save building left dictionary as a string
    #formatted like this
    # 'item1,item1 value,item2,item2 value, etcetc
    #easier to count later
    r_data = ''
    for r in building_left:
        r_data = r_data + r + ',' + str(building_left[r]) + ','
    file.write(r_data + '\n')


    file.close()
    print()
    print('Game saved!')

#function to load game
def load_game():
    print()
    print('Loading Game...')
    print()

    #say turn is global
    #read 1st line, which is turn no.
    #convert line frm str to int
    #assign turn as the line inside
    global turn
    file = open("game.txt", "r")

    turn = int(file.readline())

    #for ech line in file
    #convert to a list
    row = 0
    for line in file:
        line = line.strip("\n")
        data_list = line.split(",")

        #each item in data list is now only datalist[a]
        #col is shared between both so
        #datalist[a] is now board[0][a], assuming row is 0
        #once col == last col no in board, aka 5, in my case
        for col in range(0, len(board)):
            board[row][col] = data_list[col]

        #then row +1, so that u get nested list
        row += 1

        #check if the no of rows is equal length of board, 6 for me,
        #if yes, stop the loop
        if row == len(board):
            break

    #next lines
    line = file.readline().strip("\n")

    #make building_list to become global so
    #it can be changed to the saved building list
    #because function choose_buildings() is dependant on this factor
    #so it cannot be diff
    global building_list

    #make building list = a list made frm the string, but split by the commas
    building_list = line.split(",")

    #remove the ending ('') which was once a comma but now is split
    building_list.remove('')

    #explanation same as building list
    #for the nxt 3 lines
    line = file.readline().strip("\n")
    
    temp_list = line.split(",")

    temp_list.remove('')

    #left side of eqn below
    #list is split to [item1, value1, item2, value2]
    #every even index item in list
    #set as the building left dict key, or more like find it inside there
    #then jump then odd index and repeat

    #right side of eqn below
    #convert the item + 1,
    #aka the odd index,
    #aka the value of the even index infront of it,
    #to become the the item and convert to int and whack it inside
    for item in range(0, len(temp_list), 2):
        building_left[temp_list[item]] = int(temp_list[item + 1])
    
    file.close()

#used to write a blank game map to overwrite the problem
#where if u load game then exit then start new game
#u get the save file instead of a blank game
def write_blank_game():
    file = open('blankgame.txt', 'w')

    file.write('1' + '\n')
    file.write('   ,   ,   ,   ,   ,   ,' + '\n')
    file.write('   ,   ,   ,   ,   ,   ,' + '\n')
    file.write('   ,   ,   ,   ,   ,   ,' + '\n')
    file.write('   ,   ,   ,   ,   ,   ,' + '\n')
    file.write('   ,   ,   ,   ,   ,   ,' + '\n')
    file.write('   ,   ,   ,   ,   ,   ,' + '\n')
    file.write('BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,BCH,FAC,HSE,SHP,HWY,' + '\n')
    file.write('BCH,8,FAC,8,HSE,8,SHP,8,HWY,8,' + '\n')
    file.close()

#used to load the blank game file
def load_blank_game():
    print()
    print('Loading Game...')
    print()

    #say turn is global
    #read 1st line, which is turn no.
    #convert line frm str to int
    #assign turn as the line inside
    global turn
    file = open("blankgame.txt", "r")

    turn = int(file.readline())

    #for ech line in file
    #convert to a list
    row = 0
    for line in file:
        line = line.strip("\n")
        data_list = line.split(",")

        #each item in data list is now only datalist[a]
        #col is shared between both so
        #datalist[a] is now board[0][a], assuming row is 0
        #once col == last col no in board, aka 5, in my case
        for col in range(0, len(board)):
            board[row][col] = data_list[col]

        #then row +1, so that u get nested list
        row += 1

        #check if the no of rows is equal length of board, 6 for me,
        #if yes, stop the loop
        if row == len(board):
            break

    #next lines
    line = file.readline().strip("\n")

    #make building_list to become global so
    #it can be changed to the saved building list
    #because function choose_buildings() is dependant on this factor
    #so it cannot be diff
    global building_list

    #make building list = a list made frm the string, but split by the commas
    building_list = line.split(",")

    #remove the ending ('') which was once a comma but now is split
    building_list.remove('')

    #explanation same as building list
    #for the nxt 3 lines
    line = file.readline().strip("\n")
    
    temp_list = line.split(",")

    temp_list.remove('')

    #left side of eqn below
    #list is split to [item1, value1, item2, value2]
    #every even index item in list
    #set as the building left dict key, or more like find it inside there
    #then jump then odd index and repeat

    #right side of eqn below
    #convert the item + 1,
    #aka the odd index,
    #aka the value of the even index infront of it,
    #to become the the item and convert to int and whack it inside
    for item in range(0, len(temp_list), 2):
        building_left[temp_list[item]] = int(temp_list[item + 1])
    
    file.close()
#--------------------------------------------------------------------------
#for the choose_buildings() function
import random

#gameboard (global)
board = [['   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ']]


#turn number (global)
turn = 1

#list of 40 buildings (global)
building_list = ['BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY',
                 'BCH', 'FAC', 'HSE', 'SHP', 'HWY']

#dictionary of no. of buildings left
building_left = {'BCH' : 8,
                 'FAC' : 8,
                 'HSE' : 8,
                 'SHP' : 8,
                 'HWY' : 8}

#list to pop into to choose for the 2 random buildings to build
choice_list = []

#dictionary of scores of buildings
building_score = {'BCH' : [],
                  'FAC' : [],
                  'HSE' : [],
                  'SHP' : [],
                  'HWY' : []}
#---------------------------------------------------------------------------

#start game (loop thingie)
main_option()

    
