import pygame

icon = pygame.image.load("data/images/icon.png")

#player images
ju1 = pygame.image.load("data/images/ju1.png")
ju2 = pygame.image.load("data/images/ju2.png")
ju3 = pygame.image.load("data/images/ju3.png")
ju4 = pygame.image.load("data/images/ju4.png")
ju5 = pygame.image.load("data/images/ju5.png")
ju6 = pygame.image.load("data/images/ju6.png")
ju7 = pygame.image.load("data/images/ju7.png")
ju8 = pygame.image.load("data/images/ju8.png")
jl1 = pygame.image.load("data/images/jl1.png")
jl2 = pygame.image.load("data/images/jl2.png")
jl3 = pygame.image.load("data/images/jl3.png")
jl4 = pygame.image.load("data/images/jl4.png")
jl5 = pygame.image.load("data/images/jl5.png")
jl6 = pygame.image.load("data/images/jl6.png")
jl7 = pygame.image.load("data/images/jl7.png")
jl8 = pygame.image.load("data/images/jl8.png")
jd1 = pygame.image.load("data/images/jd1.png")
jd2 = pygame.image.load("data/images/jd2.png")
jd3 = pygame.image.load("data/images/jd3.png")
jd4 = pygame.image.load("data/images/jd4.png")
jd5 = pygame.image.load("data/images/jd5.png")
jd6 = pygame.image.load("data/images/jd6.png")
jd7 = pygame.image.load("data/images/jd7.png")
jd8 = pygame.image.load("data/images/jd8.png")
jr1 = pygame.image.load("data/images/jr1.png")
jr2 = pygame.image.load("data/images/jr2.png")
jr3 = pygame.image.load("data/images/jr3.png")
jr4 = pygame.image.load("data/images/jr4.png")
jr5 = pygame.image.load("data/images/jr5.png")
jr6 = pygame.image.load("data/images/jr6.png")
jr7 = pygame.image.load("data/images/jr7.png")
jr8 = pygame.image.load("data/images/jr8.png")
juroll = pygame.image.load("data/images/juroll.png")
juroll1 = pygame.image.load("data/images/juroll1.png")
juroll2 = pygame.image.load("data/images/juroll2.png")
juroll3 = pygame.image.load("data/images/juroll3.png")
jlroll = pygame.image.load("data/images/jlroll.png")
jlroll1 = pygame.image.load("data/images/jlroll1.png")
jlroll2 = pygame.image.load("data/images/jlroll2.png")
jlroll3 = pygame.image.load("data/images/jlroll3.png")
jdroll = pygame.image.load("data/images/jdroll.png")
jdroll1 = pygame.image.load("data/images/jdroll1.png")
jdroll2 = pygame.image.load("data/images/jdroll2.png")
jdroll3 = pygame.image.load("data/images/jdroll3.png")
jrroll = pygame.image.load("data/images/jrroll.png")
jrroll1 = pygame.image.load("data/images/jrroll1.png")
jrroll2 = pygame.image.load("data/images/jrroll2.png")
jrroll3 = pygame.image.load("data/images/jrroll3.png")
playerImg = jd1

woodraft = pygame.image.load("data/images/wood_raft.png")
item_woodraft = "data/images/item_wood_raft.png"

#enemy images
snakel1 = pygame.image.load("data/images/snakel1.png")
snakel2 = pygame.image.load("data/images/snakel2.png")
snakel3 = pygame.image.load("data/images/snakel3.png")
snakel4 = pygame.image.load("data/images/snakel4.png")
snaker1 = pygame.image.load("data/images/snaker1.png")
snaker2 = pygame.image.load("data/images/snaker2.png")
snaker3 = pygame.image.load("data/images/snaker3.png")
snaker4 = pygame.image.load("data/images/snaker4.png")

#tiles
grass = pygame.image.load("data/images/tile_grass.png")
grass_edge1 = pygame.image.load("data/images/tile006.png")
grass_edge2 = pygame.image.load("data/images/tile005.png")
grass_edge3 = pygame.image.load("data/images/tile004.png")
grass_edge = grass_edge1
grass_corner1 = pygame.image.load("data/images/tile009.png")
grass_corner2 = pygame.image.load("data/images/tile008.png")
grass_corner3 = pygame.image.load("data/images/tile007.png")
grass_corner = grass_corner1
grass_inner1 = pygame.image.load("data/images/tile_grasscorner_inner3.png")
grass_inner2 = pygame.image.load("data/images/tile_grasscorner_inner2.png")
grass_inner3 = pygame.image.load("data/images/tile_grasscorner_inner1.png")
grass_inner = grass_inner1
dock_down = pygame.image.load("data/images/tile_dock_down.png")
dock_right = pygame.image.load("data/images/tile_dock_right.png")
dock_up = pygame.image.load("data/images/tile_dock_up.png")
dock_up2 = pygame.image.load("data/images/dock_up_connected.png")
tile_anim = 0
water = pygame.image.load("data/images/tile_water.png")
crate = pygame.image.load("data/images/crate.png")
bush = "data/images/berry_bush.png"
bush_empty = "data/images/berry_bush_empty.png"
housefloor = pygame.image.load("data/images/housefloor.png")
housewall = pygame.image.load("data/images/housewall.png")
housecorner_nw = pygame.image.load("data/images/housecorner_nw.png")
housecorner_ne = pygame.image.load("data/images/housecorner_ne.png")
housecorner_sw = pygame.image.load("data/images/housecorner_sw.png")
housecorner_se = pygame.image.load("data/images/housecorner_se.png")
housedoor = pygame.image.load("data/images/housedoor.png")

#other
sign = pygame.image.load("data/images/sign.png")
smallsign = pygame.image.load("data/images/smallsign.png")
tinysign = pygame.image.load("data/images/tinysign.png")
dummy = pygame.image.load("data/images/dummy.png")
dummy1 = pygame.image.load("data/images/dummy1.png")
dummy2 = pygame.image.load("data/images/dummy2.png")
dummy3 = pygame.image.load("data/images/dummy3.png")
tree = pygame.image.load("data/images/tree.png")
dummyImg = dummy

#items
item_log = pygame.image.load("data/images/item_log.png")
item_knife = pygame.image.load("data/images/item_knife.png")
item_woodsword = pygame.image.load("data/images/item_woodsword.png")
item_bat = pygame.image.load("data/images/item_homerun.png")
item_woodhammer = pygame.image.load("data/images/item_woodhammer.png")
item_woodstaff = pygame.image.load("data/images/item_woodstaff.png")
item_slingshot = pygame.image.load("data/images/item_slingshot.png")
slingshot_ammo = pygame.image.load("data/images/bullet_slingshot.png")
item_woodhelm = pygame.image.load("data/images/item_woodhelm.png")
item_woodchest = pygame.image.load("data/images/item_woodchest.png")
item_woodlegs = pygame.image.load("data/images/item_woodlegs.png")
item_woodboots = pygame.image.load("data/images/item_woodboots.png")
item_battlesnake = pygame.image.load("data/images/item_battlesnake.png")
item_garlic = pygame.image.load("data/images/item_garlic.png")
item_snakemeat = pygame.image.load("data/images/item_snakemeat.png")
item_cooked_snakemeat = pygame.image.load("data/images/item_cooked_snakemeat.png")
item_burnt_snakemeat = pygame.image.load("data/images/item_burnt_snakemeat.png")
item_berry = pygame.image.load("data/images/item_berry.png")
item_blowpipe = pygame.image.load("data/images/item_blowpipe.png")
item_torch = pygame.image.load("data/images/item_torch.png")
item_green_overcoat = pygame.image.load("data/images/item_green_overcoat.png")
item_jeans = pygame.image.load("data/images/item_jeans.png")
item_boots = pygame.image.load("data/images/item_boots.png")

#unobtainable funny developer items
item_burninator = "data/images/item_burninator.png"

#house
house = pygame.image.load("data/images/house.png")
house1 = pygame.image.load("data/images/house1.png")
house2 = pygame.image.load("data/images/house2.png")
house3 = pygame.image.load("data/images/house3.png")
house4 = pygame.image.load("data/images/house4.png")
house5 = pygame.image.load("data/images/house5.png")
housedebris = pygame.image.load("data/images/housedebris.png")
houseImg = housedebris

pygame.mixer.init()
walk1 = pygame.mixer.Sound("data/audio/h.wav")
walk2 = pygame.mixer.Sound("data/audio/h2.wav")
hit = pygame.mixer.Sound("data/audio/hit.wav")
slam = pygame.mixer.Sound("data/audio/slam.wav")
stab = pygame.mixer.Sound("data/audio/stab.wav")
whip = pygame.mixer.Sound("data/audio/whip.wav")
punch = pygame.mixer.Sound("data/audio/punch.wav")
shot = pygame.mixer.Sound("data/audio/shoot.wav")
bullet_hit = pygame.mixer.Sound("data/audio/bullet.wav")
enemy_die = pygame.mixer.Sound("data/audio/enemy_die.wav")
crit = pygame.mixer.Sound("data/audio/crit.wav")
saviour = "data/audio/saviour.wav"
caverns = "data/audio/caverns.wav"
spelunking = "data/audio/spelunking.wav"
song1 = "data/audio/song1.wav"
title_theme = "data/audio/title.wav"
farewell = "data/audio/farewell.wav"
john_doe = "data/audio/john doe.wav"
united = "data/audio/united.wav"
pumpkins = "data/audio/pumpkins.wav"
frostbite = "data/audio/frostbite.wav"
menu_theme = "data/audio/take it easy.wav"
murky_waters = "data/audio/murky waters.wav"
nightfall = "data/audio/nightfall.wav"
fall_theme_1 = "data/audio/pumpkins.wav"
game_over_theme = "data/audio/game_over.wav"

#ui
menuImg = pygame.image.load("data/images/title.png")
play = pygame.image.load("data/images/play.png")
play_clicked = pygame.image.load("data/images/play_clicked.png")
textbox = pygame.image.load("data/images/textbox.png")
hotbar = pygame.image.load("data/images/hotbar.png")
inventoryImg = pygame.image.load("data/images/menu.png")
equipsmenu = pygame.image.load("data/images/equips_menu.png")
savemenu = pygame.image.load("data/images/save_menu.png")
craftingmenu = pygame.image.load("data/images/crafting_menu.png")
heart = pygame.image.load("data/images/heart.png")
drumstick = pygame.image.load("data/images/chicken.png")
droplet = pygame.image.load("data/images/droplet.png")
clock_img = pygame.image.load("data/images/clock.png")
coin = pygame.image.load("data/images/coin.png")
shield = pygame.image.load("data/images/shield.png")
itembox = pygame.image.load("data/images/itembox.png")
itembox_cursor = pygame.image.load("data/images/itembox_cursor.png")
map_img = pygame.image.load("data/images/map.png")
night_shading = pygame.image.load("data/images/night_shading.png")
night_shading2 = pygame.image.load("data/images/night_shading2.png")
naming_screen = pygame.image.load("data/images/naming_screen.png")
empty_healthbar = pygame.image.load("data/images/empty_healthbar.png")
emptybar = pygame.image.load("data/images/emptybar.png")
healthbar_segment = pygame.image.load("data/images/healthbar_segment.png")
hungerbar_segment = pygame.image.load("data/images/hungerbar_segment.png")
thirstbar_segment = pygame.image.load("data/images/thirstbar_segment.png")
menu_cursor = pygame.image.load("data/images/menu_cursor.png")
game_over = pygame.image.load("data/images/game_over.png")