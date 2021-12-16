from os import path

import pygame


class GameOver(pygame.sprite.Sprite):
    game_over = pygame.image.load(path.join("data", "gameover.png"))

    def __init__(self, screen_width, *args):
        super(GameOver, self).__init__(*args)
        self.image = self.game_over
        self.rect = self.game_over.get_rect()
        self.width = screen_width
        self.rect.x, self.rect.y = -self.width, 0
        self.step = 5

    def update(self, *args):
        self.rect.move_ip(self.step, 0)
        if not self.rect.x:
            self.step = 0


class Game:
    def __init__(self, **kwargs):
        self.size = kwargs.get("size", (600, 400))
        self.bg_color = kwargs.get("bg_color", (0, 0, 0))
        self.title = kwargs.get("title", "New Game")
        self.FPS = kwargs.get("FPS", 30)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        self.objects_groups = dict()

    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def game_update(self):
        for group in self.objects_groups.values():
            group.update()

    def game_render(self):
        self.screen.fill(self.bg_color)
        for group in self.objects_groups.values():
            group.draw(self.screen)

    def add_group(self, name):
        self.objects_groups[name] = pygame.sprite.Group()

    def play(self):
        while self.game_events():
            self.game_update()
            self.game_render()

            pygame.display.flip()
            self.clock.tick(self.FPS)
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game(size=(600, 300), bg_color=(0, 0, 255), title="Game over", FPS=30)
    game.add_group("game_over")
    end = GameOver(game.size[0], game.objects_groups["game_over"])
    game.play()
