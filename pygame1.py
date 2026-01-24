import pygame

pygame.init()
screen = pygame.display.set.mode((400,500))
done = False
while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True # 🔹 stop the loop

    pygame.display.flip()

pygame.quit() # 🔹 quit after loop ends