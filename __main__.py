print("Loading...")

import pygame
from pynput import keyboard
import os
import json
from YourKeys import backspaceKeys, specialKeys, spaceKeys

os.system("title KeyboardSounds")

pygame.mixer.init()

os.system("cls" if os.name == "nt" else "clear")
print("KeyboardSounds 1.0.4\nCreated By TMG")

# Load sound configuration from Sounds.json
try:
    with open(os.path.join(__file__, "..", "Sounds.json"), "r") as Sounds:
        Sounds = json.load(Sounds)
except FileNotFoundError:
    print("Did you delete Sounds.json?")
    exit()

yourSet = Sounds["Set"]
if "all" in Sounds[yourSet]:
    try:
        default = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["all"]))
        special = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["all"]))
        space = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["all"]))
        backspace = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["all"]))
    except FileNotFoundError:
        print("Did you delete or misspell your sound file?? Double-check Sounds.json and your Sounds directory")
        exit()
else:
    try:
        default = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["default"]))
        special = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["special"]))
        space = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["space"]))
        backspace = pygame.mixer.Sound(os.path.join(__file__, "..", "Sounds", yourSet, Sounds[yourSet]["backspace"]))
    except FileNotFoundError:
        print("Did you delete or miss any of your sound files? Double-check Sounds.json and your Sounds directory")
        exit()

def play_sound(sound):
    sound.play()

def on_press(key):
    try:
        # Play special sound for control, alt, shift, and function keys
        if key in specialKeys:
            play_sound(special)
        # Play space sound for space key
        elif key in spaceKeys:
            play_sound(space)
        # Play backspace sound for backspace key
        elif key in backspaceKeys:
            play_sound(backspace)
        # Play default sound for all other keys
        else:
            play_sound(default)
    except AttributeError:
        play_sound(default)

# Start listening for keypresses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
