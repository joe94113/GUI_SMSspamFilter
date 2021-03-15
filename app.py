import random
import pandas as pd
import string
import nltk

# DearPyGUI Imports
from dearpygui.core import *
from dearpygui.simple import *

# functions.py Imports
from functions import categorize_words, pre_process, predict

nltk.download('punkt')
nltk.download('stopwords')
pred = []


def check_spam(pred):
    with window("Simple SMS Spam Filter"):
        if not pred:
            add_spacing(count=12)
            add_separator()
            add_spacing(count=12)

            input_value = get_value("Input")
            input_value = pre_process(input_value)
            # 取出預測結果,及顏色
            pred_text, text_color = predict(input_value)

            pred.append(pred_text)
            add_text(pred[-1], color=text_color)
        else:
            # 隱藏原本輸出結果
            hide_item(pred[-1])
            input_value = get_value("Input")
            input_value = pre_process(input_value)
            pred_text, text_color = predict(input_value)

            pred.append(pred_text)
            add_text(pred[-1], color=text_color)

# window object settings
# 設定視窗寬750，高720
set_main_window_size(750, 720)
# 設置字體比例
set_global_font_scale(1.25)
set_theme("Cherry")
set_style_window_padding(30, 30)

# 設定視窗內的app視窗
with window("Simple SMS Spam Filter", width=730, height=677):
    print("GUI is running")
    # 視窗沿X,Y軸為0
    set_window_pos("Simple SMS Spam Filter", 0, 0)

    # logo，放圖片的格子
    add_drawing("logo", width=730, height=290)
    # 增加分隔線
    add_separator()
    # 增加間距
    add_spacing(count=12)

    # 增加文字，instructions指示
    add_text("Please enter an SMS message of your choice to check if it's spam or not", color=[255, 250, 250])
    add_spacing(count=12)

    # collect input
    add_input_text("Input", width=415, default_value="type message here!")
    add_spacing(count=12)
    # 按下按鈕，跑check_spam函式
    add_button("check", callback=lambda x, y: check_spam(pred))

# place the image inside the space
draw_image("logo", "logo_spamFilter.png", (680, 290), (10, 10))

start_dearpygui()
