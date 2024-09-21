# KeyboardSounds V1.0.4
[Releases](https://github.com/GDTMG232/KeyboardSounds/releases) , [V1.0.4 Notes](#patch-notes-for-v104) , [KeyboardSounds Website](https://gdtmg232.github.io/KeyboardSounds) , [TMG's Discord Server](https://discord.com/invite/QtXPH9SVzV)

## Installation

Download and install Python [from here](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe) (Make sure to add PIP and also add Python to PATH)

Open the `Install Requirements.bat` file to install required dependencies for the `__main__.py` file to work properly

## How to use this program

Just run the `__main__.py` file with Python

You can use Folders and your own sounds if you'd like, for example:
```
KeyboardSounds/
└── Sounds/
    └── yourSoundsSet/
        ├── default.mp3
        ├── special.mp3
        ├── space.mp3
        └── backspace.mp3
```

and in the `Sounds.json` file you can add a Key to the JSON.

```json
{
    "Set": "YourSoundSet",
    "..." : [
        "...",
    ],
    "YourSoundSet" : {
        "default": "default.mp3",
        "special": "special.mp3", 
        "space": "space.mp3",
        "backspace": "backspace.mp3"
    }
}
```

You can also change what keys are considered Special or Backspace and whatnot in the `YourKeys.py` file

also no im not making `YourKeys.py` a JSON file, I can't be asked 😭

## Patch Notes for V1.0.4

Added a new function
In Sounds.json you can have an `"all"` key so you don't have to set everything to the same file.

Download V1.0.4 [here](https://github.com/GDTMG232/KeyboardSounds/releases/tag/v1.0.4)
