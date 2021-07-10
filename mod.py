def foo():
    return "Welcome to foo()..."

def bar():
    return "Welcom to bar()..."

class Animal:
    def __init__(self, breed):
        self.breed = breed
    
    def speak(self):
        return "woof!"


if __name__ == '__main__':
    print(foo())
    print(bar())
    d = Animal("dog")
    print(d.speak())
    