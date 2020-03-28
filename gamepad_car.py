from gpiozero import Motor
import pygame

steering = Motor(forward=4, backward=14)
motor = Motor(forward=17, backward=18)

#initializes pygame
pygame.init()

#creates a controller object
controller = pygame.joystick.Joystick(0)

#initializes the controller
controller.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if controller.get_axis(0) < 0:
                print(controller.get_axis(0))
                steering.forward()
            elif controller.get_axis(0) > 0:
                print(controller.get_axis(0))
                steering.backward()
            elif controller.get_axis(0) == 0:
                steering.stop()
                
            if event.type == pygame.JOYBUTTONDOWN:
                if controller.get_button(0):
                    print("X Pressed")
                elif controller.get_button(1):
                    print("Circle Pressed")
                elif controller.get_button(2):
                    print("Triangle Pressed")
                elif controller.get_button(3):
                    print("Square Pressed")
                elif controller.get_button(4):
                    print("L1 Pressed")
                elif controller.get_button(5):
                    print("R1 Pressed")
                elif controller.get_button(6):
                    print("L2 Pressed")
                    motor.backward()
                elif controller.get_button(7):
                    print("R2 Pressed")
                    motor.forward()
                elif controller.get_button(8):
                    print("SHARE Pressed")
                elif controller.get_button(9):
                    print("OPTIONS Pressed")
                elif controller.get_button(10):
                    print("Power Button Pressed")
                elif controller.get_button(11):
                    print("Left Analog (L3) Pressed")
                elif controller.get_button(12):
                    print("Right Analog (R3) Pressed")

            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")
                motor.stop()

except KeyboardInterrupt:
    print("EXITING NOW")
    controller.quit()
