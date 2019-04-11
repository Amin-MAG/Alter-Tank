
from functions import *


def main():
    
    menu_display = True

    while GAME_IS_RUNNING:
        if menu_display:
            main_menu()
            pygame.time.wait(1000)
            menu_display = False
        clock.tick(60)
        pygame.display.update()


main()
