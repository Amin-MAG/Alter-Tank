from game_setting import *

##################
# Game Functions #
##################


def wall_collision(point):
    global MAZE
    pixel_rgb = get_color(MAZE, point)
    if 85 > pixel_rgb[0] > 70:
        return True


def get_color(surface, position):
    col = surface.get_at(position)
    return col.r, col.g, col.b


def check_boom(ball, tank):
    passing_time = time.time() - ball.get_time()
    if passing_time > 0.3:
        if ((abs(ball.get_center_location()[0] - tank.get_location()[0]))**2 + (abs(ball.get_center_location()[1] - tank.get_location()[1]))**2)**0.5 <= BALL_RADIUS + TANK_RADIUS:
            return True
    return False


def play_sound(sound):

    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(0)

def draw_text(surf, text, color, size, location):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surface = font.render(text, True, color)       ## True denotes the font to be anti-aliased
    text_rect = text_surface.get_rect()
    text_rect.midtop = location
    surf.blit(text_surface, text_rect)

def draw_score(color ,score):
    if color == "Red":
        location = (991,100)
    if color == "Green" :
        location = (991,275)
    if color == "Blue" :
        location = (991,450)
    draw_text(screen, score, BLACK, 60, location)

def help_2player():
    screen.blit(HELP_2PLAYER, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", BLACK, 30, (WIDTH/2, (HEIGHT/2)+200))
            pygame.display.update()

    screen.fill(BLACK)
    draw_text(screen, "GET READY!", WHITE, 40, (WIDTH/2, HEIGHT/2))
    pygame.display.update()

def help_3player():

        screen.blit(HELP_3PLAYER, (0,0))
        pygame.display.update()

        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    break
            elif ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            else:
                draw_text(screen, "Press [ENTER] To Begin", BLACK, 30, (WIDTH/2, (HEIGHT/2)+200))
                pygame.display.update()

        screen.fill(BLACK)
        draw_text(screen, "GET READY!", WHITE, 40, (WIDTH/2, HEIGHT/2))
        pygame.display.update()

def main_menu():

    screen.blit(START_MENU_IMG, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_2:
                import AlterTank_2player
            if ev.key == pygame.K_3:
                import AlterTank_3player
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Press [2] To Begin 2 player", BLACK, 40, (WIDTH/2, HEIGHT/2))
            draw_text(screen, "Press [3] To Begin 3 player", BLACK, 40, (WIDTH/2, (HEIGHT/2)+50))
            draw_text(screen, "press [Q] To Quit",BLACK, 40, (WIDTH/2, (HEIGHT/2)+100))
            pygame.display.update()
    pygame.display.update()


def get_possible_positions(number):

    final_random_positions = []
    map_positions = list(TANK_POSSIBLE_POSITIONS)

    for i in range(NUMBER_OF_POSITIONS):
        map_positions[i] = list(map_positions[i])

    for i in range(number):
        random_index = random.randint(0, len(map_positions)-1)
        final_random_positions.append(map_positions[random_index])
        map_positions.pop(random_index)

    return final_random_positions


def reset_map():
    map_index = random.randint(1, NUMBER_OF_MAP)
    return pygame.image.load(MAZE_TEXT.format(str(map_index)))

