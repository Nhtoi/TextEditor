class GapBuffer():
    buffPosition = (0,0)
    def __init__(self, cap = 16):
        assert cap > 0
        self.start = 0
        self.end = cap
        #data coming from the typed characters
        self.data = [" "] * cap
        self.size = cap
    
    def print(self):
        print("".join(self.data))

    def create(self, string):
        str_len = len(string)
        assert str_len <= self.size, "String too big for the buffer"
        
        for i in range(str_len):
            self.data[i] = string[i]

        self.start = str_len
        self.end = self.size

#grap cursor position and then insert a character at the place and then return the new built string
    def insert(self, pos, character):
        pass
    # def _rezise(self):
    #     pass
    # def delete():
    #     pass
            
string = "insert the pointer at the end of the word pointer" 
buffer = GapBuffer(cap=len(string) + 16)
buffer.create(string)
buffer.print()
print(buffer.insert((0,17), "inserting a new sentence in the middle"))
buffer.print()