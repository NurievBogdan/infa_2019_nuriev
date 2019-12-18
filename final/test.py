import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("polny pizdec")
pygame.image.load("screenshot_2.png")

dog_surf = pygame.image.load("screenshot_2.png")
dog_rect = dog_surf.get_rect(bottomright=(400, 300))
win.blit(dog_surf, dog_rect)
x = 50
y = 50

width = 40
height = 50
speed = 5

run = True 
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.draw.rect(win, (0,0,255), (x, y, width, height))
	pygame.display.update()

pygame.quit()
