# Thư viện
import pygame

class menu():
    def __init__(self):
        # Khởi tạo pygame
        pygame.init()
        
        # Điều chỉnh giao diện
        WIDTH = 1280
        HEIGHT = 720
        display = pygame.display.set_mode((WIDTH, HEIGHT))
        
        # FPS
        self.CLOCK = pygame.time.Clock()
        
        # Trạng thái chạy
        self.running = True
    def ui(self):
        """
        Hàm chạy giao diện phần mềm
        """
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.display.fill((255, 255, 255))
            pygame.display.flip()
            self.CLOCK.tick(60)
        pygame.quit()
