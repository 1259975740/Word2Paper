# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import Menu
from sys import exit
from threading import Thread
from time import sleep
from queue import Queue
import os
from os import path
from tkinter import filedialog as fd
from Tab2 import Tab2
import sys
sys.path.append('../')
from PIL import Image, ImageFont
import numpy as np
from handright import Template, handwrite
from multiprocessing import Pool
import time
from Fun.fun1 import *
from PIL import ImageTk,Image

class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.resizable(0,0)    #这个是设置窗口不可缩放
        self.win.title('妙笔生花')
        self.win.iconbitmap(r'./app.ico')
        self._createWidget()

    def _runTrans(self,input_path,output_path,font_path,line_spacing,font_size,
                  fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
                  disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
                  line_spacing_sigma,font_size_sigma,word_spacing_sigma,background): 
        trans(input_path,output_path,font_path,line_spacing,font_size,
            fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
            disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
            line_spacing_sigma,font_size_sigma,word_spacing_sigma,background)
        
    def _testTrans(self,input_path,output_path,font_path,line_spacing,font_size,
                  fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
                  disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
                  line_spacing_sigma,font_size_sigma,word_spacing_sigma,background): 
        trans(input_path,output_path,font_path,line_spacing,font_size,
            fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
            disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
            line_spacing_sigma,font_size_sigma,word_spacing_sigma,background,if_test=True)
        self.tab2Widget.createImage()
        self.tab2Widget._image = ImageTk.PhotoImage(self.tab2Widget.pil_image)
        self.tab2Widget.canvas.create_image(20,20,anchor='nw',image=self.tab2Widget._image)
        
    def createRunThread(self):
        input_path = str(self.inEntry.get())
        output_path = str(self.outEntry.get())
        font_path = str(self.fntEntry.get())  
        line_spacing = float(str(self.lineSpcEty.get())) 
        font_size = float(str(self.fntSizeCom.get()))
        left_margin = float(str(self.leftMar.get()))
        right_margin = float(str(self.rightMar.get()))
        top_margin = float(str(self.topMar.get()))
        bottom_margin = float(str(self.bottomMar.get()))
        word_spacing = float(str(self.wrdDistEry.get()))
        line_spacing_sigma = float(str(self.lineSpcSigEry.get()))
        font_size_sigma = float(str(self.fntSizeSigEry.get()))
        word_spacing_sigma = float(str(self.wrdSigEry.get()))
        disturb_x_sigma = float(str(self.xSigEry.get()))
        disturb_y_sigma = float(str(self.ySigEry.get()))
        disturb_theta_sigma = float(str(self.thetaSigEry.get()))
        fill = int(float(str(self.fntColCom.get())))
        background = str(self.bGEntry.get())
        run = Thread(target=self._runTrans,args=(input_path,output_path,font_path,line_spacing,font_size,
                                                 fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
                                                 disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
                                                 line_spacing_sigma,font_size_sigma,word_spacing_sigma,background))    #创建一个线程，线程运行 methodInAThread
        run.setDaemon(True)    #将线程设置成守护线程
        run.start()
        
    def createTestThread(self):
        input_path = str(self.inEntry.get())
        output_path = str(self.outEntry.get())
        font_path = str(self.fntEntry.get())  
        line_spacing = float(str(self.lineSpcEty.get())) 
        font_size = float(str(self.fntSizeCom.get()))
        left_margin = float(str(self.leftMar.get()))
        right_margin = float(str(self.rightMar.get()))
        top_margin = float(str(self.topMar.get()))
        bottom_margin = float(str(self.bottomMar.get()))
        word_spacing = float(str(self.wrdDistEry.get()))
        line_spacing_sigma = float(str(self.lineSpcSigEry.get()))
        font_size_sigma = float(str(self.fntSizeSigEry.get()))
        word_spacing_sigma = float(str(self.wrdSigEry.get()))
        disturb_x_sigma = float(str(self.xSigEry.get()))
        disturb_y_sigma = float(str(self.ySigEry.get()))
        disturb_theta_sigma = float(str(self.thetaSigEry.get()))
        fill = int(str(self.fntColCom.get()))
        background = str(self.bGEntry.get())
        test = Thread(target=self._testTrans,args=(input_path,output_path,font_path,line_spacing,font_size,
                                                 fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
                                                 disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
                                                 line_spacing_sigma,font_size_sigma,word_spacing_sigma,background))  
        test.setDaemon(True)
        test.start()
        
    def _clickRunBut(self):
        self.createRunThread()
    
    def _clickTstBut(self):
        self.createTestThread()
         
    
    def _getFileName(self):
        fDir = os.path.join( os.path.dirname(__file__),'../Input')  #���ϼ��ļ�Ŀ¼��
        fName = fd.askopenfilename(parent=self.inOuFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.inEntry.delete(0,tk.END)   
        self.inEntry.insert(0,fName)   
    
    def _getFileName2(self):
        fDir = os.path.join( os.path.dirname(__file__),'../Output')  #���ϼ��ļ�Ŀ¼��
        fName = fd.askdirectory(parent=self.inOuFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.outEntry.delete(0,tk.END)   
        self.outEntry.insert(0,fName)   
    
    def _getFileName3(self):
        fDir = os.path.join( os.path.dirname(__file__),'../Font')  #���ϼ��ļ�Ŀ¼��
        fName = fd.askopenfilename(parent=self.inOuFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.fntEntry.delete(0,tk.END)   
        self.fntEntry.insert(0,fName) 
        
    def _getFileName4(self):
        fDir = os.path.join( os.path.dirname(__file__),'../Background')  #���ϼ��ļ�Ŀ¼��
        fName = fd.askopenfilename(parent=self.inOuFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.bGEntry.delete(0,tk.END)   
        self.bGEntry.insert(0,fName)     
    

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
            
    def _createWidget(self):
        self.menuBar = Menu(self.win)
        self.win.configure(menu=self.menuBar)

        self.startMenu = Menu(self.menuBar,tearoff=0)
        self.startMenu.add_command(label='保存为')
        self.startMenu.add_separator()
        self.startMenu.add_command(label='退出',command=self._quit)
        self.menuBar.add_cascade(label='开始',menu=self.startMenu)
        
        self.helpMenu = Menu(self.menuBar,tearoff=0)
        self.helpMenu.add_command(label='帮助')
        self.helpMenu.add_command(label='关于')
        self.menuBar.add_cascade(label='其他',menu=self.helpMenu)
        
        
        self.tabControl = ttk.Notebook(self.win)
        self.tab1 = ttk.LabelFrame(self.tabControl)
        self.tab2 = ttk.LabelFrame(self.tabControl)
        self.tabControl.add(self.tab1,text='参数设置')
        self.tabControl.add(self.tab2,text='效果预览')
        self.tabControl.pack(fill='both',expand=1)
        
        self.zhuo = ttk.Frame(self.tab1)
        self.zhuo.grid(column=0,row=0)
        
        self.inOuFrm = ttk.LabelFrame(self.zhuo,text='文件管理')
        self.inOuFrm.grid(column=0,row=0,sticky='W')
        
        self.inBut = ttk.Button(self.inOuFrm,text='输入文件',
                               command=self._getFileName)
        self.inBut.grid(column=0,row=0)
        self.fDir = os.path.abspath(os.path.join( os.path.dirname(__file__),".."))

        self.default_value = tk.StringVar()
        self.default_value.set(self.fDir+'\Input\demo.docx')
        
        self.default_value2 = tk.StringVar()
        self.default_value2.set(self.fDir+'\Output')
        
        self.default_value3 = tk.StringVar()
        self.default_value3.set(self.fDir+'\Font\瘦金简体.ttf')
        
        self.default_value5 = tk.StringVar()
        self.default_value5.set(self.fDir+r'\Background\background_01.jpg')
        
        self.inEntry = ttk.Entry(self.inOuFrm,width=60,textvariable=self.default_value)
        self.inEntry.grid(column=1,row=0)
        self.inEntry.focus()

        self.outBut = ttk.Button(self.inOuFrm,text='输出文件夹',
                               command=self._getFileName2)
        self.outBut.grid(column=0,row=1)
        self.outEntry = ttk.Entry(self.inOuFrm,width=60,textvariable=self.default_value2)
        self.outEntry.grid(column=1,row=1)
        
        self.fntBut = ttk.Button(self.inOuFrm,text='搜索字体',command=self._getFileName3)
        self.fntBut.grid(column=0,row=2)
        self.fntEntry = ttk.Entry(self.inOuFrm,width=60,textvariable=self.default_value3)
        self.fntEntry.grid(column=1,row=2)

        self.backGndBut = ttk.Button(self.inOuFrm,text='搜索背景',command=self._getFileName4)
        self.backGndBut.grid(column=0,row=3)
        self.bGEntry = ttk.Entry(self.inOuFrm,width=60,textvariable=self.default_value5)
        self.bGEntry.grid(column=1,row=3)
        
        for child in self.inOuFrm.winfo_children():
            child.grid_configure(padx=10,pady=10,sticky='W')
        
        self.miniCon = tk.Frame(self.zhuo)
        self.miniCon.grid(column=0,row=3,sticky='W')
        ttk.Label(self.miniCon,text='字体大小').grid(column=0,row=0)
#        self.fntSizeCom = ttk.Combobox(self.miniCon)
#        self.fntSizeCom['value']=(80,90,100)
        self._fntSize = tk.StringVar()
        self._fntSize.set(100)
        self.fntSizeCom = ttk.Entry(self.miniCon,textvariable=self._fntSize)
        self.fntSizeCom.grid(column=1,row=0,sticky='W')
#        self.fntSizeCom.current(2)
        
        ttk.Label(self.miniCon,text='字体颜色').grid(column=2,row=0)
#        self._fntCol = tk.StringVar()
 #       self._fntCol.set(0)
        self.fntColCom = ttk.Combobox(self.miniCon,state='readonly')
  #      self.fntColCom.grid(column=3,row=0,sticky='W')
        self.fntColCom['value']=(0,255,666)
        self.fntColCom.grid(column=3,row=0,sticky='W')
        self.fntColCom.current(0)
 
 
        ttk.Label(self.miniCon,text='行间距').grid(column=0,row=1)
        self.default_value4 = tk.StringVar()
        self.default_value4.set(150)
        self.lineSpcEty = ttk.Entry(self.miniCon,textvariable=self.default_value4)
        self.lineSpcEty.grid(column=1,row=1)   
        ttk.Label(self.miniCon,text='字距').grid(column=2,row=1)
        self._linespc = tk.StringVar()
        self._linespc.set(15)
        self.wrdDistEry = ttk.Entry(self.miniCon,textvariable=self._linespc)
        self.wrdDistEry.grid(column=3,row=1) 
        
        self.plcFrm = ttk.Labelframe(self.zhuo,text='字体位置')
        self.plcFrm.grid(column=0,row=1,sticky='W')
        ttk.Label(self.plcFrm,text='左间隔').grid(column=0,row=0)
        self._left = tk.StringVar()
        self._left.set(250)
        self.leftMar = ttk.Entry(self.plcFrm,textvariable=self._left)
        self.leftMar.grid(column=1,row=0)
        
        ttk.Label(self.plcFrm,text='右间隔').grid(column=2,row=0)
        self._right = tk.StringVar()
        self._right.set(100)
        self.rightMar = ttk.Entry(self.plcFrm,textvariable=self._right)
        self.rightMar.grid(column=3,row=0)
        
        ttk.Label(self.plcFrm,text='上间隔').grid(column=0,row=1)
        self._top = tk.StringVar()
        self._top.set(30)
        self.topMar = ttk.Entry(self.plcFrm,textvariable=self._top)
        self.topMar.grid(column=1,row=1)        
        
        ttk.Label(self.plcFrm,text='下间隔').grid(column=2,row=1)
        self._bottom = tk.StringVar()
        self._bottom.set(100)
        self.bottomMar = ttk.Entry(self.plcFrm,textvariable=self._bottom)
        self.bottomMar.grid(column=3,row=1)    
        
        for child in self.plcFrm.winfo_children():
            child.grid_configure(padx=10,pady=10,sticky='W')
        
        self.dtbFrm = ttk.Labelframe(self.zhuo,text='扰动设置')
        self.dtbFrm.grid(column=0,row=2,sticky='W')
        ttk.Label(self.dtbFrm,text='行距扰动').grid(column=0,row=0)
        self._lineSpcSig = tk.StringVar()
        self._lineSpcSig.set(6)
        self.lineSpcSigEry = ttk.Entry(self.dtbFrm,textvariable=self._lineSpcSig)
        self.lineSpcSigEry.grid(column=1,row=0)  
       
        ttk.Label(self.dtbFrm,text='字体大小扰动').grid(column=2,row=0)
        self._fntSizeSig = tk.StringVar()
        self._fntSizeSig.set(1)
        self.fntSizeSigEry = ttk.Entry(self.dtbFrm,textvariable=self._fntSizeSig)
        self.fntSizeSigEry.grid(column=3,row=0)  
        
        ttk.Label(self.dtbFrm,text='字距扰动').grid(column=0,row=1)
        self._wrdSpcSig = tk.StringVar()
        self._wrdSpcSig.set(3)
        self.wrdSigEry = ttk.Entry(self.dtbFrm,textvariable=self._wrdSpcSig)
        self.wrdSigEry.grid(column=1,row=1)  
        
        ttk.Label(self.dtbFrm,text='字体旋转扰动').grid(column=2,row=1)
        self._thetaSig = tk.StringVar()
        self._thetaSig.set(0.03)
        self.thetaSigEry = ttk.Entry(self.dtbFrm,textvariable=self._thetaSig)
        self.thetaSigEry.grid(column=3,row=1) 
        
        ttk.Label(self.dtbFrm,text='笔画横线扰动').grid(column=0,row=2)
        self._xySig = tk.StringVar()
        self._xySig.set(3)
        self.xSigEry = ttk.Entry(self.dtbFrm,textvariable=self._xySig)
        self.xSigEry.grid(column=1,row=2)         

        ttk.Label(self.dtbFrm,text='笔画纵线扰动').grid(column=2,row=2)
        self.ySigEry = ttk.Entry(self.dtbFrm,textvariable=self._xySig)
        self.ySigEry.grid(column=3,row=2)     
        
        for child in self.dtbFrm.winfo_children():
            child.grid_configure(padx=10,pady=10,sticky='W')
        
        self.runBut = ttk.Button(self.miniCon,text='转换',command=self._clickRunBut)
        self.runBut.grid(column=0,row=2)
        
        self.testBut = ttk.Button(self.miniCon,text='测试',command=self._clickTstBut)
        self.testBut.grid(column=1,row=2)
        
        for child in self.miniCon.winfo_children():
            child.grid_configure(padx=10,pady=10,sticky='W')        
          
        

        """页面2开发"""
        self.tab2Widget = Tab2(self.tab2)
 
oop = OOP()
oop.win.mainloop()