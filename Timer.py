"""Timer"""
import pygame


class Timer:
    """Timer Class"""
    def __init__(self):
        pygame.init()
        # width, height, screen
        self.WIDTH = 1100
        self.HEIGHT = 609
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        # font
        self.font = pygame.font.Font("Roboto-Bold.ttf", int(self.HEIGHT/10))
        # times
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.millisecond = 0
        # clock and running
        self.clock = pygame.time.Clock()
        self.running = True
        # timer
        self.timer = pygame.USEREVENT
        # colors
        self.textColor = (220, 220, 220)
        self.bgColor = (30, 30, 30)
        # counter
        self.counter = None

    def check(self):
        """check"""
        if self.millisecond == 101:
            self.millisecond = 0
            self.second += 1

        if self.second == 60:
            self.second = 0
            self.minute += 1

        if self.minute == 60:
            self.minute = 0
            self.hour += 1

    def resize(self, w, h):
        """resize"""
        # width, height, screen
        self.WIDTH = w
        self.HEIGHT = h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        # font
        self.font = pygame.font.Font("Roboto-Bold.ttf", int(self.HEIGHT / 10))

    def event(self):
        """event loop"""
        for event in pygame.event.get():
            # quit from app
            if event.type == pygame.QUIT:
                self.running = False
            # timer
            if event.type == self.timer and self.counter is True:
                self.millisecond += 1
                self.check()

            # clicks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.counter is None:
                    self.counter = False

                if event.key == pygame.K_SPACE and self.counter is True:
                    self.counter = None

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and self.counter is False:
                    pygame.time.set_timer(self.timer, 10)
                    self.counter = True

            if event.type == pygame.VIDEORESIZE:
                self.resize(event.w, event.h)



    def run(self):
        """main function"""
        while self.running:
            # FPS
            self.clock.tick(100)
            self.event()
            self.draw()

    def draw(self):
        """draw"""
        self.screen.fill(self.bgColor)
        string = ""
        texts = [self.hour, self.minute, self.second, self.millisecond]
        # add hour and minute
        for t in texts:
            if len(str(t)) == 1:
                string += f"0{t}."
            elif len(str(t)) == 2:
                string += f"{t}."

        string = string[:-1]

        # create text, rect
        text = self.font.render(string, True, self.textColor)
        rect = text.get_rect(center=(self.WIDTH/2, self.HEIGHT/3))

        # draw
        self.screen.blit(text, rect)
        pygame.display.flip()


if __name__ == '__main__':
    Timer().run()
