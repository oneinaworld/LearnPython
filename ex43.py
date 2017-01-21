# -*- coding:utf-8 -*-

from sys import exit
from random import randint

class Scene(object):      # scene类
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()
        exit(1)
        
class Engine(object):
    def __inif__(self, scene_map):
        pass
        
    def play(self):
        pass
        
       
class Death(Scene):        # death是scene类
    def enter(self):
        pass
        
        
class CentralCorridor(Scene):    # centralcorridor是scene类
    def enter(self):
        pass
        
        
class LaserWeaponArmory(Scene):     # laserweaponarmory是scene类
    def enter(self):
        pass
        
        
class TheBridge(Scene):        # thebridge是scene类
    def enter(self):
        pass
        
        
class EscapePod(Scene):        # escapepod是scene类
    def enter(self):
        pass
        
        
class Map(object):
    def __inif__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
