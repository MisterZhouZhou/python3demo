from selenium import webdriver
import pandas as pd
import urllib
import json
import os
import re

# 音乐信息类
class Musci_info(object):
    def __init__(self, id):
        self.id = id

    # 保存音乐文件到
    def save_csv(self, music_info, path, head=None):
        # 将音乐信息存储到 .../data/歌手/ 目录下面，并以xx.csv存储
        data = pd.DataFrame(music_info, columns=head)
        # index=False去掉DataFrame默认的index列
        data.to_csv("{0}/singer{1}.csv".format(path, str(self.id)), encoding="utf-8", index=False)

        # 获取音乐信息
    def get_music_info(self):
        url = "https://music.163.com/#/artist?id={0}".format(self.id)
        # path = '/usr/local/bin/chromedriver'
        driver = webdriver.Chrome()
        driver.implicitly_wait(6)

        driver.maximize_window()
        driver.get(url)
        '''
                frame标签有frameset、frame、iframe三种，frameset跟其他普通标签没有区别，不会影响到正常的定位，而frame与iframe对selenium定位而言是一样的，selenium有一组方法对frame进行操作。
                driver.switch_to.frame() # 切到iframe里面
                driver.switch_to.parent_frame() # 切回父级
                driver.switch_to.default_content() # 切回主文档
        '''
        # 切换到contentFrame
        driver.switch_to.frame('contentFrame')
        # 切到iframe里面，可以根据id或name值来定位，这里是根据name值定位，看上述图1
        artist_name = driver.find_element_by_id('artist-name').text
        path = os.getcwd() + "/data/{0}".format(artist_name)
        # 在当前工作路径下创建一个/data/歌手名字文件夹，例如:...../data/薛之谦
        # 调用os模块判断是否存在
        if not os.path.exists(path):
            os.makedirs(path)
        # 找到歌手所有的歌曲，find_element...是找到了当前html标签，然后find_elements...多了个s，这里返回一个包含多个歌曲信息的list,每个list里面有多个tr标签。一个tr对应一个歌曲，看上述图2
        tr_list = driver.find_element_by_id("hotsong-list").find_elements_by_tag_name("tr")
        music_info = []
        # 对每个tr标签进行遍历，寻找对应信息的标签内容，把音乐的名字及链接找出来,看上述图3
        for i in range(len(tr_list)):
            content = tr_list[i].find_element_by_class_name('txt')
            href = content.find_element_by_tag_name('a').get_attribute('href')
            title = content.find_element_by_tag_name('b').get_attribute('title')
            music_info.append((title, href))
        # 返回音乐信息及当前歌手的路径地址
        return music_info, path


# 下载类
class Download_Music(object):
    # 初始化上述的歌曲名字，id，及存储的路径
    def __init__(self, music_name, music_id, path):
        self.music_name = music_name
        self.music_id = music_id
        self.path = path

    def save_txt(self):
        url = 'http://music.163.com/song/media/outer/url?id=' + str(self.music_id) + '.mp3'
        file_path = '{0}/{1}.txt'.format(self.path, self.music_name)
        with open(file_path, 'w') as f:
            json.dump(url, f)

    def download_mp3(self):
        # 定义url,请求的api
        url = 'http://music.163.com/song/media/outer/url?id=' + str(self.music_id) + '.mp3'
        try:
            print("正在下载：{0}".format(self.music_name))
            # 通过urllib.request.urlretrieve进行下载歌曲
            urllib.request.urlretrieve(url, '{0}/{1}.mp3'.format(self.path, self.music_name))
            print("Finish...")
        except:
            print("Failed...")


# 保存音乐信息
def saveMusicInfo(current_path, file_path):
    mu_info = pd.read_csv(file_path, engine='python', encoding='utf-8')
    '''
        通过iterrows遍历音乐信息的music文件
        iterrows返回的是一个元组(index,mu)
        '''
    for index, mu in mu_info.iterrows():
        music = mu['music']  # 取对应的歌曲
        # 通过正则取出歌曲对应的链接中的id
        regex = re.compile(r'(id)(=)(.*)')
        link = re.search(regex, mu['link']).group(3)
        music = Download_Music(music, link, current_path)
        music.save_txt()
        music.download_mp3()


# 根据歌手id获取信息
def getMusicBySingerId(singerName,singerId):
    current_path = os.getcwd() + "/data/{0}".format(singerName)
    file_path = '{0}/singer{1}.csv'.format(current_path, str(singerId))
    if os.path.exists(file_path):
        saveMusicInfo(current_path, file_path)
    else:
        # 歌手信息
        mu_info = Musci_info(singerId)
        # 类初始化
        music_info, path = mu_info.get_music_info()
        # 存储音乐的歌名及链接至csv文件
        mu_info.save_csv(music_info, path, head=['music', 'link'])
        saveMusicInfo(current_path, file_path)


if __name__ == '__main__':
    # https://music.163.com/#/artist?id=861777
    getMusicBySingerId("华晨宇",861777)
    print('d')