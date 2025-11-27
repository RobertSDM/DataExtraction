import pandas as pd
import os
from pages import pages
from parser import columns_position, get_table, parse_cols
from constants import column_line_position


def test_multi_table_concat():
    df = None

    for page in pages:
        lines = page.split("\n")

        table = get_table(lines)
        if table[0][-1] == "\r":
            table = [l[:-1] for l in table]

        positions = columns_position(lines[column_line_position])
        columns = parse_cols(table, positions)

        ph_df = pd.DataFrame(columns)

        if df is None:
            df = ph_df
        else:
            df = pd.concat([df, ph_df], ignore_index=True)

    assert not df.empty
