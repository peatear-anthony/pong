from math import ceil
import numpy as np

class Settings():
    def __init__(self):
        #
        self.title = "Peter Pong"
        # Screen settings
        self.width = 1000
        self.length = 600
        self.bg_color =(202, 204, 206)

        # Paddle Settings
        self.paddle_width = 150
        self.paddle_height = 20
        self.paddle_sections = 13 #Must be odd
        self.paddle_color = (10, 25, 0)
        self.paddle_speed_factor = 0.8
        self._update_paddle_width()

        # Ball settings
        self.ball_diameter = 15
        self.ball_color = (0, 0, 0)
        self.ball_speed_magnitude = 1.2
        self.ball_x_speed_levels = (self.paddle_sections-1)/2

        # Mode
        self.shoot_mode = False
        self.shoot_ball = False
        
        # Velocity settings
        self.theta_max = 90
        self.theta_min = 10 #25 degrees
        self._create_paddle_to_vel_dic()

    def _create_paddle_to_vel_dic(self):
        self._create_paddle_x_level_dict()
        self._create_velocity_dict()

        self.paddlex_to_velx = {x:self.velocity_x_dict[level] 
        for x, level in self.paddle_x_level_dict.items()}

        self.paddlex_to_vely = {x:self.velocity_y_dict[level] 
        for x, level in self.paddle_x_level_dict.items()}

    def _create_velocity_dict(self):
        increment =  (self.theta_max-self.theta_min)/self.level_index
        levels = [level for level 
        in sorted(set(self.paddle_x_level_dict.values()))]
        angles = [self.theta_max-(level*increment) for level in levels]

        self.velocity_x_dict ={level:np.cos(np.deg2rad(angle))
            for level, angle in zip(levels,angles)}
        self.velocity_y_dict ={level:np.sin(np.deg2rad(angle))
            for level, angle in zip(levels,angles)}

    def _create_paddle_x_level_dict(self):
        # Create a dict of x values on the paddle to 
        self.paddle_x_level_dict={}
        self.pixels_per_section = int(self.paddle_width/self.paddle_sections)
        self.level_index = -(self.paddle_sections-1)/2
        count = 1

        for _ in range(0, self.paddle_sections):
            for _ in range(0, self.pixels_per_section):
                self.paddle_x_level_dict[count] = self.level_index
                count +=1
            self.level_index += 1

    def _update_paddle_width(self):
        # Updates the paddle width to ensure it is divisable 
        # by the # of sections
        self.new_paddle_width = ceil(self.paddle_width/self.paddle_sections)*\
            self.paddle_sections
        self.paddle_width = self.new_paddle_width 


if __name__ =="__main__":
    # For testing purposes only
    settings = Settings()



