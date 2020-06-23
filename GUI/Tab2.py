# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk

from PIL import ImageTk,Image
class Tab2():
    def __init__(self,tab):
        self._createWidget(tab)

        
    def _createWidget(self,tab):
        self.zhuo = tk.Frame(tab,bg='red')
        self.zhuo.grid(column=0,row=0)
        self.canvas = tk.Canvas(self.zhuo,width=500,height=600)
        self.createImage()
        self.image = ImageTk.PhotoImage(self.pil_image)    #这里就不是 tk.PhotoImage 了
        self.canvas.create_image(20,20,anchor='nw',image=self.image)    #打开图像
        self.canvas.grid(row=0,column=0,columnspan=2)
        
    def _resize(self,w, h, w_box, h_box, pil_image):  
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])  
        width = int(w*factor)  
        height = int(h*factor)  
        self.pil_image = pil_image.resize((width, height), Image.ANTIALIAS) 

    
    def createImage(self):        
        pil_image = Image.open(r'../test.jpg')    #记得在缩放图像之前，要用 Image 模块打开。
        w, h = pil_image.size
        w_box = 800   #大伙可以调节这个，来设置图片的大小。当然，也建议读者们把他设为 公有的。
        h_box = 1200
        self._resize(w,h,w_box,h_box,pil_image)