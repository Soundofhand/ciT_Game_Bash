import pygame
from pygame.math import Vector2
from constants import *


# 1 Tile ist 32 Pixel 
# Engster Raum ist 16 Pixel


class Enemies(pygame.sprite.Sprite):

    def __init__(self, path_nodes, enemy_image): #initializes an enemy object, takes the planned waypoints mapping and uses the first node as spawnpoint, takes a single image to spawn the enemy with
        pygame.sprite.Sprite.__init__(self)

        self.path_nodes = path_nodes
        self.position = Vector2(self.path_nodes[0]) #Starting position is first index position of path nodes, vector2 adds math to this shit
        self.target_node = 1  #placeholder, only goes to [1]
        self.image = enemy_image 
        self.rect = self.image.get_rect() #draws a rectangle for enemy position and for the enemy_image to slot in
        self.rect.center = self.position #centers the image
        #currently unused:
        self.name = "Untamed Aphid"
        self.health = 10 #* wave_modifier
        self.damage = 0 #* wave_modifier
        self.movement_speed = 1200 / TICK_RATE
        self.attribute = "None"

    def update(self):
        self.move_enemy

    def move_enemy(self):
        self.target = Vector2(self.path_nodes[self.target_node]) #currently only takes initialized target_node as next target 
        self.movement = self.target - self.position # does a delta between position and target for vector
        self.position += self.movement.normalize() #supposed to update by calculated vector after normalization, doesnt work rn
        self.rect.center = self.position #updates center 


    def draw_enemy_path():
        path_nodes = [        
            (50,50),
            (100,100),
            (150,100),
            (150,150),
            (200,150),
            (200,200)
        ]
        return path_nodes
                 

    def attack(self): #currently unused
        # implement attack logic here
        print(f"The {self.name} attacks you for {self.damage} damage!")


    def take_damage(self, amount): #currently unused
        self.health -= amount
        print(f"You hit the {self.name} for {amount} damage!")
        if self.health <= 0:
            print(f"The {self.name} has been defeated!")
