from graphics import *
import random


class GameRound:

    def __init__(self, windowName):
        self.windowName = "w"
        
        self.playerChoice = 1
        self.CPUchoice = 1

        self.playerScore = 0
        self.cpuScore = 0



    def getPlayerChoice(self):
        return self.playerChoice

    def getCPUchoice(self):
        return self.CPUchoice

    def getPlayerScore(self):
        return self.playerScore

    def getCPUscore(self):
        return self.cpuScore


    
    def drawIntro(self, windowName):
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



    def setPlayerChoice(self, windowName):
        alert = Text(Point(3, 3), "Make your Choice!")   
        alert.draw(windowName)

        playerClick = windowName.getMouse() 

        while playerClick.getY() > 2:
            alert.setText("Choose from the bottom squares!")
            playerClick = windowName.getMouse() 

    
        if(playerClick.getX() <= 2):
            alert.setText("You chose Rock!") #1
            for j in range(10):
                update(15)
            alert.undraw()
            self.playerChoice = 1
            

        elif(playerClick.getX() >= 2 and playerClick.getX() <= 4):
            alert.setText("You chose Paper!") #2
            for j in range(10):
                update(15)
            alert.undraw()
            self.playerChoice = 2
            

        else:
            alert.setText("You chose Scissors!") #3
            for j in range(10):
                update(15)    
            alert.undraw()
            self.playerChoice = 3

            

    def setCPUchoice(self): 
        cpuNum = random.randint(1, 30)

        if(cpuNum % 3 == 0):
            self.CPUchoice = 3
            
        elif(cpuNum % 2 == 0):
            self.CPUchoice = 2
            
        else:
            self.CPUchoice = 1



    def clearSquares(self, windowName):
        for i in range(3):
            playerSquare = Rectangle(Point(0 + (i * 2), 0), Point(2 + (i * 2), 2))
            playerSquare.setOutline("black")
            playerSquare.setFill("white")
            playerSquare.draw(windowName)

            cpuSquare = Rectangle(Point(0 + (i * 2), 4), Point(2 + (i * 2), 6))
            cpuSquare.setOutline("white")
            cpuSquare.setFill("black")
            cpuSquare.draw(windowName)



    def cycleAnimation(self, windowName):
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



    def drawChoices(self, windowName):
        playerIcons = [Image(Point(1, 1), "rockLarge.gif"), Image(Point(3, 1), "paperLarge.gif"), Image(Point(5, 1), "scissorsLarge.gif")]

        cpuIcons = [Image(Point(5, 5), "cpuRock.gif"), Image(Point(3, 5), "cpuPaper.gif"), Image(Point(1, 5), "cpuScissors.gif")]

        playerIcons[self.playerChoice - 1].draw(windowName)
        cpuIcons[self.CPUchoice - 1].draw(windowName)

            

    def chooseWinner(self, windowName):

        winner = Text(Point(3, 3), "")
        winner.setTextColor("azure")
        winner.setSize(24)
        winner.draw(windowName)

        #*** Indexes ***
        # 1 = Rock
        # 2 = Paper
        # 3 = Scissors

        if(self.playerChoice == self.CPUchoice):
            winner.setText("It's a draw!")
            for j in range(20):
                    update(15)
            winner.undraw() 

        elif(self.playerChoice == 1 and self.CPUchoice == 2): #cpu(paper) beats player(rock)
            winner.setTextColor("red")
            winner.setText("CPU wins.")
            for j in range(20):
                    update(15)
            winner.undraw()
            self.cpuScore = self.cpuScore + 1

        elif(self.playerChoice == 1 and self.CPUchoice == 3): #player(rock) beats cpu(scissors)
            winner.setTextColor("lime")
            winner.setText("Player wins!")
            for j in range(20):
                    update(15)
            winner.undraw()
            self.playerScore = self.playerScore + 1

        elif(self.playerChoice == 2 and self.CPUchoice == 1): #player(paper) beats cpu(rock)
            winner.setTextColor("lime")
            winner.setText("Player wins!")
            for j in range(20):
                    update(15)
            winner.undraw()
            self.playerScore = self.playerScore + 1

        elif(self.playerChoice == 2 and self.CPUchoice == 3): #cpu(scissors) beats player(paper)
            winner.setTextColor("red")
            winner.setText("CPU wins.")
            for j in range(20):
                    update(15)
            winner.undraw()
            self.cpuScore = self.cpuScore + 1

        elif(self.playerChoice == 3 and self.CPUchoice == 1): #cpu(rock) beats player(scissors)
            winner.setTextColor("red")
            winner.setText("CPU wins.")
            for j in range(20):
                    update(15)
            winner.undraw()
            self.cpuScore = self.cpuScore + 1

        elif(self.playerChoice == 3 and self.CPUchoice == 2): #player(scissors) beats cpu(paper)
            winner.setTextColor("lime")
            winner.setText("Player wins!")
            for j in range(20):
                    update(15)
            winner.undraw()
            self.playerScore = self.playerScore + 1



    def scoreDisplay(self, windowName):
        playerLabel = Text(Point(0.5, 2.2), 'Player: ' + format(self.playerScore))
        playerLabel.setSize(20)
        playerLabel.setTextColor("lime")
        playerLabel.draw(windowName)

        compLabel = Text(Point(5.6, 3.7), 'CPU: ' + format(self.cpuScore))
        compLabel.setSize(20)
        compLabel.setTextColor("red")
        compLabel.draw(windowName)  

        for a in range(30):
            update(15)

        playerLabel.undraw()
        compLabel.undraw()

#**********************************************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************************************

def main():
    
    numOfRounds = getRounds()
    
    transcript = open("gameTranscript.txt", "a")
    transcript.writelines(["\nNumber of rounds: ", str(numOfRounds)])

    win = GraphWin("Rock-Paper-Scissors", 600, 600, autoflush = False)
    win.setCoords(0, 0, 6, 6)
    win.setBackground("cornflower blue")

    RPSround = GameRound(win)
    roundCount = 0

    for i in range(numOfRounds):

        RPSround.drawIntro(win)

        RPSround.setPlayerChoice(win)

        RPSround.clearSquares(win)

        RPSround.setCPUchoice()

        RPSround.cycleAnimation(win)

        #******************************************************

        Pindex = RPSround.getPlayerChoice()

        Cindex = RPSround.getCPUchoice()

        #*** Indexes ***
        # 1 = Rock
        # 2 = Paper
        # 3 = Scissors

        transcript.writelines(["\n\nRound #", str(i + 1)])

        if(Pindex == 1):
            transcript.writelines("\nPlayer: Rock")
        elif(Pindex == 2):
            transcript.writelines("\nPlayer: Paper")
        else:
            transcript.writelines("\nPlayer: Scissors")
            
        if(Cindex == 1):
            transcript.writelines("\nCPU: Rock")
        elif(Cindex == 2):
            transcript.writelines("\nCPU: Paper")
        else:
            transcript.writelines("\nCPU: Scissors")

        #*****************************************************

        RPSround.drawChoices(win)

        RPSround.chooseWinner(win)

        RPSround.scoreDisplay(win)

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
    
#********************************************************************************************************************************************************************************************

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

#********************************************************************************************************************************************************************************************
 
main()
