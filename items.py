
#item stuff
#first index: image, type, name, desc, tier, value
#second index:
#for weapons: weapon type, low dmg, high dmg, crit chance, use type, autofire, knockback (tiles), range, cooldown, effect
#for armour: equipment type, def, atk, luck, speed, effect, effect duration, effect description
#for consumables: hp, hunger, thirst, sleep, effect, effect duration, effect description
#third index:
#for ranged weapons: projectile shot, projectile amount, spread
#for consumables/traps: uses

green_overcoat = [[17,"armour","Green Overcoat","Stylish, but not very protective.",1,0],["body",0,0,0,0,0]]
jeans = [[18,"armour","Jeans","Some sturdy jeans.",1,0],["legs",0,0,0,0,0]]
boots = [[19,"armour","Boots","Average boots.",1,0],["shoes",0,0,0,0,0]]
boxing_glove = [[0,"armour","Boxing Glove","Protects you from fatal blows.",5,0],["acc",0,0,0,0,0]]


log = [[0,"item","Log","A log, used for basic crafting.",1,1]]
scrap_metal = [[0,"item","Scrap Metal","You might be able to make tools with this.",2,10]]
coal = [[0,"item","Coal","A hunk of coal.",2,25]]

knife = [[1,"weapon","Knife","A dull knife.",1,3],["melee",3,6,4,"stab",False,0,0,20,0]]
wood_sword = [[2,"weapon","Wood Sword","It's quite shabby, but it works.",1,2],["melee",8,10,5,"swing",False,0.5,0,30,0]]
baseball_bat = [[3,"weapon","Baseball Bat","Home run!",1,3],["melee",10,15,5,"swing",False,0.5,0,40,0]]
wood_hammer = [[4,"weapon","Wood Hammer","A shoddy yet powerful mallet.",1,4],["melee",14,18,5,"slam",False,1,0,60,0]]
wood_staff = [[5,"weapon","Wood Staff","It's incredibly weak.",1,3],["melee",5,8,5,"swing",False,0.5,0,30,0]]
slingshot = [[6,"weapon","Slingshot","It fires rocks.",1,3],["ranged",4,9,5,"shoot",False,0,4,20,0]]
wood_helm = [[7,"armour","Wood Helm","Barely protective.",1,2],["head",1,0,0,0,0]]
wood_platemail = [[8,"armour","Wood Chestplate","It smells like wood.",1,5],["body",1,0,0,0,0]]
wood_leggings = [[9,"armour","Wood Leggings","Very uncomfortable.",1,4],["legs",1,0,0,0,0]]
wood_boots = [[10,"armour","Wood Boots","Can you even call these boots?",1,1],["shoes",0,0,0,0,0]]
snakemeat = [[11,"item","Snake Meat","Gross!",1,-1]]
cooked_snakemeat = [[12,"consumable","Cooked Snake Meat","It's an acquired taste.",1,-1],[5,4,0,0,0]]
burnt_snakemeat = [[13,"consumable","Burnt Snake Meat","'Charbroiled to perfection'? Really?",0,-1],[-5,2,-10,0,0]]
battlesnake = [[14,"weapon","Battlesnake","What kind of weapon is this?",3,45],["melee",19,23,6,"spin",False,0.5,0,30,0]]
rusty_axe = [[15,"weapon","Rusty Axe","It's really dull, but it still works.",1,4],["melee",2,5,3,"swing",False,0.5,0,40,0]]
blowpine = [[15,"weapon","Blowpine","Shoots ridiculously fast.",2,35],["ranged",1,2,2,"shoot",False,0,5,5,0]]
blowpipe = [[15,"weapon","Blowpipe","Used for long-range combat.",2,35],["ranged",7,13,5,"shoot",False,0,5,50,0]]
torch = [[16,"weapon","Torch","Use it to join an angry mob, or as a light source.",3,15],["melee",5,9,4,"swing",False,0.5,0,30,1,12,"Causes enemies to burn for 12 seconds. Also provides light."]]
serrated_destroyer = [[0,"weapon","Serrated Destroyer","It's quite powerful. Handle it with care.",4,650],["melee",27,38,7,]]
minigun = [[0,"weapon","Minigun","It's not very 'mini', is it?",5,1250],["ranged",1,3,8,"shoot",True,0,5,2,0]]
sniper_rifle = [[0,"weapon","Sniper Rifle","Good for building a 'long-distance relationship'.",5,1575],["ranged",40,90,50,"shoot",False,0,50,180,0]]
the_tenderizer = [[0,"weapon","The Tenderizer","Great at rendering your foes useless.",5,2000],["melee",56,97,10,"slam",False,3,120,5,10,"Breaks your foe's limbs for 10 seconds."]]
nuclear_sabre = [[0,"weapon","Nuclear Sabre","Slice your enemies in two with ease.",5,1750],["melee",45,85,15,"swing",False,1.5,60,6,15,"Inflicts radiation for 15 seconds."]]
wicked_blade = [[0,"weapon","Wicked Blade","Destroy everything and anything at the cost of your own life.",6,4500],["melee",95,170,25,"swing",False,1,0,80,7,0,"Deals damage to you if it does not do a critical hit."]]
lucky_seven = [[0,"weapon","Lucky Seven","I'm feeling lucky.",7,7777777],["melee",7,7777777,7,"swing",True,7,0,70,0]]

medkit = [[0,"consumable","Medkit","Repairs broken bones.",3,35],[35,0,0,0,0,0,0]]
hawkberry = [[0,"consumable","Hawkberry","It really dries out your mouth.",1,-1],[2,1,-4,0,0]]
coffee = [[0,"consumable","Coffee","Careful not to drink too much.",2,25],[0,0,6,3,1,60,"Keeps you awake 3 hours longer and makes you hyper for a minute."]]
triple_espresso = [[0,"consumable","Triple Espresso","You won't sit still for a day after having this stuff.",6,100],[0,0,6,18,1,1080,"Keeps you awake 18 hours longer and makes you hyper for a whole day."]]
atomic_energy_drink = [[0,"consumable","Atomic Energy Drink","Now 80% more radioactive!",4,45],[0,4,12,5,1,240,"Keeps you awake 5 hours longer and makes you hyper for 4 minutes."]]
utopian_cola = [[0,"consumable","Utopian Cola","Contains more sugar than it's legally allowed to.",2,7],[0,3,8,0,1,30,"Makes you hyper for 30 seconds."]]
utopian_cola_diet = [[0,"consumable","Utopian Cola Diet","It's the exact same, but with a new kind of sugar!",2,10],[0,3,8,0,1,30,"Makes you hyper for 30 seconds."]]
