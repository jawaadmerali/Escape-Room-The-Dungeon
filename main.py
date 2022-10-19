import random
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


#custom intro story 
print(f'A king asks you for your name.')
name = input('What is your name? ')
print(f'You do not remember anything but you woke up in a dark dungeon,    ahead of you are 3 doors. You realize that there is a maze behind the door and that you lose a life every time you guess. You have to escape and may get some hints {name}!')
door = input('Please choose a door (1, 2, or 3): ')

correct_door = random.choice(['1', '2', '3'])

while door!= correct_door:
  door = input('Nope, try again! 1, 2, or 3. ')

def puzzle():

  #custom message before seeing password list 

  options = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']

  correct_password = random.choice(options)
 
  for each_guess in options:
    if each_guess == correct_password:   
      print(each_guess.capitalize())
    else:
      print(each_guess)

  #custom message before asking for a guess

  password_guess = input('Choose the password from the list.\n ') 
 

  while password_guess != correct_password:
    print('Incorrect password. Try again. ')
    password_guess = input('Password: ')

  #success message
 
"""
room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'x...x',
  'xxxxx',
]
"""
#customize room layout 
room = [
  'xxxxxxexxxxxxx',
  'x..j.......pxx',
  'xxsxxxxxxxfxx',
]

def announce_walls(current_row, current_col):
  if room[current_row - 1][current_col] == 'x': #up
    print('There is a wall up. ')
  elif room[current_row + 1][current_col] == 'x': #down
    print('There is a wall down. ')
  elif room[current_row][current_col - 1] == 'x': #left
    print('There is a wall left. ')
  elif room[current_row][current_col + 1] == 'x': #right
    print('There is a wall right. ')
      
def move(current_row, current_col, direction):
  new_row = current_row
  new_col = current_col

  if direction == 'up':
    new_row -= 1
  elif direction == 'down':
    new_row += 1
  elif direction == 'left':
    new_col -= 1
  elif direction == 'right':
    new_col += 1
  else:
    print(f'You can not move {direction_choice}. Try up, down, left, or right')

  if room[new_row][new_col] == 'x': # Hit a wall!
    print('You can not move that way')
    return current_row, current_col

  if room[new_row][new_col] == 'j': # Hit a wall!
    print('You made it to a hint!! The escape is somewhere 1 row up ')
    return current_row, current_col
  
  if room[new_row][new_col] == 's': # Hit a wall!
    print('You made it to a hint!! The escape is somewhere 2 rows up')
    return current_row, current_col

  if room[new_row][new_col] == 'p': # Hit a wall!
    print('SUPER HINT: The escape is left 5 and up 1.')
    return current_row, current_col
  if room[new_row][new_col] == 'f': # Hit a wall!
    print('No hint for you!')
    return current_row, current_col
  
  return new_row, new_col

player_row = 1
player_col = 1

while room[player_row][player_col] != 'e':
  announce_walls(player_row, player_col)
  direction_choice = input('What direction would you like to move? ')
  player_row, player_col = move(player_row, player_col, direction_choice)
  print(f'New row is {player_row}')
  print(f'New col is {player_col}')

print('You escaped! ')
  

#customize to fit your theme!

