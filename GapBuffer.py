import sys

class GapBuffer():
    buffPosition = (0,0)
    def __init__(self, cap = 100):
        assert cap > 0
        self.start = 0
        self.end = cap
        #data coming from the typed characters
        self.data = [" "] * cap
        self.size = cap
    
    def print(self):
        sys.stdout.write('\r\033[K')
        visible = "".join(self.data[:self.start] + self.data[self.end:])
        sys.stdout.write(visible)
        sys.stdout.write(f'\r\033[{self.start + 1}G')  
        sys.stdout.flush()
   
    #usable for when loading a file and need to create a buffer for it    
    # def create(self, string):
    #     str_len = len(string)
    #     assert str_len <= self.size, "file too big for the buffer"
    #     for i in range(str_len):
    #         self.data[i] = string[i]
    #     self.start = str_len
    #     self.end = self.size
    #     return self.print()

#grap cursor position and then insert a character at the place and then return the new built string
    def insert(self, pos, string):
        self._movegap(pos)
        for c in string:
            if self.start == self.end:
                self._rezise()
            self.data[self.start] = c
            self.start += 1
        return self.print()
        
    def _rezise(self):
        oldsize = self.size
        newmax = oldsize * 2
        new_data = [""] * newmax
        tail_end = oldsize - self.end
        for i in range(self.start):
            new_data[i] = self.data[i]
        new_gap_end =  newmax - tail_end
        for i in range(tail_end):
            new_data[new_gap_end + i] = self.data[self.end + i]
        self.data = new_data
        self.end = new_gap_end
        self.size = newmax
    
    def _movegap(self, pos):
        x = pos
        if len(self.data) <= self.end:
            return
        if x < self.start: 
            while self.start > x:
                self.start -= 1
                self.end -= 1
                # if self.data[self.end] is None:
                #     break
                self.data[self.end] = self.data[self.start]
                self.data[self.start] = ""
        elif x > self.start:
            while self.start < x:
                # if self.data[self.end] is None:
                #     break
                self.data[self.start] = self.data[self.end]
                self.data[self.end] = ""
                self.start += 1
                self.end += 1

    def backspace(self, pos):
        self._movegap(pos)
        if self.start > 0:
            self.start -= 1
            self.data[self.start] = ""
        return self.print()

