if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    import pygame
    pygame.init()
    size = width, height = 2 * n * k, 2 * n * k
    screen = pygame.display.set_mode(size)
    xc, yc = width // 2, height // 2
    COLORS = ('red', 'green', 'blue')
    for i in range(k - 1, -1, -1):
        pygame.draw.circle(screen, COLORS[(i % 3) % 3], (xc, yc), n * (i + 1))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
