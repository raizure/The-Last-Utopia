import pygame, random
from images import *
from items import *

spawnable_tiles = [1]

class enemy():
    def __init__(self,x,y,speed,hp,maxhp,defense,atk,facing,ai,drops,dropchances,anim,img,name,enemy_id,area):
        self.x = x
        self.y = y
        self.speed = speed
        self.hp = hp
        self.maxhp = maxhp
        self.defense = defense
        self.atk = atk
        self.facing = facing
        self.ai = ai
        self.drops = drops
        self.dropchances = dropchances
        self.anim = anim
        self.img = img
        self.name = name
        self.enemy_id = enemy_id
        self.area = area
        self.rect = pygame.Rect(self.x,self.y+11,15,4)
    def animate(self,player):
        self.anim += 1
        if self.name == "tattlesnake":
            self.rect = pygame.Rect(self.x-player.x,self.y+11-player.y,15,4)
            if self.facing == 0:
                self.x -= self.speed
                if self.anim == 0:
                    self.img = snakel1
                if self.anim == 5:
                    self.img = snakel2
                if self.anim == 10:
                    self.img = snakel3
                if self.anim == 15:
                    self.img = snakel4
                if self.anim == 20:
                    self.anim = 0
            if self.facing == 1:
                self.x += self.speed
                if self.anim == 0:
                    self.img = snaker1
                if self.anim == 5:
                    self.img = snaker2
                if self.anim == 10:
                    self.img = snaker3
                if self.anim == 15:
                    self.img = snaker4
                if self.anim == 20:
                    self.anim = 0
                    
    def check_health(self,drop_list,enemylist,player):
        if self.hp < 0:
            x = 0
            for drop in self.drops:
                dropchance = random.randint(self.dropchances[x][0],self.dropchances[x][1])
                if dropchance == 1:
                    drop_list.append([self.drops[x],(self.x,self.y),pygame.Rect(self.x-player.x,self.y-player.y,15,15)])
                x += 1
            enemylist.remove(self)

def spawn_enemy(gmap,enemy_list):
    try:
        spawn_x = random.randint(0,18)
        spawn_y = random.randint(0,16)
        if gmap[spawn_x][spawn_y] not in spawnable_tiles:
            spawn_enemy(gmap,enemy_list)
        else:
            enemy_list.append(enemy(spawn_x*15,spawn_y*15,0.25,45,45,3,5,random.randint(0,1),1,[snakemeat,battlesnake],[[1,2],[1,25]],0,snakel1,"tattlesnake",1,1))
    except IndexError:
        pass
