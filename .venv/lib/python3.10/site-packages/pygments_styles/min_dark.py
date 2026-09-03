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

__all__ = ["MinDarkStyle"]


class Colors:
    """Min Dark palette from the official theme JSON."""

    # https://github.com/miguelsolorio/min-theme/blob/master/themes/min-dark.json
    background = "#1f1f1f"
    foreground = "#EAEAEA"  # readable default text
    highlight = "#79b8ff33"  # subtle selection-like highlight
    error = "#cd3131"

    # Editor elements
    line_number = "#727272"

    # Token accents
    purple = "#b392f0"  # functions/types/headings
    blue = "#79b8ff"  # constants/support/properties
    red = "#f97583"  # keywords/operators
    orange = "#FF9800"  # parameters
    tag_orange = "#ffab70"  # tags/strings
    comment = "#6b737c"
    white = "#f8f8f8"  # numeric/placeholder


class MinDarkStyle(Style):
    """
    Pygments style based on the Min Dark theme.

    https://github.com/miguelsolorio/min-theme
    """

    name = "min-dark"
    aliases = ["Min Dark"]

    background_color = Colors.background
    highlight_color = Colors.highlight
    line_number_color = Colors.line_number

    styles = {
        Text: Colors.foreground,
        Escape: Colors.blue,
        Error: Colors.error,
        # Keywords and operators
        Keyword: Colors.red,
        Keyword.Constant: Colors.white,
        Keyword.Pseudo: Colors.red,
        Keyword.Type: Colors.red,
        Operator: Colors.red,
        Operator.Word: Colors.red,
        # Names
        Name.Attribute: Colors.purple,
        Name.Builtin: Colors.purple,
        Name.Class: Colors.purple,
        Name.Constant: Colors.blue,
        Name.Decorator: Colors.blue,
        Name.Entity: Colors.purple,
        Name.Exception: Colors.blue,
        Name.Function: Colors.purple,
        Name.Property: Colors.blue,
        Name.Label: Colors.blue,
        Name.Tag: Colors.tag_orange,
        Name.Variable: Colors.foreground,
        # Literals / strings / numbers
        Literal: Colors.blue,
        String: Colors.tag_orange,
        String.Affix: Colors.red,
        String.Backtick: Colors.blue,
        String.Escape: Colors.red,
        String.Interpol: Colors.red,
        String.Regex: Colors.tag_orange,
        String.Symbol: Colors.blue,
        Number: Colors.white,
        # Comments
        Comment: Colors.comment,
        Comment.Preproc: Colors.red,
        Comment.PreprocFile: Colors.blue,
        # Generic / diffs / headings
        Generic.Deleted: Colors.error,
        Generic.Emph: f"italic {Colors.foreground}",
        Generic.Error: Colors.error,
        Generic.Heading: Colors.purple,
        Generic.Inserted: "#3a632a",
        Generic.Output: Colors.tag_orange,
        Generic.Prompt: Colors.red,
        Generic.Strong: f"bold {Colors.purple}",
        Generic.Subheading: Colors.purple,
        Generic.Traceback: Colors.error,
    }
