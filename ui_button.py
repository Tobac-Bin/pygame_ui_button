from typing import Tuple
import pygame

class Button:
    def __init__(
        self,
        x, 
        y, 
        image, 
        screen, 
        scale: int,
    ) -> None:
        """
            Create GUI Button
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (
            int(width * scale),
            int(height * scale)
        ))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self._clicked = False
        self.__img = pygame.transform.scale(image, (
            int(width * scale),
            int(height * scale)
        ))
    def draw(self, surface: pygame.Surface): 
        """
            Draw the Button
            ```
            btn = Button(x=100, y=100, image="path/to/image", screen=pygame.display.set_mode((830, 580)), scale=1)
            btn.draw()
            ```
        """
        self.screen.blit( self.image, (self.rect.x, self.rect.y))
    def clicked(self, key: Tuple[
        bool,
        bool,
        bool
    ]):
        """
            On Click event
        """
        def _inner(func):
            self._pos = pygame.mouse.get_pos()
            _action = False
            if self.rect.collidepoint(self._pos):
                if pygame.mouse.get_pressed() == key:                
                    if not self._clicked:
                        self._clicked = True
                        _action = True
            if pygame.mouse.get_pressed() == (False, False, False):
                self._clicked = False
            self.screen.blit( self.image, (self.rect.x, self.rect.y))
            if _action: func()
        return _inner
    def setHoverSkin(self, hover_skin: pygame.Surface):
        """
            Set hover skin
        """
        self._pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self._pos):
            self.image = hover_skin
        else:
            self.image = self.__img
    def normal(self, func):
        """
            On normal event
        """
        self._pos = pygame.mouse.get_pos()
        if not self.rect.collidepoint(self._pos):
            func()
    def hover(self, func):
        """
            On hover event
        """
        self._pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self._pos):
            func()