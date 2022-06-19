import pyautogui
from PIL import ImageGrab
import cv2
import numpy as np
import pygetwindow as gw
import time
from pynput.mouse import Controller


def buffSelector(buffList, setTemplateWidth, setTemplateHeight):
    translatedBuffList = list()

    if '2xBoss' in buffList:
        boss2x = cv2.imread('Buffs/2xBoss.JPG', 0)
        boss2x = cv2.resize(boss2x, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(boss2x)
    if 'atk2xFireRateLess' in buffList:
        atk2xFireRateLess = cv2.imread('Buffs/atk2xFireRateLess.JPG', 0)
        atk2xFireRateLess = cv2.resize(atk2xFireRateLess, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(atk2xFireRateLess)
    if 'buffChoicePlus2' in buffList:
        buffChoicePlus2 = cv2.imread('Buffs/buffChoicePlus2.JPG', 0)
        buffChoicePlus2 = cv2.resize(buffChoicePlus2, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(buffChoicePlus2)
    if 'critRate2xCritDamageLess' in buffList:
        critRate2xCritDamageLess = cv2.imread('Buffs/critRate2xCritDamageLess.JPG', 0)
        critRate2xCritDamageLess = cv2.resize(critRate2xCritDamageLess, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(critRate2xCritDamageLess)
    if 'dwarfism' in buffList:
        dwarfism = cv2.imread('Buffs/dwarfism.JPG', 0)
        dwarfism = cv2.resize(dwarfism, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(dwarfism)
    if 'FireRate2xAtkLess' in buffList:
        FireRate2xAtkLess = cv2.imread('Buffs/FireRate2xAtkLess.JPG', 0)
        FireRate2xAtkLess = cv2.resize(FireRate2xAtkLess, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(FireRate2xAtkLess)
    if 'gigantism' in buffList:
        gigantism = cv2.imread('Buffs/gigantism.JPG', 0)
        gigantism = cv2.resize(gigantism, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(gigantism)
    if 'gigaPet' in buffList:
        gigaPet = cv2.imread('Buffs/gigaPet.JPG', 0)
        gigaPet = cv2.resize(gigaPet, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(gigaPet)
    if 'goodLuck' in buffList:
        goodLuck = cv2.imread('Buffs/goodLuck.JPG', 0)
        goodLuck = cv2.resize(goodLuck, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(goodLuck)
    if 'infiniteEnergy' in buffList:
        infiniteEnergy = cv2.imread('Buffs/infiniteEnergy.JPG', 0)
        infiniteEnergy = cv2.resize(infiniteEnergy, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(infiniteEnergy)
    if 'maxBuffsPlus3' in buffList:
        maxBuffsPlus3 = cv2.imread('Buffs/maxBuffsPlus3.JPG', 0)
        maxBuffsPlus3 = cv2.resize(maxBuffsPlus3, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(maxBuffsPlus3)
    if 'monstersSplitInto2' in buffList:
        monsterSplitInto2 = cv2.imread('Buffs/monstersSplitInto2.JPG', 0)
        monsterSplitInto2 = cv2.resize(monsterSplitInto2, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(monsterSplitInto2)
    if 'moreBonusRooms' in buffList:
        moreBonusRooms = cv2.imread('Buffs/moreBonusRooms.JPG', 0)
        moreBonusRooms = cv2.resize(moreBonusRooms, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(moreBonusRooms)
    if 'moreCritDmg' in buffList:
        moreCritDamage = cv2.imread('Buffs/moreCritDmg.JPG', 0)
        moreCritDamage = cv2.resize(moreCritDamage, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(moreCritDamage)
    if 'moreEnemies' in buffList:
        moreEnemies = cv2.imread('Buffs/moreEnemies.JPG', 0)
        moreEnemies = cv2.resize(moreEnemies, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(moreEnemies)
    if 'moreRooms' in buffList:
        moreRooms = cv2.imread('Buffs/moreRooms.JPG', 0)
        moreRooms = cv2.resize(moreRooms, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(moreRooms)
    if 'moreShield_doesNotRegen' in buffList:
        moreShield_doesNotRegen = cv2.imread('Buffs/moreShield_doesNotRegen.JPG', 0)
        moreShield_doesNotRegen = cv2.resize(moreShield_doesNotRegen, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(moreShield_doesNotRegen)
    if 'multipleStatues' in buffList:
        multipleStatues = cv2.imread('Buffs/multipleStatues.JPG', 0)
        multipleStatues = cv2.resize(multipleStatues, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(multipleStatues)
    if 'newMount' in buffList:
        newMount = cv2.imread('Buffs/newMount.JPG', 0)
        newMount = cv2.resize(newMount, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(newMount)
    if 'newWeapon' in buffList:
        newWeapon = cv2.imread('Buffs/newWeapon.JPG', 0)
        newWeapon = cv2.resize(newWeapon, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(newWeapon)
    if 'randomLevels' in buffList:
        randomLevels = cv2.imread('Buffs/randomLevels.JPG', 0)
        randomLevels = cv2.resize(randomLevels, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(randomLevels)
    if 'regenHP' in buffList:
        regenHP = cv2.imread('Buffs/regenHP.JPG', 0)
        regenHP = cv2.resize(regenHP, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(regenHP)
    if 'skillCooldownLow' in buffList:
        skillCooldownLow = cv2.imread('Buffs/skillCooldownLow.JPG', 0)
        skillCooldownLow = cv2.resize(skillCooldownLow, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(skillCooldownLow)
    if 'switchCharacter' in buffList:
        switchCharacter = cv2.imread('Buffs/switchCharacter.JPG', 0)
        switchCharacter = cv2.resize(switchCharacter, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(switchCharacter)
    if 'weaponsWithAttachment' in buffList:
        weaponsWithAttachment = cv2.imread('Buffs/weaponsWithAttachment.JPG', 0)
        weaponsWithAttachment = cv2.resize(weaponsWithAttachment, (int(setTemplateWidth), int(setTemplateHeight)))
        translatedBuffList.append(weaponsWithAttachment)

    for buff in buffList:
        if 'freeSlot' == buff:
            translatedBuffList.append('freeSlot')

    return translatedBuffList


def resizeTemplate():
    # Screen
    window_name = 'bluestacks'
    screenWindow = gw.getWindowsWithTitle(window_name)[0]
    screenWindow.activate()

    # Gets the screen resolution to be multiplied by the ratio of icon size to the resolution
    screen_res = [screenWindow.width, screenWindow.height]

    targetTemplateWidth = round(screen_res[0] / 18.5)
    targetTemplateHeight = round(screen_res[1] / 10)

    return targetTemplateWidth, targetTemplateHeight


def determineBuffPresence(buff, screen2):
    if buff == 'freeSlot':
        match = True
    else:
        result = cv2.matchTemplate(screen2, buff, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.7
        if max_val > threshold:
            match = True
        else:
            match = False
    return match


def multipleBuffRecognition(buffList, executionLength):
    running = True
    allBuffsMatched = False
    ctime = time.time()

    mouse = Controller()

    # Gets desired buffs from the program
    templateData = resizeTemplate()
    translatedBuffs = buffSelector(buffList, templateData[0], templateData[1])

    while running:
        # Screen
        window_name = 'bluestacks'
        screenWindow = gw.getWindowsWithTitle(window_name)[0]
        screenWindow.activate()
        screen = np.array(ImageGrab.grab(bbox=(screenWindow.left + (screenWindow.width * 0.4),
                                               screenWindow.top + (screenWindow.height * 0.2),
                                               screenWindow.left + (screenWindow.width * 0.7),
                                               screenWindow.top + (screenWindow.height * 0.5))))

        grayScreen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

        screen2 = grayScreen.copy()

        # Returns True if something matches the template
        buff1 = determineBuffPresence(translatedBuffs[0], screen2)
        buff2 = determineBuffPresence(translatedBuffs[1], screen2)
        buff3 = determineBuffPresence(translatedBuffs[2], screen2)
        buff4 = determineBuffPresence(translatedBuffs[3], screen2)

        if buff1:
            print('Buff 1 Passed')
            if buff2:
                print('Buff 2 Passed')
                if buff3:
                    print('Buff 3 Passed')
                    if buff4:
                        print('Buff 4 Passed. All desired buffs are selected')
                        allBuffsMatched = True

        dtime = time.time()
        if round(dtime - ctime) == executionLength:
            break

        mouse.position = (screenWindow.left, screenWindow.top)
        mouse.move(screenWindow.width * 0.67, screenWindow.height * 0.37)

        if allBuffsMatched:
            return True

        pyautogui.click()

# Problem: Goes over a complete match because of its speed in clicking or something.
