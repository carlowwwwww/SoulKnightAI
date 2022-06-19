import pyautogui
import customtkinter
from PIL import Image, ImageTk

screen_size = pyautogui.size()

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry(f"{int(screen_size[0] * 0.285)}x{int(screen_size[1] * 0.838)}")
app.title("Buff Selector")


def button_function(buff):
    global buffList
    if buff == 'Run':
        print('Program Starting')
    elif buff == 'Clear Selection':
        buffList = list()
        print(buffList)
        print('Buff Selection Cleared')
    elif buff == 'Delete Last':
        del buffList[-1]
        print(buffList)
    else:
        if len(buffList) == 4:
            print('Maximum amount of buffs selected. Please press "Run Program"')
        else:
            buffList.append(buff)
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
clearSelection = customtkinter.CTkButton(master=app, text="Clear Selection", command=lambda: button_function('Clear Selection'))
clearSelection.grid(row=0, column=0, padx=5, pady=15)

runProgram = customtkinter.CTkButton(master=app, text="Run Program", command=lambda: button_function('Run'))
runProgram.grid(row=0, column=1, padx=5, pady=5)

runProgram = customtkinter.CTkButton(master=app, text="Delete Last", command=lambda: button_function('Delete Last'))
runProgram.grid(row=0, column=2, padx=5, pady=5)

buff1 = customtkinter.CTkButton(master=app, text="", image=boss2x, command=lambda: button_function(1))
buff1.grid(row=1, column=0, padx=5, pady=5)

buff2 = customtkinter.CTkButton(master=app, text="", image=atk2xFireRateLess, command=lambda: button_function(2))
buff2.grid(row=1, column=1, padx=5, pady=5)

buff3 = customtkinter.CTkButton(master=app, text="", image=buffChoicePlus2, command=lambda: button_function(3))
buff3.grid(row=1, column=2, padx=5, pady=5)

buff4 = customtkinter.CTkButton(master=app, text="", image=critRate2xCritDamageLess, command=lambda: button_function(4))
buff4.grid(row=2, column=0, padx=5, pady=5)

buff5 = customtkinter.CTkButton(master=app, text="", image=dwarfism, command=lambda: button_function(5))
buff5.grid(row=2, column=1, padx=5, pady=5)

buff6 = customtkinter.CTkButton(master=app, text="", image=FireRate2xAtkLess, command=lambda: button_function(6))
buff6.grid(row=2, column=2, padx=5, pady=5)

buff7 = customtkinter.CTkButton(master=app, text="", image=gigantism, command=lambda: button_function(7))
buff7.grid(row=3, column=0, padx=5, pady=5)

buff8 = customtkinter.CTkButton(master=app, text="", image=gigaPet, command=lambda: button_function(8))
buff8.grid(row=3, column=1, padx=5, pady=5)

buff9 = customtkinter.CTkButton(master=app, text="", image=goodLuck, command=lambda: button_function(9))
buff9.grid(row=3, column=2, padx=5, pady=5)

buff10 = customtkinter.CTkButton(master=app, text="", image=infiniteEnergy, command=lambda: button_function(10))
buff10.grid(row=4, column=0, padx=5, pady=5)

buff11 = customtkinter.CTkButton(master=app, text="", image=maxBuffsPlus3, command=lambda: button_function(11))
buff11.grid(row=4, column=1, padx=5, pady=5)

buff12 = customtkinter.CTkButton(master=app, text="", image=monstersSplitInto2, command=lambda: button_function(12))
buff12.grid(row=4, column=2, padx=5, pady=5)

buff13 = customtkinter.CTkButton(master=app, text="", image=moreBonusRooms, command=lambda: button_function(13))
buff13.grid(row=5, column=0, padx=5, pady=5)

buff14 = customtkinter.CTkButton(master=app, text="", image=moreCritDmg, command=lambda: button_function(14))
buff14.grid(row=5, column=1, padx=5, pady=5)

buff15 = customtkinter.CTkButton(master=app, text="", image=moreEnemies, command=lambda: button_function(15))
buff15.grid(row=5, column=2, padx=5, pady=5)

buff16 = customtkinter.CTkButton(master=app, text="", image=moreRooms, command=lambda: button_function(16))
buff16.grid(row=6, column=0, padx=5, pady=5)

buff17 = customtkinter.CTkButton(master=app, text="", image=moreShield_doesNotRegen, command=lambda: button_function(17))
buff17.grid(row=6, column=1, padx=5, pady=5)

buff18 = customtkinter.CTkButton(master=app, text="", image=multipleStatues, command=lambda: button_function(18))
buff18.grid(row=6, column=2, padx=5, pady=5)

buff19 = customtkinter.CTkButton(master=app, text="", image=newMount, command=lambda: button_function(19))
buff19.grid(row=7, column=0, padx=5, pady=5)

buff20 = customtkinter.CTkButton(master=app, text="", image=newWeapon, command=lambda: button_function(20))
buff20.grid(row=7, column=1, padx=5, pady=5)

buff21 = customtkinter.CTkButton(master=app, text="", image=randomLevels, command=lambda: button_function(21))
buff21.grid(row=7, column=2, padx=5, pady=5)

buff22 = customtkinter.CTkButton(master=app, text="", image=regenHP, command=lambda: button_function(22))
buff22.grid(row=8, column=0, padx=5, pady=5)

buff23 = customtkinter.CTkButton(master=app, text="", image=skillCooldownLow, command=lambda: button_function(23))
buff23.grid(row=8, column=1, padx=5, pady=5)

buff24 = customtkinter.CTkButton(master=app, text="", image=switchCharacter, command=lambda: button_function(24))
buff24.grid(row=8, column=2, padx=5, pady=5)

buff25 = customtkinter.CTkButton(master=app, text="", image=weaponsWithAttachment, command=lambda: button_function(25))
buff25.grid(row=9, column=0, padx=5, pady=5)


app.mainloop()
