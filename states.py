import pygame

from player import Player
from widgets import Button, Text

from pygame.locals import K_p, KEYDOWN


class GameStateManager:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.play_state = PlayState(self.width, self.height, self)
        self.pause_state = PauseState(self.width, self.height, self)
        self.game_over_state = GameOverState(self.width, self.height, self)
        self.menu_state = MenuState(self.width, self.height, self)
        self.win_state = WinState(self.width, self.height, self)

        self.active = self.menu_state

        self.close = False

    def play(self):
        self.active = self.play_state

    def menu(self):
        self.active = self.menu_state
        self.play_state = PlayState(self.width, self.height, self)

    def pause(self) -> None:
        self.active = self.pause_state

    def game_over(self) -> None:
        self.active = self.game_over_state

    def win(self) -> None:
        self.active = self.win_state

    def stop(self) -> None:
        self.close = True


class PlayState:
    def __init__(self, w: int, h: int, gsm: GameStateManager) -> None:
        self.width = w
        self.height = h

        self.gsm = gsm

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.player = Player(self.width // 2, self.height * 0.8, self.width, self.height)
        
    def event(self, event: pygame.event.EventType) -> None:
        if event.type == KEYDOWN:
            if event.key == K_p:
                self.gsm.pause()

        self.player.event(event)

    def update(self) -> None:
        self.player.update()

        if self.player.dead:
            self.gsm.game_over()

    def render(self, screen: pygame.Surface) -> None:
        self.player.render(screen)


class PauseState:
    def __init__(self, w: int, h: int, gsm: GameStateManager) -> None:
        self.width = w
        self.height = h

        self.gsm = gsm

        self.font = pygame.font.SysFont('Source Code Pro', 50)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Resume', self.gsm.play),
            Button(self.width // 2, self.height // 2 + 100, 250, 75, 'Menu', self.gsm.menu),
            Text(self.width // 2, self.height // 3, 'Pause', (255, 255, 255))
        ]

    def event(self, event: pygame.event.EventType) -> None:
        for widget in self.widgets:
            widget.event(event)

    def update(self) -> None:
        for widget in self.widgets:
            widget.update()

    def render(self, screen: pygame.Surface) -> None:
        self.gsm.play_state.render(screen)

        for widget in self.widgets:
            widget.render(screen)


class MenuState:
    def __init__(self, w, h, gsm):
        self.width = w
        self.height = h

        self.gsm = gsm

        self.font = pygame.font.SysFont('Source Code Pro', 50)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Play', self.gsm.play),
            Button(self.width // 2, self.height // 2 + 100, 250, 75, 'Quit', self.gsm.stop),
            Text(self.width // 2, self.height // 3, 'Snake', (255, 255, 255))
        ]

    def event(self, event):
        for widget in self.widgets:
            widget.event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def render(self, screen):
        for widget in self.widgets:
            widget.render(screen)


class GameOverState:
    def __init__(self, w, h, gsm):
        self.width = w
        self.height = h

        self.gsm = gsm

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Menu', self.gsm.menu),
            Text(self.width // 2, self.height // 3, 'Game Over!', (255, 255, 255))
        ]

    def event(self, event):
        for widget in self.widgets:
            widget.event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def render(self, screen):
        self.gsm.play_state.render(screen)

        for widget in self.widgets:
            widget.render(screen)
 

class WinState:
    def __init__(self, w, h, gsm):
        self.width = w
        self.height = h

        self.gsm = gsm

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Menu', self.gsm.menu),
            Text(self.width // 2, self.height // 3, 'You Won!', (255, 255, 255))
        ]

    def event(self, event):
        for widget in self.widgets:
            widget.event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def render(self, screen):
        self.gsm.play_state.render(screen)

        for widget in self.widgets:
            widget.render(screen)
