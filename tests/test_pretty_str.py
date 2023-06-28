import unittest

from src.pretty_str import pretty_str
from src.ansi_codes import DEFAULT_FACE, DEFAULT_COLOR, DEFAULT_BG_COLOR


class TestPrettyStr(unittest.TestCase):

    def test_input_modes(self) -> None:
        reg_str = "hello world"
        bold_str = f"\033[1m{reg_str}\033[m"
        # regular input
        self.assertEqual(bold_str, pretty_str(reg_str, "bold"))
        # case insensitive
        self.assertEqual(bold_str, pretty_str(reg_str, "BOLD"))
        # None
        self.assertEqual(reg_str, pretty_str(reg_str))
        self.assertEqual(reg_str, pretty_str(reg_str, None))
        # iterable
        self.assertEqual(bold_str, pretty_str(reg_str, ["bold"]))
        self.assertEqual(bold_str, pretty_str(reg_str, ["bold", None]))
        self.assertEqual(bold_str, pretty_str(reg_str, ["bold", "bold"]))
        self.assertEqual(reg_str, pretty_str(reg_str, []))
        self.assertEqual(reg_str, pretty_str(reg_str, [None]))

    def test_invalid_input(self) -> None:
        reg_str = "hello world"
        self.assertRaises(ValueError, pretty_str, reg_str, "")
        self.assertRaises(ValueError, pretty_str, reg_str, "NonAttr")
        self.assertRaises(ValueError, pretty_str, reg_str, [""])
        self.assertRaises(ValueError, pretty_str, reg_str, ["NonAttr"])
        self.assertRaises(ValueError, pretty_str, reg_str, ["NonAttr", None])
        self.assertRaises(ValueError, pretty_str, reg_str, ["bold", "NonAttr"])

    def test_face(self) -> None:
        reg_str = "hello world"
        bold_str = f"\033[1m{reg_str}\033[m"
        default_str = f"\033[{DEFAULT_FACE}m{reg_str}\033[m"
        self.assertEqual(bold_str, pretty_str(reg_str, "bold"))
        self.assertEqual(default_str, pretty_str(reg_str, "default_face"))

    def test_color(self) -> None:
        reg_str = "hello world"
        blue_str = f"\033[34m{reg_str}\033[m"
        default_str = f"\033[{DEFAULT_COLOR}m{reg_str}\033[m"
        self.assertEqual(blue_str, pretty_str(reg_str, "blue"))
        self.assertEqual(default_str, pretty_str(reg_str, "default_color"))

    def test_bg_color(self) -> None:
        reg_str = "hello world"
        bg_red_str = f"\033[41m{reg_str}\033[m"
        default_str = f"\033[{DEFAULT_BG_COLOR}m{reg_str}\033[m"
        self.assertEqual(bg_red_str, pretty_str(reg_str, "bg_red"))
        self.assertEqual(default_str, pretty_str(reg_str, "default_bg_color"))

    def test_multi_attrs(self) -> None:
        reg_str = "hello world"
        bold_blue_str = f"\033[1;34m{reg_str}\033[m"
        bold_blue_bg_red_str = f"\033[1;34;41m{reg_str}\033[m"
        bold_italic_str = f"\033[1;3m{reg_str}\033[m"
        self.assertEqual(bold_blue_str, pretty_str(reg_str, ["bold", "blue"]))
        self.assertEqual(
            bold_blue_bg_red_str,
            pretty_str(reg_str, ["bold", "blue", "bg_red"])
        )
        self.assertEqual(
            bold_italic_str,
            pretty_str(reg_str, ["bold", "italic"])
        )

    def test_nested_attrs(self) -> None:
        b_hello_i_world_blue_str = (
            f"\033[1;34mhello\033[m\033[34m \033[m\033[3;34mworld\033[m"
        )
        b_hello_str = pretty_str("hello", "bold")
        i_world_str = pretty_str("world", "italic")
        self.assertEqual(
            b_hello_i_world_blue_str,
            pretty_str(f"{b_hello_str} {i_world_str}", "blue")
        )

    def test_nested_default_attrs(self) -> None:
        world = pretty_str(
            "world",
            ["default_face", "default_color", "default_bg_color"]
        )
        default_world = (
            f"\033[{DEFAULT_FACE};{DEFAULT_COLOR};{DEFAULT_BG_COLOR}mworld\033[m"
        )
        self.assertEqual(default_world, world)
        bold_blue_bg_red_str = (
            f"\033[1;34;41mhello \033[m{default_world}\033[1;34;41m!\033[m"
        )
        self.assertEqual(
            bold_blue_bg_red_str,
            pretty_str(f"hello {world}!", ["bold", "blue", "bg_red"])

        )



if __name__ == "__main__":
    unittest.main()
