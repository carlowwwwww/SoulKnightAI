import pyautogui
import customtkinter
from PIL import Image, ImageTk

from PIL import ImageGrab
import cv2
import numpy as np
import pygetwindow as gw
import time
from pynput.mouse import Button, Controller
# ------------------------------------------------------------------------------------------------------------ #
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
screen_size = pyautogui.size()
app.geometry(f"{int(screen_size[0] * 0.285)}x{int(screen_size[1] * 0.838)}")
app.resizable(False, False)
app.title("Buff Selector")


def buffSelector(buffList):
    translatedBuffList = list()

    if '2xBoss' in buffList:
        boss2x = cv2.imread('Buffs/2xBoss.JPG', 0)
        translatedBuffList.append(boss2x)
    if 'atk2xFireRateLess' in buffList:
        atk2xFireRateLess = cv2.imread('Buffs/atk2xFireRateLess.JPG', 0)
        translatedBuffList.append(atk2xFireRateLess)
    if 'buffChoicePlus2' in buffList:
        buffChoicePlus2 = cv2.imread('Buffs/buffChoicePlus2.JPG', 0)
        translatedBuffList.append(buffChoicePlus2)
    if 'critRate2xCritDamageLess' in buffList:
        critRate2xCritDamageLess = cv2.imread('Buffs/critRate2xCritDamageLess.JPG', 0)
        translatedBuffList.append(critRate2xCritDamageLess)
    if 'dwarfism' in buffList:
        dwarfism = cv2.imread('Buffs/dwarfism.JPG', 0)
        translatedBuffList.append(dwarfism)
    if 'FireRate2xAtkLess' in buffList:
        FireRate2xAtkLess = cv2.imread('Buffs/FireRate2xAtkLess.JPG', 0)
        translatedBuffList.append(FireRate2xAtkLess)
    if 'gigantism' in buffList:
        gigantism = cv2.imread('Buffs/gigantism.JPG', 0)
        translatedBuffList.append(gigantism)
    if 'gigaPet' in buffList:
        gigaPet = cv2.imread('Buffs/gigaPet.JPG', 0)
        translatedBuffList.append(gigaPet)
    if 'goodLuck' in buffList:
        goodLuck = cv2.imread('Buffs/goodLuck.JPG', 0)
        translatedBuffList.append(goodLuck)
    if 'infiniteEnergy' in buffList:
        infiniteEnergy = cv2.imread('Buffs/infiniteEnergy.JPG', 0)
        translatedBuffList.append(infiniteEnergy)
    if 'maxBuffsPlus3' in buffList:
        maxBuffsPlus3 = cv2.imread('Buffs/maxBuffsPlus3.JPG', 0)
        translatedBuffList.append(maxBuffsPlus3)
    if 'monstersSplitInto2' in buffList:
        monsterSplitInto2 = cv2.imread('Buffs/monstersSplitInto2.JPG', 0)
        translatedBuffList.append(monsterSplitInto2)
    if 'moreBonusRooms' in buffList:
        moreBonusRooms = cv2.imread('Buffs/moreBonusRooms.JPG', 0)
        translatedBuffList.append(moreBonusRooms)
    if 'moreCritDmg' in buffList:
        moreCritDamage = cv2.imread('Buffs/moreCritDmg.JPG', 0)
        translatedBuffList.append(moreCritDamage)
    if 'moreEnemies' in buffList:
        moreEnemies = cv2.imread('Buffs/moreEnemies.JPG', 0)
        translatedBuffList.append(moreEnemies)
    if 'moreRooms' in buffList:
        moreRooms = cv2.imread('Buffs/moreRooms.JPG', 0)
        translatedBuffList.append(moreRooms)
    if 'moreShield_doesNotRegen' in buffList:
        moreShield_doesNotRegen = cv2.imread('Buffs/moreShield_doesNotRegen.JPG', 0)
        translatedBuffList.append(moreShield_doesNotRegen)
    if 'multipleStatues' in buffList:
        multipleStatues = cv2.imread('Buffs/multipleStatues.JPG', 0)
        translatedBuffList.append(multipleStatues)
    if 'newMount' in buffList:
        newMount = cv2.imread('Buffs/newMount.JPG', 0)
        translatedBuffList.append(newMount)
    if 'newWeapon' in buffList:
        newWeapon = cv2.imread('Buffs/newWeapon.JPG', 0)
        translatedBuffList.append(newWeapon)
    if 'randomLevels' in buffList:
        randomLevels = cv2.imread('Buffs/randomLevels.JPG', 0)
        translatedBuffList.append(randomLevels)
    if 'regenHP' in buffList:
        regenHP = cv2.imread('Buffs/regenHP.JPG', 0)
        translatedBuffList.append(regenHP)
    if 'skillCooldownLow' in buffList:
        skillCooldownLow = cv2.imread('Buffs/skillCooldownLow.JPG', 0)
        translatedBuffList.append(skillCooldownLow)
    if 'switchCharacter' in buffList:
        switchCharacter = cv2.imread('Buffs/switchCharacter.JPG', 0)
        translatedBuffList.append(switchCharacter)
    if 'weaponsWithAttachment' in buffList:
        weaponsWithAttachment = cv2.imread('Buffs/weaponsWithAttachment.JPG', 0)
        translatedBuffList.append(weaponsWithAttachment)

    for buff in buffList:
        if 'freeSlot' in buffList:
            translatedBuffList.append('slot')

    return translatedBuffList


def determineBuffPresence(buff, targetTemplateHeight, screen_res, template_h, template_w, match, screen2):
    if buff == 'freeSlot':
        match = True
    else:
        if template_h > targetTemplateHeight:
            if match:
                pass
            else:
                buff = cv2.resize(buff, (0, 0), fx=0.8, fy=0.8)
        if template_h < targetTemplateHeight:
            if match:
                pass
            else:
                buff = cv2.resize(buff, (0, 0), fx=0.8, fy=0.8)

        result = cv2.matchTemplate(screen2, buff, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.7
        if max_val > threshold:
            print(f'Match Success - Width: {screen_res[0]}, Height: {screen_res[1]}, Template height: {template_h}')
            match = True
        else:
            print(
                f'No match found - Width: {screen_res[0]}, Height: {screen_res[1]}, Template height: {template_h}')
            match = False
    return match, buff


def multipleBuffRecognition(buffList):
    running = True
    buffMatch = False
    ctime = time.time()

    # Enables the control of the mouse
    mouse = Controller()
    #
    # buff1 = cv2.imread('Buffs/moreEnemies.JPG', 0)
    # buff2 = cv2.imread('Buffs/atk2xFireRateLess.JPG', 0)
    # buff3 = 'none'
    # buff4 = 'none'
    #
    # buffList = [buff1, buff2, buff3, buff4]

    # Gets desired buffs from the program
    translatedBuffs = buffSelector(buffList)

    while running:
        # Screen
        window_name = 'notepad'
        screenWindow = gw.getWindowsWithTitle(window_name)[0]
        screenWindow.activate()
        screen = np.array(ImageGrab.grab(bbox=(screenWindow.left + (screenWindow.width*0.4),
                                               screenWindow.top + (screenWindow.height*0.2),
                                               screenWindow.left + (screenWindow.width*0.7),
                                               screenWindow.top + (screenWindow.height*0.5))))

        grayScreen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

        # Gets the screen resolution to be multiplied by the ratio of icon size to the resolution
        screen_res = [screenWindow.width, screenWindow.height]

        screen2 = grayScreen.copy()

        # Gets the template height and width for buffs and reset button
        template_h, template_w = translatedBuffs[0].shape

        # The best height for the template to be in comparison to the window height
        targetTemplateHeight = screen_res[1] / 10

        # Returns True if something matches the template
        buff1 = determineBuffPresence(translatedBuffs[0], targetTemplateHeight, screen_res, template_h, template_w, buffMatch, screen2)
        buff2 = determineBuffPresence(translatedBuffs[1], targetTemplateHeight, screen_res, template_h, template_w, buffMatch, screen2)
        buff3 = determineBuffPresence(translatedBuffs[2], targetTemplateHeight, screen_res, template_h, template_w, buffMatch, screen2)
        buff4 = determineBuffPresence(translatedBuffs[3], targetTemplateHeight, screen_res, template_h, template_w, buffMatch, screen2)

        # Sets the template to its correct width and height to be used for future loops
        translatedBuffs[0] = buff1[1]
        translatedBuffs[1] = buff2[1]
        translatedBuffs[2] = buff3[1]
        translatedBuffs[3] = buff4[1]

        if buff1[0]:
            print('Buff 1 Passed')
            if buff2[0]:
                print('Buff 2 Passed')
                if buff3[0]:
                    print('Buff 3 Passed')
                    if buff4[0]:
                        print('Buff 4 Passed. All desired buffs are selected')
                        break

        mouse.position = (screenWindow.left, screenWindow.top)
        mouse.move(screenWindow.width*0.5, screenWindow.height*0.37)
        mouse.click(Button.left, 1)

        dtime = time.time()

        # Creates a timer. After the timer expires, the loop breaks
        if round(dtime - ctime) == 5:
            break

        cv2.imshow('Python Window', screen)
        cv2.waitKey(0)

    time.sleep(1)


def button_function(buff):
    global buffList
    if buff == 'Run':
        if len(buffList) < 1:
            print('You need to select at least 1 buff.')
        elif 1 <= len(buffList) < 4:
            while len(buffList) <= 4:
                buffList.append('freeSlot')
                print(buffList)
                multipleBuffRecognition(buffList)
        else:
            print('Program Starting')
            multipleBuffRecognition(buffList)
    else:
        if len(buffList) == 4:
            print('Maximum amount of buffs selected. Please press "Run Program"')
        else:
            buffList.append(buff)
            print(buffList)


def clearSelection():
    global buffList
    buffList = list()
    print(buffList)
    print('Buff Selection Cleared')


def deleteLast():
    del buffList[-1]
    print(buffList)


buffList = []

# Image
boss2x = (Image.open('Buffs/2xBoss.JPG')).resize((50, 50))
boss2x = ImageTk.PhotoImage(boss2x)

atk2xFireRateLess = (Image.open('Buffs/atk2xFireRateLess.JPG')).resize((50, 50))
atk2xFireRateLess = ImageTk.PhotoImage(atk2xFireRateLess)

buffChoicePlus2 = (Image.open('Buffs/buffChoicePlus2.JPG')).resize((50, 50))
buffChoicePlus2 = ImageTk.PhotoImage(buffChoicePlus2)

critRate2xCritDamageLess = (Image.open('Buffs/critRate2xCritDamageLess.JPG')).resize((50, 50))
critRate2xCritDamageLess = ImageTk.PhotoImage(critRate2xCritDamageLess)

dwarfism = (Image.open('Buffs/dwarfism.JPG')).resize((50, 50))
dwarfism = ImageTk.PhotoImage(dwarfism)

FireRate2xAtkLess = (Image.open('Buffs/FireRate2xAtkLess.JPG')).resize((50, 50))
FireRate2xAtkLess = ImageTk.PhotoImage(FireRate2xAtkLess)

gigantism = (Image.open('Buffs/gigantism.JPG')).resize((50, 50))
gigantism = ImageTk.PhotoImage(gigantism)

gigaPet = (Image.open('Buffs/gigaPet.JPG')).resize((50, 50))
gigaPet = ImageTk.PhotoImage(gigaPet)

goodLuck = (Image.open('Buffs/goodLuck.JPG')).resize((50, 50))
goodLuck = ImageTk.PhotoImage(goodLuck)

infiniteEnergy = (Image.open('Buffs/infiniteEnergy.JPG')).resize((50, 50))
infiniteEnergy = ImageTk.PhotoImage(infiniteEnergy)

maxBuffsPlus3 = (Image.open('Buffs/maxBuffsPlus3.JPG')).resize((50, 50))
maxBuffsPlus3 = ImageTk.PhotoImage(maxBuffsPlus3)

monstersSplitInto2 = (Image.open('Buffs/monstersSplitInto2.JPG')).resize((50, 50))
monstersSplitInto2 = ImageTk.PhotoImage(monstersSplitInto2)

moreBonusRooms = (Image.open('Buffs/moreBonusRooms.JPG')).resize((50, 50))
moreBonusRooms = ImageTk.PhotoImage(moreBonusRooms)

moreCritDmg = (Image.open('Buffs/moreCritDmg.JPG')).resize((50, 50))
moreCritDmg = ImageTk.PhotoImage(moreCritDmg)

moreEnemies = (Image.open('Buffs/moreEnemies.JPG')).resize((50, 50))
moreEnemies = ImageTk.PhotoImage(moreEnemies)

moreRooms = (Image.open('Buffs/moreRooms.JPG')).resize((50, 50))
moreRooms = ImageTk.PhotoImage(moreRooms)

moreShield_doesNotRegen = (Image.open('Buffs/moreShield_doesNotRegen.JPG')).resize((50, 50))
moreShield_doesNotRegen = ImageTk.PhotoImage(moreShield_doesNotRegen)

multipleStatues = (Image.open('Buffs/multipleStatues.JPG')).resize((50, 50))
multipleStatues = ImageTk.PhotoImage(multipleStatues)

newMount = (Image.open('Buffs/newMount.JPG')).resize((50, 50))
newMount = ImageTk.PhotoImage(newMount)

newWeapon = (Image.open('Buffs/newWeapon.JPG')).resize((50, 50))
newWeapon = ImageTk.PhotoImage(newWeapon)

randomLevels = (Image.open('Buffs/randomLevels.JPG')).resize((50, 50))
randomLevels = ImageTk.PhotoImage(randomLevels)

regenHP = (Image.open('Buffs/regenHP.JPG')).resize((50, 50))
regenHP = ImageTk.PhotoImage(regenHP)

skillCooldownLow = (Image.open('Buffs/skillCooldownLow.JPG')).resize((50, 50))
skillCooldownLow = ImageTk.PhotoImage(skillCooldownLow)

switchCharacter = (Image.open('Buffs/switchCharacter.JPG')).resize((50, 50))
switchCharacter = ImageTk.PhotoImage(switchCharacter)

weaponsWithAttachment = (Image.open('Buffs/weaponsWithAttachment.JPG')).resize((50, 50))
weaponsWithAttachment = ImageTk.PhotoImage(weaponsWithAttachment)


# Use CTkButton instead of tkinter Button
clearSelectedBuffs = customtkinter.CTkButton(master=app, text="Clear Selection", command=clearSelection)
clearSelectedBuffs.grid(row=0, column=0, padx=5, pady=15)

deleteLastBuff = customtkinter.CTkButton(master=app, text="Delete Last", command=deleteLast)
deleteLastBuff.grid(row=0, column=2, padx=5, pady=5)

runProgram = customtkinter.CTkButton(master=app, text="Run Program", command=lambda: button_function('Run'))
runProgram.grid(row=0, column=1, padx=5, pady=5)

buff1 = customtkinter.CTkButton(master=app, text="", image=boss2x, command=lambda: button_function('2xBoss'))
buff1.grid(row=1, column=0, padx=5, pady=5)

buff2 = customtkinter.CTkButton(master=app, text="", image=atk2xFireRateLess, command=lambda: button_function('atk2xFireRateLess'))
buff2.grid(row=1, column=1, padx=5, pady=5)

buff3 = customtkinter.CTkButton(master=app, text="", image=buffChoicePlus2, command=lambda: button_function('buffChoicePlus2'))
buff3.grid(row=1, column=2, padx=5, pady=5)

buff4 = customtkinter.CTkButton(master=app, text="", image=critRate2xCritDamageLess, command=lambda: button_function('critRate2xCritDamageLess'))
buff4.grid(row=2, column=0, padx=5, pady=5)

buff5 = customtkinter.CTkButton(master=app, text="", image=dwarfism, command=lambda: button_function('dwarfism'))
buff5.grid(row=2, column=1, padx=5, pady=5)

buff6 = customtkinter.CTkButton(master=app, text="", image=FireRate2xAtkLess, command=lambda: button_function('FireRate2xAtkLess'))
buff6.grid(row=2, column=2, padx=5, pady=5)

buff7 = customtkinter.CTkButton(master=app, text="", image=gigantism, command=lambda: button_function('gigantism'))
buff7.grid(row=3, column=0, padx=5, pady=5)

buff8 = customtkinter.CTkButton(master=app, text="", image=gigaPet, command=lambda: button_function('gigaPet'))
buff8.grid(row=3, column=1, padx=5, pady=5)

buff9 = customtkinter.CTkButton(master=app, text="", image=goodLuck, command=lambda: button_function('goodLuck'))
buff9.grid(row=3, column=2, padx=5, pady=5)

buff10 = customtkinter.CTkButton(master=app, text="", image=infiniteEnergy, command=lambda: button_function('infiniteEnergy'))
buff10.grid(row=4, column=0, padx=5, pady=5)

buff11 = customtkinter.CTkButton(master=app, text="", image=maxBuffsPlus3, command=lambda: button_function('maxBuffsPlus3'))
buff11.grid(row=4, column=1, padx=5, pady=5)

buff12 = customtkinter.CTkButton(master=app, text="", image=monstersSplitInto2, command=lambda: button_function('monstersSplitInto2'))
buff12.grid(row=4, column=2, padx=5, pady=5)

buff13 = customtkinter.CTkButton(master=app, text="", image=moreBonusRooms, command=lambda: button_function('moreBonusRooms'))
buff13.grid(row=5, column=0, padx=5, pady=5)

buff14 = customtkinter.CTkButton(master=app, text="", image=moreCritDmg, command=lambda: button_function('moreCritDmg'))
buff14.grid(row=5, column=1, padx=5, pady=5)

buff15 = customtkinter.CTkButton(master=app, text="", image=moreEnemies, command=lambda: button_function('moreEnemies'))
buff15.grid(row=5, column=2, padx=5, pady=5)

buff16 = customtkinter.CTkButton(master=app, text="", image=moreRooms, command=lambda: button_function('moreRooms'))
buff16.grid(row=6, column=0, padx=5, pady=5)

buff17 = customtkinter.CTkButton(master=app, text="", image=moreShield_doesNotRegen, command=lambda: button_function('moreShield_doesNotRegen'))
buff17.grid(row=6, column=1, padx=5, pady=5)

buff18 = customtkinter.CTkButton(master=app, text="", image=multipleStatues, command=lambda: button_function('multipleStatues'))
buff18.grid(row=6, column=2, padx=5, pady=5)

buff19 = customtkinter.CTkButton(master=app, text="", image=newMount, command=lambda: button_function('newMount'))
buff19.grid(row=7, column=0, padx=5, pady=5)

buff20 = customtkinter.CTkButton(master=app, text="", image=newWeapon, command=lambda: button_function('newWeapon'))
buff20.grid(row=7, column=1, padx=5, pady=5)

buff21 = customtkinter.CTkButton(master=app, text="", image=randomLevels, command=lambda: button_function('randomLevels'))
buff21.grid(row=7, column=2, padx=5, pady=5)

buff22 = customtkinter.CTkButton(master=app, text="", image=regenHP, command=lambda: button_function('regenHP'))
buff22.grid(row=8, column=0, padx=5, pady=5)

buff23 = customtkinter.CTkButton(master=app, text="", image=skillCooldownLow, command=lambda: button_function('skillCooldownLow'))
buff23.grid(row=8, column=1, padx=5, pady=5)

buff24 = customtkinter.CTkButton(master=app, text="", image=switchCharacter, command=lambda: button_function('switchCharacter'))
buff24.grid(row=8, column=2, padx=5, pady=5)

buff25 = customtkinter.CTkButton(master=app, text="", image=weaponsWithAttachment, command=lambda: button_function('weaponsWithAttachment'))
buff25.grid(row=9, column=0, padx=5, pady=5)


app.mainloop()

# if __name__ == '__main__':
#     main()

# Code Completed
