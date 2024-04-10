import pygame
import random
import math
import time

pygame.init()

# Width and Height and FPS
W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Arkanoid ")
clock = pygame.time.Clock()
done = False
menu_choice = None
playing = False
bg = (0, 0, 0)


def main_menu():
    menu_font = pygame.font.SysFont('comicsansms', 40)
    menu_items = ["Play", "Settings", "Quit"]
    selected_item = 0
    subtitle_font = pygame.font.SysFont('comicsansms', 20)
    title_font = pygame.font.SysFont('comicsansms', 80)
    title_text = title_font.render("Arkanoid", True, (255, 255, 255))
    while True:
        screen.fill(bg)
        screen.blit(title_text, (W // 2 - title_text.get_width() // 2, H // 4 - title_text.get_height() // 2))
        for i, item in enumerate(menu_items):
            color = (255, 255, 255) if i == selected_item else (128, 128, 128)
            text = menu_font.render(item, True, color)
            text_rect = text.get_rect(center=(W // 2, H // 2 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    return menu_items[selected_item]


def settings_menu():
    global ball_color, paddle_color
    settings_font = pygame.font.SysFont('comicsansms', 40)
    settings_items = ["Ball Color", "Paddle Color", "Return to Game"]
    selected_item = 0

    while True:
        screen.fill(bg)
        settings_title = settings_font.render("Settings", True, (255, 255, 255))
        screen.blit(settings_title,
                    (W // 2 - settings_title.get_width() // 2, H // 4 - settings_title.get_height() // 2))

        # Display current ball color
        ball_color_rect = pygame.Rect(W // 4 + 420, H // 2 - 20, 40, 40)
        pygame.draw.rect(screen, ball_color, ball_color_rect)

        # Display current paddle color
        paddle_color_rect = pygame.Rect(W // 4 + 440, H // 2 + 30, 40, 40)
        pygame.draw.rect(screen, paddle_color, paddle_color_rect)

        for i, item in enumerate(settings_items):
            color = (255, 255, 255) if i == selected_item else (128, 128, 128)
            text = settings_font.render(item, True, color)
            text_rect = text.get_rect(center=(W // 2, H // 2 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(settings_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(settings_items)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:  # Ball Color
                        ball_color = pygame.Color(random.randint(0, 255), random.randint(0, 255),
                                                  random.randint(0, 255))
                    elif selected_item == 1:  # Paddle Color
                        paddle_color = pygame.Color(random.randint(0, 255), random.randint(0, 255),
                                                    random.randint(0, 255))
                    elif selected_item == 2:  # Return to Game
                        return


# paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
paddle_color = pygame.Color(255, 255, 255)  # Initial paddle color (white)

# Ball
ballRadius = 20
ballSpeed = 5
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
ball_color = pygame.Color(255, 0, 0)  # Initial ball color (red)

dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                          100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255),
               random.randrange(0, 255), random.randrange(0, 255))
              for i in range(10) for j in range(4)]

# special blocks
num_special = num_unbreakable = random.randint(4, 7)
special_list = [(color_list[i], block_list[i]) for i in (random.randrange(0, 40) for j in range(num_special))]
special_color_list = [pair[0] for pair in special_list]
special_block_list = [pair[1] for pair in special_list]

# unbreakable blocks
unbreakable_list = [(color_list[i], block_list[i]) for i in (random.randrange(0, 40) for j in range(num_unbreakable)) if
                    block_list[i] not in special_block_list]
unbreakable_color_list = [pair[0] for pair in unbreakable_list]
unbreakable_block_list = [pair[1] for pair in unbreakable_list]

# Game over Screen
losefont = pygame.font.SysFont('comicsansms',
                               40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('Win', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


# Coordinates for a star inside a special block
def coordines_star(center):
    inner_radius = 8
    outer_radius = 20
    points = []
    angle = math.radians(-90)
    for _ in range(10):
        radius = outer_radius if len(points) % 2 == 0 else inner_radius
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
        angle += math.radians(360 / 10)
    return points


while not done:
    if menu_choice is None:
        menu_choice = main_menu()
    if menu_choice == "Quit":
        done = True
        continue
    if menu_choice == "Settings":
        settings_menu()
        menu_choice = None
    if menu_choice == "Play":
        playing = True
        menu_choice = 1
    while playing:
        # Events
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                ballSpeed += 0.05
                if paddle.width > 75:
                    paddle.width -= 1
            if event.type == pygame.QUIT:
                playing = False
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_menu()
        screen.fill(bg)
        # Drawing blocks
        [pygame.draw.rect(screen, color_list[color], block)
         for color, block in enumerate(block_list)  # drawing blocks
         if (color_list[color], block) not in special_list and (color_list[color], block) not in unbreakable_list]
        # Drawing special blocks
        for special_color, special_block in special_list:
            pygame.draw.rect(screen, special_color, special_block)
            pygame.draw.polygon(screen, (255 - special_color[0], 255 - special_color[1], 255 - special_color[2]),
                                (coordines_star(special_block.center)), 0)
        # Drawing unbreakable blocks
        for unbreakable_color, unbreakable_block in unbreakable_list:
            pygame.draw.rect(screen, unbreakable_color, unbreakable_block)
            pygame.draw.line(screen,
                             (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                             unbreakable_block.topleft, unbreakable_block.bottomright, width=3)
            pygame.draw.line(screen,
                             (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                             unbreakable_block.bottomleft, unbreakable_block.topright, width=3)
            pygame.draw.line(screen,
                             (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                             unbreakable_block.topright, unbreakable_block.bottomright, width=3)
            pygame.draw.line(screen,
                             (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                             unbreakable_block.topleft, unbreakable_block.bottomleft, width=3)
            pygame.draw.line(screen,
                             (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                             unbreakable_block.bottomleft, unbreakable_block.bottomright, width=3)
            pygame.draw.line(screen,
                             (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                             unbreakable_block.topleft, unbreakable_block.topright, width=3)
        pygame.draw.rect(screen, paddle_color, paddle)
        pygame.draw.circle(screen, ball_color, ball.center, ballRadius)

        # Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        # Collision left
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        # Collision top
        if ball.centery < ballRadius + 50:
            dy = -dy
        # Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        # Collision blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            if block_list[hitIndex] not in unbreakable_block_list:
                hitRect = block_list.pop(hitIndex)
                hitColor = color_list.pop(hitIndex)
            else:
                hitRect = block_list[hitIndex]
                hitColor = color_list[hitIndex]
            # if the rect is special, we get 2 points and paddle width will increase by 15 pixels for it
            if hitRect in special_block_list:
                special_block_list.remove(hitRect)
                special_color_list.remove(hitColor)
                special_list.remove((hitColor, hitRect))
                game_score += 2
                paddle.width += 15
                collision_sound.play()
            elif hitRect in unbreakable_block_list:
                collision_sound.play()
            else:
                game_score += 1
                collision_sound.play()
            dx, dy = detect_collision(dx, dy, ball, hitRect)

        # Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        # Win/lose screens
        if ball.bottom > H:
            time.sleep(0.1)
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
        elif not (len(block_list) - len(unbreakable_list)):
            ballSpeed = 0
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)

        # Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
        # Screen update
        pygame.display.flip()
        clock.tick(FPS)
pygame.quit()