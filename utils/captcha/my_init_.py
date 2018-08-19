# #encoding:utf-8
# import random
# import string
# #导入图形处理需要的库
# #Image : 一个画布
# #ImageDraw :一支画笔
# #ImageFont :画笔的字体
# from PIL import Image,ImageDraw,ImageFont
# #定义一个产生验证码的类
# class Captcha(object):
#     #验证码位数
#     number = 4
#     #验证码图形的宽、高
#     size = (100,30)
#     #字体的大小
#     fontsize = 25
#     #干扰线的条数
#     line_num = 2
#     # 构建一个验证码源文本
#     SOURCE = list(string.ascii_letters)
#     for i in range(10):
#         SOURCE.append(str(i))
#     #产生干扰线的内部方法，画线，起点到终点，再加上线宽
#     @classmethod
#     def __gene_line(cls,draw,width,height):
#         begin = (random.randint(0,width),random.randint(0,height))
#         end = (random.randint(0,width),random.randint(0,height))
#         draw.line([begin,end],fill =cls.__gene_random_color(),width=2)
#     #绘制干扰点
#     @classmethod
#     def __gene_points(cls,draw,point_chance,width,height):
#         chance = min(100,max(0,int(point_chance)))
#         for w in range(width):
#             for h in range(height):
#                 tmp = random.randint(0,100)
#                 if tmp>100-chance:
#                     draw.point((w,h),fill=cls.__gene_random_color())
#     #生成随机的颜色
#     @classmethod
#     def __gene_random_color(cls,start=0,end=255):
#         random.seed()
#         return (random.randint(start,end),random.randint(start,end),random.randint(start,end))
#
#     # 随机选择一个字体
#     @classmethod
#     def __gene_random_font(cls):
#         fonts = [
#             'Courgette-Regular.ttf',
#             'LHANDW.TTF',
#             'Lobster-Regular.ttf',
#             'verdana.ttf'
#         ]
#         font = random.choice(fonts)
#         return 'utils/captcha/'+font
#     #用来随机产生一个字符串（包括英文和数字）
#     @classmethod
#     def gene_text(cls,number):
#         #number是位数
#         return ''.join(random.sample(cls.SOURCE,number))
#     #生成验证码
#     @classmethod
#     def gene_graph_captcha(cls):
#         #验证码的大小
#         width,height = cls.size
#         # 创建图片
#         image = Image.new('RGBA',(width,height),cls.__gene_random_color(0,100))
#         #验证码的字体
#         font = ImageFont.truetype(cls.__gene_random_font(),cls.fontsize)
#         #创建画笔
#         draw = ImageDraw.Draw(image)
#         #生成字符串
#         text = cls.gene_text(cls.number)
#         #获得字体的宽、高
#         font_width,font_height = font.getsize(text)
#         #填充字符串，将字符串填充到画布上
#         draw.text(((width-font_width)/2,(height-font_height)/2),text,font=font,fill=cls.__gene_random_color(150,255))
#         #绘制干扰线
#         for x in range(0,cls.line_num):
#             cls.__gene_line(draw,width,height)
#         #绘制干扰点
#         cls.__gene_points(draw,10,width,height)
#         return (text,image)
