import os
import subprocess


def main():
    with (
        open("requirements.txt", "r") as rf,
        open("requirements-x86.in", "w") as wf,
    ):
        fmt_content = ""

        for line in rf.readlines():
            fmt_content += line.split("==")[0] + "\n"

        wf.write(fmt_content)

    os.remove("requirements.txt")


if __name__ == "__main__":
    main()
