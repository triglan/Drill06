from pico2d import *
import random

open_canvas()

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')
TUK_WIDTH, TUK_HEIGHT = 800, 600


def handle_events():
    global running, x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            running = False

running = True
x , y = 800 // 2, 600 // 2 # character coord
px, py, ax, ay = 0, 0, random.randint(100, 700), random.randint(100, 700) # prevent, arrow coord
frame = 0
i = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if frame == 0:
        t = i / 100
        x = (1 - t) * px + t * ax
        y = (1 - t) * py + t * ay
        i += 2
        if i > 100:
            ax, ay = random.randint(100, 700), random.randint(100, 700)
            px, py = x ,y
            i = 0

    if px < ax:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)

    arrow.draw(ax,ay)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

close_canvas()