import datetime
import os
import time
from tkinter.filedialog import askdirectory
import pyautogui as pyt
import pandas as pd
from parser import columns_position, get_page, get_table, parse_cols
from constants import column_line_position


def main():
    df = None

    out_dir = askdirectory(mustexist=True, title="Local para salvar o relatório")
    strdate = datetime.datetime.now().strftime("%d-%m-%Y")

    time.sleep(2)

    for _ in range(20):
        page = get_page()

        lines = page.split("\n")
        lines = [" " + l.replace("\r", "") + " " for l in lines]

        table = get_table(lines)

        column_line = lines[column_line_position]

        positions = columns_position(column_line)
        columns = parse_cols(table, positions)

        ph_df = pd.DataFrame(columns)
        if df is None:
            df = ph_df
        else:
            df = pd.concat([df, ph_df], ignore_index=True)

        pyt.press("f8")
        time.sleep(0.2)

    df = df.drop("Usuário", axis=1)
    df.to_excel(os.path.join(out_dir, f"relatorio_{strdate}.xlsx"), index=False)


if __name__ == "__main__":
    main()
