# -*- coding:utf-8 -*-

from sys import exit
from random import randint

class Scene(object):      # scene类
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()
        exit(1)
        
class Engine(object):
    def __inif__(self, scene_map):       #  为什么有这个？
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()     
        last_scene = self.scene_map.next_scene('finished')       
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
            # be sure to print out the last scene
            current_scene.enter()
        
       
class Death(Scene):        # death是scene类
    def enter(self):       # 为什么还要再定义enter函数？
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
        
        
class Map(object):            # Map类
    def __inif__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
        
a_map = Map('central_corridor')        # central corridor是一个map，也是一个scene？
a_game = Engine(a_map)           
a_game.play()
