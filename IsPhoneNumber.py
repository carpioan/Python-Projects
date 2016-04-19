import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600),0, 32)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   sys.exit()

 #PROCESSES
 #LOGIC

 #LOGIC
 #DRAW
 pygame.display.flip()
 #DRAW