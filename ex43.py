# -*- coding:utf-8 -*-

from sys import exit
from random import randint

class Scene(object):      # scene类
    def enter(self):      # 定义enter动作
        print "This scene is not yet configured. Subclass it and implement enter()
        exit(1)
        
class Engine(object):
    def __init__(self, scene_map):       # 每个engine类，默认有scene_map属性。
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()        # 当运行play时，定义现在的场景与scene_map的联系（opening_scene的动作在map中定义）
        last_scene = self.scene_map.next_scene('finished')    # 定义上一个场景与next_scene的联系（next_scene的动作在map中定义）
        
        while current_scene != last_scene:                    # 确保二者不是一个场景
            next_scene_name = current_scene.enter()           # 进入现在的场景后，即为下一个场景
            current_scene = self.scene_map.next_scene(next_scene_name)      # 定义现在的场景与下一个场景名字的联系
            
            # be sure to print out the last scene
            current_scene.enter()                             # 进入现在的场景
        
       
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
