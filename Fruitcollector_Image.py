import pgzrun
import random

#screen size
WIDTH=1000
HEIGHT=400

#PLAYER(BASKET)
basket = Actor("basket2")
#giving the position to the basket
basket.pos = (WIDTH // 2, HEIGHT - 50)

#FALLING OBJECT(FRUIT)
fruit = Actor("apple")
#Giving a randoim position for the apple to fall 
fruit.pos = (random.randint(50,WIDTH - 50) , 0)

#GAME VARIABLES
score=0
lives=3
speed=3

def draw():
    screen.clear()
    screen.blit("background", (0,0)) #ADDING A BACKGROUND IMAGER IF NEEDED
    #basket and fruit is added on top of the background
    basket.draw()
    fruit.draw()
    #adding the font of the game at the corners
    screen.draw.text(f"Score: {score}", (10,10), fontsize=30, color="white")
    screen.draw.text(f"Lives: {lives}", (10,50), fontsize=30, color="white")
    #if lives get over the the final message is displayed
    if lives <=0:
        screen.fill("black")
        #The message to be displayed after you lose the game or your lives are over
        screen.draw.text("Time's up! Your Final score: " + str(score), midtop=(WIDTH/2,10),fontsize=40,color="pink")

def update():
    global score,lives,speed

    #move basket with arrow keys
    #this makes the basket move to the right or the left aadding or subtracting 50 from the width
    if keyboard.left and basket.x > 50:
        basket.x -= 5
    if keyboard.right and basket.x < WIDTH - 50:
        basket.x +=5

    #mOVE FRUIT DOWN
    #giving the speed to the fruit(apple) for falling from the top to the bottom
    fruit.y +=speed 

    #Check for collision
    if fruit.colliderect(basket):
        score += 1 #adds your score up by 1 every ti e  yoy get the fruit in the basket
        fruit.pos = (random.randint(50, WIDTH - 50), 0) #RESET FRUIT POSITION
        speed +=0.2 #increase difficulty formaking teh game interesting

    #if fruit reaches the bottom, lose a life
    if fruit.y > HEIGHT:
        lives -= 1 #if the fruit toche sthe bottom you automattically lose a life 
        fruit.pos = (random.randint(50,WIDTH - 50), 0) #gives the new position to the fruit 

    #End game if no lives left 

pgzrun.go()