import pygame as pg
import time


def main():
    display_window = pg.display.set_mode((533, 947))
    back_img = pg.image.load('img/background0.png')

    pg.mixer.init()
    pg.mixer.music.load('music/tickle.mp3')
    pg.mixer.music.play()

    for i in range(15):
        display_window.blit(back_img, (0, 0))
        pg.display.flip()
        time.sleep(1)


if __name__ == '__main__':
    main()
