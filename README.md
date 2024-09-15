## Installation

Download and install Python [from here](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe)

In CMD or Terminal you can run `pip install pygame pynput` for the `__main__.py` file to work properly

## How to use this program

Just run the `__main__.py` file with Python

You can use Folders and your own sounds if you'd like, for example:
```
KeyboardSounds/
└── yourSoundsSet/
     ├── default.mp3
     ├── special.mp3
     ├── space.mp3
     └── backspace.mp3
```

and in the `__main__.py` file you can add a Key to the `Sounds` variable, like this:

```py
# Your Sounds here

Sounds = {
    ... : [
        ...
    ],
    "yourSoundsSet" : [
        "default.mp3", "special.mp3", "space.mp3", "backspace.mp3"
    ]
}

Set = "yourSoundsSet" # Set this to the set of sounds you'd like to use
```

It MUST be in the order `default special space backspace` otherwise it will not work