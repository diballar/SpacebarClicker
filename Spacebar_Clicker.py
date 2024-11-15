#variables
score = 0
p_sec = 0
p_click = 1
shop_ = 0
s_pressed = 0
p_pressed = 0
item_namelist = ["robotic finger", "stronger finger", "more coming soon!"]
item_price_rfog = 100
item_price_sfog = 200
item_pricelist = [item_price_rfog, item_price_sfog, 0]
r_arrow_p = 0
l_arrow_p = 0
en = 0

#imports
import os
from threading import Thread
import keyboard
import time

#time for the points per second
time1 = time.time()
        
while True:
    if shop_ == 0:
        
        #drawwing the main screen
        os.system('cls')
        print("[Spacebar Clicker!]")
        print(f"       {p_sec}")
        print(f"       {p_click}")
        print(f"       {score}")
        print("")
        print("     [shop (s)]")

        #checking if space has been pressed
        if keyboard.is_pressed('space') and x == 0:
            x = 1
            score += p_click
        if not keyboard.is_pressed('space'):
            x = 0

        #checking if s is pressed (opens the shop)
        if keyboard.is_pressed('s') and s_pressed == 0:
            s_pressed = 1
            shop_ = 1
        if not keyboard.is_pressed('s'):
            s_pressed = 0

        #per second thing
        time2 = time.time()
        time_ = time2 - time1
        if round(time_ - 0.5) / 1 == 1:
            score += p_sec
            time1 = time.time()
    if shop_ == 1:
        
        #drawing shop and getting item
        item_name = item_namelist[en]
        item_price = item_pricelist[en]
        os.system('cls')
        print(f"{score}       [shop]")
        print(f"<     {item_name}     >")
        print(f"<        {item_price}             >")
        print("")
        print("     [purchase (p)]")
        
        #scrolling through items
        if not en == 2:
            if keyboard.is_pressed('right') and r_arrow_p == 0:
                en += 1
                r_arrow_p = 1
        if not keyboard.is_pressed('right'):
            r_arrow_p = 0

        if not en == 0:
            if keyboard.is_pressed('left') and l_arrow_p == 0:
                en -= 1
                l_arrow_p = 1
        if not keyboard.is_pressed('left'):
            l_arrow_p = 0

        #purchasing
        if keyboard.is_pressed('p') and p_pressed == 0 and score >= item_price:
            p_pressed = 1
            score -= item_price
            item_pricelist[en] = item_pricelist[en] * 2
            if en == 0:
                p_sec += 0.5
            if en == 1:
                p_click += 0.5
        if not keyboard.is_pressed('p'):
            p_pressed = 0

        #closing the shop
        if keyboard.is_pressed('s') and s_pressed == 0:
            s_pressed = 1
            shop_ = 0
            time1 = time.time()
        if not keyboard.is_pressed('s'):
            s_pressed = 0
    