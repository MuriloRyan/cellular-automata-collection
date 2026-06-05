import pygame
from forest_age import ForestFire

class ForestFireScreen:
    def __init__(self, width=640, height=640, cell_size=10):
        pygame.init()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Forest Fire - Age & Food System")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Cores Base
        self.COLOR_EMPTY = (139, 69, 19) # Marrom Terra
        self.COLOR_FIRE  = (255, 69, 0)  # Vermelho Alaranjado
        self.COLOR_FOOD  = (220, 20, 60) # Vermelho Maçã (Crimson)
        
        # Tabela de tons de verde por idade (RGB)
        self.tree_ages = {
            0: (144, 238, 144), # Nova
            1: (50, 205, 50),   # Jovem
            2: (34, 139, 34),   # Adulta 1
            3: (0, 100, 0),     # Adulta 2
            4: (20, 40, 20)     # Velha
        }

    def get_tree_color(self, age):
        # Aqui aplicamos a lógica de "frames per age step"
        # Dividimos a idade por 20 para que a cor mude mais devagar
        visual_age = age // 20 
        return self.tree_ages.get(min(visual_age, 4), self.tree_ages[4])

    def render(self, grid):
        self.screen.fill((255, 255, 255))
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                cell = grid[x][y]
                rect = pygame.Rect(
                    x * self.cell_size, 
                    y * self.cell_size, 
                    self.cell_size, 
                    self.cell_size
                )

                # 1. Desenha o Estado da Célula (Fundo)
                if cell.state == 0: # EMPTY
                    pygame.draw.rect(self.screen, self.COLOR_EMPTY, rect)
                elif cell.state == 1: # TREE
                    color = self.get_tree_color(cell.age)
                    pygame.draw.rect(self.screen, color, rect)
                elif cell.state == 2: # FIRE
                    pygame.draw.rect(self.screen, self.COLOR_FIRE, rect)

                # 2. Desenha a Comida (Sobreposição)
                # Só desenha comida se não estiver pegando fogo
                if cell.has_food and cell.state != 2:
                    # Desenha um quadrado menor (maçã) no centro da célula
                    food_margin = self.cell_size // 4
                    food_rect = pygame.Rect(
                        x * self.cell_size + food_margin,
                        y * self.cell_size + food_margin,
                        self.cell_size - (food_margin * 2),
                        self.cell_size - (food_margin * 2)
                    )
                    pygame.draw.rect(self.screen, self.COLOR_FOOD, food_rect)
        
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self, fps=30):
        self.clock.tick(fps)
    
    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    ff = ForestFire(horizontal_size=64, vertical_size=64)
    ff.generate_forest(density=0.4)
    
    screen = ForestFireScreen(width=640, height=640, cell_size=10)
    
    while screen.running:
        screen.handle_events()
        screen.render(ff.grid)
        ff.cycle()
        screen.update(fps=15)
    
    screen.quit()