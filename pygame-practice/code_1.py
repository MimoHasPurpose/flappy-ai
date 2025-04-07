import pygame

#setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Sammie or Samantha!!")

clock=pygame.time.Clock(  )
running =True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
   

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

