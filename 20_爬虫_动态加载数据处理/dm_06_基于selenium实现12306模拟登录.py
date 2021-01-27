from selenium import webdriver
import time
from PIL import Image

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get("https://kyfw.12306.cn/otn/login/init")

time.sleep(1)

# save_screenshot 就是将当前页面进行截图且保存
bro.save_screenshot("aa.png")

# 确定验证码图片对应的左上角和右下角的坐标（裁定的区域就确定）
code_img_ele = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
location = code_img_ele.location  # 验证码图片左上角坐标x,y

size = code_img_ele.size  # 验证码标签对应的长和宽

# 左上角和右下角坐标
rangle = (
    int(location['x']),
    int(location['y']),
    int(location['x'] + size['width']),
    int(location['y'] + size['height'])
)
# 至此验证码图片区域就确定下来了

i = Image.open('./aa.png')
code_img_name = './code.png'

# crop 根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)

# 将验证码图片提交给超级鹰及逆行识别
