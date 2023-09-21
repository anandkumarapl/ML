class Subject:
    def __init__(self, name=None, maxmarks=None, passmarks=None, obtainedmarks=None) -> None:
        if name is None:
            self.name = (input("name"))
        else:
            self.name = name
        if maxmarks is None:
            self.maxmarks = int(input("maxmarks"))
        else:
            self.maxmarks = maxmarks

        if passmarks is None:
            self.passmarks = int(input("passmarks"))
        else:
            self.passmarks = passmarks

        if obtainedmarks is None:
            self.obtainedmarks = int(input("obtainedmarks"))
        else:
            self.obtainedmarks = obtainedmarks
    def __str__(self) -> str:
        return "name={0},maxmarks={1},passmarks{2}, obtainedmarks={3}".format(self.name,self.maxmarks,self.passmarks,self.obtainedmarks)
