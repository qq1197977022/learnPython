import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """飞船子弹模型"""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # 创建一个子弹并设置初始位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 存储子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """更新子弹位置"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """将子弹绘制到屏幕上"""
        pygame.draw.rect(self.screen, self.color, self.rect)
