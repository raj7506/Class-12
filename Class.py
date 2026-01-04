class myclass:
    __privateVar = 27;
    def __privateMet(self):
        print("I'm inside myClass")
    def hello(self):
        print("Private variable value: ", myclass.__privateVar)
foo = myclass()
foo.hello()
foo.__privateMet