class Settings():
    def __init__(self):
        #
        self.title = "Peter Pong"

        # Screen settings
        self.width = 1000
        self.length = 800

        self.bg_color =(202, 204, 206)

        # Paddle Settings
        self.paddle_width = 200
        self.paddle_height = 20
        self.paddle_color = (0, 0, 0)
        self.paddle_speed_factor = 3

        # Ball settings
        self.ball_diameter = 15
        self.ball_color = (0, 0, 0)
        self.ball_speed_magnitude = 2
        self.create_speed_dict()

    def create_speed_dict(self):
        self.speed_dict={}
        self.sections = 11
        self.pixels_per_section = int(self.paddle_width/self.sections)

        self.level_index = -(self.sections-1)/2
        count = 1

        for x in range(0, self.sections):
            for y in range(0, self.pixels_per_section):
                self.speed_dict[count] = self.level_index
                count +=1
            self.level_index += 1

        print(self.speed_dict)



