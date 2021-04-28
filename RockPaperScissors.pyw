from graphics import *
import random
def main():
    
    numOfRounds = getRounds()
    
    transcript = open("gameTranscript.txt", "a")
    transcript.writelines(["\n\n# of rounds: ", str(numOfRounds)])
    
    roundCount = 0
    playerPoints = 0
    cpuPoints = 0
    
    for i in range(numOfRounds):

        win = GraphWin("Rock-Paper-Scissors", 600, 600, autoflush = False)
        win.setCoords(0, 0, 6, 6)
        win.setBackground("cornflower blue")

        drawIntro(win)        

        #*** Indexes ***
        # 1 = Rock
        # 2 = Paper
        # 3 = Scissors
        
        playerIndex = getChoice(win)
        cpuIndex = getCPUchoice()
        
        transcript.writelines(["\n\nRound #", str(i + 1)])
        
        if(playerIndex == 1):
            pTranscript = "Rock"
        elif(playerIndex == 2):
            pTranscript = "Paper"
        else:
            pTranscript = "Scissors"
            
        if(cpuIndex == 1):
            cpuTranscript = "Rock"
        elif(cpuIndex == 2):
            cpuTranscript = "Paper"
        else:
            cpuTranscript = "Scissors"
        
        transcript.writelines(["\nPlayer: ", pTranscript])
        transcript.writelines(["\nCPU: ", cpuTranscript])

        clearSquares(win)

        cycleAnimation(win)

        drawChoices(playerIndex, cpuIndex, win)

        roundWinner = chooseWinner(playerIndex, cpuIndex, win)
        
        if(roundWinner == 2):
            pass
        elif(roundWinner == 1):
            playerPoints = playerPoints + 1
        else:
            cpuPoints = cpuPoints + 1
            
        scoreDisplay(playerPoints, cpuPoints, win)
            
        roundCount = roundCount + 1
        
        if(roundCount == numOfRounds):
            for k in range(10):
                update(15)
            exitAlert = Text(Point(3, 3), "Click again to exit!")
            exitAlert.setTextColor("white")
            exitAlert.setSize(24)
            exitAlert.draw(win)
            win.getMouse()
            transcript.close()

        win.close()
    

#********************************************************************************************************************************    
#**************************************************** Functions ***************************************************************** 
#********************************************************************************************************************************

def getRounds():
    initWindow = GraphWin("RockPaperScissors", 200, 200, autoflush = False)
    initWindow.setCoords(0, 0, 2, 2)
    initWindow.setBackground("gray")
    
    inputMessage = Text(Point(1, 1.5), "How many rounds do\n you want to play?:")
    inputMessage.setTextColor("white")
    inputMessage.setSize(12)
    inputMessage.draw(initWindow)
    
    roundsBox = Entry(Point(1, 1), 5)
    roundsBox.setText("1")
    roundsBox.draw(initWindow)
    
    enterButton = Rectangle(Point(0.7, 0.5), Point(1.3, 0.7))
    enterButton.setFill("white")
    enterButton.draw(initWindow)
    buttonText = Text(Point(1, 0.6), "Enter")
    buttonText.setSize(10)
    buttonText.draw(initWindow)
    
    initWindow.getMouse()
    rounds = int(roundsBox.getText())
    
    while(rounds <= 0):
        inputMessage.setText("Enter a number greater\n than 0!")
        initWindow.getMouse()
        rounds = int(roundsBox.getText())       
    
    initWindow.close()
    return rounds





                    
def drawIntro(windowName):
    icons = ["rockLarge.gif", "paperLarge.gif", "scissorsLarge.gif", "cpuScissors.gif", "cpuPaper.gif", "cpuRock.gif"]
    
    
    for i in range(3):
        choiceSquare = Rectangle(Point(0 + (i * 2), 0), Point(2 + (i * 2), 2))
        choiceIcons = Image(Point(1 + (i *2), 1), icons[i])
        choiceSquare.setOutline("black")
        choiceSquare.setFill("white")
        choiceSquare.draw(windowName)
        choiceIcons.draw(windowName)

        upperSquare = Rectangle(Point(0 + (i * 2), 4), Point(2 + (i * 2), 6))
        cpuIcons = Image(Point(1 + (i * 2), 5), icons[i + 3])
        upperSquare.setOutline("white")
        upperSquare.setFill("black")
        upperSquare.draw(windowName)   
        cpuIcons.draw(windowName)
        
        
        
        
        
def scoreDisplay(playerScore, cpuScore, windowName):
    playerLabel = Text(Point(0.5, 2.2), 'Player: ' + format(playerScore))
    playerLabel.setSize(20)
    playerLabel.setTextColor("lime")
    playerLabel.draw(windowName)
    
    compLabel = Text(Point(5.6, 3.7), 'CPU: ' + format(cpuScore))
    compLabel.setSize(20)
    compLabel.setTextColor("red")
    compLabel.draw(windowName)  
    
    for a in range(20):
        update(15)
    
    
    
    
    
    
def getChoice(windowName):
    alert = Text(Point(3, 3), "Make your Choice!")   
    alert.draw(windowName)
    
    playerChoice = windowName.getMouse() 
    
    while playerChoice.getY() > 2:
        alert.setText("Choose from the bottom squares!")
        playerChoice = windowName.getMouse() 
    
        
    if(playerChoice.getX() <= 2):
        alert.setText("You chose Rock!") #1
        for j in range(10):
            update(15)
        alert.undraw()
        return 1
    
    elif(playerChoice.getX() >= 2 and playerChoice.getX() <= 4):
        alert.setText("You chose Paper!") #2
        for j in range(10):
            update(15)
        alert.undraw()    
        return 2
    
    else:
        alert.setText("You chose Scissors!") #3
        for j in range(10):
            update(15)    
        alert.undraw()    
        return 3

    
    
    
    
    
def clearSquares(windowName):
    for i in range(3):
        playerSquare = Rectangle(Point(0 + (i * 2), 0), Point(2 + (i * 2), 2))
        playerSquare.setOutline("black")
        playerSquare.setFill("white")
        playerSquare.draw(windowName)
            
        cpuSquare = Rectangle(Point(0 + (i * 2), 4), Point(2 + (i * 2), 6))
        cpuSquare.setOutline("white")
        cpuSquare.setFill("black")
        cpuSquare.draw(windowName)
    
    
    
    
    
    
def cycleAnimation(windowName):
    rock = Image(Point(1, 1), "rockLarge.gif")
    paper = Image(Point(3, 1), "paperLarge.gif")
    scissors = Image(Point(5, 1), "scissorsLarge.gif")
    
    rock2 = Image(Point(5, 5), "cpuRock.gif")
    paper2 = Image(Point(3, 5), "cpuPaper.gif")
    scissors2 = Image(Point(1, 5), "cpuScissors.gif")
    
    for i in range(10):
        rock.draw(windowName)
        rock2.draw(windowName)
        update(15)
        rock.undraw()
        rock2.undraw()
        
        paper.draw(windowName)
        paper2.draw(windowName)
        update(15)
        paper.undraw()
        paper2.undraw()
        
        scissors.draw(windowName)
        scissors2.draw(windowName)
        update(15)
        scissors.undraw()
        scissors2.undraw()
        
        
        
        
        
        
def getCPUchoice(): 
    cpuChoice = random.randint(1, 30)
    
    if(cpuChoice % 3 == 0):
        return 3
    elif(cpuChoice % 2 == 0):
        return 2
    else:
        return 1


    
    
    

def chooseWinner(playerChoice, CPUchoice, windowName):
    
    winner = Text(Point(3, 3), "")
    winner.setTextColor("azure")
    winner.setSize(24)
    winner.draw(windowName)
    
    #*** Indexes ***
    # 1 = Rock
    # 2 = Paper
    # 3 = Scissors
    
    if(playerChoice == CPUchoice):
        winner.setText("It's a draw!")
        for j in range(20):
            update(15)
        winner.undraw() 
        return 2
        
    elif(playerChoice == 1 and CPUchoice == 2): #cpu(paper) beats player(rock)
        winner.setTextColor("red")
        winner.setText("CPU wins.")
        for j in range(20):
            update(15)
        winner.undraw() 
        return 0
        
    elif(playerChoice == 1 and CPUchoice == 3): #player(rock) beats cpu(scissors)
        winner.setTextColor("lime")
        winner.setText("Player wins!")
        for j in range(20):
            update(15)
        winner.undraw() 
        return 1
    
    elif(playerChoice == 2 and CPUchoice == 1): #player(paper) beats cpu(rock)
        winner.setTextColor("lime")
        winner.setText("Player wins!")
        for j in range(20):
            update(15)
        winner.undraw() 
        return 1
        
    elif(playerChoice == 2 and CPUchoice == 3): #cpu(scissors) beats cpu(paper)
        winner.setTextColor("red")
        winner.setText("CPU wins.")
        for j in range(20):
            update(15)
        winner.undraw()  
        return 0
        
    elif(playerChoice == 3 and CPUchoice == 1): #cpu(rock) beats player(scissors)
        winner.setTextColor("red")
        winner.setText("CPU wins.")
        for j in range(20):
            update(15)
        winner.undraw() 
        return 0
        
    elif(playerChoice == 3 and CPUchoice == 2): #player(scissors) beats cpu(paper)
        winner.setTextColor("lime")
        winner.setText("Player wins!")
        for j in range(20):
            update(15)
        winner.undraw() 
        return 1 
    
    
    
    
    
        
def drawChoices(playerChoice, CPUchoice, windowName):
    playerIcons = [Image(Point(1, 1), "rockLarge.gif"), Image(Point(3, 1), "paperLarge.gif"), Image(Point(5, 1), "scissorsLarge.gif")]
    
    cpuIcons = [Image(Point(5, 5), "cpuRock.gif"), Image(Point(3, 5), "cpuPaper.gif"), Image(Point(1, 5), "cpuScissors.gif")]
    
    playerIcons[playerChoice - 1].draw(windowName)
    cpuIcons[CPUchoice - 1].draw(windowName)
   

#*********************************************************************************************************************************    
 
main()