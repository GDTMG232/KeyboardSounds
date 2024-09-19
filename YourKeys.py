# no i cant make this a json file, dont ask me for it

from pynput import keyboard

functionKeys = [
    keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5,
    keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10,
    keyboard.Key.f11, keyboard.Key.f12, keyboard.Key.f13, keyboard.Key.f14, keyboard.Key.f15, 
    keyboard.Key.f16, keyboard.Key.f17, keyboard.Key.f18, keyboard.Key.f19, keyboard.Key.f20,
    keyboard.Key.f21, keyboard.Key.f22, keyboard.Key.f23, keyboard.Key.f24
]

specialKeys = [
    keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_gr, keyboard.Key.alt_l, keyboard.Key.shift_l,
    keyboard.Key.shift_r, keyboard.Key.esc, keyboard.Key.cmd_l, keyboard.Key.cmd_r, keyboard.Key.caps_lock,
    keyboard.Key.page_down, keyboard.Key.page_up, keyboard.Key.insert, keyboard.Key.esc, keyboard.Key.up,
    keyboard.Key.down, keyboard.Key.left, keyboard.Key.right
] + functionKeys

backspaceKeys = [
    keyboard.Key.backspace, keyboard.Key.delete
]

spaceKeys = [
    keyboard.Key.space
]