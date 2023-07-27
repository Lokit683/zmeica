import pygame
from time import sleep
import random

size = 50
x, y = random.randrange(0, 600, size), random.randrange(0, 600, size)
eat = random.randrange(0, 600, size), random.randrange(0, 600, size)
lenght = 1
snake = [(x, y)]
moveX, moveY = 0, 0

pygame.init()
sc = pygame.display.set_mode((700, 600))

def text(text, color, x, y, zc):
	f1 = pygame.font.Font(None, zc)
	text1 = f1.render(text, 1, color)
	sc.blit(text1, (x, y))

timeZ = 0

while True:
	sleep(0.16)
	sc.fill(pygame.Color('gray'))
	x += moveX * size
	y += moveY * size
	if not moveX == 0 or moveY == 0:
			timeZ = timeZ+0.15
	if not len(snake) == 1:
		if (x,y) in snake[-lenght:]:
			text("GAME OVER", pygame.Color("red"), 250, 250, 36)
			pygame.display.update()
			sleep(3)
			exit()

	snake.append((x,y))
	snake = snake[-lenght:]
	if x <= -50:
		text("GAME OVER", pygame.Color("red"), 250, 250, 36)
		pygame.display.update()
	if y <= -50:
		text("GAME OVER", pygame.Color("red"), 250, 250, 36)
		pygame.display.update()
	if y >= 600:
		text("GAME OVER", pygame.Color("red"), 250, 250, 36)
		pygame.display.update()
	if x >= 600:
		text("GAME OVER", pygame.Color("red"), 250, 250, 36)
		pygame.display.update()

	if snake[-1] == eat:
		eat = random.randrange(0, 600, size), random.randrange(0, 600, size)
		lenght += 1
	if eat in snake[-lenght:]:
		eat = random.randrange(0, 600, size), random.randrange(0, 600, size)
		pygame.draw.rect(sc, pygame.Color('red'), (*eat, size, size))
	else:
		pygame.draw.rect(sc, pygame.Color('red'), (*eat, size, size))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				moveX, moveY = -1, 0
			if event.key == pygame.K_RIGHT:
				moveX, moveY = 1, 0
			if event.key == pygame.K_UP:
				moveX, moveY = 0, -1
			if event.key == pygame.K_DOWN:
				moveX, moveY = 0, 1
	text(f"SCORE: {lenght}", pygame.Color("green"), 5,5, 36)
	[(pygame.draw.rect(sc, pygame.Color('blue'), (i, j, size, size))) for i,j in snake]
	pygame.draw.rect(sc, pygame.Color('black'), (600, 0, 100, 600))
	text(f"T: {str(timeZ).split('.')[0]}", pygame.Color("red"), 620, 250, 20)
	pygame.display.update()
