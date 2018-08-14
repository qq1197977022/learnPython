import pygame, time
from pygame.locals import *


class SurfWindow(object):
    def __init__(self, size_tup):
        self.surf_window = pygame.display.set_mode(size_tup)  # 调用用于控制屏幕和窗口的display模块,创建一个display surface
        self.surf_back = pygame.image.load('img/background.png')  # 加载图片

        pygame.mixer.init()
        pygame.mixer.music.load('music/music_back0.mp3')
        pygame.mixer.music.play(0, 0.0)

    def display(self):
        rect_back = self.surf_window.blit(self.surf_back, (0, 0))
        pygame.display.update(rect_back)  # 部分更新


class Hero(object):
    def __init__(self, position_lst):
        self.position_lst = position_lst
        self.surf_hero1 = pygame.image.load('img/hero1.png')

    def display(self, surf_window):
        rect_hero1 = surf_window.surf_window.blit(self.surf_hero1, self.position_lst)
        pygame.display.update(rect_hero1)

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
            self.position_lst[0] -= 5
        elif direction == 1:
            self.position_lst[0] += 5
        elif direction == 2:
            self.position_lst[1] -= 5
        elif direction == 3:
            self.position_lst[1] += 5
        self.display(surf_window)

    def fire(self):
        print(f'{"发射子弹":-^60}')


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

    while True:    # 事件处理
        surf_window.display()
        hero.display(surf_window)
        event_process(hero, surf_window)
        time.sleep(0.01)


if __name__ == '__main__':
    main()

