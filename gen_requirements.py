import os
import subprocess


def main():
    subprocess.run(
        "python -m pip freeze > requirements.txt".split(" "),
        check=True,
        shell=True,
    )

    with open("requirements.txt", "r", encoding="utf-8") as rf,open("requirements-x86.in", "w", encoding="utf-8") as wf:
        fmt_content = ""

        for line in rf.readlines():
            fmt_content += line.split("==")[0] + "\n"

        wf.write(fmt_content)

    os.remove("requirements.txt")


if __name__ == "__main__":
    main()
