import pygame as pg
import random as r
from pygame.locals import *


def color() -> list:
    "makes random color"
    color = [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]
    return color


def particle_move(particles: list, window, BLACK: tuple, fade: int) -> None:
    "moves all particles"
    for particle in particles:
        pg.draw.rect(window, BLACK, particle[0])
        particle[0].left += particle[2]
        particle[0].bottom += particle[3]
        for rgb in particle[1]:
           if rgb >= fade:
              particle[1][particle[1].index(rgb)] -= fade
        pg.draw.rect(window, particle[1], particle[0])
    pg.time.wait(50)
    pg.display.flip()


def particle_generator(particle_count: int, shot: object, particle_height: int, particle_width: int) -> list:
    "generates list of particles"
    particles = []
    for i in range(particle_count):
        x = r.randint(-20, 20)
        y = int((20 * 20 - x * x) ** 0.5)
        y = r.randint(-y, y)
        particles.append([Rect(shot.left + r.randint(0, 5), shot.bottom, particle_height, particle_width), color(), x, y])
    return particles


#-------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    pg.init()
    clock = pg.time.Clock()

    #==================SETTINGS=====================

    shot_speed = 10
    particle_count = 600
    particle_height = 4
    particle_width = 4

    #===============================================

    window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("FIREWORK")

    WINX = window.get_width()
    WINY = window.get_height()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    run = True
    shot = Rect(r.randint(0, WINX), WINY, 10, 10)
    particles = particle_generator(particle_count, shot, particle_height, particle_width)
    fade = r.randint(5, 10)

    window.fill(BLACK)

    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                shot_color = color()
                for i in range(r.randint(shot_speed * 3, WINY // shot_speed)):
                    pg.draw.rect(window, BLACK, shot)
                    shot.bottom -= shot_speed
                    pg.draw.rect(window, shot_color, shot)
                    pg.time.wait(10)
                    pg.display.flip()

                pg.draw.rect(window, BLACK, shot)
                window.fill(WHITE)
                pg.display.flip()
                pg.time.wait(10)
                window.fill(BLACK)
                pg.display.flip()
                particles = particle_generator(particle_count, shot, particle_height, particle_width)
                fade = r.randint(5, 10)

                for i in range(r.randint(35, 45)):
                    for event in pg.event.get():
                        if event.type == pg.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                            pg.quit()
                            run = False
                    particle_move(particles, window, BLACK, fade)
                
                shot = Rect(r.randint(0, WINX), WINY, 10, 10)
                window.fill(BLACK)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
