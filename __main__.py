import pygame
from pynput import keyboard
import os
import json

pygame.mixer.init()

# Load sound configuration from Sounds.json
with open("Sounds.json", "r") as Sounds:
    Sounds = json.load(Sounds)

yourSet = Sounds["Set"]

# Load sounds based on the selected set
default = pygame.mixer.Sound(os.path.join("Sounds", yourSet, Sounds[yourSet][0]))
special = pygame.mixer.Sound(os.path.join("Sounds", yourSet, Sounds[yourSet][1]))
space = pygame.mixer.Sound(os.path.join("Sounds", yourSet, Sounds[yourSet][2]))
backspace = pygame.mixer.Sound(os.path.join("Sounds", yourSet, Sounds[yourSet][3]))

def play_sound(sound):
    sound.play()

FunctionKeys = [keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12, keyboard.Key.f13, keyboard.Key.f14, keyboard.Key.f15, 
keyboard.Key.f16, keyboard.Key.f17, keyboard.Key.f18, keyboard.Key.f19, keyboard.Key.f20, keyboard.Key.f21, keyboard.Key.f22, keyboard.Key.f23, keyboard.Key.f24]

def on_press(key):
    try:
        # Play special sound for control, alt, shift, and function keys
        if key in [keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, 
                   keyboard.Key.alt_gr, keyboard.Key.alt, 
                   keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r, keyboard.Key.esc] + FunctionKeys:
            play_sound(special)
        # Play space sound for space key
        elif key == keyboard.Key.space:
            play_sound(space)
        # Play backspace sound for backspace key
        elif key == keyboard.Key.backspace:
            play_sound(backspace)
        # Play default sound for all other keys
        else:
            play_sound(default)
    except AttributeError:
        play_sound(default)

# Start listening for keypresses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
