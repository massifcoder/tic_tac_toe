import os

array = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def draw(arr):
  sum1=0
  sum2=0
  sum3=0
  sum4=0
  sum5=0
  sum6=0
  sum7=0
  sum8=0
  for x in range(0,len(arr)):
    sum1 = sum1+ ( 0 if arr[0][x] ==' ' else ( 1 if arr[0][x] == 'X' else 5 ) )
    sum2 = sum2+( 0 if arr[1][x] ==' ' else ( 1 if arr[1][x] == 'X' else 5 ) )
    sum3 = sum3+( 0 if arr[2][x] ==' ' else ( 1 if arr[2][x] == 'X' else 5 ) )
    sum4 = sum4+( 0 if arr[x][0] ==' ' else ( 1 if arr[x][0] == 'X' else 5 ) )
    sum5 = sum5+( 0 if arr[x][1] ==' ' else ( 1 if arr[x][1] == 'X' else 5 ) )
    sum6 = sum6+( 0 if arr[x][2] ==' ' else ( 1 if arr[x][2] == 'X' else 5 ) )
    sum7 = sum7+( 0 if arr[x][x] ==' ' else ( 1 if arr[x][x] == 'X' else 5 ) )
    sum8 = sum8+( 0 if arr[2-x][2-x] ==' ' else ( 1 if arr[2-x][2-x] == 'X' else 5 ) )
  if sum1==3 or sum1==15 or sum2==3 or sum2==15 or sum3==3 or sum3==15 or sum4==3 or sum4==15 or sum5==3 or sum5==15 or sum6==3 or sum6==15 or sum7==3 or sum7==15 or sum8==3 or sum8==15:
    return True
  return False

def change_user(user):
  if user == 1:
    return 2
  else:
    return 1

check=0
user = 2

while check ==0 :
  os.system('clear')
  user = change_user(user)
  print(f'Now turn is of user {user}\n\n')
  print(f'                 {array[0][0]} | {array[0][1]} | {array[0][2]} ')
  print('                ___|___|___')
  print('                   |   |   ')
  print(f'                 {array[1][0]} | {array[1][1]} | {array[1][2]} ')
  print('                ___|___|___')
  print('                   |   |   ')
  print(f'                 {array[2][0]} | {array[2][1]} | {array[2][2]} ')
  points = input('Choose the points to set your mark, eg for first row and second column type 12')
  if(user==1):
    to = array[int(points[0])][int(points[1])]
    if to == ' ':
      array[int(points[0])][int(points[1])]='X'
    else:
      print('You missed the turn!! You choose the wrong place.')
  else:
    toa =  array[int(points[0])][int(points[1])]
    if toa == ' ':
      array[int(points[0])][int(points[1])]='O'
    else:
      print('You missed the turn!! You choose the wrong place.')
  if draw(array) == True:
    os.system('clear')
    print(f'Congratulations!!! User {user} won the match.')
    print(f'\n\n\n        (▀̿Ĺ̯▀̿ ̿)      User {user}')
    print('      ༼ つ ◕_◕ ༽つ  You won')
    print('      (づ｡◕‿‿◕｡)づ')
    break
