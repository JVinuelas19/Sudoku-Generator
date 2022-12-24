import pygame
import sudoku 

#Creating the window for the game. 
WIDTH, HEIGHT = 730, 730
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Constants used in the game
BACKGROUND_COLOR = ((133, 199, 242))
VALUE_COLOR = ((52, 31, 151))
BLACK = ((0, 0, 0))
FPS = 60
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 40)
sketchy = sudoku.gen_sketchy_sudoku(9, sudoku.pick_difficulty('Medium'))

def draw_window():
    WIN.fill(BACKGROUND_COLOR)
    for i in range(10):
        if i%3 == 0:
            pygame.draw.line(WIN, BLACK, (70, 70+70*i), (700, 70+70*i), 4)
            pygame.draw.line(WIN, BLACK, (70+70*i, 70), (70+70*i ,700), 4)
        pygame.draw.line(WIN, BLACK, (70, 70+70*i), (700, 70+70*i), 2)
        pygame.draw.line(WIN, BLACK, (70+70*i, 70), (70+70*i ,700), 2)
    for i in range(0, len(sketchy[0])):
        for j in range(0, len(sketchy[0])):
            if 0<sketchy[i][j]<10:
                value = FONT.render(str(sketchy[i][j]), True, BLACK)
                WIN.blit(value, ((j+1)*70 + 25, (i+1)*70 + 5))
    #The update function takes all the changes done to the window and show them in the screen. If we don't call this function no changes will happen
    pygame.display.update()


def main():
    #Main loop of the game
    pygame.display.set_caption("Sudoku Masters")
    clock = pygame.time.Clock() #The clock will control the speed of the loop to the FPS we set in the FPS constant
    run = True
    while run:
        clock.tick(FPS)
        #Event manager
        for event in pygame.event.get():
            #This event handles the "Pressing x button", so once we press it the program will shut down
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


#This line is used to avoid the game starts running when it is imported in another file. It makes sure to only run the main from this file and not from
#Other files
if __name__ == "__main__":
    main()
