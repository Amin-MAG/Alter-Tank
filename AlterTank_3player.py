
from tank import *

positions = get_possible_positions(3)
alterTank1 = ATank("Red", positions[0][0], positions[0][1], 180, IMG_TANK1, CONTROL_TANK1)
alterTank2 = ATank("Green", positions[1][0], positions[1][1], 0, IMG_TANK2, CONTROL_TANK2)
alterTank3 = ATank("Blue", positions[2][0], positions[2][1], 0, IMG_TANK3, CONTROL_TANK3)

help_3player_menu = True


def main_loop():

    global help_3player_menu

    positions = get_possible_positions(3)
    alterTank1.change_location(positions[0][0], positions[0][1], 180)
    alterTank2.change_location(positions[1][0], positions[1][1], 0)
    alterTank3.change_location(positions[2][0], positions[2][1], 0)

    tank_list = [alterTank1, alterTank2, alterTank3]
    player_numbers = len(tank_list)

    for tank in tank_list:
        tank.reset_balls()

    ending_time = -1

    while GAME_IS_RUNNING:

        if player_numbers < 2:
            if ending_time == -1:
                ending_time = time.time()
            if time.time() - ending_time > GAME_OVER_TIME:
                for tank in tank_list:
                    if tank.get_exist():
                        tank.score += 1
                    draw_score(tank.color, str(tank.score))
                    tank.is_exist = 1
                pygame.time.wait(2000)
                main_loop()
        if help_3player_menu:
            help_3player()
            pygame.time.wait(1000)
            help_3player_menu = False
        ##########
        # Events #
        ##########

        ball_list = []
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            for tank in tank_list:
                tank.shoot_control(event)

        for tank in tank_list:
            ball_list += tank.get_balls()

        for ball in ball_list:
            for tank in tank_list:
                if check_boom(ball, tank) and tank.get_exist():
                    tank.is_exist = 0
                    play_sound(EXPLOSION_SOUND)
                    tank.destroy()
                    for shooting_tank in tank_list:
                        shooting_tank.poping_ball(ball)
                    player_numbers -= 1

        screen.blit(MAZE, (0, 0))
        screen.blit(SCORE_FRAME_3player, (701, 0))

        for tank in tank_list:
            if tank.get_exist():
                tank.move_control()
                tank.build()
            elif time.time() - tank.get_death_time() < EXPLOSION_TIME:
                tank.build()

            for ball in tank.get_balls():
                ball.go(BALL_SPEED)
                ball.draw_ball()
            tank.check_balls()

        for tank in tank_list:
            draw_score(tank.color, str(tank.score))

        clock.tick(60)
        pygame.display.update()


main_loop()
