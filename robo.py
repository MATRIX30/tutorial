class Robot:
    """Represens a robot with a name."""
    #The constructor
    def __init__(self, name, model):
        self.__name= name # A tribute
        self.model= model 
    #Method
    def introduce(self):
        print(f"I am{self.__name}.")
    
gemini= Robot("Gemini","2025A0")
print(gemini.__name)
print(gemini.model)
gemini.introduce()
