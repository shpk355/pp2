import pygame

white = (255, 255, 255)
eraser = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = white
    last_pos = None

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_BACKSPACE:
                    mode = eraser
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_s:
                    drawsquare(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), mode)
                elif event.key == pygame.K_t:
                    drawTriangle(screen, pygame.mouse.get_pos(), mode)
                elif event.key == pygame.K_9:
                    drawTriangle2(screen, pygame.mouse.get_pos(), mode)
                elif event.key == pygame.K_7:
                    rombus(screen, pygame.mouse.get_pos(), mode)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # start a new line
                last_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                # draw a line from the last point to the current point
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(screen, start_pos, end_pos, radius, mode)
                    last_pos = end_pos

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, start, end, width, color_mode):
    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)  # 4th parameter is outline of the rectangle

def drawsquare(screen, mouse_pos, a, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, a, a)
    pygame.draw.rect(screen, color, rect, 3)

def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3)  # 4th parameter is outline of the rectangle

def drawTriangle(screen, mouse_pos, color):
     x = mouse_pos[0]
     y = mouse_pos[1]
     pygame.draw.line(screen, color, (x, y), (x+100,y), 3)
     pygame.draw.line(screen, color, (x, y), (x, y+100), 3)
     pygame.draw.line(screen, color, (x+100, y), (x, y+100), 3)


def drawTriangle2(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.line(screen, color, (x, y), (x + 100, y - 59), 3)
    pygame.draw.line(screen, color, (x, y), (x + 100, y + 59), 3)
    pygame.draw.line(screen, color, (x + 100, y - 59), (x + 100, y + 59), 3)

def rombus(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.line(screen, color, (x, y), (x - 59, y + 100), 3)
    pygame.draw.line(screen, color, (x, y), (x + 59, y + 100), 3)
    pygame.draw.line(screen, color, (x, y + 200), (x - 59, y + 100), 3)
    pygame.draw.line(screen, color, (x, y + 200), (x + 59, y + 100), 3)

main()