# This code was created by CHARTIER Max, MENARD Marley, BORDEL Tristan, Hawa, Rith (nom de famille!)
# This is the main of our code, it countains all the loops that make the game playable and all the images needed to make
# it as enjoyable as possible. We used the library pycharm to develop our game, because it is known as an easy way
# to access the 2D world from Python. All code bellow plays a part in the good functioning of our game and it will all
# be explained.

# Here in the first few lines we import all the libraries we will need, random to generate random numbers, pygame to use
# pygame, sys to be able to quit the loops, math which will play a really important part in the creating of gravity and
# finally the importation of our own created GIF_animation.py code.
from GIF_animation import Flower, Zombie, Spider, Bee
import random
import pygame
import sys
import math
import time

# We need to initialize pygame in order for it to work, same with the clock. We also have our main images, such as the
# player, the arrow and the background.
pygame.init()
clock = pygame.time.Clock()
background_image = pygame.image.load("Images/background_for_game.png")
image = pygame.image.load(r"Images/Player_image1.gif")
image = pygame.transform.scale(image, (110, 150))
arrow_image = pygame.image.load("Images/ball2.png")

# The difficulty level and the number of lifes is defined here so that we can use thel after.
difficulty = 1
lifes = 3

# Also an important thing in pygame, to have a display screen we need to initialize it, therefor we need to create
# two variable, width and height that will be taken into the creation of the screen for its size. The name of the 
# window will be ARCANE ARCHER
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ARCANE ARCHER")


# Definition of our first class!!
class Button:
    """To create a button."""

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """Initializes the parameters of the button (image, position, text, font, color and color when the mouse is
        matching the position)."""

        super().__init__()

        # The image for the background of the button:
        self.image = image

        # The coordinates of the button:
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        # Determine the font which will be used for the text:
        self.font = font

        # Determine the natural color of the text
        self.base_color = base_color
        # Determine the modified color of the text when the coordinates of the mouse will match the coordinates
        # of the button:
        self.hovering_color = hovering_color

        # Text to insert in the button:
        self.text_input = text_input
        # Apply the color to the text:
        self.text = self.font.render(self.text_input, True, self.base_color)

        # If we don't want to insert an image in the button (only clickable text):
        if self.image is None:
            self.image = self.text

        # Create the rectangle around the image with four parameters : the coordinates x and y, the width and the
        # height.
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def check_for_input(self, position):
        """Returns True if the user clicked on the rectangle covering the surface of the button.
        In brief, allows two make the connection between the button and the linked menu."""

        # The function is called once the 'click' of the user has already been detected.
        # If the coordinates of the 'click' are in the surface covered by the button, it sends the user to the game,
        # the game mode menu, or closes the library and the game.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def change_button_color(self, position):
        """Changes the color of the text if the mouse is over the button."""

        # Either the coordinates of the button's rectangle match the position of the mouse.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        # Either it doesn't and the color of the text remains the same.
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def update(self, surface):
        """Updates the displayed button."""
        # If an image is provided :
        if self.image is not None:
            surface.blit(self.image, self.rect)
        # Update the text
        surface.blit(self.text, self.text_rect)


def create_sprites_flower(coordinates_flower):
    """Create the sprites for the FLOWER."""
    # Creating sprites and form a group with them for the FLOWER
    moving_sprites_flower = pygame.sprite.Group()
    flower = Flower(coordinates_flower[0], coordinates_flower[1])
    moving_sprites_flower.add(flower)

    return moving_sprites_flower


def create_sprites_zombie(coordinates_zombie):
    """Create the sprites for the ZOMBIE."""
    # Creating sprites and form a group with them for the ZOMBIE
    moving_sprites_zombie = pygame.sprite.Group()
    zombie = Zombie(coordinates_zombie[0], coordinates_zombie[1])
    moving_sprites_zombie.add(zombie)

    return moving_sprites_zombie


def create_sprites_spider(coordinates_spider):
    """Create the sprites for the SPIDER."""
    # Creating sprites and form a group with them for the SPIDER
    moving_sprites_spider = pygame.sprite.Group()
    spider = Spider(coordinates_spider[0], coordinates_spider[1])
    moving_sprites_spider.add(spider)

    return moving_sprites_spider


def create_sprites_bee(coordinates_bee):
    """Create the sprites for the SPIDER."""
    # Creating sprites and form a group with them for the BEE
    moving_sprites_bee = pygame.sprite.Group()
    bee = Bee(coordinates_bee[0], coordinates_bee[1])
    moving_sprites_bee.add(bee)

    return moving_sprites_bee


def game_mode():
    """Game loop for the GAME MODE menu."""

    # Display the background
    main_menu_background = pygame.transform.scale(pygame.image.load("assets/main_menu_bg.png"), (1200, 600))
    screen.blit(main_menu_background, (0, 0))

    # Initialize the basic color of the text buttons
    base_color_easy = '#d7fcd4'
    base_color_medium = '#d7fcd4'
    base_color_hard = '#d7fcd4'
    global difficulty

    while True:
        # Get the position of the mouse
        game_mode_mouse_pos = pygame.mouse.get_pos()

        # Display the title of the menu : GAME MODE
        game_mode_text = pygame.font.Font("assets/Font_SaintCarellClean.otf", 45).render("GAME MODE", True, "#eae6e5")
        game_mode_rect_text = game_mode_text.get_rect(center=(600, 150))
        screen.blit(game_mode_text, game_mode_rect_text)

        # Create the 'EASY' game mode button
        game_mode_easy_button = Button(image=None, pos=(400, 300), text_input="EASY",
                                       font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                       base_color=base_color_easy, hovering_color="#76c893")
        # Create the 'MEDIUM' game mode button
        game_mode_medium_button = Button(image=None, pos=(600, 300), text_input="MEDIUM",
                                         font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                         base_color=base_color_medium, hovering_color="#76c893")
        # Create the 'HARD' game mode button
        game_mode_hard_button = Button(image=None, pos=(800, 300), text_input="HARD",
                                       font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                       base_color=base_color_hard, hovering_color="#76c893")

        # Create the 'BACK' button
        game_mode_back_button = Button(image=None, pos=(60, 30), text_input="BACK",
                                       font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 30),
                                       base_color="#d7fcd4", hovering_color="White")

        # If the mouse of the player is on a button, the color of the text changes
        # - For the 'BACK' button:
        game_mode_back_button.change_button_color(game_mode_mouse_pos)
        game_mode_back_button.update(screen)
        # - For the 'EASY' button:
        game_mode_easy_button.change_button_color(game_mode_mouse_pos)
        game_mode_easy_button.update(screen)
        # - For the 'MEDIUM' button:
        game_mode_medium_button.change_button_color(game_mode_mouse_pos)
        game_mode_medium_button.update(screen)
        # - For the 'HARD' button:
        game_mode_hard_button.change_button_color(game_mode_mouse_pos)
        game_mode_hard_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_mode_back_button.check_for_input(game_mode_mouse_pos):
                    # Go back to the main menu
                    main_menu()
                if game_mode_easy_button.check_for_input(game_mode_mouse_pos):
                    difficulty = 1
                    # 'EASY' button gets the accentuated color
                    base_color_easy = '#e9190f'
                    # 'MEDIUM and 'HARD' get the basic color
                    base_color_medium = '#d7fcd4'
                    base_color_hard = '#d7fcd4'
                if game_mode_medium_button.check_for_input(game_mode_mouse_pos):
                    difficulty = 2
                    # 'MEDIUM' button gets the accentuated color
                    base_color_medium = '#e9190f'
                    # 'EASY' and 'HARD' get the basic color
                    base_color_easy = '#d7fcd4'
                    base_color_hard = '#d7fcd4'
                if game_mode_hard_button.check_for_input(game_mode_mouse_pos):
                    difficulty = 3
                    # 'HARD' gets the accentuated color
                    base_color_hard = '#e9190f'
                    # 'EASY' and 'MEDIUM' get the basic color
                    base_color_easy = '#d7fcd4'
                    base_color_medium = '#d7fcd4'
        pygame.display.flip()


def pause_state():
    """Pauses the game and displays a little menu"""
    pause = True
    while pause:
        # Get the position of the mouse
        pause_mouse_pos = pygame.mouse.get_pos()

        # Create the 'resume' button to pause the game
        resume_button = Button(image=None, pos=(55, 60), text_input="RESUME",
                               font=pygame.font.Font("assets/Font_Gameplay.ttf", 20),
                               base_color="White",
                               hovering_color="Black")

        main_menu_button = Button(image=None, pos=(70, 100), text_input="MAIN MENU",
                                  font=pygame.font.Font("assets/Font_Gameplay.ttf", 20),
                                  base_color="White",
                                  hovering_color="Black")

        # If the mouse of the player is on a button, the color of the text changes
        resume_button.change_button_color(pause_mouse_pos)
        main_menu_button.change_button_color(pause_mouse_pos)
        resume_button.update(screen)
        main_menu_button.update(screen)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Resume the game
                if resume_button.check_for_input(pause_mouse_pos):
                    # Return to the game
                    pause = False
                if main_menu_button.check_for_input(pause_mouse_pos):
                    # Go back to the main menu
                    main_menu()

        pygame.display.flip()


def play():
    """Game loop for the game."""
    # Here we redfine the variables as global, to be able to use them anywhere, in every loop
    global lifes
    global difficulty
    # The direction will correspond to the way the character is oriented, game pause is pretty self-explanatory and jump
    # just tell us the character is not jumping
    game_paused = False
    direction = True
    jump = False
    level = 1
    # Level 1 will correspond to the first level you face, the coordinates of the character are given, so that you 
    # appear on the screen, and same for the flower and the spider that will appear randomly which will be your 
    # enemies. 
    if level == 1:
        x = 50
        y = 450
        shoot_plant = random.randint(50, 1150)
        coordinates_flower = (shoot_plant, 499)
        x_im_spider = random.randint(50, 1150)
        coordinates_spider = (x_im_spider, 0)
        if x > 1100:
            level += 1
        # if you go past the edge of the screen you will change levels
        moving_sprites_flower, moving_sprites_spider = create_sprites_flower(coordinates_flower), \
                                                       create_sprites_spider(coordinates_spider)


    # creates the moving sprites
    ###################################################
    # Variable that will be used to make the enemies shoot and right under the creation of their projectiles
    time_shoot_enemy = 0
    blow_plant = pygame.image.load(r'Images/shoot_plant.png')
    acid_spider = pygame.image.load(r'Images/acid_spider.png')
    fire_plant = False
    # This condition makes the plant shoot in the direction of the character, it would be too easy if she kept 
    # shooting towards one side 
    if shoot_plant > x:
        shoot_plant += 5
    else:
        shoot_plant -= 5
    # gives the coordinates to the shoot
    x_plant = shoot_plant
    y_plant = 478
    # gives the information about the spider
    fire_spider = False
    x_im_spider += 5
    y_spider = 50

    while True:
        # In this loop, we first initialize a lot of variable to be able to use them for the jump and for the arrow
        # trajectory
        vel = 9
        mass = 1
        arrow_x = x
        arrow_y = y
        arrow_speed = 5
        arrow_angle = 0
        arrow_fired = False
        arrow_velocity_x = 0
        arrow_velocity_y = 0
        gravity = 0.1  # set gravity
        shot_strength = 0.8  # set initial shot strength
        shot_strength_scale = 3.2  # set shot strength scale

        while not game_paused:
            key_pressed_is = pygame.key.get_pressed()
            if level == 2:
                # Fill the screen with black color
                screen.fill((0, 0, 0))
                # Render the text
                font = pygame.font.Font(None, 120)  # Increased font size to 64
                text_color = (255, 255, 255)  # White
                text = font.render("NEXT LEVEL", True, text_color)
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
                # Blit the text onto the screen
                screen.blit(text, text_rect)
                # Update the screen
                pygame.display.flip()
                # Wait for 3 seconds
                time.sleep(1.5)
                # Increment the level
                level += 1

            if level == 3:
                x = 50
                y = 450
                x_plant = random.randint(50, 1150)
                coordinates_flower = (x_plant, 499)
                x_im_spider = random.randint(50, 1150)
                coordinates_spider = (x_im_spider, 0)
                # if you go past the edge of the screen you will change levels
                moving_sprites_flower, moving_sprites_spider = create_sprites_flower(coordinates_flower), \
                                                               create_sprites_spider(coordinates_spider)
                level +=1

            if key_pressed_is[pygame.K_q]:
                x -= 3
                direction = False
            if key_pressed_is[pygame.K_d]:
                x += 3
                direction = True
            if x > 1200:
                level +=1
                x = 10

            if arrow_fired:
                arrow_x += arrow_velocity_x
                arrow_y += arrow_velocity_y
                arrow_velocity_y += gravity

            if arrow_y + arrow_image.get_height() > 750:
                arrow_fired = False
                arrow_velocity_x = 0
                arrow_velocity_y = 0
            if arrow_y + arrow_image.get_height() > 620:
                arrow_fired = False
                arrow_velocity_x = 0
                arrow_velocity_y = 0

            # Draw arrow if fired
            if not jump:
                # if space bar is pressed
                if key_pressed_is[pygame.K_SPACE]:
                    # make is jump equal to True
                    jump = True
            if jump:
                # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
                Force = (1 / 4) * mass * (vel ** 2)
                # change in the y co-ordinate
                y -= Force
                # decreasing velocity while going up and become negative while coming down
                vel = vel - 1

                # object reached its maximum height
                if vel < 0:
                    # negative sign is added to counter negative velocity
                    mass = -1
                # objected reaches its original state
                if vel == -10:
                    # making is jump equal to false
                    jump = False
                    vel = 9
                    mass = 1

            # We need to draw the elements:
            # - Screen color
            screen.blit(background_image, (0, 0))



            if arrow_fired:
                screen.blit(pygame.transform.rotate(arrow_image, math.degrees(-arrow_angle)), (arrow_x, arrow_y))
                if x < arrow_x:
                    arrow_angle += shot_strength / 60
                if x > arrow_x:
                    arrow_angle -= shot_strength / 60

            # Get the position of the mouse
            play_mouse_pos = pygame.mouse.get_pos()

            # print(play_mouse_pos) ##########################

            # Create the '||' button to go back to pause the game
            play_back_button = Button(image=None, pos=(20, 20), text_input="| |",
                                      font=pygame.font.Font("assets/Font_Gameplay.ttf", 20), base_color="White",
                                      hovering_color="Black")

            # If the mouse of the player is on the button, the color of the text changes
            play_back_button.change_button_color(play_mouse_pos)
            play_back_button.update(screen)

            # - Draw the sprites
            moving_sprites_flower.draw(screen)
            moving_sprites_spider.draw(screen)

            # - Update the displayed sprites
            moving_sprites_flower.update(0.02)
            moving_sprites_spider.update(0.15)

            ################################################
            time_shoot_enemy += 1
            if difficulty == 1:
                if round(time_shoot_enemy) % 500 == 0:
                    fire_plant = True
                if round(time_shoot_enemy) % 500 == 0:
                    fire_spider = True
            if difficulty == 2:
                if round(time_shoot_enemy) % 400 == 0:
                    fire_plant = True
                if round(time_shoot_enemy) % 400 == 0:
                    fire_spider = True
            if difficulty == 3:
                if round(time_shoot_enemy) % 300 == 0:
                    fire_plant = True
                if round(time_shoot_enemy) % 300 == 0:
                    fire_spider = True
            game_over = False
            if lifes <= 0:
                font = pygame.font.SysFont(None, 100)
                img = font.render('GAME OVER', True, (0, 10, 90))
                screen.blit(img, (400, 300))


            if fire_plant:
                if shoot_plant < x:
                    x_plant += 5
                else:
                    x_plant -= 5
                screen.blit(blow_plant, (x_plant, y_plant + 35))

            if x_plant < 0 or x_plant > 1200:
                fire_plant = False
                x_plant = shoot_plant

            if (x - 20 < x_plant < x + 20) and (y - 30 < y_plant < y + 30):
                lifes -= 1
                x_plant = shoot_plant
                fire_plant = False

            ####################################

            font = pygame.font.SysFont(None, 30)
            img = font.render('Lives =', True, (0, 10, 90))
            screen.blit(img, (50, 50))
            img = font.render(str(lifes), 1, (0, 10, 90))
            screen.blit(img, (130, 50))

            if fire_spider:
                y_spider += 5
                screen.blit(acid_spider, (x_im_spider, y_spider))

            if x - 20 < x_im_spider < x + 20 and y - 20 < y_spider < y + 20:
                lifes -= 1
                y_spider = 0
                fire_spider = False

            if y_spider < 0 or y_spider > 1200:
                fire_spider = False
                y_spider = 0

            if (x_plant - 30 < arrow_x < x_plant + 30) and (y_plant - 20 < arrow_y < y_plant + 40):
                arrow_fired = False
                coordinates_flower = (900, 900)
                y_plant = 9000
                moving_sprites_flower = create_sprites_flower(coordinates_flower)
            if (x_im_spider - 40 < arrow_x < x_im_spider + 40) and (-20 < arrow_y < 20):
                arrow_fired = False
                arrow_x = 90000
                coordinates_spider = (900, 900)
                x_im_spider = 9000
                y_spider = 9000
                moving_sprites_spider = create_sprites_spider(coordinates_spider)

                ##################################################
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and not arrow_fired:
                    arrow_fired = True
                    arrow_x = x
                    arrow_y = y
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    arrow_angle = math.atan2(y + 25 - mouse_y, x + 50 - mouse_x)
                    arrow_velocity_x = -arrow_speed * math.cos(arrow_angle) * shot_strength
                    arrow_velocity_y = -arrow_speed * math.sin(arrow_angle) * shot_strength
                    shot_strength = 0.8
                if event.type == pygame.KEYDOWN and not arrow_fired and event.key == pygame.K_l:
                    shot_strength = min(2.0, shot_strength + 0.4)
                if event.type == pygame.QUIT:
                    # Shut down the pygame library
                    pygame.quit()
                    # Exit the program
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back_button.check_for_input(play_mouse_pos):
                        # Pause the game
                        pause_state()
                if event.type == pygame.QUIT:
                    # Shut down the pygame library
                    pygame.quit()
                    # Exit the program
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Exit the pause menu
                    game_paused = False
            # - Update what is displayed on the screen
            if direction:
                screen.blit(pygame.transform.flip(image, True, False), (x, y))
            if not direction:
                screen.blit(image, (x, y))
            pygame.display.flip()
            clock.tick(60)

        pygame.display.flip()


def main_menu():
    """Game loop for the MAIN MENU."""
    while True:
        # Display the background
        main_menu_background = pygame.transform.scale(pygame.image.load("assets/main_menu_bg.png"), (1200, 600))
        screen.blit(main_menu_background, (0, 0))

        # Get the position of the mouse
        menu_mouse_pos = pygame.mouse.get_pos()

        # Display the title of the menu
        menu_text = pygame.font.Font("assets/Font_SaintCarellClean.otf", 100).render("MAIN MENU", True, "#eae6e5")
        menu_rect_text = menu_text.get_rect(center=(600, 120))
        screen.blit(menu_text, menu_rect_text)

        # Create the 'PLAY' button
        play_button = Button(image=pygame.image.load("assets/button_background.png"), pos=(600, 250), text_input="PLAY",
                             font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 40), base_color="#d7fcd4",
                             hovering_color="White")
        # Create the 'GAME_MODE' button
        game_mode_button = Button(image=pygame.image.load("assets/button_background.png"), pos=(600, 400),
                                  text_input="GAME MODE", font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 40),
                                  base_color="#d7fcd4", hovering_color="White")
        # Create the 'QUIT' button
        quit_button = Button(image=pygame.image.load("assets/button_background.png"), pos=(600, 550), text_input="QUIT",
                             font=pygame.font.Font("assets/Font_SaintCarellClean.otf", 40), base_color="#d7fcd4",
                             hovering_color="White")

        # The color of the text displayed on the button changes if the mouse is on it
        for button in [play_button, game_mode_button, quit_button]:
            button.change_button_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Shut down the pygame library
                pygame.quit()
                # Exit the program
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()
                if game_mode_button.check_for_input(menu_mouse_pos):
                    game_mode()
                if quit_button.check_for_input(menu_mouse_pos):
                    # Shut down the pygame library
                    pygame.quit()
                    # Exit the program
                    sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
