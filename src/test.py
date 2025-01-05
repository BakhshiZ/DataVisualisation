import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Trackpad Click Test")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Button {event.button} clicked at {event.pos}")
        elif event.type == pygame.MOUSEMOTION:
            print(f"Mouse moved to {event.pos}")

pygame.quit()
