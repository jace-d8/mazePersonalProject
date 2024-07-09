import pygame
import constants as c
from app import App


class Button:
    def __init__(self, x, y, w, h, text, color, hov_color, font_size):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hov_color
        self.font = pygame.font.SysFont('Arial', font_size)
        self.is_checked = False

    def draw(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(App.SCREEN, self.hover_color, self.rect)
        else:
            pygame.draw.rect(App.SCREEN, self.color, self.rect)

        # pygame.draw.rect(App.SCREEN, c.RED, self.rect)
        text_surf = self.font.render(self.text, True, c.WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        App.SCREEN.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False


class BackDrop:
    def __init__(self, color, x, y, w, h):
        self.color = color
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        pygame.draw.rect(App.SCREEN, self.color, self.rect)


class Slider:
    def __init__(self, button_color, slider_color, x, y, w, h):
        self.button_color = button_color
        self.slider_color = slider_color
        # self.button = pygame.Rect()
        self.slider = pygame.Rect(x, y, w, h)
