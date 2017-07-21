# appium原理：1.server and andriod connection，
from appium import webdriver
import time
import re
import requests
import json
import subprocess
# using images model
import os
import platform
import tempfile
import shutil
from PIL import Image
# using images model
import pytesseract

import multiprocessing

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# get user tempfile
PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")
# get user tempfile


#images_to_string
def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'rt', encoding='utf-8') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text
    #print(image_to_string('/Users/VANXV/Downloads/pyocr.png', False, '-l chi_sim'))

#DiffImg coding
class Appium_Extend(object):
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot_by_element(self, element):
        # 先截取整个屏幕，存储至系统临时目录下
        self.driver.get_screenshot_as_file(TEMP_FILE)

        # 获取元素bounds
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

        # 截取图片
        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(TEMP_FILE)

        return self

    def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):
        # 自定义截取范围
        self.driver.get_screenshot_as_file(TEMP_FILE)
        box = (start_x, start_y, end_x, end_y)

        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(TEMP_FILE)

        return self

    def write_to_file(self, dirPath, imageName, form="png"):
        # 将截屏文件复制到指定目录下
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))

    def load_image(self, image_path):
        # 加载目标图片供对比用
        if os.path.isfile(image_path):
            load = Image.open(image_path)
            return load
        else:
            raise Exception("%s is not exist" % image_path)

            # http://testerhome.com/topics/202

    def same_as(self, load_image, percent):
        # 对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
        import math
        import operator

        image1 = Image.open(TEMP_FILE)
        image2 = load_image

        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, \
                                                         histogram1, histogram2))) / len(histogram1))
        if differ <= percent:
            return True
        else:
            return False

class getimages():
    def get_screenshot_by_element(self, element):
        # 先截取整个屏幕，存储至系统临时目录下
        self.driver.get_screenshot_as_file(TEMP_FILE)

        # 获取元素bounds
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

        # 截取图片
        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(TEMP_FILE)
        newImage.save("//Users/VANXV/Downloads/new.png")
        image1 = Image.open(TEMP_FILE)
        text = image_to_string(TEMP_FILE, False, '-l chi_sim')
        return text

        return self

    def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):
        # 自定义截取范围
        self.driver.get_screenshot_as_file(TEMP_FILE)
        box = (start_x, start_y, end_x, end_y)

        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(TEMP_FILE)
        return self

    def images_to_string(self, image):
        image = Image.open(TEMP_FILE)

    def write_to_file(self, dirPath, imageName, form="png"):
        # 将截屏文件复制到指定目录下
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))

    def load_image(self, image_path):
        # 加载目标图片供对比用
        if os.path.isfile(image_path):
            load = Image.open(image_path)
            return load
        else:
            raise Exception("%s is not exist" % image_path)
    # DiffImg coding

#using reference
class QQaction():
    def connect(self):
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabWidget[1]/android.widget.FrameLayout[1]').click()
        self.driver.implicitly_wait(15)

    def freindConcentGetQQnumber(self):
        self.driver.implicitly_wait(5)
        try:
            self.driver.implicitly_wait(2)
            try:
                getQQnumber = self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
            except:
                getQQnumber = self.driver.find_element_by_xpath('//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]/android.widget.TextView[2]')
            self.driver.implicitly_wait(5)
            objectid = re.findall(r'(\d+)', getQQnumber.text)
            return objectid[len(objectid)-1]
        except:
            swipe.qqswipe(self)
            self.driver.implicitly_wait(5)
            try:
                getQQnumber = self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView')
            except:
                getQQnumber = self.driver.find_element_by_xpath('//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]/android.widget.TextView[2]')
            self.driver.implicitly_wait(2)
            objectid = re.findall(r'(\d+)', getQQnumber.text)
            return objectid[len(objectid)-1]

    def friendConcentSendMessage(self):
        self.driver.implicitly_wait(15)
        try:
            self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[1]').click()
        except:
            self.driver.find_element_by_xpath('//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.Button[1]').click()
        self.driver.implicitly_wait(15)
        print('start send message')
        # input connect
        # self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').send_keys(self.mark['content'])
        # self.driver.implicitly_wait(15)
        # send_message
        # self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
        # self.driver.implicitly_wait(15)
        # RETURN
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        self.driver.implicitly_wait(15)

class swipe():
    def qqswipe(self):
        for i in range(1):
            print('好友滚动', i + 1)
            self.driver.swipe(start_x=400, start_y=450, end_x=500, end_y=100, duration=500)
            self.driver.implicitly_wait(15)
    def qqnumberswipe(self):
        for i in range(1):
            print('列表滑动', i + 1)
            self.driver.swipe(start_x=400, start_y=270, end_x=500, end_y=100, duration=500)
            self.driver.implicitly_wait(15)
class multipleLoop(multiprocessing.Process):
    def __init__(self, mobile_id_for):
        multiprocessing.Process.__init__(self)
        self.mobile_id_for = mobile_id_for

    def run(self):
        print(self.mobile_id_for)
        time.sleep(self.mobile_id_for)
        whilen =1
        while whilen == 1:
            response = requests.post('http://127.0.0.1:8000/auto/task/' + str(self.mobile_id_for) + '/')
            data = response.json()
            self.mark = {}
            for x, y in data.items():
                # x = x.encode('utf-8')
                # try:
                #     y = y.encode('utf-8')
                self.mark[x] = y
            # data中 1.APP名，2.Activety名， 3任务信息
            print(data)
            desired_caps = {
                'platformName': 'Android',
                'deviceName': self.mark['deviceName'],
                'platformVersion': self.mark['platformVersion'],
                'appPackage': self.mark['appPackage'],
                'appActivity': self.mark['appActivity'],
                #'udid': self.mark['udid'],
                #'exported': "True",
                'unicodeKeyboard': "True",
                'resetKeyboard': "True",
            }

            self.driver = webdriver.Remote(self.mark['webserverurl'], desired_caps)

            mobiletask_taskSort_choices = (
            (1, 'add_User'),
            (2, 'ADD_GROUP'),
            (3, 'send_message_to_friend_list'),
            (4, 'send_message_to_GROUP_list'),
            (5, 'send_message_to_user_Accoutid'),
            (6, 'send_message_to_GROUP_Accoutid'),
            (7, 'Get_Pople_list'),
            (8, 'Get_Group_list'),
            (9, 'Get_Group_People_list'),
            )
            #---- loop select_work----#
            if self.mark['taskSort'] == 1:
                multipleLoop.QQaddPeople(self)
            elif self.mark['taskSort'] == 2:
                multipleLoop.QQaddGroup(self)
            elif self.mark['taskSort'] == 3:
                multipleLoop.send_message_to_friend_list(self)

            # ---- loop select_work----#
    #Need add_QQ_list
    def QQaddPeople(self):
        try:
            time.sleep(7)
            print('click')
            QQaction.connect(self)
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]").send_keys(self.mark['AccountId'])
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]").click()
            #self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]").click()
            time.sleep(7)
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]").clear()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]").send_keys(self.mark['content'])
            time.sleep(5)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]").click()
            time.sleep(2)
            print('end')
        except:
            pass
        print('click')
    #Need add_Group_list
    def QQaddGroup(self):
        try:
            self.driver.implicitly_wait(15)
            print('click')
            #click friend
            self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabWidget[1]/android.widget.FrameLayout[1]').click()
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]").click()
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]").send_keys(self.mark['AccountId'])
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]").click()
            time.sleep(5)
            #self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]").click()
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").clear()
            #self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys(self.mark['content'])
            #self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]").send_keys(self.mark['content'])
            time.sleep(5)
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[3]/android.widget.TextView[1]").click()
            print('click')
        except:
            pass
    #Need Send_message_Need_time
    def send_message_to_friend_list(self):

        self.driver.implicitly_wait(15)
        #click contact
        QQaction.connect(self)
        #click friendlist
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        #GO_TOP
        for i in range(3):
            self.driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=1000)
            self.driver.implicitly_wait(15)
        #get_elementlist
        elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
        #open_sendlist
        self.driver.implicitly_wait(15)
        if elementsList[2].tag_name == 'android.widget.RelativeLayout':
            elementsList[1].click()

        self.driver.implicitly_wait(15)
        objectnumber = 0
        AllNumber = 0
        objectName = ''
        objectid = 0 #accuont
        objectEnd = 0
        severQQ = 0

        #get_log
        severQQ = str(requests.get('http://127.0.0.1:8000/auto/tasklog/' + str(self.mark['mobileID']) + '/' + str(self.mark['taskid']) + '/').text)
        response0 = str(0)
        if severQQ == response0:
            tempElement = elementsList[2].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
            tempElement.click()
            self.driver.implicitly_wait(15)
            objectid = QQaction.freindConcentGetQQnumber(self)

            QQaction.friendConcentSendMessage(self)
            responsetext ='http://127.0.0.1:8000/auto/tasklogdone/' + str(self.mark['mobileID']) + '/' + str(self.mark['taskid']) + '/' + str(objectid) + '/'
            response = requests.post(responsetext)
            # click contact
            self.driver.implicitly_wait(15)

        print(severQQ)
        while (objectEnd != 1):
            selectTrue = 0
            elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
            self.driver.implicitly_wait(15)
            for N in range(1, elementsList.__len__()-1):
                if N < 2:
                    continue
                print('N:' + str(N) + 'LIST:' + str(elementsList.__len__()))
                if N == (elementsList.__len__()-2):
                    # rollin
                    print('in rollin list from 379')
                    swipe.qqnumberswipe(self)
                    selectTrue = 0
                    try:
                        self.driver.implicitly_wait(15)
                        if elementsList[elementsList.__len__()-1].tag_name == 'android.widget.LinearLayout':
                            #tempElement = elementsList[elementsList.__len__()-1].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
                            #self.driver.implicitly_wait(15)
                            #tempElement.click
                            #self.driver.implicitly_wait(15)
                            print('382')
                            #GetQQnumbertry = QQaction.freindConcentGetQQnumber(self)
                            #if GetQQnumbertry == objectid:
                            break
                        break
                    except:
                        break
                if elementsList[N].tag_name == 'android.widget.LinearLayout':
                    self.driver.implicitly_wait(15)
                    tempElement = elementsList[N].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
                    self.driver.implicitly_wait(15)
                    tempElement.click()
                    self.driver.implicitly_wait(15)
                    print('394')
                    objectid = QQaction.freindConcentGetQQnumber(self)
                    #objectid = re.findall(r'(\d+)', self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').text)[0]
                    #self.driver.implicitly_wait(15)
                    # RETURN
                    time.sleep(1)
                    try:
                        self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView').click()
                    except:
                        self.driver.find_element_by_xpath('//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()
                    print('return')
                    self.driver.implicitly_wait(15)
                    print('objectid:' + str(objectid))
                    if selectTrue == 0:
                        if severQQ == objectid:
                            selectTrue = 1
                            continue
                        # rolling
                        else:
                            continue

                    else:
                        self.driver.implicitly_wait(15)
                        tempElement = elementsList[N].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
                        tempElement.click()
                        self.driver.implicitly_wait(15)
                        # rolling
                        swipe.qqswipe(self)
                        objectid = re.findall(r'(\d+)', self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').text)[0]
                        self.driver.implicitly_wait(15)
                        print('test last firend')
                        QQaction.friendConcentSendMessage(self)
                        QQaction.connect(self)
                        responsetext = 'http://127.0.0.1:8000/auto/tasklogdone/' + str(self.mark['mobileID']) + '/' + str(self.mark['taskid']) + '/' + str(objectid) + '/'
                        response = requests.post(responsetext)
                        elementsListadd1 = N + 1
                        print(elementsListadd1)
                        print(elementsList[elementsListadd1].tag_name)
                        if elementsList[elementsListadd1].tag_name == 'android.widget.RelativeLayout':
                            objectEnd == 1
                            print(objectEnd)

    # def send_message_to_friend_listimage(self):
    #     #try:
    #     print('click')
    #     self.driver.implicitly_wait(15)
    #     #click contact
    #     self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabWidget[1]/android.widget.FrameLayout[1]').click()
    #     self.driver.implicitly_wait(15)
    #     #click friendlist
    #     self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
    #     #GO_TOP
    #     for i in range(3):
    #         self.driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=1000)
    #         self.driver.implicitly_wait(15)
    #     #get_elementlist
    #     elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
    #     #open_sendlist
    #     self.driver.implicitly_wait(15)
    #     if elementsList[2].tag_name == 'android.widget.RelativeLayout':
    #         elementsList[1].click()
    #
    #     #test elemnt imgage_to_string
    #     #tempElement = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/android.widget.RelativeLayout[2]/android.view.View[1]")
    #     #getimages.get_screenshot_by_element(self, tempElement)
    #     #test elemnt imgage_to_string
    #     self.driver.implicitly_wait(15)
    #     #add_people_parameter
    #     objectnumber = 0
    #     objectName = ''
    #     objectid = 0 #accuont
    #     objectEnd = 0
    #     imagestext = ''
    #
    #     #get_log
    #     response = str(requests.get('http://127.0.0.1:8000/auto/tasklog/' + str(self.mark['mobileID']) + '/' + str(self.mark['taskid']) + '/').text)
    #     response0 = str(0)
    #     if response == response0:
    #         elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
    #         tempElement = elementsList[2].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
    #         objectName = getimages.get_screenshot_by_element(self, tempElement)
    #         tempElement.click()
    #         self.driver.implicitly_wait(15)
    #         objectid = re.findall(r'(\d+)', self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').text)[0]
    #         self.driver.implicitly_wait(15)
    #         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[1]').click()
    #         self.driver.implicitly_wait(15)
    #         #input connect
    #         #self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').send_keys(self.mark['content'])
    #         #self.driver.implicitly_wait(15)
    #         #send_message
    #         #self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
    #         #self.driver.implicitly_wait(15)
    #         #RETURN
    #         time.sleep(1)
    #         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
    #         self.driver.implicitly_wait(15)
    #         responsetext ='http://127.0.0.1:8000/auto/tasklogdone/' + str(self.mark['mobileID']) + '/' + str(self.mark['taskid']) + '/' + str(objectName) + '/' + str(objectid) + '/'
    #         response = requests.post(responsetext)
    #         # click contact
    #         self.driver.implicitly_wait(15)
    #     else:
    #         objectName = response
    #         print(objectName)
    #         while (objectEnd != 1):
    #             selectTrue = 0
    #             elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
    #             self.driver.implicitly_wait(15)
    #             for N in range(0, elementsList.__len__()-1):
    #                 if N == elementsList.__len__() - 2:
    #                     # rolling
    #                     for i in range(2):
    #                         print('开始执行滑动', i + 1)
    #                         self.driver.swipe(start_x=50, start_y=0, end_x=50, end_y=450, duration=800)
    #                         self.driver.implicitly_wait(15)
    #                         try:
    #                             elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
    #                             self.driver.implicitly_wait(15)
    #                             tempElement = elementsList[N].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
    #                             self.driver.implicitly_wait(15)
    #                             imagestext = getimages.get_screenshot_by_element(self, tempElement)
    #                             if imagestext == objectName:
    #                                 objectEnd == 1
    #                         except:
    #                             break
    #
    #                 if elementsList[N].tag_name == 'android.widget.LinearLayout':
    #                     elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
    #                     self.driver.implicitly_wait(15)
    #                     tempElement = elementsList[N].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
    #                     self.driver.implicitly_wait(15)
    #                     imagestext = getimages.get_screenshot_by_element(self, tempElement)
    #                     print('imagestext' + imagestext)
    #                     print('objectName'+ objectName)
    #                     if selectTrue == 0:
    #                         if imagestext == objectName:
    #                             objectnumber = N
    #                             selectTrue = 1
    #                             continue
    #                         # rolling
    #                         else:
    #                             continue
    #                     if elementsList[N + 1].tag_name == 'android.widget.RelativeLayout':
    #                         objectEnd == 1
    #                     else:
    #                         elementsList = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/*")
    #                         self.driver.implicitly_wait(15)
    #                         tempElement = elementsList[N].find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]')
    #                         objectName = getimages.get_screenshot_by_element(self, tempElement)
    #                         tempElement.click()
    #                         self.driver.implicitly_wait(15)
    #                         # rolling
    #                         for i in range(1):
    #                             print('开始执行滑动', i + 1)
    #                             self.driver.swipe(start_x=50, start_y=333, end_x=50, end_y=50, duration=1000)
    #                         self.driver.implicitly_wait(15)
    #                         objectid = re.findall(r'(\d+)', self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').text)[0]
    #                         self.driver.implicitly_wait(15)
    #                         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[1]').click()
    #                         self.driver.implicitly_wait(15)
    #                         # input connect
    #                         #self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').send_keys(self.mark['content'])
    #                         #self.driver.implicitly_wait(15)
    #                         # send_message
    #                         #self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
    #                         #self.driver.implicitly_wait(15)
    #                         # RETURN
    #                         time.sleep(1)
    #                         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
    #                         self.driver.implicitly_wait(15)
    #                         responsetext = 'http://127.0.0.1:8000/auto/tasklogdone/' + str(self.mark['mobileID']) + '/' + str(self.mark['taskid']) + '/' + str(objectName) + '/' + str(objectid) + '/'
    #                         response = requests.post(responsetext)
    #                         # click contact
    #                         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabWidget[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]').click()
    #                         self.driver.implicitly_wait(15)

    #Need Send_Group_Message_Need_time
    def send_message_to_GROUP_list(self):
        pass

    def send_message_to_GROUP_list(self):
        pass

    def send_message_to_user_Accoutid(self):
        pass

    def send_message_to_user_Accoutid(self):
        pass

    def send_message_to_GROUP_Accoutid(self):
        pass

    #No Need
    def Get_Pople_list(self):
        time.sleep(7)
        print('click')
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabWidget[1]/android.widget.FrameLayout[1]').click()
        time.sleep(5)

        cc = self.driver.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.AbsListView[1]/android.widget.LinearLayout")
        ccc = cc[1].find_element_by_xpath("//android.widget.FrameLayout[1]")
        getimages_class = getimages(self.driver)
        getimages_class.get_screenshot_by_element(ccc)

    #No Need
    def Get_Group_list(self):
        pass
    def Get_Group_People_list(self):
        pass

if __name__ == '__main__':
    mobile_id = [1]
    for mobile_id_for in mobile_id:
        locals()['a' + str(mobile_id_for)] = multipleLoop(mobile_id_for)
        locals()['a' + str(mobile_id_for)].start()
        locals()['a' + str(mobile_id_for)].join()#加进去以后不会报错，得查查什么原因。
        #locals()['a' + str(mobile_id_for)].start()