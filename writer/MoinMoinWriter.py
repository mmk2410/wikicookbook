class MoinMoinWriter():
    """
    MoinMoin wiki syntax writer.

    Except for newline, linebreak, hrule, table_row_end and macro all commands don't add a newline at the end.

    Nothing is printed, all is returned.
    """

    def newline(self):
        """
        Prints nothing and appends a newline.
        """
        return "\n"

    def linebreak(self):
        """
        Print a froced linebreak (<br>).
        """
        return "<<BR>>\n"

    def hrule(self):
        """
        Print a horizontal rule.
        """
        return "----\n"

    def ulitem(self, text, level=1):
        """
        Print a unordered list item with given level.
        """
        whitespace = " " * level
        return f"{whitespace}* {text}"

    def olitem(self, text, level=1):
        """
        Print a orderd list item with given level.
        """
        whitespace = " " * level
        return f"{whitespace}1. {text}"

    def text(self, text, bold=False, italics=False):
        """
        Just print the given text.
        """
        if bold and italics:
            return f"*****{text}*****"
        elif bold:
            return f"***{text}***"
        elif italics:
            return f"**{text}**"
        else:
            return text

    def link(self, text, url, arguments="", display=False):
        if display:
            if arguments:
                return "{{" + url + f"|{text}|" + arguments + "}}"
            else:
                return "{{" + url + f"|{text}" + "}}"
        else:
            if arguments:
                return f"[[{url}|{text}|{arguments}]]"
            else:
                return f"[[{url}|{text}]]"

    def macro(self, macro, arguments=""):
        return f"<<{macro}({arguments})>>"

    def table_cell(self, text, arguments=""):
        if text:
            return f"||<{arguments}> {text} "
        else:
            return "||"

    def table_row_end(self):
        return "||\n"
