import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 把飞船图片加载进内存
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 存储飞船位置
        self.center = float(self.rect.centerx)
        
        # 移动标记默认为False
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        self.center = self.screen_rect.centerx
        
    def update(self):
        """更新飞船中心位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 通过飞船中心位置更新图形位置
        self.rect.centerx = self.center

    def blitme(self):
        """在当前位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
