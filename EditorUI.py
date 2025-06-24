#WORK IN PROGRESS
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure((0,2), weight=1)
                    
        self.button1 = customtkinter.CTkButton(self, text="Open", command=self.startTyping)
        self.button1.grid(row=0, column=0, padx=20, pady=20)
        
        self.button2 = customtkinter.CTkButton(self, text="Quit", command=self.quitApp)
        self.button2.grid(row=1, column=0, padx=40, pady=20)

    def startTyping(self):
        print("Start Typing")
       

    def quitApp(self):
        print("Exiting the text editor")
        return self.destroy()

app = App()
app.mainloop()