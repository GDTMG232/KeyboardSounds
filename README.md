## Installation

Download and install Python [from here](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe)

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
    "Set": "osu!",
    "..." : [
        "...",
    ],
    "yourSoundsSet" : [
        "default.mp3", "special.mp3", "space.mp3", "backspace.mp3"
    ]
}
```

It MUST be in the order `default , special , space , backspace` otherwise it will not work as you expect it to
