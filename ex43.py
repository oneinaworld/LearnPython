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
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in tis container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't "
        print "get the bomb. The code is 3digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))      # 随机生成密码
        guess = raw_input("[keypad]> ")        # 输入所猜密码
        guesses = 0                            # 猜的次数初始赋值0
        
        while guess != code and guesses < 10:        # 当猜不中时，且猜的次数小于10次时
            print "BZZZZEDDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:                      # 当猜中密码时
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'                # 下一关，桥
        else:                                  # 当猜不中时
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'                     # 死亡
        
        
class TheBridge(Scene):        # thebridge是scene类
    def enter(self):         
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to "
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        
        action = raw_input("> ")       # 弄出动静太大会死
        
        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a "
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You died knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        
        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off thei tin can."
            return 'escape_pod'
        esle:
            print "DOES NOT COMPUTE!"
            return "the_bridge"         # 为什么不是print，而是用return？return后为什么用字符串？
        
        
class EscapePod(Scene):        # escapepod是scene类
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look . There's 5 pods, which one"
        print "do you take?"
        
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")
        
        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            reutrn 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a "
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            
            return 'finished'
        

class Finished(Scene):            # 结束也是一个场景！
    
    def enter(self):
        print "You won! Good job."
        return 'finished'
        
        
class Map(object):            # Map类
    
    scenes = {                 # 用字典把前面类中return的结果与Scene类对应起来。为什么不直接return类呢？
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished(),
    }
    
    def __inif__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):        # 定义next_scene的动作，从Map中取得scene名，得到对应类名，并赋值给val
        val = Map.scenes.get(scene_name)      # 从Map类中所定义的字典中取得类名
        
    def opening_scene(self):           # 定义opening_scene的动作。在next_scene中运行start_scene参数
        return self.next_scene(self.start_scene)
        
        
        
a_map = Map('central_corridor')        # 载入第一张地图'central_corrridor'
a_game = Engine(a_map)                 # 载入第一个引擎，由第一张地图对应而来
a_game.play()                          # 执行引擎中play运作
