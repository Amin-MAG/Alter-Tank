
from functions import *


class Ball:

    def __init__(self, x, y, angle):
        self.__yPos = y
        self.__angle = angle
        angle_radian = (self.__angle*(math.pi/180))
        self.__xPos = x - (TANK_RADIUS-BALL_RADIUS+2)*math.cos(angle_radian)
        self.__yPos = y + (TANK_RADIUS-BALL_RADIUS+2)*math.sin(angle_radian)
        self.vertical_move = 0
        self.horizontal_move = 0
        self.__time = time.time()
        self.__points = {}
        self.horizontal_neg = 1
        self.vertical_neg = 1

    def go(self, value):

        x = int(self.__xPos)
        y = int(self.__yPos)

        self.__points ={
                        "right": (x+BALL_RADIUS, y+0),
                        "top": (x+0, y+BALL_RADIUS),
                        "left": (x-BALL_RADIUS, y-0),
                        "bottom": (x-0, y-BALL_RADIUS)}

        angle_radian = (self.__angle*(math.pi/180))

        if wall_collision(self.__points['right']) or wall_collision(self.__points['left']):
            self.horizontal_neg *= -1
        if wall_collision(self.__points['bottom']) or wall_collision(self.__points['top']):
            self.vertical_neg *= -1

        self.horizontal_move = self.horizontal_neg * -value*math.cos(angle_radian)
        self.vertical_move = self.vertical_neg * value*math.sin(angle_radian)

        self.__xPos += self.horizontal_move
        self.__yPos += self.vertical_move

    def get_center_location(self):
        return int(self.__xPos), int(self.__yPos)

    def get_angle(self):
        return self.__angle

    def get_time(self):
        return self.__time

    def draw_ball(self):
        return pygame.draw.circle(screen, BLACK, self.get_center_location(), BALL_RADIUS)
