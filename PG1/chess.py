if __name__ == '__main__':
    w, n = list(map(int, input().split()))
    while w % n != 0:
        print('Неверный ввод: w должно делиться на n')
        w, n = list(map(int, input().split()))

    import pygame
    pygame.init()
    size = width, height = w, w
    screen = pygame.display.set_mode(size)
    screen.fill('white')
    for r in range(n):
        for c in range(n):
            if (r + c) % 2 == 0:
                screen.fill('black', pygame.Rect(c * (w // n), r * (w // n), w // n, w // n))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
