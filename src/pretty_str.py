from collections.abc import Iterable

from .ansi_codes import FACES, COLORS, BG_COLORS

Attrs = tuple[set[int], int | None, int | None]

NULL_ATTRS = (set(), None, None)


def _parse_control_nums(control_nums: str) -> Attrs:
    """Turn the numbers portion of a control sequence into Attrs"""
    if not control_nums:
        return NULL_ATTRS
    faces, color, bg = set(), None, None
    for num in control_nums.split(";"):
        num = int(num)
        if num in FACES.values():
            faces.add(num)
        elif num in COLORS.values():
            color = num
        elif num in BG_COLORS.values():
            bg = num
    return faces, color, bg


def _update_attrs(old_attrs: Attrs, new_attrs: Attrs) -> Attrs:
    """Update old_attr with new_attr if attr exists"""
    new_faces = old_attrs[0] | new_attrs[0]
    if 0 in new_faces:
        new_faces = {0}
    new_color = new_attrs[1] if new_attrs[1] else old_attrs[1]
    new_bg_color = new_attrs[2] if new_attrs[2] else old_attrs[2]
    return new_faces, new_color, new_bg_color


def _make_control_sequence(attrs: Attrs) -> str:
    """Turn Attrs into a full control sequence"""
    face_codes = ";".join(map(str, attrs[0]))
    codes = ";".join(
        str(code)
        for code in (face_codes, attrs[1], attrs[2])
        if code
    )
    return f"\033[{codes}m"


def _make_pretty_str(text: str, default_attrs: Attrs) -> str:
    """Split text into control sequence-delimited substrings and update the
    control sequences for each substring, then join the substrings"""
    text = f"\033[m{text}".removeprefix("\033[").removesuffix("\033[m")
    substrs = []
    for substr in text.split("\033["):
        ctrl_nums, content = substr.split("m", 1)
        if content:
            attrs = _parse_control_nums(ctrl_nums)
            attrs = _update_attrs(default_attrs, attrs)
            substrs.append(_make_control_sequence(attrs) + content + "\033[m")
    return "".join(substrs)


def _parse_pretty_attrs(attrs: str | None | Iterable[str | None]=None) -> Attrs:
    """Turn pretty_str input attributes into Attrs tuple"""
    if attrs is None or isinstance(attrs, str):
        attrs = [attrs]
    face_codes = set()
    color_code = None
    bg_code = None
    for attr in attrs:
        if attr is None:
            continue
        attr = attr.lower()
        if attr in FACES:
            face_codes.add(FACES[attr])
            continue
        elif attr in COLORS:
            color_code = COLORS[attr]
            continue
        elif attr in BG_COLORS:
            bg_code = BG_COLORS[attr]
            continue
        else:
            raise ValueError(f"Unrecognized pretty_str attribute: {attr}")
    return (face_codes, color_code, bg_code)


def pretty_str(
    text: str,
    attributes: str | None | Iterable[str | None]=None
) -> str:
    """Use ANSI format codes to adjust typeface, background color and foreground
    color of input text; only supports 16 terminal colors"""
    default_attrs = _parse_pretty_attrs(attributes)
    if default_attrs == NULL_ATTRS:
        return text
    return "".join(_make_pretty_str(text, default_attrs))
