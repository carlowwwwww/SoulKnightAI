from PIL import ImageGrab
import cv2
import numpy as np
import pygetwindow as gw
from time import sleep


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


def main():
    running = True
    loop = 0
    boss2x = cv2.imread('Buffs/infiniteEnergy.JPG', 0)

    templateData = resizeTemplate()
    boss2x = cv2.resize(boss2x, (templateData[0], templateData[1]))

    while running:
        # Screen
        window_name = 'bluestacks'
        screenWindow = gw.getWindowsWithTitle(window_name)[0]
        screenWindow.activate()
        screen = np.array(ImageGrab.grab(bbox=(screenWindow.left + (screenWindow.width * 0.4),
                                               screenWindow.top + (screenWindow.height * 0.2),
                                               screenWindow.left + (screenWindow.width * 0.7),
                                               screenWindow.top + (screenWindow.height * 0.5))))

        screen_res = [screenWindow.width, screenWindow.height]
        template_h, template_w = boss2x.shape

        grayScreen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        screen2 = grayScreen.copy()

        result = cv2.matchTemplate(screen2, boss2x, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_val)

        # 0.775 is the most stable while max threshold is 0.85 (supposed to be the max)
        threshold = 0.6
        if max_val > threshold:
            print(
                f'{loop}. Match Success - Width: {screen_res[0]}, Height: {screen_res[1]}, Template size: {template_w}, {template_h}')
            loop += 1
        else:
            print(
                f'{loop}. No match found - Width: {screen_res[0]}, Height: {screen_res[1]}, Template size: {template_w}, {template_h}')
            loop += 1

        cv2.imshow('Python Window', screen)

        if cv2.waitKey(1) == ord('q'):
            break

        sleep(0.3)


if __name__ == '__main__':
    main()

# def buffSelector():
#     playerBuffs = list()
#     for i in range(4):
#         buff = input('What buff would you like to have? ')
#         playerBuffs.append(int(buff))
#
#     buffList = list()
#     # Buffs
#     for buff in playerBuffs:
#         if 1 in playerBuffs:
#             boss2x = cv2.imread('Buffs/2xBoss.JPG', 0)
#             buffList.append(boss2x)
#         elif 2 in playerBuffs:
#             atk2xFireRateLess = cv2.imread('Buffs/atk2xFireRateLess.JPG', 0)
#             buffList.append(atk2xFireRateLess)
#         elif 3 in playerBuffs:
#             buffChoicePlus2 = cv2.imread('Buffs/buffChoicePlus2.JPG', 0)
#             buffList.append(buffChoicePlus2)
#         elif 4 in playerBuffs:
#             critRate2xCritDamageLess = cv2.imread('Buffs/critRate2xCritDamageLess.JPG', 0)
#             buffList.append(critRate2xCritDamageLess)
#         elif 5 in playerBuffs:
#             dwarfism = cv2.imread('Buffs/dwarfism.JPG', 0)
#             buffList.append(dwarfism)
#         elif 6 in playerBuffs:
#             FireRate2xAtkLess = cv2.imread('Buffs/FireRate2xAtkLess.JPG', 0)
#             buffList.append(FireRate2xAtkLess)
#         elif 7 in playerBuffs:
#             gigantism = cv2.imread('Buffs/gigantism.JPG', 0)
#             buffList.append(gigantism)
#         elif 8 in playerBuffs:
#             gigaPet = cv2.imread('Buffs/gigaPet.JPG', 0)
#             buffList.append(gigaPet)
#         elif 9 in playerBuffs:
#             goodLuck = cv2.imread('Buffs/goodLuck.JPG', 0)
#             buffList.append(goodLuck)
#         elif 10 in playerBuffs:
#             infiniteEnergy = cv2.imread('Buffs/infiniteEnergy.JPG', 0)
#             buffList.append(infiniteEnergy)
#         elif 11 in playerBuffs:
#             maxBuffsPlus3 = cv2.imread('Buffs/maxBuffsPlus3.JPG', 0)
#             buffList.append(maxBuffsPlus3)
#         elif 12 in playerBuffs:
#             monsterSplitInto2 = cv2.imread('Buffs/monstersSplitInto2.JPG', 0)
#             buffList.append(monsterSplitInto2)
#         elif 13 in playerBuffs:
#             moreAggressiveEnemies = cv2.imread('Buffs/moreAggressiveEnemies.JPG', 0)
#             buffList.append(moreAggressiveEnemies)
#         elif 14 in playerBuffs:
#             moreBonusRooms = cv2.imread('Buffs/moreBonusRooms.JPG', 0)
#             buffList.append(moreBonusRooms)
#         elif 15 in playerBuffs:
#             moreCritDamage = cv2.imread('Buffs/moreCritDmg.JPG', 0)
#             buffList.append(moreCritDamage)
#         elif 16 in playerBuffs:
#             moreEnemies = cv2.imread('Buffs/moreEnemies.JPG', 0)
#             buffList.append(moreEnemies)
#         elif 17 in playerBuffs:
#             moreRooms = cv2.imread('Buffs/moreRooms.JPG', 0)
#             buffList.append(moreRooms)
#         elif 18 in playerBuffs:
#             moreShield_doesNotRegen = cv2.imread('Buffs/moreShield_doesNotRegen.JPG', 0)
#             buffList.append(moreShield_doesNotRegen)
#         elif 19 in playerBuffs:
#             multipleStatues = cv2.imread('Buffs/multipleStatues.JPG', 0)
#             buffList.append(multipleStatues)
#         elif 20 in playerBuffs:
#             newMount = cv2.imread('Buffs/newMount.JPG', 0)
#             buffList.append(newMount)
#         elif 21 in playerBuffs:
#             newWeapon = cv2.imread('Buffs/newWeapon.JPG', 0)
#             buffList.append(newWeapon)
#         elif 22 in playerBuffs:
#             randomLevels = cv2.imread('Buffs/randomLevels.JPG', 0)
#             buffList.append(randomLevels)
#         elif 23 in playerBuffs:
#             regenHP = cv2.imread('Buffs/regenHP.JPG', 0)
#             buffList.append(regenHP)
#         elif 24 in playerBuffs:
#             skillCooldownLow = cv2.imread('Buffs/skillCooldownLow.JPG', 0)
#             buffList.append(skillCooldownLow)
#         elif 25 in playerBuffs:
#             switchCharacter = cv2.imread('Buffs/switchCharacter.JPG', 0)
#             buffList.append(switchCharacter)
#         elif 26 in playerBuffs:
#             weaponsWithAttachment = cv2.imread('Buffs/weaponsWithAttachment.JPG', 0)
#             buffList.append(weaponsWithAttachment)
#         elif 0 in playerBuffs:
#             buffList.append('none')
#
#     return buffList
