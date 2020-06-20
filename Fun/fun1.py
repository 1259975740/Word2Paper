# coding: utf-8
from PIL import Image, ImageFont
import numpy as np
from handright import Template, handwrite
from multiprocessing import Pool
import time
from Fun.fun2 import *
from tkinter import messagebox as mBox

def trans(input_path,output_path,font_path,line_spacing,font_size,
          fill,left_margin,top_margin,right_margin,bottom_margin,word_spacing,
          disturb_x_sigma,disturb_y_sigma,disturb_theta_sigma,
          line_spacing_sigma,font_size_sigma,word_spacing_sigma,background,if_test=False):
    
    background=Image.open(background)
    width, height = background.size
    background = background.resize((np.int(3*width),np.int(2.5*height)),resample=Image.LANCZOS)
    if not if_test:
        text = read_docx(input_path)
    else:
        text = """
    卿寻鲤影剔浮英， 
    我恨浮英掩玉卿。
     难教芳心知我心， 
     孤烛半影又天明。
    """
    time_start = time.time()
    template = Template(
        background=background,
        font_size=font_size,
        font=ImageFont.truetype(font_path),
        line_spacing=line_spacing,
        fill=fill,  # ���塰��ɫ��
        left_margin=left_margin,
        top_margin=-top_margin,
        right_margin=right_margin,
        bottom_margin=bottom_margin,
        word_spacing=word_spacing,
        line_spacing_sigma=line_spacing_sigma,  # �м������Ŷ�
        font_size_sigma=font_size_sigma,  # �����С����Ŷ�
        word_spacing_sigma=word_spacing_sigma,  # �ּ������Ŷ�
        end_chars="，。;、“”",  # ��ֹ�ض��ַ����Ű��㷨���Զ����ж�����������
        perturb_x_sigma=disturb_x_sigma,  # �ʻ�����ƫ������Ŷ�
        perturb_y_sigma=disturb_y_sigma,  # �ʻ�����ƫ������Ŷ�
        perturb_theta_sigma=disturb_theta_sigma,  # �ʻ���תƫ������Ŷ�
    )
    images = handwrite(text, template)
    for i, im in enumerate(images):
        assert isinstance(im, Image.Image)
        if not if_test:
            im.save(output_path+"\{}.jpg".format(i))
        else:
            im.save(r"../test.jpg")
    time_end = time.time()
    print(time_end-time_start)
    mBox.showinfo('提示', '运行完毕')

