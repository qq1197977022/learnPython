import pygame, time, random
from pygame.locals import *


class SurfWindow(object):
    def __init__(self, size_tup):
        self.surf_window = pygame.display.set_mode(size_tup)  # 调用用于控制屏幕和窗口的display模块,创建一个display surface
        self.surf_back = pygame.image.load('img/background2.png')  # 加载图片

        pygame.mixer.init()
        pygame.mixer.music.load('music/music_back0.mp3')
        pygame.mixer.music.play(0, 0.0)

    def display(self):
        # rect_back = self.surf_window.blit(self.surf_back, (0, 0))
        # pygame.display.update(rect_back)  # 部分更新
        self.surf_window.blit(self.surf_back, (0, 0))


class Hero(object):
    def __init__(self, hero_position_lst):
        self.hero_position_lst = hero_position_lst
        self.surf_hero1 = pygame.image.load('img/hero1.png')
        self.bullet_lst = []   # 弹仓

    def display(self, surf_window):
        # rect_hero1 = surf_window.surf_window.blit(self.surf_hero1, self.hero_position_lst)
        # pygame.display.update(rect_hero1)   # 部分更新
        surf_window.surf_window.blit(self.surf_hero1, self.hero_position_lst)

        for bullet in self.bullet_lst:
            bullet.display(surf_window)
            bullet.move()
            self.clear_bullet_lst(bullet)

    def move(self, direction, surf_window):
        """
        :param direction:
            0. left
            1. right
            2. up
            3. down
        :param surf_window:
        :return: None
        """
        if direction == 0:
            self.hero_position_lst[0] -= 10
        elif direction == 1:
            self.hero_position_lst[0] += 10
        elif direction == 2:
            self.hero_position_lst[1] -= 10
        elif direction == 3:
            self.hero_position_lst[1] += 10
        self.display(surf_window)

    def fire(self):    # 开火
        print(f'{"发射子弹":-^60}')
        bullet = Bullet([self.hero_position_lst[0] + 40, self.hero_position_lst[1] - 18])
        # bullet.display(surf_window)
        self.bullet_lst.append(bullet)  # 子弹压入弹夹

    def clear_bullet_lst(self, bullet):    # 退蛋壳
        if bullet.bullet_position_lst[1] < 0:
            self.bullet_lst.remove(bullet)


class Bullet(object):
    def __init__(self, bullet_position_lst, is_hero=True):
        if is_hero:
            self.bullet_position_lst = bullet_position_lst
            self.surf_bullet = pygame.image.load('img/bullet.png')
        else:
            self.bullet_position_lst = bullet_position_lst
            self.surf_bullet = pygame.image.load('img/bullet1.png')

    def display(self, surf_window):
        # r = surf_window.surf_window.blit(self.surf_bullet, self.bullet_position_lst)
        # pygame.display.update(r)
        surf_window.surf_window.blit(self.surf_bullet, self.bullet_position_lst)

    def move(self, is_hero=True):
        """
        :param is_hero:
            1.True: hero , default
            2.False: enemy
        :return:
        """
        if is_hero:
            self.bullet_position_lst[1] -= 10
        else:
            self.bullet_position_lst[1] += 5


class Enemy(object):
    def __init__(self, enemy_position_lst):
        self.enemy_position_lst = enemy_position_lst
        self.surf_enemy = pygame.image.load('img/enemy0.png')
        self.flag = True   # 左右移动开关
        self.bullet_lst = []    # 弹夹

    def display(self, surf_window):
        surf_window.surf_window.blit(self.surf_enemy, self.enemy_position_lst)
        self.fire()
        self.move()
        for bullet in self.bullet_lst:
            bullet.display(surf_window)
            bullet.move(is_hero=False)
            self.clear_bullet_lst(bullet)

    def move(self):
        if self.flag:
            if self.enemy_position_lst[0] < 429:
                self.enemy_position_lst[0] += random.randint(3, 5)
            else:
                self.flag = False
        else:
            if self.enemy_position_lst[0] > 0:
                self.enemy_position_lst[0] -= random.randint(3, 5)
            else:
                self.flag = True

    def fire(self):
        if 25 < random.randint(0, 50) < 28:   # 控制敌机射击频率
            bullet = Bullet([self.enemy_position_lst[0] + 22, self.enemy_position_lst[1] + 35], is_hero=False)
            self.bullet_lst.append(bullet)

    def clear_bullet_lst(self, bullet):
        if bullet.bullet_position_lst[1] > 852:
            self.bullet_lst.remove(bullet)


def event_process(hero, surf_window):
    e_quee = pygame.event.get()
    print(f'事件队列: {e_quee}')
    for e in e_quee:
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_a or e.key == K_LEFT:
                hero.move(0, surf_window)
            elif e.key == K_d or e.key == K_RIGHT:
                hero.move(1, surf_window)
            elif e.key == K_w or e.key == K_UP:
                hero.move(2, surf_window)
            elif e.key == K_s or e.key == K_DOWN:
                hero.move(3, surf_window)
            elif e.key == K_SPACE:
                hero.fire()


def main():
    surf_window = SurfWindow((480, 852))
    hero = Hero([190, 710])
    enemy = Enemy([0, 0])
    # enemy1 = Enemy([330, 0])
    # enemy2 = Enemy([230, 0])
    # enemy3 = Enemy([130, 0])
    while True:    # 事件处理
        surf_window.display()
        hero.display(surf_window)
        enemy.display(surf_window)
        # enemy1.display(surf_window)
        # enemy2.display(surf_window)
        # enemy3.display(surf_window)

        pygame.display.flip()   # 刷新整个display surface, 解决V1.0中闪烁bug

        event_process(hero, surf_window)

        time.sleep(0.01)


if __name__ == '__main__':
    main()

