from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global cx, cy, ax, ay # 클릭 위치
    global countClick # 리스트에 저장된 클릭 횟수

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            ax, ay = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            cx.append(event.x)
            cy.append(TUK_HEIGHT - 1 - event.y)
            countClick+=1


running = True
x , y = TUK_WIDTH // 2, TUK_HEIGHT // 2 # character coord
px, py, ax, ay = TUK_WIDTH // 2, TUK_HEIGHT // 2, 0, 0 # prevent, arrow coord
cx, cy = [], []
countClick, count = 0, 0
frame, i = 0, 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if count < countClick and frame == 0:
        t = i / 100
        x = (1 - t) * px + t * cx[count]
        y = (1 - t) * py + t * cy[count]
        i += 2
        if i > 100:
            px, py = x ,y
            count += 1
            i = 0

    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    for j in range(count, countClick):
        arrow.draw(cx[j], cy[j])

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

close_canvas()