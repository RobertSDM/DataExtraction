from collections import defaultdict

import pyperclip
from constants import table_columns_and_types as tcol
import pyautogui as pyt


def columns_position(col_line: str) -> dict[str, int]:
    """Identify where a column start or end

    Args
        col_line: Line representing the columns
    Returns
        Columns start or end positions
    """

    positions = defaultdict(list)
    col = False
    coli = 0
    pos = []

    for i, l in enumerate(col_line):
        if l == " ":
            if col:
                pos.append(i)
                if tcol[coli][1] == "int":
                    positions[tcol[coli][0]] = i

                pos = []
                coli += 1

            col = False
            continue

        if not col:
            pos.append(i - 1)
            if tcol[coli][1] == "str":
                positions[tcol[coli][0]] = i - 1

        col = True

    return dict(positions)


def parse_cols(
    table: list[str],
    column_positions: dict[str, int],
) -> dict[str, str]:
    """Parse and extract the values from the columns in the provided table

    Args
        table: The lines that represent a table
        column_positions: The position of the columns title, identifying where the table start or end

    Returns
        A dict containing the columns, easy format to create a pandas.Dataframe
    """

    cols = defaultdict(list)
    tmp = ""

    for row in table:
        gi = 0
        for i, cl in enumerate(row):
            if cl == " ":
                if tmp != "":
                    cols[tcol[gi][0]].append(tmp)
                    tmp = ""
                    gi += 1
                else:
                    if (
                        gi < len(tcol)
                        and tcol[gi][1] == "int"
                        and i >= column_positions[tcol[gi][0]]
                    ):
                        cols[tcol[gi][0]].append("-")
                        gi += 1

                continue

            tmp += cl

    return dict(cols)


def get_table(lines: list[str]) -> list[str]:
    """Get the table from lines

    Args
        lines: The lines containing the table
    Returns
        The table
    """

    table_start = 0
    table_end = 0

    for i, line in enumerate(lines):
        if line.strip()[:3] == "---":
            table_start = i + 4
            break

    for i, line in enumerate(lines[table_start:]):
        if line[:20] == " " * 20:
            table_end = table_start + i
            break

    return lines[table_start:table_end]


def get_page() -> str:
    """Copy the legacy screen

    Returns
        The legacy screen as string
    """

    with pyt.hold("ctrl"):
        pyt.press("a")
        pyt.press("c")

    return pyperclip.paste()
