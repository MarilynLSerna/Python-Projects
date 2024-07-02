
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #Label for instructions
        self.label = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.label.grid(row=0, column =0, padx=(10,10), pady=(10,0), columnspan=2)

        #Entry widget for custom text input
        self.custom_text = Entry(self.master, width=75)
        self.custom_text.grid(row=1, column=0, padx=(10, 10), pady=(10,10), columnspan=2)
        
        #Button to generate defualt HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10), pady=(10,10,))

        #Button to generate custom HTML page
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.custom_text.get()
        #Check if the text is not empty
        if htmlText.strip():
            htmlFile = open("index.html", "w")
            htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
            htmlFile.write(htmlContent)
            htmlFile.close()
            webbrowser.open_new_tab("index.html")
        else:
            print("Please enter text")

    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
