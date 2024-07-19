from game import Game
import pygame
import Constants
import json

def main():
    pygame.init()
    running = True
    size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    #loading all level data using JSON
    fileObject = open("data.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    
    game = Game(screen, aList[1]['Astroids'], aList[1]['Stars'], aList[1]['Bg_image'])
    
    clock = pygame.time.Clock()
            
    while running:            
        #Update object positions, check for collisions, edge of screen etc
        game.run_logic()
        
        #Process events (Keystrokes, mouse clicks, etc.)
        running = game.process_events()
    
        #Draw current frame
        running = game.display_frame(screen)
    
        #Pause for next frame
        clock.tick(60)
    
    pygame.quit()
    
#Call main function start
if __name__ == "__main__":
    main()
    