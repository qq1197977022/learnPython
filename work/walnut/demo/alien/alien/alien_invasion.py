import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_function as gf


def run_game():
    # 初始化屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 开始按钮
    play_button = Button(ai_settings, screen, "Play")
    
    # 游戏状态、设置、分数版
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # 屏幕背景色
    bg_color = (230, 230, 230)
    
    # 创建一个外星飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # 创建一组外星飞船
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开启游戏主运行循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()



