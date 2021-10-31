from pygame import *
import random

init()

width = 800
height = 600

screen = display.set_mode((width,height))

endProgram = False

class Menu():
	def drawScreen(self):
		logo = image.load("PyGames.png")
		screen.blit(logo,(150,150))
		tenlives = image.load("10lives.png")
		tenlives = transform.scale(tenlives,(180,35))
		screen.blit(tenlives,(185,305))
		fivelives = image.load("5lives.png")
		fivelives = transform.scale(fivelives,(180,35))
		screen.blit(fivelives,(435,305))
		threelives = image.load("3lives.png")
		threelives = transform.scale(threelives,(180,35))
		screen.blit(threelives,(185,455))
		onelives = image.load("1life.png")
		onelives = transform.scale(onelives,(180,35))
		screen.blit(onelives,(435,455))

class buttons():
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.w = width
		self.h = height
		self.rect = Rect(self.x,self.y,self.w,self.h)
	def drawButton(self,pos,buttoncol,buttonhover):
		if (self.rect).collidepoint(pos):
			self.buttoncol = buttonhover
		else:
			self.buttoncol = buttoncol
		self.difficulty = draw.rect(screen,(self.buttoncol),(self.x,self.y,self.w,self.h))

class cbuttons():
	def __init__(self,x,y,rad):
		self.x = x
		self.y = y
		self.r = rad
		self.buttoncol = (255,255,255)
	def drawButton(self,pos,buttoncol,buttonhover):
		self.difficulty = draw.circle(screen,(self.buttoncol),(self.x,self.y),self.r)
		if (self.difficulty).collidepoint(pos):
			self.buttoncol = buttonhover
		else:
			self.buttoncol = buttoncol

class RLGL():
	def drawScreen(self,lightcol,round1):
		rlglback = image.load('rlgl.jpg')
		rlglback = transform.scale(rlglback,(800,600))
		screen.blit(rlglback,(0,0))
		finish = draw.line(screen,(0,0,0),(650,0),(650,600),2)
		border1 = draw.rect(screen,(0,0,0),(778,198,24,44))
		light1 = draw.rect(screen,(lightcol),(780,200,20,40))
		border2 = draw.rect(screen,(0,0,0),(778,358,24,44))
		light2 = draw.rect(screen,(lightcol),(780,360,20,40))
		font1 = font.Font(None,40)
		roundnum = font1.render(str(round1)+"/5",True,(0,0,0))
		screen.blit(roundnum,(385,50))
	def player(self,playerx,playery):
		player = draw.rect(screen,(0,0,255),(playerx,playery,50,50))

class tugofwar():
	def drawScreen(self,ropex,round2):
		draw.rect(screen,(0,0,255),(ropex+50,250,40,95))
		draw.rect(screen,(255,0,0),(ropex+610,250,40,95))
		draw.line(screen,(139,105,20),(ropex,299),(ropex + 700,299),4)
		indicator = draw.rect(screen,(255,0,0),(ropex+348,299,4,12))
		font1 = font.Font(None,40)
		roundnum = font1.render(str(round2)+"/3",True,(0,0,0))
		screen.blit(roundnum,(385,50))
		loseblock = draw.rect(screen,(0,0,0),(550,350,250,250))
		winblock = draw.rect(screen,(0,0,0),(0,350,250,250))

class oddeven():
	def drawScreen(self,rand,handy):
		font1 = font.Font(None,50)
		randnum = font1.render(str(rand),True,(0,0,0))
		hand = image.load("hand.png")
		hand = transform.scale(hand,(150,350))
		screen.blit(hand,(325,handy))
		screen.blit(randnum,(405,handy+180))

def livesleft(lives):
	pos = 0
	x = 20
	while pos < lives:
		draw.circle(screen,(255,0,0),(x,20),7)
		x += 20
		pos += 1

def marblesleft(marbles):
	pos = 0
	x = 300
	marble = image.load("marble.png")
	marble = transform.scale(marble,(50,50))
	while pos < marbles:
		screen.blit(marble,(x,530))
		x += 50
		pos += 1

class gb():
	def drawScreen(self):
		draw.rect(screen,(84,84,84),(0,0,150,600))
		draw.rect(screen,(84,84,84),(650,0,150,600))
		draw.line(screen,(0,0,0),(150,225),(650,225),4)
		draw.line(screen,(0,0,0),(150,375),(650,375),4)
	def player(self,playerx,playery):
		self.player1 = draw.rect(screen,(0,0,255),(playerx,playery,50,50))
	def glass(self,x,y):
		self.glass1 = draw.rect(screen,(130,255,250),(x,y,25,50))

RLGL = RLGL()
menu = Menu()
tugwar = tugofwar()
oe = oddeven()
gb = gb()

difficulty1 = buttons(175,275,200,100)
difficulty2 = buttons(425,275,200,100)
difficulty3 = buttons(175,425,200,100)
difficulty4 = buttons(425,425,200,100)

odd = cbuttons(200,400,75)
even = cbuttons(600,400,75)
handy = -350

back = buttons(10,10,50,50)
back1 = buttons(10,10,50,50)

lives = 1
playerx = 50
playery = random.randint(100,450)
playerxmove = False

ropex = 50
speed = 14
round2 = 1

gtime = random.randint(4,5)
round1 = 1

marbles = 3
round3 = 1
marbel = image.load('marble.jpg')
marbel = transform.scale(marbel,(800,600))

glassplayerx = 50
glassplayery = 237
glassspeed = 2
glassx = 625
choose = [237,312]
glassy = random.choice(choose)
round4 = 1
gbback = image.load('glassbridge.jpg')
gbback = transform.scale(gbback,(800,600))

death = False
main = True
redlightinfo = False
redlight = False
tugofwarinfo = False
tugofwar = False
oddeveninfo = False
oddeven = False
guess = False
glassbridgeinfo = False
glassbridge = False
winscreen = False

lifelost = False

while not endProgram:
	if death == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram =True
		
		screen.fill((255,0,0))
		
		smiley = image.load("squidguysmiling.jpg")
		screen.blit(smiley,(10,80))
		
		font2 = font.Font(None,60)
		elim = font2.render("Eliminated",True,(0,0,0))
		gw = font2.render("Goodbye World :(",True,(0,0,0))
		screen.blit(elim,(300,20))
		screen.blit(gw,(250,540))
		
		back.drawButton(mouse.get_pos(),(0,0,255),(0,0,190))
		draw.line(screen,(255,255,255),(50,20),(20,35),5)
		draw.line(screen,(255,255,255),(20,35),(50,50),5)
		
		if e.type == MOUSEBUTTONDOWN:
			if (back.rect).collidepoint(mouse.get_pos()):
				main = True
				death = False
				lives = 1
				playerx = 50
				playery = random.randint(100,450)
				playerxmove = False

				ropex = 50
				speed = 14
				round2 = 1

				gtime = random.randint(4,5)
				round1 = 1
		
		display.flip()
		
	if main == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
		
		screen.fill((0,0,0))
		
		difficulty1.drawButton(mouse.get_pos(),(255,255,255),(203,211,203))
		difficulty2.drawButton(mouse.get_pos(),(0,255,0),(9,185,9))
		difficulty3.drawButton(mouse.get_pos(),(255,146,0),(191,110,0))
		difficulty4.drawButton(mouse.get_pos(),(255,0,0),(184,0,0))
		menu.drawScreen()
		
		if e.type == MOUSEBUTTONDOWN:
			if (difficulty1.rect).collidepoint(mouse.get_pos()):
				lives = 10
				redlightinfo = True
				main = False
			if (difficulty2.rect).collidepoint(mouse.get_pos()):
				lives = 5
				redlightinfo = True
				main = False
			if (difficulty3.rect).collidepoint(mouse.get_pos()):
				lives = 3
				redlightinfo = True
				main = False
			if (difficulty4.rect).collidepoint(mouse.get_pos()):
				lives = 1
				redlightinfo = True
				main = False
		
		display.flip()

	if redlightinfo == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram
				
		screen.fill((0,0,0))
		continue1 = buttons(675,50,75,75)
		continue1.drawButton(mouse.get_pos(),(0,0,255),(0,0,190))
		draw.line(screen,(255,255,255),(685,60),(740,90),9)
		draw.line(screen,(255,255,255),(685,115),(740,90),9)
		
		fontrlgl = font.Font('futurefont.otf',30)
		fontrlgl1 = font.Font('futurefont.otf',15)
		
		rlgl1 = fontrlgl.render("Red Light Green Light",True,(255,255,255))
		rlgl2 = fontrlgl1.render("This is your first game. I hope you are ready.",True,(255,255,255))
		rlgl3 = fontrlgl1.render("The gates will be alternating from green to red.",True,(255,255,255))
		rlgl4 = fontrlgl1.render("During a green phase press the left arrow to move forward.",True,(255,255,255))
		rlgl5 = fontrlgl1.render("But be careful...",True,(255,255,255))
		rlgl6 = fontrlgl1.render("when the gate is red you must stop or a life will be lost.",True,(255,255,255))
		rlgl7 = fontrlgl1.render("You must make it to the end 5 times in order to move on",True,(255,255,255))
		rlgl8 = fontrlgl1.render("If all lives are lost you will be eliminated.",True,(255,255,255))
		rlgl9 = fontrlgl1.render("Lives are displayed in the top left of your screen.",True,(255,255,255))
		rlgl10 = fontrlgl1.render("With the rounds left to complete in the centre.",True,(255,255,255))
		rlgl11 = fontrlgl1.render("Good Luck player 105",True,(255,255,255))
		
		screen.blit(rlgl1,(120,70))
		screen.blit(rlgl2,(10,180))
		screen.blit(rlgl3,(10,210))
		screen.blit(rlgl4,(10,240))
		screen.blit(rlgl5,(10,270))
		screen.blit(rlgl6,(10,300))
		screen.blit(rlgl7,(10,330))
		screen.blit(rlgl8,(10,430))
		screen.blit(rlgl9,(10,460))
		screen.blit(rlgl10,(10,490))
		screen.blit(rlgl11,(10,520))
		
		if e.type == MOUSEBUTTONDOWN:
			if (continue1.rect).collidepoint(mouse.get_pos()):
				redlight = True
				redlightinfo = False
				Gstart_ticks = time.get_ticks()
		display.flip()

	if redlight == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram
			if e.type == KEYDOWN:
				if e.key == K_RIGHT:
					playerxmove = True
			if e.type == KEYUP:
				if e.key == K_RIGHT:
					playerxmove = False
		
		screen.fill((255,255,255))
		
		Gseconds=(time.get_ticks()-Gstart_ticks)/1000
		
		if lives == 0:
			redlight = False
			death = True
		
		if playerxmove == True:
			playerx += 1
			
		if Gseconds < gtime:
			RLGL.drawScreen((0,255,0),round1)
		elif Gseconds > gtime-0.02 and Gseconds < gtime+0.02:
			Rstart_ticks=time.get_ticks()
		else:
			Rseconds=(time.get_ticks()-Rstart_ticks)/1000
			if playerxmove == True and Rseconds > 0.5:
				lifelost = True
				lives -= 1
				playerx = 50
			RLGL.drawScreen((255,0,0),round1)
			if Rseconds > 2 or lifelost == True:
				gtime = random.randint(4,5)
				Gstart_ticks=time.get_ticks()
				Rseconds = 0
				lifelost = False
		
		RLGL.player(playerx,playery)
		
		if playerx >= 655:
			playerx = 50
			playery = random.randint(100,450)
			round1 += 1
		
		if round1 == 6:
			tugofwarinfo = True
			redlight = False
			playerx = 50
			round1 = 1
		livesleft(lives)
			
		display.flip()
	
	if tugofwarinfo == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
				
		screen.fill((0,0,0))
		continue2 = buttons(675,50,75,75)
		continue2.drawButton(mouse.get_pos(),(0,0,255),(0,0,190))
		draw.line(screen,(255,255,255),(685,60),(740,90),9)
		draw.line(screen,(255,255,255),(685,115),(740,90),9)
		
		fonttw = font.Font('futurefont.otf',30)
		fonttw1 = font.Font('futurefont.otf',15)
		
		tw1 = fonttw.render("Tug Of War",True,(255,255,255))
		tw2 = fonttw1.render("For your second game, you will be competing in tug of war.",True,(255,255,255))
		tw3 = fonttw1.render("The space bar is the only thing between you and certain death",True,(255,255,255))
		tw4 = fonttw1.render("spam it to gain a greater pull over your opponent",True,(255,255,255))
		tw5 = fonttw1.render("However...",True,(255,255,255))
		tw6 = fonttw1.render("3 rounds of this will be played",True,(255,255,255))
		tw7 = fonttw1.render("and every round you will be slightly weakened.",True,(255,255,255))
		tw8 = fonttw1.render("drag the red flag in the centre across to your side",True,(255,255,255))
		tw9 = fonttw1.render("and in doing so, pulling your opponent off the edge.",True,(255,255,255))
		tw10 = fonttw1.render("your opponent won't go down without a fight though.",True,(255,255,255))
		tw11 = fonttw1.render("Good Luck player 105",True,(255,255,255))
		
		screen.blit(tw1,(260,70))
		screen.blit(tw2,(10,180))
		screen.blit(tw3,(10,210))
		screen.blit(tw4,(10,240))
		screen.blit(tw5,(10,270))
		screen.blit(tw6,(10,300))
		screen.blit(tw7,(10,330))
		screen.blit(tw8,(10,430))
		screen.blit(tw9,(10,460))
		screen.blit(tw10,(10,490))
		screen.blit(tw11,(10,520))
		
		if e.type == MOUSEBUTTONDOWN:
			if (continue2.rect).collidepoint(mouse.get_pos()):
				tugofwar = True
				tugofwarinfo = False
		display.flip()
	
	if tugofwar == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram
			if e.type == KEYDOWN:
				if e.key == K_SPACE:
					ropex -= speed
		screen.fill((255,255,255))
		
		twback = image.load('tugofwar.jpg')
		twback = transform.scale(twback,(1000,800))
		screen.blit(twback,(-100,0))
		
		livesleft(lives)
		
		if ropex+348 > 550:
			ropex = 50
			lives -= 1
		
		if ropex+348 < 250:
			ropex = 50
			round2 += 1
			speed -= 2
		
		tugwar.drawScreen(ropex,round2)
		ropex += 1
		
		if lives == 0:
			tugofwar = False
			death = True
		
		if round2 == 4:
			oddeveninfo = True
			tugofwar = False
			ropex = 50
			round2 = 1
		
		display.flip()
	
	if oddeveninfo == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
		
		screen.fill((0,0,0))
		continue3 = buttons(675,50,75,75)
		continue3.drawButton(mouse.get_pos(),(0,0,255),(0,0,190))
		draw.line(screen,(255,255,255),(685,60),(740,90),9)
		draw.line(screen,(255,255,255),(685,115),(740,90),9)
		
		fontoe = font.Font('futurefont.otf',30)
		fontoe1 = font.Font('futurefont.otf',15)
		
		oe1 = fontoe.render("Odd or Even",True,(255,255,255))
		oe2 = fontoe1.render("player 105 will start this game with 3 marbles.",True,(255,255,255))
		oe3 = fontoe1.render("A hand will be hidden displaying a certain number",True,(255,255,255))
		oe4 = fontoe1.render("You will be guessing whether the number is odd or even. ",True,(255,255,255))
		oe5 = fontoe1.render("If you get it correct you will receive a marble",True,(255,255,255))
		oe6 = fontoe1.render("Guess wrong and you will lose one.",True,(255,255,255))
		oe7 = fontoe1.render("The number will be randomised 1-9.",True,(255,255,255))
		oe8 = fontoe1.render("7 rounds of this will be played",True,(255,255,255))
		oe9 = fontoe1.render("If you have at least 1 marble left at the end, you will progress.",True,(255,255,255))
		oe10 = fontoe1.render("if all your marbles are stolen, a life will be lost.",True,(255,255,255))
		oe11 = fontoe1.render("Good Luck player 105",True,(255,255,255))
		
		screen.blit(oe1,(260,70))
		screen.blit(oe2,(10,180))
		screen.blit(oe3,(10,210))
		screen.blit(oe4,(10,240))
		screen.blit(oe5,(10,270))
		screen.blit(oe6,(10,300))
		screen.blit(oe7,(10,330))
		screen.blit(oe8,(10,430))
		screen.blit(oe9,(10,460))
		screen.blit(oe10,(10,490))
		screen.blit(oe11,(10,520))
		
		if e.type == MOUSEBUTTONDOWN:
			if (continue3.rect).collidepoint(mouse.get_pos()):
				oddeven = True
				oddeveninfo = False
		display.flip()
	
	if oddeven == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
		
		screen.fill((255,255,255))
		screen.blit(marbel,(0,0))
		
		odd.drawButton(mouse.get_pos(),(255,255,0),(210,210,0))
		even.drawButton(mouse.get_pos(),(0,255,255),(0,200,200))
		
		if guess == False:
			font3 = font.Font(None,50)
			pickoe = font3.render("Odd or Even",True,(0,0,0))
			screen.blit(pickoe,(300,200))
			if e.type == MOUSEBUTTONDOWN:
				if (odd.difficulty).collidepoint(mouse.get_pos()):
					guess = True
					rand = random.randint(1,9)
					handtime = time.get_ticks()
					pick = 'odd'
				if (even.difficulty).collidepoint(mouse.get_pos()):
					guess = True
					rand = random.randint(1,9)
					handtime = time.get_ticks()
					pick = 'even'
		else:
			oe.drawScreen(rand,handy)
			if handy < 0:
				handy += 10
			if handy == 0:
				handseconds=(time.get_ticks()-handtime)/1000
				if handseconds > 3.5:
					if rand % 2 == 1 and pick == 'even' or rand % 2 == 0 and pick == 'odd':
						marbles -= 1
					else:
						marbles += 1
					guess = False
					handy = -350
					round3 += 1
		
		marblesleft(marbles)
		livesleft(lives)
		
		font4 = font.Font(None,50)
		oddtext = font4.render("Odd",True,(0,0,0))
		screen.blit(oddtext,(165,380))
		eventext = font4.render("Even",True,(0,0,0))
		screen.blit(eventext,(560,380))
		font5 = font.Font(None,40)
		roundnum5 = font5.render(str(round3)+"/7",True,(0,0,0))
		screen.blit(roundnum5,(685,50))
		
		if round3 > 7 and marbles > 0:
			glassbridgeinfo = True
			oddeven = False
			marbles = 3
			round3 = 1
		
		if marbles == 0:
			marbles = 3
			round3 = 1
			lives -= 1
		
		if lives == 0:
			oddeven = False
			death = True
		
		display.flip()
	
	if glassbridgeinfo == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
		
		screen.fill((0,0,0))
		continue4 = buttons(675,50,75,75)
		continue4.drawButton(mouse.get_pos(),(0,0,255),(0,0,190))
		draw.line(screen,(255,255,255),(685,60),(740,90),9)
		draw.line(screen,(255,255,255),(685,115),(740,90),9)
		
		fontgb = font.Font('futurefont.otf',30)
		fontgb1 = font.Font('futurefont.otf',15)
		
		gb1 = fontgb.render("Glass Bridge",True,(255,255,255))
		gb2 = fontgb1.render("This is the final game",True,(255,255,255))
		gb3 = fontgb1.render("You will use the up and down arrows to change positions.",True,(255,255,255))
		gb4 = fontgb1.render("the left/right arrows will be used to move on the bridge.",True,(255,255,255))
		gb5 = fontgb1.render("You must make it to the other side 4 times",True,(255,255,255))
		gb6 = fontgb1.render("but beware...",True,(255,255,255))
		gb7 = fontgb1.render("sharp glass sheets must be dodged to avoid being pushed off.",True,(255,255,255))
		gb8 = fontgb1.render("glass will be fired from either path",True,(255,255,255))
		gb9 = fontgb1.render("and Speed of glass will increase every journey.",True,(255,255,255))
		gb10 = fontgb1.render("This is the last step until fame and fortune.",True,(255,255,255))
		gb11 = fontgb1.render("Good Luck player 105",True,(255,255,255))
		
		screen.blit(gb1,(240,70))
		screen.blit(gb2,(10,180))
		screen.blit(gb3,(10,210))
		screen.blit(gb4,(10,240))
		screen.blit(gb5,(10,270))
		screen.blit(gb6,(10,300))
		screen.blit(gb7,(10,330))
		screen.blit(gb8,(10,430))
		screen.blit(gb9,(10,460))
		screen.blit(gb10,(10,490))
		screen.blit(gb11,(10,520))
		
		if e.type == MOUSEBUTTONDOWN:
			if (continue4.rect).collidepoint(mouse.get_pos()):
				glassbridge = True
				glassbridgeinfo = False
		display.flip()
	
	if glassbridge == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
		
		screen.fill((255,255,255))
		
		screen.blit(gbback,(0,0))
		
		gb.glass(glassx,glassy)
		gb.drawScreen()
		gb.player(glassplayerx,glassplayery)
		
		glassx -= glassspeed
		
		if (gb.glass1).colliderect(gb.player1) and glassplayerx < 600:
			lives -= 1
			glassplayerx = 50
			glassplayery = 237
			glassspeed = 2
			glassx = 700
			round4 = 1
			
		
		if e.type == KEYDOWN:
			if e.key == K_UP:
				glassplayery = 237
			if e.key == K_DOWN:
				glassplayery = 312
			if e.key == K_LEFT:
				glassplayerx -= 2
			if e.key == K_RIGHT:
				glassplayerx += 2
		
		livesleft(lives)
		
		if glassx < 150:
			glassx = 625
			glassy = random.choice(choose)
		
		font6 = font.Font(None,40)
		roundnum6 = font6.render(str(round4)+"/4",True,(0,0,0))
		screen.blit(roundnum6,(385,50))
		
		if glassplayerx > 660:
			round4 += 1
			glassplayerx = 50
			glassspeed += 1
		
		if lives == 0:
			glassbridge = False
			death = True
		
		if round4 > 4:
			winscreen = True
			glassbridge = False
			glassplayerx = 50
			glassplayery = 237
			glassspeed = 2
			glassx = 700
			round4 = 1
		
		display.flip()
	
	if winscreen == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
		
		screen.fill((0,0,0))
		
		prize = image.load('prize.jpg')
		prize = transform.scale(prize,(800,450))
		screen.blit(prize,(0,0))
		
		font10 = font.Font('futurefont.otf',30)
		font11 = font.Font('futurefont.otf',20)
		wintext = font10.render("Well done player 105",True,(255,255,255))
		wintext2 = font11.render("The vips were impressed with your performance",True,(255,255,255))
		screen.blit(wintext,(150,475))
		screen.blit(wintext2,(10,540))
		
		back1.drawButton(mouse.get_pos(),(0,0,255),(0,0,190))
		draw.line(screen,(255,255,255),(50,20),(20,35),5)
		draw.line(screen,(255,255,255),(20,35),(50,50),5)
		
		if e.type == MOUSEBUTTONDOWN:
			if (back1.rect).collidepoint(mouse.get_pos()):
				main = True
				winscreen = False
				lives = 1
				playerx = 50
				playery = random.randint(100,450)
				playerxmove = False

				ropex = 50
				speed = 14
				round2 = 1

				gtime = random.randint(4,5)
				round1 = 1
		
		display.flip()
