from datetime import datetime
from flask import render_template, request,Flask
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import pkuseg
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread


with open('E:\竞赛数据集\设计大赛\Python评论.txt', encoding='utf-8') as f:
    file = f.read()
    seg = pkuseg.pkuseg()
    text = seg.cut(file)
    text = str(text)
@app.route('/', methods=['POST'])
def upload():
    bg_pic = imread('E:\竞赛数据集\设计大赛\R-C.jpg')
    wordcloud = WordCloud(mask=bg_pic,background_color='white',font_path='E:\竞赛数据集\设计大赛\华文楷体.ttf',scale=1.5).generate(text)
    '''参数说明：
    mask:设置背景图片   background_color:设置背景颜色
    scale:按照比例进行放大画布，此处指长和宽都是原来画布的1.5倍
    generate(text)：根据文本生成词云 '''

    plt.imshow(wordcloud)
    #显示图片时不显示坐标尺寸
    plt.axis('off')
    #显示词云图片
    plt.show()
