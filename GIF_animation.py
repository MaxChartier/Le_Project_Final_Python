import pygame


# Flower class
class Flower(pygame.sprite.Sprite):
    """To animate the flower."""

    def __init__(self, pos_x, pos_y):
        """Initialize the array with the flower's sprites."""

        super().__init__()

        self.sprites_flower = []

        # Define the size of the sprites (in pixels)
        gif_size = (80, 80)

        # Import and resize sprites
        sprite_flower_0 = pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower0.png").convert_alpha()
        sprite_flower_0 = pygame.transform.scale(sprite_flower_0, gif_size)

        sprite_flower_1 = pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower1.png").convert_alpha()
        sprite_flower_1 = pygame.transform.scale(sprite_flower_1, gif_size)

        # Put the sprites in the sprites array
        self.sprites_flower.append(sprite_flower_0)
        self.sprites_flower.append(sprite_flower_1)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_flower[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_flower):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_flower[int(self.actual_sprite)]


# Zombie class
class Zombie(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_zombie = []

        # Define the size of the sprites (in pixels)
        gif_size = (60, 60)

        # Import and resize images
        sprite_zombie_0 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie0.png").convert_alpha()
        sprite_zombie_0 = pygame.transform.scale(sprite_zombie_0, gif_size)

        sprite_zombie_1 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie1.png").convert_alpha()
        sprite_zombie_1 = pygame.transform.scale(sprite_zombie_1, gif_size)

        sprite_zombie_2 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie2.png").convert_alpha()
        sprite_zombie_2 = pygame.transform.scale(sprite_zombie_2, gif_size)

        sprite_zombie_3 = pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie3.png").convert_alpha()
        sprite_zombie_3 = pygame.transform.scale(sprite_zombie_3, gif_size)

        # Put the sprites in the sprites array
        self.sprites_zombie.append(sprite_zombie_0)
        self.sprites_zombie.append(sprite_zombie_1)
        self.sprites_zombie.append(sprite_zombie_2)
        self.sprites_zombie.append(sprite_zombie_3)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_zombie[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_zombie):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_zombie[int(self.actual_sprite)]


# Spider class
class Spider(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_spider = []

        # Define the size of the sprites (in pixels)
        gif_size = (60, 60)

        # Import and resize images
        sprite_spider_00 = pygame.image.load("PNJ/spider/spider/sprite_spider00.png").convert_alpha()
        sprite_spider_00 = pygame.transform.scale(sprite_spider_00, gif_size)

        sprite_spider_01 = pygame.image.load("PNJ/spider/spider/sprite_spider01.png").convert_alpha()
        sprite_spider_01 = pygame.transform.scale(sprite_spider_01, gif_size)

        sprite_spider_02 = pygame.image.load("PNJ/spider/spider/sprite_spider02.png").convert_alpha()
        sprite_spider_02 = pygame.transform.scale(sprite_spider_02, gif_size)

        sprite_spider_03 = pygame.image.load("PNJ/spider/spider/sprite_spider03.png").convert_alpha()
        sprite_spider_03 = pygame.transform.scale(sprite_spider_03, gif_size)

        sprite_spider_04 = pygame.image.load("PNJ/spider/spider/sprite_spider04.png").convert_alpha()
        sprite_spider_04 = pygame.transform.scale(sprite_spider_04, gif_size)

        sprite_spider_05 = pygame.image.load("PNJ/spider/spider/sprite_spider05.png").convert_alpha()
        sprite_spider_05 = pygame.transform.scale(sprite_spider_05, gif_size)

        sprite_spider_06 = pygame.image.load("PNJ/spider/spider/sprite_spider06.png").convert_alpha()
        sprite_spider_06 = pygame.transform.scale(sprite_spider_06, gif_size)

        sprite_spider_07 = pygame.image.load("PNJ/spider/spider/sprite_spider07.png").convert_alpha()
        sprite_spider_07 = pygame.transform.scale(sprite_spider_07, gif_size)

        sprite_spider_08 = pygame.image.load("PNJ/spider/spider/sprite_spider08.png").convert_alpha()
        sprite_spider_08 = pygame.transform.scale(sprite_spider_08, gif_size)

        sprite_spider_09 = pygame.image.load("PNJ/spider/spider/sprite_spider09.png").convert_alpha()
        sprite_spider_09 = pygame.transform.scale(sprite_spider_09, gif_size)

        sprite_spider_10 = pygame.image.load("PNJ/spider/spider/sprite_spider10.png").convert_alpha()
        sprite_spider_10 = pygame.transform.scale(sprite_spider_10, gif_size)

        sprite_spider_11 = pygame.image.load("PNJ/spider/spider/sprite_spider11.png").convert_alpha()
        sprite_spider_11 = pygame.transform.scale(sprite_spider_11, gif_size)

        sprite_spider_12 = pygame.image.load("PNJ/spider/spider/sprite_spider12.png").convert_alpha()
        sprite_spider_12 = pygame.transform.scale(sprite_spider_12, gif_size)

        # Put the sprites in the sprites array
        self.sprites_spider.append(sprite_spider_00)
        self.sprites_spider.append(sprite_spider_01)
        self.sprites_spider.append(sprite_spider_02)
        self.sprites_spider.append(sprite_spider_03)
        self.sprites_spider.append(sprite_spider_04)
        self.sprites_spider.append(sprite_spider_05)
        self.sprites_spider.append(sprite_spider_06)
        self.sprites_spider.append(sprite_spider_07)
        self.sprites_spider.append(sprite_spider_08)
        self.sprites_spider.append(sprite_spider_09)
        self.sprites_spider.append(sprite_spider_10)
        self.sprites_spider.append(sprite_spider_11)
        self.sprites_spider.append(sprite_spider_12)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_spider[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_spider):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_spider[int(self.actual_sprite)]


# Bee class
class Bee(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_bee = []

        # Define the size of the sprites (in pixels)
        gif_size = (160, 160)

        # Import and resize images
        sprite_bee_0 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee0.png").convert_alpha()
        sprite_bee_0 = pygame.transform.scale(sprite_bee_0, gif_size)

        sprite_bee_1 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee1.png").convert_alpha()
        sprite_bee_1 = pygame.transform.scale(sprite_bee_1, gif_size)

        sprite_bee_2 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee2.png").convert_alpha()
        sprite_bee_2 = pygame.transform.scale(sprite_bee_2, gif_size)

        sprite_bee_3 = pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee3.png").convert_alpha()
        sprite_bee_3 = pygame.transform.scale(sprite_bee_3, gif_size)

        # Put the sprites in the sprites array
        self.sprites_bee.append(sprite_bee_0)
        self.sprites_bee.append(sprite_bee_1)
        self.sprites_bee.append(sprite_bee_2)
        self.sprites_bee.append(sprite_bee_3)

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_bee[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_bee):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_bee[int(self.actual_sprite)]