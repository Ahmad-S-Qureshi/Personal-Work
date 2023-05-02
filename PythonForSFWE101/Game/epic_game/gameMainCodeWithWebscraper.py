import pygame
from pygame.locals import *
from random import randrange, choice
from datetime import datetime
from os import listdir, path, curdir, remove
from time import sleep
from threading import Thread
from webscraper import get_images
from PIL import Image

def main():
    # Grabs pictures for use as the enemy
    imageGrabber = Thread(target=get_images, daemon=True)
    imageGrabber.start()
    while(len(listdir(path.join(curdir, "images")))<1):
        sleep(0.5)

    # Initialise screen and display game name
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Triple Letter Speed')
    
    # Fill background with plain color
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((30, 30, 30))

    # Prepare opening text
    font = pygame.font.Font(None, 36)
    drawInstructions(background, font, screen)
    drawCenteredText("Press the A key to begin", background, font, screen.get_size()[1]-80, screen)

    # Prepare rectangle for playerhealth
    playerHealthPos = Rect(30, 30, 30, screen.get_size()[1]//255*255)
    playerHealthColor = [0, 0, 255]
    BASEPLAYERPOS = Rect(30, 30, 30, screen.get_size()[1]//255*255)
    BACKGROUNDCOLOR = (0,0,20)

    #Prepares for random image enemies
    imageSurface = pygame.Surface((screen.get_size()[0]//2, screen.get_size()[1]//2))

    # Prepare rectangle for enemy health
    enemyHealthPos = Rect(screen.get_size()[0]-60, 30, 30, screen.get_size()[1]//255*255)
    enemyHealthColor = [0, 0, 255]
    BASEENEMYPOS = Rect(screen.get_size()[0]-60, 30, 30, screen.get_size()[1]//255*255)

    # Display everything for the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    pygame.key.set_repeat()

    # Prepares Starting configuration of variables for gameplay
    opening = True
    lettersPressed = resetPressed()
    turnPassed = True
    turnStartTime = datetime.now().timestamp()
    gameGoing = True
    score = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            
            # Handles closing the window and removes all downloaded images
            if event.type == QUIT:
                for file in listdir(path.join(curdir, "images")):
                    remove(path.join(curdir, "images", file))
                return
            if event.type == KEYDOWN and gameGoing:
                keyboardState = pygame.key.get_pressed()
                # Closes game if user hits delete (Developmental Artifact)
                if(keyboardState[127]):
                    return
                # Runs on the first button press and sets up the background and whatnot, also changes the flag of opening to false
                elif(opening and keyboardState[65+32]):
                    
                    # Resets everything and sets letters to some random ones
                    letters = grandReset(background, BACKGROUNDCOLOR, screen, font, opening, imageSurface)
                    
                    # Sets game running booleans
                    opening = False
                    gameGoing = True

                    # Initializes time between turns (hard-coded at 3 seconds)
                    timeBetweenTurns = 3

                    # Sets all starting colors to 
                    playerHealthColor = [0,0,255]
                    enemyHealthColor = [0,0,255]

                    # Stores starting time for later use and for use between turns
                    turnStartTime = datetime.now().timestamp()

                    # Sets score to zero for start
                    score = 0
                    
                    # Runs code for turn resetting 
                    letters = turnReset(background, screen, font, BACKGROUNDCOLOR)
                    pygame.display.flip()
                    
                # Updates Health Values based on button pressed and strikes-through letters when pressed
                elif(not opening):
                    if(not(letters[0] == " ")):

                        # Checks if input is the first letter
                        if(keyboardState[ord(letters[0])+32] and (not(lettersPressed[0]))):
                            onLetterPress(lettersPressed, 1, background, screen, font)

                        # Checks if input is the second letter
                        elif(keyboardState[ord(letters[1])+32] and (not(lettersPressed[1]))):
                            onLetterPress(lettersPressed, 2, background, screen, font)

                        # Checks if input is the third letter
                        elif(keyboardState[ord(letters[2])+32] and (not(lettersPressed[2]))):
                            onLetterPress(lettersPressed, 3, background, screen, font)

                    # Displays a flag to the user that the turn has failed (NYI)
                    else:
                        turnPassed = False
                        FailedSymbol = font.render("Turn Failed", 9, (255, 30, 30))
                        FailedSymbolPos = Rect(screen.get_width()/2-60, screen.get_height()-122, 30, 40)
                        background.blit(FailedSymbol, FailedSymbolPos)
                        screen.blit(background, (0,0))
                        pygame.display.flip()
                                  
        # Waits for the delay between moves to elapse and updates time before the next attack
        if(not(opening) and (gameGoing)):
            # Runs after turn timer
            if(turnStartTime + timeBetweenTurns < datetime.now().timestamp()):

                # Performs Turn, takes health from user if turn was failed and takes enemy health otherwise
                if(lettersPressed[0] and lettersPressed[1] and lettersPressed[2] and turnPassed):
                    if(enemyHealthColor[2]-40 >0):
                        enemyHealthPos = updateHealth(screen, background, enemyHealthPos, 40, BACKGROUNDCOLOR, screen.get_size()[1])
                        pygame.draw.rect(background, BACKGROUNDCOLOR, BASEENEMYPOS)
                        enemyHealthColor = [enemyHealthColor[0]+40, 0, enemyHealthColor[2]-40]

                    # If enemy health is gone, resets enemy
                    else: 
                        enemyHealthPos = Rect(screen.get_size()[0]-60, 30, 30, screen.get_size()[1]//255*255)
                        enemyHealthColor = [0, 0, 255]
                        timeBetweenTurns = timeBetweenTurns * 0.85
                        drawEnemy(background, screen, BACKGROUNDCOLOR, imageSurface)

                    # Updates enemy health bar whether or not they were reset and draws to screen
                    pygame.draw.rect(background, enemyHealthColor, enemyHealthPos)
                    score = score + 1
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
                    
                else:

                    # Takes user health if turn was failed
                    if(playerHealthColor[2] - 15 > 0): 
                        playerHealthPos = updateHealth(screen, background, playerHealthPos, 15, BACKGROUNDCOLOR, screen.get_size()[1])
                        playerHealthColor = [playerHealthColor[0]+15, 0, playerHealthColor[2]-15]
                        pygame.draw.rect(background, BACKGROUNDCOLOR, BASEPLAYERPOS)
                        pygame.draw.rect(background, playerHealthColor, playerHealthPos)
                        
                        # Resets turn failed flag if a turn has been failed at this point, display no mess up yet otherwise
                        try:
                            FailedSymbol.fill(BACKGROUNDCOLOR)
                            background.blit(FailedSymbol, FailedSymbolPos)
                        except: 
                            print("No mess up yet")
                        screen.blit(background, (0,0))
                        pygame.display.flip()

                    #Displays end screen if user health has completely drained
                    else: 
                        background.fill((30, 30, 30))
                        gameGoing = False
                        drawInstructions(background, font, screen)

                        # Tells the user how to play again
                        drawCenteredText("Your score was " +str(score) +" press A to play again", background, font, screen.get_size()[1]-80, screen)
                        screen.blit(background, (0, 0))
                        pygame.display.flip()

                if(gameGoing):
                    # Resets Screen Between turns once health has been updated for both parties also resets the list of letters pressed and the turnPassed flag
                    letters = turnReset(background, screen, font, BACKGROUNDCOLOR)
                    lettersPressed = resetPressed()
                    # Resets fail symbol
                    try:
                        FailedSymbol.fill(BACKGROUNDCOLOR)
                        background.blit(FailedSymbol, FailedSymbolPos)
                    except: 
                        print("No mess up yet")

                    # Resets flags and booleans for between turns
                    pygame.display.flip()
                    turnStartTime = datetime.now().timestamp()
                    turnPassed = True

        # Runs reset feature if A is pressed on game over screen
        elif((not gameGoing)): 
            # Grabs all pressed letters
            keyboardState = pygame.key.get_pressed()

            # Checks for letter A
            if(keyboardState[65+32]):
                # Resets letters
                letters = updateLetters()

                # Resets all variables and screen
                letters = grandReset(background, BACKGROUNDCOLOR, screen, font, opening, imageSurface)

                # Resets health
                playerHealthColor = [0,0,270]

                # Updates boolean to say game is going
                gameGoing = True

                # Resets turn timer
                timeBetweenTurns = 3
                turnStartTime = datetime.now().timestamp()

                # Resets score
                score = 0

                # Resets player and enemy health
                playerHealthPos.height = screen.get_size()[1]//255*255
                enemyHealthPos.height = screen.get_size()[1]//255*255
                playerHealthColor = [0,0,255]
                enemyHealthColor = [0,0,255]

                # Updates the screen
                pygame.display.flip()

# Returns the inputted box but shorter to account for damage 
def updateHealth(background, surface, box, change, color, screenHeight):
    temp = Rect(box.left, box.top, box.w, box.h-change*(screenHeight//255))
    pygame.draw.rect(background, color, box)
    background.blit(surface, temp)
    return temp

# Returns health completely restored for next enemy or consecutive runs of player
def resetHealth(background, surface, box, screenHeight):
    temp = Rect(box.left, box.top, box.w, (screenHeight//255*255))
    pygame.draw.rect(background, [0, 0, 255], box)
    background.blit(surface, temp)
    return temp

# Returns a new set of random letters
def updateLetters():
    # temp array to hold letters
    temp = [" ", " ", " "]

    # Each position in array is updated
    temp[0] = chr(randrange(65, 91))
    temp[1] = chr(randrange(65, 91))
    temp[2] = chr(randrange(65, 91))

    # returns temp array
    return temp  

# Resets values and dispalys new letters for new turn
def turnReset(background, screen, font, BACKGROUNDCOLOR):
    # Covers the last tuen
    drawBottomTextCover(background, screen, BACKGROUNDCOLOR)

    # Updates letters and displays the new letters to print
    letters = updateLetters()
    drawCenteredText("Press the " + letters[0] + " " + letters[1] + " " + letters[2] + " keys", background, font, screen.get_size()[1]-80, screen)

    # blits everything to screen
    screen.blit(background, (0, 0))

    # Returns the letters for future use
    return letters

# Resets pressed keys
def resetPressed():
    return [False, False, False]

# Resets when new game is started, displaying text and a quick "wait" for the next turn
def grandReset(background, BACKGROUNDCOLOR, screen, font, opening, imageSurface):
    # Covers screen in background color
    background.fill(BACKGROUNDCOLOR)

    # Draws enemy for future use
    drawEnemy(background, screen, BACKGROUNDCOLOR, imageSurface)

    # Draws enemy and player health (the //255 is to ensure that the size is divisible by 255 for all screen sizes)
    playerHealthPos = Rect(30, 30, 30, screen.get_size()[1]//255*255)
    enemyHealthPos = Rect(screen.get_size()[0]-60, 30, 30, screen.get_size()[1]//255*255)

    # Draws health bars
    pygame.draw.rect(background, ((0, 0, 255)), playerHealthPos)
    pygame.draw.rect(background, (0, 0, 255), enemyHealthPos)

    # Draws text for health bars
    drawText("Player Health", background, font, 60, screen.get_size()[1]/2 - 100, screen)
    drawText("Enemy Health", background, font, screen.get_size()[0]-250, screen.get_size()[1]/2 - 100, screen)

    # Displays to the user to eait for the game to load
    if(not opening):
        drawCenteredText("Wait a moment!", background, font, screen.get_size()[1]-80, screen)
    else:
        print("first reset")
    
    # resets letters and sends the background to the screen
    letters = updateLetters()
    screen.blit(background, (0,0))

    return letters

# Draws a set of centered instructions for use in the starting and game over screens
def drawInstructions(background, font, screen):
    drawCenteredText("This is a test of skill and luck", background, font, 0, screen)
    drawCenteredText("You will be given an increasingly smaller amount of time to press 3 buttons in order to attack ", background, font, 40, screen)
    drawCenteredText("Should you fail to press all three, you will lose health", background, font, 80, screen)
    drawCenteredText("You do not need to press them at the same time, just press them", background, font, 120, screen)

# Draws centered text a bit less painfully
def drawCenteredText(text, background, font, height, screen):

    # Renders text onto a pygame rect object at the height of the input
    tempText = font.render(text, 1, (180, 180, 180))
    tempTextRect = tempText.get_rect()
    tempTextPos = Rect(0, height, tempTextRect.w, tempTextRect.h)

    # Grabs the center X-value of the screen
    centerXPos = background.get_rect().centerx
    tempTextPos.centerx = centerXPos
    background.blit(tempText, tempTextPos)

    # Updates the screen with text
    screen.blit(background, (0,0))

# Draws text using a top-right coordinate but does not center the text
def drawText(text, background, font, x, y, screen):
    tempText = font.render(text, 1, (180, 180, 180))
    tempTextRect = tempText.get_rect()
    tempTextPos = Rect(x, y, tempTextRect.w, tempTextRect.h)
    background.blit(tempText, tempTextPos)
    screen.blit(background, (0,0))
    
# Covers text to prepare for new set of letters and updates bottom edge damage indicators
def drawBottomTextCover(background, screen, BACKGROUNDCOLOR):
    cover = Rect(screen.get_size()[0]/2 - 50000, screen.get_size()[1]-100, 100000, 100)
    cover = pygame.draw.rect(background, BACKGROUNDCOLOR, cover)
    screen.blit(screen, cover)

# Draws Enemy using images from the webscraper
def drawEnemy(background, screen, BACKGROUNDCOLOR, imageSurface):
    imageSurface.fill(BACKGROUNDCOLOR)
    backgroundLoaded = False
    imageLoaded = False

    # Prints if and when the images are being loaded
    print("loading background")
    while(not backgroundLoaded):
        while(imageLoaded == False):
            # Attempts to load iamges, removing all broken images
            filepath = "./images/" + choice(listdir("./images"))
            try:
                img = pygame.image.load(filepath)
                imageLoaded = True
            except:
                remove(filepath)

        # Ensures that image meets size constraints and updates while values
        if(img.get_rect().h>=imageSurface.get_rect().h and img.get_rect().w>=imageSurface.get_rect().w):
            image = Image.open(filepath)
            image = image.resize((imageSurface.get_rect().h, imageSurface.get_rect().w))
            img = pygame.image.load(filepath)
            imageSurface.blit(img, (0,0))
            background.blit(imageSurface, (screen.get_size()[0]//2-imageSurface.get_rect().w//2, screen.get_size()[1]//2 - imageSurface.get_rect().h//2))
            backgroundLoaded = True
            print("loaded background")

        # Removes all broken images
        else:
            imageLoaded = False
            remove(filepath)

    # Grabs images if there aren't enough
    if len(listdir(path.join(curdir, "images"))) < 50:
        imageGrabber = Thread(target=get_images, daemon=True)
        imageGrabber.start()

# Makes letter covers for when letters are pressed
def makeLetterCover(letterNum, background, screen, font):
    letterCover = font.render("—", 9, (180, 180, 180))

    # Makes the letter cover and puts it in position
    letterCoverPos = Rect(screen.get_width()/2-35 + 25 * letterNum, screen.get_height()-82, 30, 40)
    background.blit(letterCover, letterCoverPos)

    # Updates the screen
    screen.blit(background, (0,0))

# Runs functions that happen when a letter is pressed, sets letter pressed to true and covers it
def onLetterPress(lettersPressed, letterNum, background, screen, font):
    lettersPressed[letterNum-1] = True
    makeLetterCover(letterNum, background, screen, font)

    # Updates the screen
    pygame.display.flip()

# Runs the Game
if __name__ == '__main__': main()