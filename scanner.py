from kivy.app import App
from kivy.config import Config
import tkinter as tk
from tkinter import filedialog,messagebox
import sys
from PIL import Image

Config.set('graphics','resizable',False)
Config.set("graphics",'width','600')
Config.set("graphics",'height','600')

class ImageManipulation:

	def thumb(file,width,height):
		x = Image.open(file)
		x.thumbnail((width,height))
		root = tk.Tk()
		root.withdraw()
		x.save(filedialog.asksaveasfilename(initialdir=".",title="Save as",defaultextension=".png"))
		root.destroy()
		

class ResizerApp(App):

	def loadfile(self):
		root = tk.Tk()
		root.withdraw()
		self.file_path = filedialog.askopenfilename()
		#self.file = file_path.split("/")
		root.destroy()

	def resizeimage(self):
		x = int(self.root.ids["width_input"].text)
		y = int(self.root.ids["height_input"].text)
		ImageManipulation.thumb(self.file_path,x,y)

	def closeapp(self):
		return sys.exit()

if __name__ == '__main__':
	ResizerApp().run()