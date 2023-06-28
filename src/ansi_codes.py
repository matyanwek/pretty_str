# see https://en.wikipedia.org/wiki/ANSI_escape_code for reference

DEFAULT_FACE = 0  # ansi normal font
FACES = {
    "default_face": DEFAULT_FACE,
    "bold": 1,
    "faint": 2,
    "italic": 3,
    "underline": 4,
    "blink": 5,
    "fastblink": 6,
    "reverse": 7,
    "invert": 7,
    "hide": 8,
    "conceal": 8,
    "strike": 9,
}

DEFAULT_COLOR = 39  # ansi default foreground colo
COLORS = {
    "default_color": DEFAULT_COLOR,
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "bright_black": 90,
    "gray": 90,
    "grey": 90,
    "bright_red": 91,
    "bright_green": 92,
    "bright_yellow": 93,
    "bright_blue": 94,
    "bright_magenta": 95,
    "bright_cyan": 96,
    "bright_white": 97,
}

DEFAULT_BG_COLOR = 49  # ansi default background color
BG_COLORS = {
    "default_bg_color": DEFAULT_BG_COLOR,
    "bg_black": 40,
    "bg_red": 41,
    "bg_green": 42,
    "bg_yellow": 43,
    "bg_blue": 44,
    "bg_magenta": 45,
    "bg_cyan": 46,
    "bg_white": 47,
    "bg_bright_black": 100,
    "bg_gray": 100,
    "bg_grey": 100,
    "bg_bright_red": 101,
    "bg_bright_green": 102,
    "bg_bright_yellow": 103,
    "bg_bright_blue": 104,
    "bg_bright_magenta": 105,
    "bg_bright_cyan": 106,
    "bg_bright_white": 107,
}
