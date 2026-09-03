from pygments.style import Style
from pygments.token import (
    Comment,
    Escape,
    Keyword,
    Name,
    String,
    Literal,
    Error,
    Generic,
    Number,
    Operator,
    Text,
)

__all__ = ["MinLightStyle"]


class Colors:
    """Min Light palette from the official theme JSON."""

    # https://github.com/miguelsolorio/min-theme/blob/master/themes/min-light.json
    foreground = "#24292e"  # token base foreground
    background = "#ffffff"  # editor.background
    highlight = "#E7F3FF52"  # bracket match/selection-like subtle highlight
    error = "#cd3131"  # token.error-token

    # editor line numbers / comments
    gray = "#c2c3c5"  # comments
    line_number = "#CCCCCC"  # editorLineNumber.foreground

    # Accents from tokenColors
    blue = "#1976D2"  # constants, variables, support, numbers
    red = "#D32F2F"  # keywords / storage
    green = "#22863a"  # strings, tags (per theme)
    purple = "#6f42c1"  # functions, types, headings
    orange = "#FF9800"  # parameters


class MinLightStyle(Style):
    """
    Pygments style based on the Min Light theme.

    https://github.com/miguelsolorio/min-theme
    """

    name = "min-light"
    aliases = ["Min Light"]

    background_color = Colors.background
    highlight_color = Colors.highlight
    line_number_color = Colors.line_number

    styles = {
        Text: Colors.foreground,
        Escape: Colors.blue,
        Error: Colors.error,
        # Keywords and operators
        Keyword: Colors.red,
        Keyword.Constant: Colors.blue,
        Keyword.Pseudo: Colors.red,
        Keyword.Type: Colors.red,
        Operator: Colors.red,
        Operator.Word: Colors.red,
        # Names
        Name.Attribute: Colors.purple,
        Name.Builtin: Colors.blue,
        Name.Builtin.Pseudo: Colors.purple,
        Name.Class: Colors.purple,
        Name.Constant: Colors.blue,
        Name.Decorator: Colors.blue,
        Name.Entity: Colors.purple,
        Name.Exception: Colors.purple,
        Name.Function: Colors.purple,
        Name.Property: Colors.blue,
        Name.Label: Colors.blue,
        Name.Tag: Colors.green,
        Name.Variable: Colors.foreground,
        # Literals / strings / numbers
        Literal: Colors.blue,
        String: Colors.green,
        String.Affix: Colors.red,
        String.Backtick: Colors.blue,
        String.Escape: Colors.red,
        String.Interpol: Colors.blue,
        String.Regex: Colors.green,
        String.Symbol: Colors.blue,
        Number: Colors.blue,
        # Comments
        Comment: Colors.gray,
        Comment.Preproc: Colors.red,
        Comment.PreprocFile: Colors.blue,
        # Generic / diffs / headings
        Generic.Deleted: Colors.red,
        Generic.Emph: f"italic {Colors.foreground}",
        Generic.Error: Colors.error,
        Generic.Heading: Colors.purple,
        Generic.Inserted: Colors.green,
        Generic.Output: Colors.green,
        Generic.Prompt: Colors.red,
        Generic.Strong: f"bold {Colors.purple}",
        Generic.Subheading: Colors.purple,
        Generic.Traceback: Colors.error,
    }
