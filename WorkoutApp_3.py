# Name: Sohaib Ahmed, @sohaibahmed7
# Date: November 4th, 2021
# Title: My Workout Application Project V3

# Importing Libraries
import pygame
import sys
from time import sleep


# Animated button for home screen (learned from Clear Code on YouTube)
class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_colour = "#66CDAA"

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_colour = "#354B5E"

        # text
        self.text_surf = font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, func):
        # elevation
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_colour, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_colour, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click(func)

    def check_click(self, func):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_colour = "#76EEC6"
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    func()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = "#66CDAA"


# Initializations and global variables
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((950, 600))
pygame.display.set_caption("Sohaib's Fitness App")
font = pygame.font.Font(None, 50)
titleFont = pygame.font.Font(None, 150)
exFont = pygame.font.Font(None, 60)
restFont = pygame.font.Font(None, 175)

# Runs through each workout using files as input
def exercises(fileName, colour):
    sleep(0.25)
    file = open(fileName)
    lines = [line.strip("\n") for line in file if line != "\n"]
    for i in range(0, len(lines), 3):
        while True:
            sets = int(lines[i + 1])
            rest = int(lines[i + 2])
            backButton()
            pygame.display.update()
            for j in range(sets):
                while True:
                    screen.fill(colour)
                    exText = exFont.render(lines[i], True, "#FFFFFF")
                    centerEx = exText.get_rect(center=(475, 225))
                    screen.blit(exText, centerEx)
                    setText = exFont.render(
                        "Set #" + str(j + 1) + " : click anywhere when done",
                        True,
                        "#FFFFFF",
                    )
                    centerSet = setText.get_rect(center=(475, 325))
                    screen.blit(setText, centerSet)
                    backButton()
                    pygame.display.update()
                    mx, my = pygame.mouse.get_pos()
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if mx > 0 and mx < 950 and my > 0 and my < 600 and b1 == 1:
                        for k in range(rest):
                            screen.fill(colour)
                            backButton()
                            restText = restFont.render(
                                "Rest: " + str(rest - k), True, "#FFFFFF"
                            )
                            centerRest = restText.get_rect(center=(475, 260))
                            screen.blit(restText, centerRest)
                            pygame.display.update()
                            sleep(1)
                        break
            break

    file.close()


# Back button used to return to home screen
def backButton():
    backFont = pygame.font.Font(None, 50)
    backText = backFont.render("Back", True, "#FFFFFF")

    pygame.draw.rect(screen, (139, 35, 35), (25, 20, 95, 50))
    screen.blit(backText, (30, 30))

    # pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mx, my = pygame.mouse.get_pos()
    b1, b2, b3 = pygame.mouse.get_pressed()
    if mx > 25 and mx < 120 and my > 20 and my < 70 and b1 == 1:
        welcomeScreen()


# Starting screen for push day function
def pushDay():
    while True:
        pushFont = pygame.font.Font(None, 125)
        pushText = pushFont.render("Push Day", True, "#FFFFFF")
        pushFont2 = pygame.font.Font(None, 75)
        pushText2 = pushFont2.render("click anywhere to start", True, "#FFFFFF")

        screen.fill((142, 229, 238))
        screen.blit(pushText, (275, 180))
        screen.blit(pushText2, (190, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mx, my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if mx > 0 and mx < 950 and my > 0 and my < 600 and b1 == 1:
            backButton()
            exercises("PushDay.txt", (142, 229, 238))

        backButton()
        pygame.display.update()


# Starting screen for pull day function
def pullDay():
    while True:
        pullFont = pygame.font.Font(None, 125)
        pullText = pullFont.render("Pull Day", True, "#FFFFFF")
        pullFont2 = pygame.font.Font(None, 75)
        pullText2 = pullFont2.render("click anywhere to start", True, "#FFFFFF")

        screen.fill((255, 174, 185))
        screen.blit(pullText, (300, 180))
        screen.blit(pullText2, (190, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mx, my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if mx > 0 and mx < 950 and my > 0 and my < 600 and b1 == 1:
            backButton()
            exercises("PullDay.txt", (255, 174, 185))

        backButton()
        pygame.display.update()


# Starting screen for leg day function
def legDay():
    while True:
        legFont = pygame.font.Font(None, 125)
        legText = legFont.render("Leg Day", True, "#FFFFFF")
        legFont2 = pygame.font.Font(None, 75)
        legText2 = legFont2.render("click anywhere to start", True, "#FFFFFF")

        screen.fill((238, 154, 73))
        screen.blit(legText, (315, 180))
        screen.blit(legText2, (190, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.event.pump()
        mx, my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if mx > 0 and mx < 950 and my > 0 and my < 600 and b1 == 1:
            backButton()
            exercises("LegDay.txt", (238, 154, 73))

        backButton()
        pygame.display.update()


# Opening screen/menu
def welcomeScreen():
    titleText = titleFont.render("WORKOUT", True, "#FFFFFF")
    centerTitle = titleText.get_rect(center=(475, 200))
    button1 = Button("PUSH", 200, 100, (125, 260), 6)
    button2 = Button("PULL", 200, 100, (375, 260), 6)
    button3 = Button("LEGS", 200, 100, (625, 260), 6)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((83, 134, 139))
        screen.blit(titleText, centerTitle)
        button1.draw(pushDay)
        button2.draw(pullDay)
        button3.draw(legDay)

        pygame.display.update()


welcomeScreen()
