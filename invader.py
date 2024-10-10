import os
import pygame
import random  #zufällige Positionen und Geschwindigkeiten erzeugen


class Settings:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 700
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")


class Enemy:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "alienbig0101.png")).convert()
        self.image.set_colorkey("black")
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect(topleft=(0, 0))  #alle neuen Gegner starten links oben
        self.speed_x = random.randint(1, 5)  #zufällige horizontale Geschwindigkeit
        self.speed_y = random.randint(1, 5)  #zufällige vertikale Geschwindigkeit

    def move(self):
        #bewegung des Gegners
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #an den Rändern abprallen
        if self.rect.right > Settings.WINDOW_WIDTH or self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.bottom > Settings.WINDOW_HEIGHT or self.rect.top < 0:
            self.speed_y *= -1


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Bitmaps laden und ausgeben")
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "defender01.png")).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, (30, 30))
    defender_rect = pygame.rect.Rect(10, 80, 30, 30)
    defender_speed = 10
    defender_derection_x = -1
    defender_derection_y = 1

    objekt1_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "stein01.png")).convert()
    objekt1_image = pygame.transform.scale(objekt1_image, (40, 40))
    objekt1_image.set_colorkey("white")
    objekt1_rect = pygame.Rect(300, 350, 40, 40)

    objekt2_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "stein02.png")).convert()
    objekt2_image = pygame.transform.scale(objekt2_image, (40, 40))
    objekt2_image.set_colorkey("white")
    objekt2_rect = pygame.Rect(90, 512, 40, 40)

    objekt3_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "stein03.png")).convert()
    objekt3_image = pygame.transform.scale(objekt3_image, (40, 40))
    objekt3_image.set_colorkey("white")
    objekt3_rect = pygame.Rect(90, 200, 40, 40)

    objekt4_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "stein04.png")).convert()
    objekt4_image = pygame.transform.scale(objekt4_image, (40, 40))
    objekt4_image.set_colorkey("white")
    objekt4_rect = pygame.Rect(500, 512, 40, 40)

    objekt5_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "stein05.png")).convert()
    objekt5_image = pygame.transform.scale(objekt5_image, (40, 40))
    objekt5_image.set_colorkey("white")
    objekt5_rect = pygame.Rect(400, 150, 40, 40)

    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "background03.png")).convert()
    background_image = pygame.transform.scale(background_image, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

    enemies = []  #liste der Gegner
    enemy_spawn_timer = 0 #timer zum Erzeugen von Gegnern

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #gegner in zufälligen Abständen erzeugen
        enemy_spawn_timer += 1
        if enemy_spawn_timer > random.randint(120, 240):  #alle 2 bis 4 Sekunden
            enemies.append(Enemy())
            enemy_spawn_timer = 0


        for enemy in enemies[:]: #"[:]" steht für eine kopie der original Liste
            enemy.move()
            #überprüfen ob der Gegner mit einem Hindernis kollidiert
            if enemy.rect.colliderect(objekt1_rect) or enemy.rect.colliderect(objekt2_rect) or enemy.rect.colliderect(objekt3_rect) or enemy.rect.colliderect(objekt4_rect) or enemy.rect.colliderect(objekt5_rect):
                enemies.remove(enemy)  #Gegner verschwindet bei Kollision


        defender_rect.move_ip(defender_derection_x * defender_speed, defender_derection_y * defender_speed)
        if defender_rect.left < 0 or defender_rect.right > Settings.WINDOW_WIDTH:
            defender_derection_x *= -1
        if defender_rect.top < 0 or defender_rect.bottom > Settings.WINDOW_HEIGHT:
            defender_derection_y *= -1

        screen.blit(background_image, (0, 0))
        screen.blit(defender_image, defender_rect)
        screen.blit(objekt1_image, objekt1_rect.topleft)
        screen.blit(objekt2_image, objekt2_rect.topleft)
        screen.blit(objekt3_image, objekt3_rect.topleft)
        screen.blit(objekt4_image, objekt4_rect.topleft)
        screen.blit(objekt5_image, objekt5_rect.topleft)

        #alle gegner anzeigen
        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect.topleft)

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
