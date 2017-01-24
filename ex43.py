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
    quips = [
        "You died. You kina suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    
    def enter(self):       # 为什么还要再定义enter函数？
        print Death.quips[randint(0, len(self.quips)-1)]   # 为什么len(self.quips)要-1？
        exit(1)
        
        
class CentralCorridor(Scene):    # centralcorridor是scene类
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "you entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin , dark grimy teeth, and evil clown cost"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        
        action = raw_input("> ")
        
        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothorn."
            print "His clown costume is flowing and moving around his body, whick throws"
            print "off your aim. Your laser hits his costume but misses him entirely."
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the fac"
            print "you are dead. Then he eats you."
            return 'death'
        
        elif action == "dodge!":
            print "Like a world class boxer your dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "band your head on the metal wall and pass out."
            print "you wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'
        
        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf neghaq gur ubhfr, fur fvgf nebha"
            print "The Gothon stops, tries not to laugh, then busts out laughing and car"
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory"       
        
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'          # 又回到起点
        
        
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
