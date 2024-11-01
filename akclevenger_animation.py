import pygame

def main():
    pygame.init()

    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Heart")

   
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("turquoise")

    
    heart = pygame.image.load("heart.png")
    heart = heart.convert_alpha()
    heart = pygame.transform.scale(heart, (100, 100))

    heart_x, heart_y = 250, 250
    speed_x, speed_y = 5, 5
   
    heart_x = 250
    heart_y = 250

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        heart_x += speed_x
        heart_y += speed_y               


        if heart_x <= 0 or heart_x + heart.get_width() >= screen.get_width():
            speed_x = -speed_x  
        if heart_y <= 0 or heart_y + heart.get_height() >= screen.get_height():
            speed_y = -speed_y  

        screen.blit(background, (0, 0))
        screen.blit(heart, (heart_x, heart_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()