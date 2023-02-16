# Created By : AreebAmir
# Date : 16/2/2023

# Warning:- Anythin happen wrong to computer and your device or anyting you are using this code. We are not reponsible of any damages.

import pygame
import serial

# Initialize Pygame and create a screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Airplane Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create a font for displaying text
font = pygame.font.Font(None, 30)

# Create a rectangle to represent the airplane
plane_rect = pygame.Rect(0, 0, 30, 120)

# Connect to the Arduino and start the main loop
ser = serial.Serial('COM19', 115200)  # Replace 'COM3' with the appropriate port name for your system
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Read the data from the Arduino and split it into x, y, and z values
    data = ser.readline().decode().strip()
    # x, y, z = [int(v.split(":")[1]) for v in data.split()]
    try:
        x, y, z = [int(v.split(":")[1].split(".")[0]) if ':' in v else 0 for v in data.split(',')]
        print(f"x={x}, y={y}, z={z}")
    except ValueError:
        print("Invalid data format")

    # Move the plane by x and y pixels
    new_x = plane_rect.x - x
    new_y = plane_rect.y - y

    # Check if the plane is going out of the screen and adjust its position
    if new_x < 0:
        new_x = 0
    elif new_x + plane_rect.width > screen.get_width():
        new_x = screen.get_width() - plane_rect.width

    if new_y < 0:
        new_y = 0
    elif new_y + plane_rect.height > screen.get_height():
        new_y = screen.get_height() - plane_rect.height

    # Update the position of the airplane rectangle
    plane_rect.topleft = (new_x, new_y)

    # Draw the airplane rectangle and a line to represent the z-axis
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, plane_rect)
    pygame.draw.line(screen, RED, (400, 300), (400 + z, 300), 5)

    # Draw the x, y, and z values on the screen
    text = font.render(f"X: {x}, Y: {y}, Z: {z}", True, BLACK)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.update()
