from images import *

def update_menu(display,imglist,menu,inv,player,selected,cursor):
    if menu == 1:
        display.blit(inventoryImg,(0,0))
        x = 0
        for item in inv:
            try:
                display.blit(imglist[item[0][0]],(x*15,15))
            except TypeError:
                pass
            x += 1
        try:
            display.blit(cursor,(selected*15,15))
        except TypeError:
            pass