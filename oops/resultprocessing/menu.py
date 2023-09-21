class menu:
    def __init__(self,add,exit,search) -> None:
        self.add=add
        self.exit=exit
        self.search=search
    def __str__(self) -> str:
        return "Add={0},Exit={1},Search={2}".format(self.add,self.exit,self.search)