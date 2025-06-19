import io

class Operations():
    def __init__(self):
        self.path = None
        self.text = None
        self.encoding = None
    
    def save(self):
        with open(self.path, 'w') as file:
            file.write(self.text)
            file.close()
    
    #create and load a gapbuffer
    def open(self):
        encoding = io.text_encoding(self.encoding)
        with open(self.path, mode='r+', encoding=encoding) as f:
            return f.read()
        

