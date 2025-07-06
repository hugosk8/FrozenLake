import pygame

CELL_SIZE = 64
COLORS = {
    "S": (0, 255, 0),
    "G": (0, 0, 255),
    "H": (0, 0, 0),
    "F": (255, 255, 255),
    "A": (255, 0, 0)
}
ASSETS = {
    "S": pygame.image.load("graphics/assets/start2.png"),
    "G": pygame.image.load("graphics/assets/goal.png"),
    "H": pygame.image.load("graphics/assets/hole.png"),
    "F": pygame.image.load("graphics/assets/frozen.png"),
    "A": pygame.image.load("graphics/assets/agent.png"),
}

def render(env):
    pygame.init()

    width = env.width * CELL_SIZE
    height = env.height * CELL_SIZE

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Frozen Lake")

    clock = pygame.time.Clock()
    running = True
    game_over = not running

    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                direction = None

                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_LEFT:
                    direction = "left"

                if direction:
                    env.move_agent(direction)

                    reward = env.get_reward()
                    print(f"Reward: {reward}")

                    if env.is_terminal_state():
                        game_over = True
                        current = env.get_current_cell()
                        print(f"🎯 État terminal atteint : {current}")
                        if current == "G":
                            print("🏁 Objectif atteint ! Bravo !")
                        elif current == "H":
                            print("💀 Tombé dans un trou ! Dommage.")
        
        for y in range(env.height):
            for x in range(env.width):
                cell = env.map[y][x]
                color = COLORS.get(cell, (100, 100, 100))
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                image = ASSETS.get(cell)
                if image:
                    screen.blit(image, (x * CELL_SIZE, y * CELL_SIZE))

                pygame.draw.rect(screen, (200, 200, 200), rect, 1)
        
        x, y = env.agent_pos
        agent_image = ASSETS.get("A")
        agent_rect = agent_image.get_rect()
        pixel_x = x * CELL_SIZE + (CELL_SIZE - agent_rect.width) // 2
        pixel_y = y * CELL_SIZE + (CELL_SIZE - agent_rect.width) // 4
        screen.blit(agent_image, (pixel_x, pixel_y))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
                