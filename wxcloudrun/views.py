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
import  os

    
@app.route('/upload', methods=['POST'])
def upload():
#     all_files = [f for f in os.listdir('/app/wxcloudrun')]
#     return str(all_files) #获取当前工作目录路径
    file = request.form.get('allcomment')
    seg = pkuseg.pkuseg()
    text = seg.cut(file)
    text = str(text)
    return "ok"
    bg_pic = imread('/app/wxcloudrun/R-C.jpg')
    wordcloud = WordCloud(mask=bg_pic,background_color='white',font_path='/app/wxcloudrun/华文楷体.ttf',scale=1.5).generate(text)
    '''参数说明：
    mask:设置背景图片   background_color:设置背景颜色
    scale:按照比例进行放大画布，此处指长和宽都是原来画布的1.5倍
    generate(text)：根据文本生成词云 '''
    
    wordcloud.to_file('/app/wxcloudrun/ciyun.jpg')
    
