from functions.tools import startGame
from functions.dataGame import clearData
clearData()
#La carrera inicia
while True:
    print('-----------------------------------')
    start = input('WELCOME AGAIN, Press any button to continue')
    startGame()