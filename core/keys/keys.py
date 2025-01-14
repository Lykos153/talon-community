from talon import Context, Module, actions, app

from ..user_settings import get_list_from_csv


def setup_default_alphabet():
    """set up common default alphabet.

    no need to modify this here, change your alphabet using alphabet.csv"""
    initial_default_alphabet = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split()
    initial_letters_string = "abcdefghijklmnopqrstuvwxyz"
    initial_default_alphabet_dict = dict(
        zip(initial_default_alphabet, initial_letters_string)
    )

    return initial_default_alphabet_dict


alphabet_list = get_list_from_csv(
    "alphabet.csv", ("Letter", "Spoken Form"), setup_default_alphabet()
)

# used for number keys & function keys respectively
digits = "zero one two three four five six seven bubbles nine".split()
f_digits = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("immune_symbol_key", desc="Symbols that can appear in a formatter")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")


@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.immune_symbol_key}")
def immune_symbol_key(m) -> str:
    "A symbol key that is allowed to appear within a format string"
    return m.immune_symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


ctx = Context()
modifier_keys = {
    "hype": "alt",  #'alter': 'alt',
    "troll": "ctrl",  #'troll':   'ctrl',
    "ship": "shift",  #'sky':     'shift',
    "soup": "super",
}
if app.platform == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"
ctx.lists["self.modifier_key"] = modifier_keys
ctx.lists["self.letter"] = alphabet_list

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
# `dictation_only_punctuation_words` is for punctuation words that you only
# want to be available during dictation, not command mode
punctuation_words = {
}

dictation_only_punctuation_words = {
    "dollar sign": "$",
    "ampersand": "&",
    "back tick": "`",
    "comma": ",",
    # Workaround for issue with conformer b-series; see #946
    "coma": ",",
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "asterisk": "*",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    # Currencies
    "euro sign": "€",
    "dollar sign": "$",
}

immune_symbol_key_words = {
    "point": ".",
    "dash": "-",
}

symbol_key_words = {
    "brick": "`",
    "stroke": "/",
    "backstroke": "\\",
    "equal": "=",
    "plus": "+",
    "grave": "`",
    "tilde": "~",
    "bang": "!",
    "score": "_",
    "quest": "?",
    "single": "'",
    "double": '"',
    "leper": "(",
    "repper": ")",
    "lacker": "[",
    "racker": "]",
    "lacer": "{",
    "racer": "}",
    "langle": "<",
    "wrangle": ">",
    "snow": "*",
    "pound": "#",
    "percy": "%",
    "tangle": "^",
    "amper": "&",
    "pipe": "|",
    "dollar": "$",
    "semi": ";",
    "stack": ":",
    "drip": ",",
       
    # "same": ";",
    # "clause": ":",
    # "slash": "/",
    # "ask": "?",
    # "yell": "!",
    # "star": "*",
    # "hash": "#",
    # "mood": "%",
    # "snail": "@",
    # "gain": "&",
    # "quid": "$",
    # "mine": "-",
    # "wax": "(",
    # "wayne": ")",
    # "quote": "'",
    # "brick": "[",
    # "brack": "]",
    # "backslash": "\\",
    # "plus": "+",
    # "tide": "~",
    # "score": "_",
    # "curl": "{",
    # "crimp": "}",
    # "small": "<",
    # "big": ">",
    # "blunt": "^",
    # "spoke": '"',
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
symbol_key_words.update(immune_symbol_key_words)
punctuation_words.update(dictation_only_punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.immune_symbol_key"] = immune_symbol_key_words
ctx.lists["self.number_key"] = {name: str(i) for i, name in enumerate(digits)}
ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}

simple_keys = [
    "end",
    "home",
    "insert",
    "space",
]

alternate_keys = {
    "clap": "enter",
    "drill": "delete",
    "scratch": "backspace",
    "scrape": "escape",
    "void": "space",
    "real": "pageup",
    "page": "pagedown",

    # "hack": "backspace",
    # "toss": "delete",
    # "yes": "enter",
    # "act": "escape",
    "tabby": "tab",
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"fun {name}": f"f{i}" for i, name in enumerate(f_digits, start=1)
}


@mod.capture(rule="spell {self.letter}+")
def spell(m) -> str:
    """Spell a word"""
    return "".join(m.letter_list)


@mod.action_class
class Actions:
    def move_cursor(s: str):
        """Given a sequence of directions, eg. 'left left up', moves the cursor accordingly using edit.{left,right,up,down}."""
        for d in s.split():
            if d in ("left", "right", "up", "down"):
                getattr(actions.edit, d)()
            else:
                raise RuntimeError(f"invalid arrow key: {d}")
