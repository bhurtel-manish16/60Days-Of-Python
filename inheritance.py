class grand:
    def __init__(self) -> None:
        print("In grand init")

    def show_grand(self):
        print("In grand class")

class parent:
    def __init__(self) -> None:
        print("In parent init")

    def show_paent(self):
        print("In parent")

class child( parent,grand,):
    def __init__(self) -> None:
        print("In child init")
        super().__init__()

    def show_child(self):
        print("In child")

c1 = child()

c1.show_child()
c1.show_paent()
c1.show_grand()