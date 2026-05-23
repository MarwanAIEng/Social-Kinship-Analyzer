import pygame
from algorithms import bfs_social, dfs_social

network = {
    "Marwan": ["Ali", "Omar"], 
    "Ali": ["Marwan", "Sara", "Zaid"], 
    "Omar": ["Marwan", "Huda"],
    "Sara": ["Ali"], 
    "Zaid": ["Ali", "Huda"], 
    "Huda": ["Omar", "Zaid"]
}

positions = {
    "Marwan": (400, 220), "Ali": (200, 360), "Omar": (600, 360),
    "Sara": (100, 510), "Zaid": (300, 510), "Huda": (700, 510)
}

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Social Media Connections AI - Marwan")
font = pygame.font.SysFont("Arial", 20, bold=True)

path = []
current_mode = "None"
btn_b = pygame.Rect(50, 25, 60, 50)   
btn_f = pygame.Rect(450, 25, 60, 50)  


running = True
while running:
    screen.fill((255, 255, 255)),

    if current_mode == "BFS":
        pygame.draw.rect(screen, (40, 40, 40), btn_b, border_radius=10)
    else:
        pygame.draw.rect(screen, (0, 128, 0), btn_b, border_radius=10) 
    text_b = font.render("B", True, (255, 255, 255))
    screen.blit(text_b, (btn_b.x + 22, btn_b.y + 12))
    label_b = font.render("Click B for BFS", True, (0, 0, 0))
    screen.blit(label_b, (btn_b.x + 75, btn_b.y + 15)) 
    if current_mode == "DFS":
        pygame.draw.rect(screen, (40, 40, 40), btn_f, border_radius=10)
    else:
        pygame.draw.rect(screen, (128, 0, 128), btn_f, border_radius=10)  
    text_f = font.render("D", True, (255, 255, 255))
    screen.blit(text_f, (btn_f.x + 22, btn_f.y + 12))
    
    label_f = font.render("Click D for DFS", True, (0, 0, 0))
    screen.blit(label_f, (btn_f.x + 75, btn_f.y + 15)) 
    pygame.draw.line(screen, (200, 200, 200), (0, 100), (800, 100), 2)

    for person, friends in network.items():
        for friend in friends:
            pygame.draw.line(screen, (220, 220, 220), positions[person], positions[friend], 2)
            
    if path:
        for i in range(len(path)-1):
            pygame.draw.line(screen, (255, 0, 0), positions[path[i]], positions[path[i+1]], 6)

    for name, pos in positions.items():
        node_color = (255, 165, 0) if name in path else (0, 102, 204)
        pygame.draw.circle(screen, node_color, pos, 30)
        screen.blit(font.render(name, True, (0, 0, 0)), (pos[0] - 25, pos[1] + 35))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_b.collidepoint(event.pos):
                path = bfs_social(network, "Marwan", "Huda")
                current_mode = "BFS"
            elif btn_f.collidepoint(event.pos):
                path = dfs_social(network, "Marwan", "Huda")
                current_mode = "DFS"

    pygame.display.flip() 
pygame.quit() 