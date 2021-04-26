from entities.racer import racer
from functions.dataGame import saveData
import turtle 

#Esta funcion solo es con fines esteticos de la pantalla y su entorno   
def enviromentGame(goal):
    #Creacion de la ventana
    win_length = goal+200
    win_height = 500
    turtle.screensize(win_length, win_height)
    
    # Cambiar bg color
    turtle.bgcolor("grey")

    # Se crea el titulo de la carrera
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-100,250)
    turtle.write("Cars Race JC", font=("arial",30,"bold"))
    turtle.penup    

    # Se coloca tierra (solo con fines esteticos)
    turtle.setpos(-goal/2,-180)
    turtle.color("chocolate")
    turtle.speed(0)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(goal)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(goal)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()
    turtle.penup()

    # Se dibuja la linea de meta
    turtle.setpos(goal/2,150)
    turtle.color("yellow")
    turtle.speed(0)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()
    turtle.penup()
    turtle.hideturtle()

#Funcion que me imprime el ganador en la pantalla
def PrintWinner(user,color):
    turtle.color(color)
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-200,180)
    turtle.write("The winner is " + user + " with his " + color + " car", font=("arial",20,"bold"))
    turtle.penup    


#Metodo de ordenamiento con el fin de encontrar la posicion de los ganadores
def ordenPorBurbuja(lista):
    tamano=len(lista)
    ps = []
    for i in range(0,tamano):    
        ps.insert(i,i)
    for _ in range(0,tamano):
        for j in range(0,tamano-1):
            if lista[j]<lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                aux2 = ps[j]
                ps[j] = ps[j+1]
                ps[j+1] = aux2
    return(ps) 

#funcion que me da los kilometros que va a durar la carrera(El valor es dividido por 10 netamente por lo visual, esto no afecta la idea del juego)
def distanceLimit():
    state = True
    while(state):
        op = int(input("to start the game you must choose the track you want to play: \n 1. 5 km \n 2. 7 km \n 3. 8 km \n"))
        if op == 1:
            goal = 500
            state = False
        elif op == 2:
            goal = 700
            state = False
        elif op == 3:
            goal = 800
            state = False
        else:
            print("Invalid option, try again")
    return goal

#Funcion que posiciona los 3 carros y les da un conductor, un carril, y un nombre
def carsStart(goal):
    carList = []
    
    state = True
    while(state):
        players = int(input("How many players wants to play?, please select between 3 and 9 players: "))
        if players >= 3 and players <= 9:    
            state = False
        else:
            print("Invalid option, try again")  
    lane = 1
    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey'] 
    start = -50*(players-1)//2
    for p in range(players):
        name = input("Playername of " + colors[p] + " car: ")
        carList.append(racer(colors[p],(-goal/2, start), lane , name))
        lane = lane + 1
        start = start + 50
    return carList

#Funcion que me da el ganador del juego, y los tres que quedaron en el podio
def winnerGame(carList,goal):
    winner = [] 
    podio= []
    car = 1 
    for c in carList:
                print("{0}\t{1}m".format(c.color, (c.pos[0] + goal/2)*10))
                x = (c.pos[0] + goal/2)*10
                podio.insert(car,x)
                car += 1     
                if c.pos[0] >= goal/2:
                    winner.append(c.name)
                    winner.append(c.color)
    return podio,winner

#Esta funcion imprime los tres ganadores en la consola
def printWinnerConsole(carList,podio):
            winners = ordenPorBurbuja(podio)
            print('The first place is for ' + carList[winners[0]].name + " with his " + carList[winners[0]].color + " car")
            print('The second place is for ' + carList[winners[1]].name + " with his " + carList[winners[1]].color + " car")
            print('The third place is for ' + carList[winners[2]].name + " with his " + carList[winners[2]].color + " car")    
            return winners
        
def race(carList,goal):
    run = True
    while run:
        for c in carList:
            c.move()
        [podio, winner] = winnerGame(carList,goal) 
        if len(winner) > 0:
            w = printWinnerConsole(carList,podio) 
            run =False  
    return w

def resp(fp,sp,tp):
    print('First place: ',fp)
    print('Second place: ',sp)
    print('Third place: ',tp)
    file = open("data.txt","w")
    file.write('First place: ' + str(fp))
    file.write('Second place: ' + str(sp))
    file.write('Third place: ' + str(tp))
    file.close()   
 
def graphicDesign(goal):
    turtle.clearscreen()
    enviromentGame(goal)

#Funcion principal que correria el juego         
def startGame():
    goal = distanceLimit()
    graphicDesign(goal)
    carList = carsStart(goal)          
    w = race(carList,goal)
    fp = saveData(carList[w[0]],"cache\\firstPlace.txt")
    sp = saveData(carList[w[1]],"cache\\secondPlace.txt")
    tp = saveData(carList[w[2]],"cache\\thirdPlace.txt")
    resp(fp,sp,tp)
    PrintWinner(carList[w[0]].name,carList[w[0]].color)
    
