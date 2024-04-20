import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Animation')

# Load the car image
car_image = pygame.image.load('car.png')
car_rect = car_image.get_rect()
car_rect.x = 0
car_rect.y = height // 2  # Center the car vertically

# Set the background color
background_color = (150, 150, 150)

# Set the speed of the car
car_speed = 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the car's position
    car_rect.x += car_speed
    if car_rect.right > width:  # Reset position after crossing the screen
        car_rect.x = -car_rect.width

    # Fill the screen with the background color
    screen.fill(background_color)

    # Blit the car image on the screen
    screen.blit(car_image, car_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
