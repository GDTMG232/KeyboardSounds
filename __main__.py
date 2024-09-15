import pygame
from pynput import keyboard
import os

# Initialize pygame mixer
pygame.mixer.init()

Sounds = {
    "osu!" : [
        "osu_default.mp3", "osu_special.mp3", "osu_space.mp3", "osu_bkspc.mp3"
    ]
}

Set = "osu!" # Set this to the set of sounds you'd like to use

# Load different sounds
default_sound = pygame.mixer.Sound(os.path.join(Set, Sounds[Set][0]))   # Replace with your default sound
special_sound = pygame.mixer.Sound(os.path.join(Set, Sounds[Set][1]))    # Replace with the special keys sound
space_sound = pygame.mixer.Sound(os.path.join(Set, Sounds[Set][2]))        # Replace with the spacebar sound
backspace_sound = pygame.mixer.Sound(os.path.join(Set, Sounds[Set][3]))  # Replace with the backspace sound

# Function to play sound
def play_sound(sound):
    sound.play()

# Callback function for key press event
def on_press(key):
    try:
        # Check if the key is a special key (Ctrl, AltGr, Function keys)
        if key in [keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, 
                   keyboard.Key.alt_gr, keyboard.Key.alt, 
                   keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r] or \
                   isinstance(key, keyboard.KeyCode) and key.char in [f'F{i}' for i in range(1, 25)]: # Checks for F1 to F24 keys (yes F13 to F24 exists)
            play_sound(special_sound)  # Special key pressed
        elif key == keyboard.Key.space:
            play_sound(space_sound)  # Spacebar pressed
        elif key == keyboard.Key.backspace:
            play_sound(backspace_sound)  # Backspace pressed
        else:
            play_sound(default_sound)  # Any other key
    except AttributeError:
        play_sound(default_sound)  # For regular keys (a-z, 0-9, etc.)

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
