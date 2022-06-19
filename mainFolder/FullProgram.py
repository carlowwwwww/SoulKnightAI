import tkinter
from MultipleBuffRecognition import multipleBuffRecognition
import pyautogui
import customtkinter
from PIL import Image, ImageTk
# ------------------------------------------------------------------------------------------------------------ #
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
screen_size = pyautogui.size()
app.geometry(f"{int(screen_size[0] * 0.285)}x{int(screen_size[1] * 0.85)}")
app.resizable(False, False)
app.title("Buff Selector")


def button_function(buff):
    global buffList
    global running

    if running:
        pass
    else:
        if buff == 'Run':
            if len(buffList) < 1:
                print('You need to select at least 1 buff.')
            elif 1 <= len(buffList) < 4:
                while len(buffList) < 4:
                    buffList.append('freeSlot')
                    running = True

                exec_len = slider.get()
                matchReport = multipleBuffRecognition(buffList, exec_len)

                if matchReport:
                    buffList = list()

                running = False
            else:
                print('Program Starting')
                running = True

                exec_len = slider.get()
                matchReport = multipleBuffRecognition(buffList, exec_len)

                if matchReport:
                    buffList = list()

                running = False
        else:
            if len(buffList) == 4:
                print('Maximum amount of buffs selected. Please press "Run Program"')
            else:
                buffList.append(buff)
                print(buffList)


# Working on implementing the progress bar. Thinking of a way to update the bar while the function is running


def clearSelection():
    global buffList
    global running
    global widgetList

    if running:
        pass
    else:
        buffList = list()
        print(buffList)
        for buff in widgetList:
            buff.configure(fg_color='#1f6aa5', state=tkinter.NORMAL)
        print('Buff Selection Cleared')


def deleteLast():
    global running

    if running:
        pass
    else:
        del buffList[-1]
        print(buffList)


def slider_event():
    pass


def changeBuffColor(buff):
    global buffList

    if len(buffList) == 4:
        pass
    else:
        buff.configure(fg_color='dark blue', state=tkinter.DISABLED)


buffList = []
running = False

imageDimensions = round(screen_size[0] / 27.2)

# Image
boss2x = (Image.open('Buffs/2xBoss.JPG')).resize((imageDimensions, imageDimensions))
boss2x = ImageTk.PhotoImage(boss2x)

atk2xFireRateLess = (Image.open('Buffs/atk2xFireRateLess.JPG')).resize((imageDimensions, imageDimensions))
atk2xFireRateLess = ImageTk.PhotoImage(atk2xFireRateLess)

buffChoicePlus2 = (Image.open('Buffs/buffChoicePlus2.JPG')).resize((imageDimensions, imageDimensions))
buffChoicePlus2 = ImageTk.PhotoImage(buffChoicePlus2)

critRate2xCritDamageLess = (Image.open('Buffs/critRate2xCritDamageLess.JPG')).resize((imageDimensions, imageDimensions))
critRate2xCritDamageLess = ImageTk.PhotoImage(critRate2xCritDamageLess)

dwarfism = (Image.open('Buffs/dwarfism.JPG')).resize((imageDimensions, imageDimensions))
dwarfism = ImageTk.PhotoImage(dwarfism)

FireRate2xAtkLess = (Image.open('Buffs/FireRate2xAtkLess.JPG')).resize((imageDimensions, imageDimensions))
FireRate2xAtkLess = ImageTk.PhotoImage(FireRate2xAtkLess)

gigantism = (Image.open('Buffs/gigantism.JPG')).resize((imageDimensions, imageDimensions))
gigantism = ImageTk.PhotoImage(gigantism)

gigaPet = (Image.open('Buffs/gigaPet.JPG')).resize((imageDimensions, imageDimensions))
gigaPet = ImageTk.PhotoImage(gigaPet)

goodLuck = (Image.open('Buffs/goodLuck.JPG')).resize((imageDimensions, imageDimensions))
goodLuck = ImageTk.PhotoImage(goodLuck)

infiniteEnergy = (Image.open('Buffs/infiniteEnergy.JPG')).resize((imageDimensions, imageDimensions))
infiniteEnergy = ImageTk.PhotoImage(infiniteEnergy)

maxBuffsPlus3 = (Image.open('Buffs/maxBuffsPlus3.JPG')).resize((imageDimensions, imageDimensions))
maxBuffsPlus3 = ImageTk.PhotoImage(maxBuffsPlus3)

monstersSplitInto2 = (Image.open('Buffs/monstersSplitInto2.JPG')).resize((imageDimensions, imageDimensions))
monstersSplitInto2 = ImageTk.PhotoImage(monstersSplitInto2)

moreBonusRooms = (Image.open('Buffs/moreBonusRooms.JPG')).resize((imageDimensions, imageDimensions))
moreBonusRooms = ImageTk.PhotoImage(moreBonusRooms)

moreCritDmg = (Image.open('Buffs/moreCritDmg.JPG')).resize((imageDimensions, imageDimensions))
moreCritDmg = ImageTk.PhotoImage(moreCritDmg)

moreEnemies = (Image.open('Buffs/moreEnemies.JPG')).resize((imageDimensions, imageDimensions))
moreEnemies = ImageTk.PhotoImage(moreEnemies)

moreRooms = (Image.open('Buffs/moreRooms.JPG')).resize((imageDimensions, imageDimensions))
moreRooms = ImageTk.PhotoImage(moreRooms)

moreShield_doesNotRegen = (Image.open('Buffs/moreShield_doesNotRegen.JPG')).resize((imageDimensions, imageDimensions))
moreShield_doesNotRegen = ImageTk.PhotoImage(moreShield_doesNotRegen)

multipleStatues = (Image.open('Buffs/multipleStatues.JPG')).resize((imageDimensions, imageDimensions))
multipleStatues = ImageTk.PhotoImage(multipleStatues)

newMount = (Image.open('Buffs/newMount.JPG')).resize((imageDimensions, imageDimensions))
newMount = ImageTk.PhotoImage(newMount)

newWeapon = (Image.open('Buffs/newWeapon.JPG')).resize((imageDimensions, imageDimensions))
newWeapon = ImageTk.PhotoImage(newWeapon)

randomLevels = (Image.open('Buffs/randomLevels.JPG')).resize((imageDimensions, imageDimensions))
randomLevels = ImageTk.PhotoImage(randomLevels)

regenHP = (Image.open('Buffs/regenHP.JPG')).resize((imageDimensions, imageDimensions))
regenHP = ImageTk.PhotoImage(regenHP)

skillCooldownLow = (Image.open('Buffs/skillCooldownLow.JPG')).resize((imageDimensions, imageDimensions))
skillCooldownLow = ImageTk.PhotoImage(skillCooldownLow)

switchCharacter = (Image.open('Buffs/switchCharacter.JPG')).resize((imageDimensions, imageDimensions))
switchCharacter = ImageTk.PhotoImage(switchCharacter)

weaponsWithAttachment = (Image.open('Buffs/weaponsWithAttachment.JPG')).resize((imageDimensions, imageDimensions))
weaponsWithAttachment = ImageTk.PhotoImage(weaponsWithAttachment)

# User Interface
slider = customtkinter.CTkSlider(master=app, from_=0, to=10, command=slider_event)
slider.place(relx=0.665, rely=0.95, anchor=tkinter.CENTER)
slider.configure(number_of_steps=2, from_=5, to=15, width=int((screen_size[0] * 0.285)/1.7), height=int((screen_size[1] * 0.85)/25))
sliderLabel = customtkinter.CTkLabel(master=app, text="Running Duration in seconds: 5, 10, 15")
sliderLabel.place(relx=0.665, rely=0.905, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=app)
progressbar.set(0)
progressbar.place(relx=0.5, rely=0.99, anchor=tkinter.CENTER)
progressbar.configure(width=int((screen_size[0] * 0.285)/1.01))

# Use CTkButton instead of tkinter Button
clearSelectedBuffs = customtkinter.CTkButton(master=app, text="Clear Selection", command=clearSelection)
clearSelectedBuffs.grid(row=0, column=0, padx=5, pady=15)

open_instructions = customtkinter.CTkButton(master=app, text="Update Soon :)")
# command=lambda: create_toplevel(app, open_instructions))
open_instructions.grid(row=0, column=2, padx=5, pady=5)

runProgram = customtkinter.CTkButton(master=app, text="Run Program", command=lambda: button_function('Run'))
runProgram.grid(row=0, column=1, padx=5, pady=5)

# Buffs
buff1 = customtkinter.CTkButton(master=app, text="", image=boss2x,
                                command=lambda: [changeBuffColor(buff1), button_function('2xBoss')])
buff1.grid(row=1, column=0, padx=5, pady=5)

buff2 = customtkinter.CTkButton(master=app, text="", image=atk2xFireRateLess,
                                command=lambda: [changeBuffColor(buff2), button_function('atk2xFireRateLess')])
buff2.grid(row=1, column=1, padx=5, pady=5)

buff3 = customtkinter.CTkButton(master=app, text="", image=buffChoicePlus2,
                                command=lambda: [changeBuffColor(buff3), button_function('buffChoicePlus2')])
buff3.grid(row=1, column=2, padx=5, pady=5)

buff4 = customtkinter.CTkButton(master=app, text="", image=critRate2xCritDamageLess,
                                command=lambda: [changeBuffColor(buff4), button_function('critRate2xCritDamageLess')])
buff4.grid(row=2, column=0, padx=5, pady=5)

buff5 = customtkinter.CTkButton(master=app, text="", image=dwarfism,
                                command=lambda: [changeBuffColor(buff5), button_function('dwarfism')])
buff5.grid(row=2, column=1, padx=5, pady=5)

buff6 = customtkinter.CTkButton(master=app, text="", image=FireRate2xAtkLess,
                                command=lambda: [changeBuffColor(buff6), button_function('FireRate2xAtkLess')])
buff6.grid(row=2, column=2, padx=5, pady=5)

buff7 = customtkinter.CTkButton(master=app, text="", image=gigantism,
                                command=lambda: [changeBuffColor(buff7), button_function('gigantism')])
buff7.grid(row=3, column=0, padx=5, pady=5)

buff8 = customtkinter.CTkButton(master=app, text="", image=gigaPet,
                                command=lambda: [changeBuffColor(buff8), button_function('gigaPet')])
buff8.grid(row=3, column=1, padx=5, pady=5)

buff9 = customtkinter.CTkButton(master=app, text="", image=goodLuck,
                                command=lambda: [changeBuffColor(buff9), button_function('goodLuck')])
buff9.grid(row=3, column=2, padx=5, pady=5)

buff10 = customtkinter.CTkButton(master=app, text="", image=infiniteEnergy,
                                 command=lambda: [changeBuffColor(buff10), button_function('infiniteEnergy')])
buff10.grid(row=4, column=0, padx=5, pady=5)

buff11 = customtkinter.CTkButton(master=app, text="", image=maxBuffsPlus3,
                                 command=lambda: [changeBuffColor(buff11), button_function('maxBuffsPlus3')])
buff11.grid(row=4, column=1, padx=5, pady=5)

buff12 = customtkinter.CTkButton(master=app, text="", image=monstersSplitInto2,
                                 command=lambda: [changeBuffColor(buff12), button_function('monstersSplitInto2')])
buff12.grid(row=4, column=2, padx=5, pady=5)

buff13 = customtkinter.CTkButton(master=app, text="", image=moreBonusRooms,
                                 command=lambda: [changeBuffColor(buff13), button_function('moreBonusRooms')])
buff13.grid(row=5, column=0, padx=5, pady=5)

buff14 = customtkinter.CTkButton(master=app, text="", image=moreCritDmg,
                                 command=lambda: [changeBuffColor(buff14), button_function('moreCritDmg')])
buff14.grid(row=5, column=1, padx=5, pady=5)

buff15 = customtkinter.CTkButton(master=app, text="", image=moreEnemies,
                                 command=lambda: [changeBuffColor(buff15), button_function('moreEnemies')])
buff15.grid(row=5, column=2, padx=5, pady=5)

buff16 = customtkinter.CTkButton(master=app, text="", image=moreRooms,
                                 command=lambda: [changeBuffColor(buff16), button_function('moreRooms')])
buff16.grid(row=6, column=0, padx=5, pady=5)

buff17 = customtkinter.CTkButton(master=app, text="", image=moreShield_doesNotRegen,
                                 command=lambda: [changeBuffColor(buff17), button_function('moreShield_doesNotRegen')])
buff17.grid(row=6, column=1, padx=5, pady=5)

buff18 = customtkinter.CTkButton(master=app, text="", image=multipleStatues,
                                 command=lambda: [changeBuffColor(buff18), button_function('multipleStatues')])
buff18.grid(row=6, column=2, padx=5, pady=5)

buff19 = customtkinter.CTkButton(master=app, text="", image=newMount,
                                 command=lambda: [changeBuffColor(buff19), button_function('newMount')])
buff19.grid(row=7, column=0, padx=5, pady=5)

buff20 = customtkinter.CTkButton(master=app, text="", image=newWeapon,
                                 command=lambda: [changeBuffColor(buff20), button_function('newWeapon')])
buff20.grid(row=7, column=1, padx=5, pady=5)

buff21 = customtkinter.CTkButton(master=app, text="", image=randomLevels,
                                 command=lambda: [changeBuffColor(buff21), button_function('randomLevels')])
buff21.grid(row=7, column=2, padx=5, pady=5)

buff22 = customtkinter.CTkButton(master=app, text="", image=regenHP,
                                 command=lambda: [changeBuffColor(buff22), button_function('regenHP')])
buff22.grid(row=8, column=0, padx=5, pady=5)

buff23 = customtkinter.CTkButton(master=app, text="", image=skillCooldownLow,
                                 command=lambda: [changeBuffColor(buff23), button_function('skillCooldownLow')])
buff23.grid(row=8, column=1, padx=5, pady=5)

buff24 = customtkinter.CTkButton(master=app, text="", image=switchCharacter,
                                 command=lambda: [changeBuffColor(buff24), button_function('switchCharacter')])
buff24.grid(row=8, column=2, padx=5, pady=5)

buff25 = customtkinter.CTkButton(master=app, text="", image=weaponsWithAttachment,
                                 command=lambda: [changeBuffColor(buff25), button_function('weaponsWithAttachment')])
buff25.grid(row=9, column=0, padx=5, pady=5)

widgetList = [buff1, buff2, buff3, buff4, buff5, buff6, buff7, buff8, buff9, buff10, buff11, buff12, buff13, buff14, buff15,
              buff16, buff17, buff18, buff19, buff20, buff21, buff22, buff23, buff24, buff25]

app.mainloop()

instructions = ''
