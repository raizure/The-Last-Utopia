import pygame, sys, ptext, pickle, random, collections
from pygame.locals import *
from images import *
from maps import *
from items import *
from menu import *
from enemies import *

class player():
    def __init__(self,x,y,speed,facing,equips,stats,canMove,effects):
        self.x = x
        self.y = y
        self.speed = speed
        self.facing = facing
        self.equips = equips
        self.stats = stats
        self.canMove = canMove
        self.effects = effects
#player stats
player.x = 75
player.y = 75
player.speed = 0.5
player.facing = 2
rolling = False
rollcounter = 0
player_anim = 0
player_anim2 = 0
playerRect = pygame.Rect((67.5,60,15,30))
player.equips = [None,None,None,None,None,None]
#player stats and skills
player.stats = [0,0,0,0,0]
player.skills = [0,0,0,0,0]
#status effects
player.effects = []
player.canMove = True
player_name = "James"

#time settings
time_frame = 0
minute = 0
hour = 6
day = 1
month = 3
year = 1
season = 1

#menu settings
menu = 0
menu_selection = 0
cursor_item = None
saved_item = None
show_ui = True

#weapon settings
weapon_rotation = 0
weapon_layer = 0

#controls how bright it is at night
lighting = 0

#hp and other stuff
max_hp = 90
hp = max_hp
max_hunger = 72
hunger = max_hunger
max_thirst = 72
thirst = max_thirst
max_sleep = 24
sleep = max_sleep
coins = 0
multiple_coins = "s"

time_num = "0"
time_text = "AM"

#item/weapon stats
use_time = 0
using = False
weapon_loc = (82.5,75)
held_item = None
selected_item = 0

#lists of entities
enemy_list = []
drop_list = []
forage_list = []

#S.T.A.L.E.
#STEALTH, TACT, AGILITY, LUCK, ENDURANCE
james_stats = [7,6,3,6,3]
dane_stats = [3,3,6,7,6]

#B.R.E.A.D.
#BUILDING, ROBOTICS, ENGINEERING, AVIATION, DEMOLITION
james_skills = [7,3,3,7,5]
dane_skills = [5,7,7,3,3]

stat_multipliers = [0,0,0,0,0,0,0,0,0]
stat_increases = [0,0,0,0,0,0,0,0,0]

james_armour = [None,green_overcoat,jeans,boots,None,None]
dane_armour = []

player.equips = james_armour
player.stats = james_stats
player.skills = james_skills

inv = []

day_hours = [[6,7,8,9,10,11,12,13,14,15,16,17,18,19],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19],
             [6,7,8,9,10,11,12,13,14,15,16]]

menu_buttons = [[pygame.Rect(0,0,120,60),0],[pygame.Rect(120,0,120,60),1],[pygame.Rect(240,0,120,60),2],[pygame.Rect(360,0,120,60),3]]
inventory_Rects = [[pygame.Rect(0,60,60,60),0],[pygame.Rect(60,60,60,60),1],[pygame.Rect(120,60,60,60),2],[pygame.Rect(180,60,60,60),3],[pygame.Rect(240,60,60,60),4],[pygame.Rect(300,60,60,60),5],[pygame.Rect(360,60,60,60),6],[pygame.Rect(420,60,60,60),7],[pygame.Rect(480,60,60,60),8],[pygame.Rect(540,60,60,60),9]]
equipment_Rects = [[pygame.Rect(0,120,60,60),0,"head"],[pygame.Rect(0,180,60,60),1,"body"],[pygame.Rect(0,240,60,60),2,"legs"],[pygame.Rect(0,300,60,60),3,"shoes"],[pygame.Rect(60,120,60,60),4,"acc"],[pygame.Rect(60,180,60,60),5,"acc"]]

tile_anim = 0

#colours for fonts
gray = (145,145,145)
white = (255,255,255)
dodgerblue = (30,144,255)
mintgreen = (30,255,144)
orange = (255,144,30)
red = (255,45,45)
purple = (255,30,255)
cyan = (30,255,255)
magenta = (255,0,255)
font_c_list = [gray,white,dodgerblue,mintgreen,orange,red,purple,cyan]

player_speed = 0.5
player_speed2 = 1

#font stuff
pygame.font.init()
font1 = "Segoe UI"
font1_c = white
item_font = white
hp_font = white

#dialogue
talking = False

talking_images = []
text_list = ["Hello. My name is Thomas. But you can just call me Tom.",f"Nice to meet you. I'm {player_name}."]
talking_list = [2,1,]
talking_image_list = [2,1]

#player input
pressed = {}

#images
player_images = [[ju1,ju2,ju3,ju4,ju5,ju6,ju7,ju8],
                 [jl1,jl2,jl3,jl4,jl5,jl6,jl7,jl8],
                 [jd1,jd2,jd3,jd4,jd5,jd6,jd7,jd8],
                 [jr1,jr2,jr3,jr4,jr5,jr6,jr7,jr8]]

player_rolling_images = [[juroll1,juroll2,juroll3,juroll1,juroll2,juroll3,juroll1,juroll2],
                         [jlroll1,jlroll2,jlroll3,jlroll1,jlroll2,jlroll3,jlroll1,jlroll2],
                         [jdroll1,jdroll2,jdroll3,jdroll1,jdroll2,jdroll3,jdroll1,jdroll2],
                         [jrroll1,jrroll2,jrroll3,jrroll1,jrroll2,jrroll3,jrroll1,jrroll2]]

image_list = [item_log,item_knife,item_woodsword,item_bat,item_woodhammer,item_woodstaff,item_slingshot,item_woodhelm,item_woodchest,item_woodlegs,item_woodboots,item_snakemeat,item_cooked_snakemeat,item_burnt_snakemeat,item_battlesnake,item_blowpipe,item_torch,item_green_overcoat,item_jeans,item_boots]

tiles = [water,grass,grass_edge,pygame.transform.rotate(grass_edge,90),pygame.transform.rotate(grass_edge,180),pygame.transform.rotate(grass_edge,270),grass_corner,pygame.transform.rotate(grass_corner,90),pygame.transform.rotate(grass_corner,180),pygame.transform.rotate(grass_corner,270)]

#screen
display = pygame.display.set_mode((600,600))
screen = pygame.Surface((150,150))
citem = pygame.Surface((15,15),pygame.SRCALPHA)
c_item = pygame.transform.scale(citem,(60,60))
surf = pygame.transform.scale(screen,(600,600))
clock = pygame.time.Clock()
pygame.display.set_caption("The Last Utopia")
pygame.display.set_icon(icon)

game_map = map1

typing = False
message = ""

ht_level0 = [24,23,22,21,20,19]
ht_level1 = [18,17,16,15,14,13]
ht_level2 = [12,11,10,9,8,7]
ht_level3 = [6,5,4,3,2,1]
ht_level4 = [0]
h_stages = ["Peckish","Hungry","Famished","Ravenous","Starving"]
t_stages = ["Fine","Thirsty","Dehydrated","Parched","Dead"]
s_stages = ["Sleepy","Sapped","Drained","Weary","Exhausted"]

h_text = ["You're starting to feel a little hungry.","You're hungry.","You could probably eat a horse.","You could probably eat a family of horses.","Eat something, before you die."]
t_text = ["You're doing just fine.","You're kind of thirsty.","You should probably drink something.","Drink something or die.","You're literally dead."]
s_text = ["You feel a little tired.","You're very tired.","Don't stay up all night!","Go to sleep. Right now.","Pulling an all-nighter, are we?"]
e_names = ["Sick","Burning","Poisoned","Venom"]
e_text = ["You feel under the weather.","Stop, drop, and roll!","You're poisoned.","Get the antidote!"]

month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
season_list = ["Spring","Summer","Autumn","Winter"]
month_ending_dates = [31,28,31,30,31,30,31,31,30,31,30,31]
season_ending_dates = [31,30,31,30]

hour_text = hour

am_range = [24,1,2,3,4,5,6,7,8,9,10,11]
pm_range = [12,13,14,15,16,17,18,19,20,21,22,23]

itemtext1 = ""
itemtext2 = ""
itemtext3 = ""
itemtext4 = ""
itemtext5 = ""
itemtext6 = ""
itemtext7 = ""

area_rects = []
tile_rects = []
song_list = [caverns,murky_waters]
area = 0

grass_tiles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

music_name = ""
music_mute = 0

crafting_list = [[log,knife],[log,log],[log,log,log],[log,log],[log,log],[log],[log,log,log],[log,log],[log,log],[snakemeat,log]]
craft_items = [wood_sword,baseball_bat,wood_hammer,wood_staff,slingshot,wood_helm,wood_platemail,wood_leggings,wood_boots,cooked_snakemeat]
craft_list = []
special_nums = [0]
tool_items = [knife]
items_craft = [[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]]
crafting_lengths = [[2,2,3,2,2,1,3,2,2,2]]

def change_music(music):
    global music_name
    if music_mute == 0:
        if music_name != music:
            pygame.mixer.music.unload()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(-1)
            music_name = music
    else:
        pygame.mixer.music.unload()
            
def add_item(inv,item):
    x = 0
    for thing in inv:
        if inv[x] != None:
            if len(inv) != x:
                x += 1
            
        else:
            inv[x] = item
            break
    
darkness_list = [night_shading,night_shading2]

def debug():
    debug_choice = input("Debug: 1: eval(), 2: exec() ")
    if debug_choice == "1":
        code = input("Debug: ")
        try:
            eval(code)
        except NameError:
            print("Debug: '" + str(code) + "' does not exist. Did you spell it right?")
        except SyntaxError:
            pass
        else:
            print(f"Debug: Successfully executed command '{code}'.")
    if debug_choice == "2":
        code = input("Debug: ")
        try:
            exec(code)
        except SyntaxError:
            pass
        else:
            print(f"Debug: Successfully executed command '{code}'.")
            
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, tiles):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if player.facing == "right":
            rect.right = tile.left
            collision_types["right"] = True
        elif player.facing == "left":
            rect.left = tile.right
            collision_types["left"] = True
        elif player.facing == "up":
            rect.top = tile.bottom
            collision_types["top"] = True
        elif player.facing == "down":
            rect.bottom = tile.top
            collision_types["bottom"] = True
    return rect, collision_types

def enemymove(rect, tiles):
    ecollision_types = {"top": False, "bottom": False, "right": False, "left": False}
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if enemy.facing == "right":
            rect.right = tile.left
            ecollision_types["right"] = True
        elif enemy.facing == "left":
            rect.left = tile.right
            ecollision_types["left"] = True
        elif enemy.facing == "up":
            rect.top = tile.bottom
            ecollision_types["top"] = True
        elif enemy.facing == "down":
            rect.bottom = tile.top
            ecollision_types["bottom"] = True
    return rect, ecollision_types

def craft(inv,num,craft_list):
    x = 0
    y = 0
    z = 0
    saved_nums = []
    craft_list = []
    for item in inv:
        try:
            if item == crafting_list[num][y]:
                saved_nums.append(x)
                craft_list.append(inv[x])
                y += 1
            x += 1
        except IndexError:
            pass
    if sorted(craft_list) == sorted(crafting_list[num]):
        for thing in saved_nums:
            for item in inv:
                if inv[saved_nums[z]] not in tool_items:
                    inv[saved_nums[z]] = None
            z += 1
        add_item(inv,craft_items[num])
                
            
item_list = [log,snakemeat]

while True:
    citem = pygame.Surface((15,15),pygame.SRCALPHA)
    
    try:
        held_item = inv[selected_item]
    except:
        itemtext1 = ""
    
    lighting = 0
    
    if held_item == torch:
        lighting = 1
        
    if hp <= 0:
        menu = 3
    
    if menu == 1:
        change_music(menu_theme)
    
    if menu == 0:
        if hour in day_hours[season-1]:
            change_music(song_list[area])
        else:
            change_music(nightfall)
            
    if menu == 3:
        change_music(game_over_theme)

    if hp <= max_hp/4:
        hp_font = red
    if hp >= max_hp - round(max_hp/4):
        hp_font = white
    if hp >= max_hp:
        hp_font = mintgreen
    
    try:
        if not inv[selected_item]:
            itemtext1 = ""
            itemtext2 = ""
            itemtext3 = ""
            itemtext4 = ""
            itemtext5 = ""
            itemtext6 = ""
            itemtext7 = ""
    except IndexError:
        itemtext1 = ""
        itemtext2 = ""
        itemtext3 = ""
        itemtext4 = ""
        itemtext5 = ""
        itemtext6 = ""
        itemtext7 = ""
    
    if len(inv) < 10:
        inv.append(None)
    
    if hp > max_hp:
        hp = max_hp
    if hunger > max_hunger:
        hunger = max_hunger
    if thirst > max_thirst:
        thirst = max_thirst
    if sleep > max_sleep:
        sleep = max_sleep
    
    healthbar_width = round(max_hp*1.5)
    healthbar_width2 = round(hp*1.5)
    
    if minute < 10:
        time_num = "0"
    else:
        time_num = ""
        
    if hour in am_range:
        time_text = "AM"
        if hour != 24:
            hour_text = hour
        else:
            hour_text = hour - 12
    if hour in pm_range:
        time_text = "PM"
        if hour != 12:
            hour_text = hour - 12
        else:
            hour_text = hour
            
    if coins == 1 or coins == -1:
        multiple_coins = ""
    else:
        multiple_coins = "s"
    
    if tile_anim == 0:
        grass_edge = grass_edge1
        grass_corner = grass_corner1
        grass_inner = grass_inner1
    if tile_anim == 20:
        grass_edge = grass_edge2
        grass_corner = grass_corner2
        grass_inner = grass_inner2
    if tile_anim == 40:
        grass_edge = grass_edge3
        grass_corner = grass_corner3
        grass_inner = grass_inner3
    if tile_anim == 60:
        tile_anim = -1
    tile_anim += 1
    
    tiles = [water,grass,grass_edge,pygame.transform.rotate(grass_edge,90),pygame.transform.rotate(grass_edge,180),pygame.transform.rotate(grass_edge,270),grass_corner,pygame.transform.rotate(grass_corner,90),pygame.transform.rotate(grass_corner,180),pygame.transform.rotate(grass_corner,270),grass_inner,pygame.transform.rotate(grass_inner,90),pygame.transform.rotate(grass_inner,180),pygame.transform.rotate(grass_inner,270)]
    
    screen.fill((0,0,0))
    tile_rects = []
    area_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            screen.blit(tiles[tile],(x*15-player.x,y*15-player.y))
            x += 1
        y += 1
        
    for item in drop_list:
        item[2] = pygame.Rect(item[1][0]-player.x,item[1][1]-player.y,15,15)
        screen.blit(image_list[item[0][0][0]],(item[2]))
        
    for enemy in enemy_list:
        screen.blit(enemy.img, (enemy.x-player.x,enemy.y-player.y))
        enemy.animate(player)
            
    pressed1 = False
    pressed2 = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            pressed[event.key] = True
            
            if typing == True:
                message += event.unicode
                
                if event.key == K_BACKSPACE:
                    message = message[:-1]
            
            if event.key == K_t:
                hp -= 10
                hunger -= 8
                thirst -= 8
                
            if event.key == K_l:
                if player.canMove == True:
                    hour = 20
                
            if event.key == K_i:
                if player.canMove == True:
                    debug()
                    
            if event.key == K_q:
                add_item(inv,item_list[random.randint(0,1)])
                
            if event.key == K_u:
                craft(inv,1,craft_list)
                
            if event.key == K_g:
                spawn_enemy(game_map,enemy_list)
                
            if event.key == K_h:
                hp = max_hp
                hunger = max_hunger
                thirst = max_thirst
                
            if event.key == K_e:
                for item in drop_list:
                    if item[2].colliderect(playerRect):
                        add_item(inv,item[0])
                        drop_list.remove(item)
            if event.key == K_LSHIFT:
                if player.canMove == True:
                    if rolling == False and rollcounter == 0:
                        rolling = True
                        player_anim = 0
                        player_anim2 = 0
            if event.key == K_TAB:
                if menu == 0:
                    menu = 1
                elif menu == 1:
                    menu = 0
            if event.key == K_RETURN:
                if menu == 0:
                    if typing == False:
                        typing = True
                        player.canMove = False
                    elif typing == True:
                        typing = False
                        player.canMove = True
            if event.key == K_1:
                selected_item = 0
            if event.key == K_2:
                selected_item = 1
            if event.key == K_3:
                selected_item = 2
            if event.key == K_4:
                selected_item = 3
            if event.key == K_5:
                selected_item = 4
            if event.key == K_6:
                selected_item = 5
            if event.key == K_7:
                selected_item = 6
            if event.key == K_8:
                selected_item = 7
            if event.key == K_9:
                selected_item = 8
            if event.key == K_0:
                selected_item = 9
        if event.type == KEYUP:
            pressed[event.key] = False
            player_anim = 0
            player_anim2 = 0
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pressed1 = True
            if event.button == 3:
                pressed2 = True
            try:
                if event.button == 4:
                    if inv[selected_item+1]:
                        selected_item += 1
                if event.button == 5:
                    if inv[selected_item-1]:
                        selected_item -= 1
            except IndexError:
                pass
            
    if menu == 0:
        if player.canMove == True:
            if pressed.get(K_w) or pressed.get(K_UP):
                player.y -= player.speed
                player.facing = 0
                player_anim += 1
            elif pressed.get(K_a) or pressed.get(K_LEFT):
                player.x -= player.speed
                player.facing = 1
                player_anim += 1
            elif pressed.get(K_s) or pressed.get(K_DOWN):
                player.y += player.speed
                player.facing = 2
                player_anim += 1
            elif pressed.get(K_d) or pressed.get(K_RIGHT):
                player.x += player.speed
                player.facing = 3
                player_anim += 1
        
    if pressed1 == True:
        if held_item:
            if menu == 0:
                if held_item[0][1] == "weapon":
                    use_time = held_item[1][7]
                    using = True
                if held_item[0][1] == "consumable":
                    hp += held_item[1][0]
                    hunger += held_item[1][1]
                    thirst += held_item[1][2]
                    sleep += held_item[1][3]
                    try:
                        player.effects.append([held_item[1][4],held_item[1][5]])
                    except IndexError:
                        pass
                    inv[selected_item] = None
            
    if player_anim == 5:
        player_anim2 = 1
    if player_anim == 10:
        player_anim2 = 2
    if player_anim == 15:
        player_anim2 = 3
    if player_anim == 20:
        player_anim2 = 4
    if player_anim == 25:
        player_anim2 = 5
    if player_anim == 30:
        player_anim2 = 6
    if player_anim == 35:
        player_anim2 = 7
    if player_anim == 40:
        player_anim2 = 1
        player_anim = 0
    playerRect = pygame.Rect((player.x,player.y+15,15,15))
    if rolling == False:
        playeranim2 = 5
        playerImg = player_images[player.facing][player_anim2]
    if rolling == True:
        playerImg = player_rolling_images[player.facing][player_anim2]
        player.speed = player_speed2
        rollcounter += 1
        if rollcounter == 60:
            rolling = False
            rollcounter = 0
            player.speed = player_speed
            
    if using == True:
        weapon_rect = pygame.Rect(weapon_loc[0],weapon_loc[1],15,15)
        for enemy in enemy_list:
            if enemy.rect.colliderect(weapon_rect):
                damage_rng = random.randint(held_item[1][1],held_item[1][2])
                crit_rng = random.randint(1,100-player.stats[3])
                if crit_rng <= held_item[1][3]:
                    damage_rng = damage_rng * 3
                enemy.hp -= damage_rng
                enemy.check_health(drop_list,enemy_list,player)
                using = False
                print(f"{damage_rng}")
        use_time -= 1
    
    try:
        item_Img = pygame.transform.rotate(image_list[held_item[0][0]],weapon_rotation)
        if weapon_layer == 0:
            if held_item[0][1] == "weapon":
                if held_item[1][0] == "melee":
                    screen.blit(item_Img,(weapon_loc))
    except TypeError:
        item_img = None
        
    screen.blit(playerImg,(67.5,60))
    
    try:
        if weapon_layer == 1:
            if held_item[0][1] == "weapon":
                if held_item[1][0] == "melee":
                    screen.blit(item_Img,(weapon_loc))
    except TypeError:
        pass
    
    if player.facing == 0:
        weapon_loc = (67.5,61.5)
        weapon_rotation = 45
        weapon_layer = 0
    if player.facing == 1:
        weapon_loc = (52.5,72.5)
        weapon_rotation = 135
        weapon_layer = 0
    if player.facing == 2:
        weapon_loc = (61.5,80.5)
        weapon_rotation = 225
        weapon_layer = 1
    if player.facing == 3:
        weapon_loc = (70.5,72.5)
        weapon_rotation = 315
        weapon_layer = 1
    
    if hour not in day_hours[season-1]:
        screen.blit(darkness_list[lighting],(0,0))
    
    if menu == 0:    
        time_frame += 1
    if time_frame == 60:
        minute += 1
        time_frame = 0
    if minute == 60:
        hour += 1
        hunger -= 1
        if season == 4:
            hunger -= 1
        thirst -= 1
        if season == 2:
            thirst -= 1
        sleep -= 1
        minute = 0
    if hour == 24:
        day += 1
        hour = 1
    if day > month_ending_dates[month-1]:
        day = 1
        month += 1
    if month > 12:
        year += 1
        month = 1
        day = 1
        
    
    screen.blit(hotbar,(0,135))
    screen.blit(heart,(0,0))
    x = 0
    for item in inv:
        try:
            screen.blit(image_list[item[0][0]],(x*15,135))
        except TypeError:
            pass
        x += 1
    try:
        screen.blit(menu_cursor,(selected_item*15,135))
    except TypeError:
        pass
        
    mouseRect = pygame.mouse.get_pos()
    update_menu(screen,image_list,menu,inv,player,selected_item,menu_cursor)
    if menu == 1:
        itemtext1 = ""
        itemtext2 = ""
        itemtext3 = ""
        itemtext4 = ""
        itemtext5 = ""
        itemtext6 = ""
        itemtext7 = ""
        if cursor_item != None:
            citem.blit(image_list[cursor_item[0][0]],(0,0))
        for rect in inventory_Rects:
            if rect[0].collidepoint(mouseRect):
                if pressed1:
                    if selected_item == rect[1]:
                        if cursor_item == None:
                            try:
                                cursor_item = inv[rect[1]]
                                saved_item = inv[rect[1]]
                                inv[rect[1]] = None
                            except IndexError:
                                pass
                        else:
                            try:
                                if inv[rect[1]] == None:
                                    inv[rect[1]] = cursor_item
                                    saved_item = None
                                    cursor_item = None
                                else:
                                    saved_item = cursor_item
                                    cursor_item = inv[rect[1]]
                                    inv[rect[1]] = saved_item
                                    saved_item = None
                            except IndexError:
                                pass
                    else:
                        selected_item = rect[1]
                elif pressed2:
                    if selected_item == rect[1]:
                        if inv[selected_item]:
                            inv[rect[1]] = None
        try:
            item_font = font_c_list[held_item[0][4]]
            itemtext1 = held_item[0][2]
            itemtext2 = held_item[0][3]
            if held_item[0][1] == "weapon":
                itemtext3 = f"Deals {held_item[1][1]}-{held_item[1][2]} {held_item[1][0]} damage."
                itemtext4 = f"{held_item[1][3]}% critical hit chance."
                try:
                    itemtext5 = f"{held_item[1][11]}"
                except IndexError:
                    pass
            if held_item[0][1] == "armour":
                itemtext3 = f"{held_item[1][1]} defense."
            if held_item[0][1] == "consumable":
                consumable_text = f""
                if held_item[1][0] != 0:
                    consumable_text += f"Heals {held_item[1][0]} HP. "
                if held_item[1][1] != 0:
                    consumable_text += f"Heals {held_item[1][1]} hunger. "
                if held_item[1][2] != 0:
                    consumable_text += f"Replenishes {held_item[1][2]} thirst. "
                itemtext3 = consumable_text
                if held_item[1][4] != 0:
                    itemtext6 = f"{held_item[1][6]}"
            if held_item[0][5] > -1:
                itemtext7 = f"Can be sold for {held_item[0][5]} coins."
            else:
                itemtext7 = "Cannot be sold."
        except TypeError:
            pass
        for button in menu_buttons:
            if button[0].collidepoint(mouseRect):
                if pressed1:
                    menu_selection = button[1]
        if menu_selection == 0:
            screen.blit(heart, (0, 31))
            screen.blit(empty_healthbar, (16,31))
            x = 0
            for i in range(hp):
                screen.blit(healthbar_segment,(17+x,31))
                x += 1
            screen.blit(drumstick, (0,46))
            screen.blit(emptybar,(16,46))
            x = 0
            for i in range(hunger):
                screen.blit(hungerbar_segment,(17+x,46))
                x += 1
            screen.blit(droplet, (0,61))
            screen.blit(emptybar,(16,61))
            x = 0
            for i in range(thirst):
                screen.blit(thirstbar_segment,(17+x,61))
                x += 1
            screen.blit(coin, (1,77))
            screen.blit(clock_img, (0,91))
        if menu_selection == 1:
            screen.blit(equipsmenu, (0, 0))
            if player.equips[0]:
                screen.blit(image_list[player.equips[0][0][0]], (0, 30))
            if player.equips[1]:
                screen.blit(image_list[player.equips[1][0][0]], (0, 45))
            if player.equips[2]:
                screen.blit(image_list[player.equips[2][0][0]], (0, 60))
            if player.equips[3]:
                screen.blit(image_list[player.equips[3][0][0]], (0, 75))
            if player.equips[4]:
                screen.blit(image_list[player.equips[4][0][0]], (15, 30))
            if player.equips[5]:
                screen.blit(image_list[player.equips[5][0][0]], (15, 45))
            for rect in equipment_Rects:
                if rect[0].collidepoint(mouseRect):
                    if pressed1:
                        if player.equips[rect[1]] != None:
                            if not cursor_item:
                                cursor_item = player.equips[rect[1]]
                                player.equips[rect[1]] = None
                            else:
                                if cursor_item[0][1] == "armour":
                                    if cursor_item[1][0] == rect[2]:
                                        saved_item = player.equips[rect[1]]
                                        player.equips[rect[1]] = cursor_item
                                        cursor_item = saved_item
                                        saved_item = None
                        else:
                            if cursor_item:
                                if cursor_item[0][1] == "armour":
                                    if cursor_item[1][0] == rect[2]:
                                        player.equips[rect[1]] = cursor_item
                                        cursor_item = None
                
        if menu_selection == 2:
            screen.blit(savemenu, (0, 0))
        if menu_selection == 3:
            screen.blit(craftingmenu, (0, 0))
            crafting_Rects = []
            x = 0
            y = 2
            for item in craft_items:
                screen.blit(image_list[item[0][0]],(x*15,y*15))
                crafting_Rects.append([pygame.Rect(x*60,y*60,60,60),items_craft[y-2][x],[[y-2],[x]],x])
                x += 1
            if x > 9:
                x = 0
                y += 1
            for rect in crafting_Rects:
                z = 0
                if rect[0].collidepoint(mouseRect):
                    crafting_desc = f"Requires: "
                    for item in crafting_list[rect[1]]:
                        if z != crafting_lengths[rect[2][0][0]][rect[2][1][0]]-1:
                            crafting_desc += f"{crafting_list[rect[1]][z][0][2]}, "
                        else:
                            crafting_desc += f"{crafting_list[rect[1]][z][0][2]}."
                        z += 1
                    item_font = font_c_list[craft_items[rect[3]][0][4]]
                    itemtext1 = f"{craft_items[rect[3]][0][2]}"
                    itemtext2 = f"{craft_items[rect[3]][0][3]}"
                    itemtext3 = crafting_desc
                    itemtext4 = ""
                    itemtext5 = ""
                    itemtext6 = ""
                    itemtext7 = ""
                    if pressed1:
                        craft(inv,rect[1],craft_list)
        
    if menu == 3:
        screen.blit(game_over,(0,0))
    
    surf = pygame.transform.scale(screen,(600,600))
    c_item = pygame.transform.scale(citem,(60,60))
    display.blit(surf,(0,0))
    if menu == 1:
        mouse_Rect = pygame.Rect(mouseRect[0]-15,mouseRect[1]-15,0,0)
        display.blit(c_item,mouse_Rect.topleft)
    
    if menu == 1:
        ptext.draw(f"{itemtext1}",(4,464),sysfontname=font1,fontsize=24,color=item_font)
        ptext.draw(f"{itemtext2}",(4,488),sysfontname=font1,fontsize=16,color=white)
        ptext.draw(f"{itemtext3}",(4,504),sysfontname=font1,fontsize=16,color=white)
        ptext.draw(f"{itemtext4}",(4,520),sysfontname=font1,fontsize=16,color=white)
        ptext.draw(f"{itemtext5}",(4,536),sysfontname=font1,fontsize=16,color=white)
        ptext.draw(f"{itemtext6}",(4,552),sysfontname=font1,fontsize=16,color=white)
        ptext.draw(f"{itemtext7}",(4,568),sysfontname=font1,fontsize=16,color=white)
        if menu_selection == 0:
            ptext.draw(f"{hp} / {max_hp} HP",(67.5,135), sysfontname=font1, fontsize=36,color=hp_font)
            ptext.draw(f"{hunger} / {max_hunger} Hunger",(67.5,195), sysfontname=font1, fontsize=36,color=font1_c)
            ptext.draw(f"{thirst} / {max_thirst} Thirst",(67.5,255), sysfontname=font1, fontsize=36,color=font1_c)
            ptext.draw(f"{coins} Dollar{multiple_coins}",(67.5,315), sysfontname=font1, fontsize=36, color=font1_c)
            ptext.draw(f"{month_list[month-1]} {day}, Year {year}", (67.5,367.5), sysfontname=font1, fontsize=18,color=font1_c)
            ptext.draw(f"{hour_text}:{time_num}{minute} {time_text}", (67.5,382.5), sysfontname=font1, fontsize=18,color=font1_c)
            ptext.draw(f"{season_list[season-1]}", (67.5,397.5), sysfontname=font1, fontsize=18,color=font1_c)

    if menu == 0:
        ptext.draw(f"{hp} / {max_hp} HP",(60,0),sysfontname=font1,fontsize=36,color=hp_font)

    clock.tick(60)
    pygame.display.update()