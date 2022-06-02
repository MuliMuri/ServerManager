import os
os._wrap_close

class CommandBox():
    def __init__(self) -> None:
        pass

    def exec(self, cmd):
        val = os.popen(cmd, 'r', 1)
        a = val.readlines()
        print(a)


if __name__ == "__main__":
    cbx = CommandBox()
    cbx.exec("ipconfig")
