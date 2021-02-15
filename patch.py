from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time

options = webdriver.ChromeOptions()
options.add_argument("lang=ko_KR")

browser = webdriver.Chrome(
    '/usr/local/bin/chromedriver', chrome_options=options)

random_wait_min = 1
random_wait_max = 5

random_next_min = 1
random_next_max = 5

refresh_count = 20
onetime_count = 25
like_count = 0

tag = ['미술', '예술', 'art', 'artist']


ID = '01047695935'  # 인스타그램 ID
PW = '!Jo36035935'  # 인스타그램 PW

# 화면 띄우기
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get("https://instagram.com")

# 로딩하는 시간 기다리기
time.sleep(2)

# Login ID 속성값 찾고 입력하기
login_id = browser.find_element_by_name('username')
login_id.send_keys(ID)

# Login PW 속성값 찾기 입력하기
login_pw = browser.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)

time.sleep(5)

# Created by CoinPipe

# # 정보 저장 팝업 닫기
# popup = browser.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/div/div/div/button')
# popup.send_keys(Keys.ENTER)

# time.sleep(2)

# 알림 설정 팝업 닫기
popup = browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]')
popup.send_keys(Keys.ENTER)

# 태그 검색 하기
search = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('#미술')

time.sleep(2)

# 최상위 검색 결과로 진입하기 Enter 두번으로 수행
search.send_keys(Keys.RETURN)  # 최상위 검색결과로 Focus 이동
search.send_keys(Keys.RETURN)  # 검색결과 새로운 창으로 이동'

prev_url = browser.current_url  # 이번 수정사항의 핵심 코드

# 다음 게시물 이동하기 함수


def nextFeed():
    time.sleep(1)
    nextFeed = browser.find_element_by_css_selector(
        'body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
    nextFeed.click()


for b in range(refresh_count):

    # 최근 게시물 중 첫번쨰 게시물 선택하기
    time.sleep(5)
    feed = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a')
    feed.send_keys(Keys.ENTER)
    nextFeed()

    for a in range(onetime_count):
        # 좋아요 누르기
        time.sleep(randint(random_wait_min, random_wait_max))
        try:
            like_list = browser.find_elements_by_xpath(
                '//article//section/span/button')
            like_list[0].click()  # list 중 0번째 버튼을 선택
            like_count += 1
            print("like count = ", like_count)
        except:
            print("exception!")

        # 다음 피드로 이동하기
        for b in range(randint(random_next_min, random_next_max)):
            nextFeed()

    browser.get(prev_url)
    print("refresh!")


# # 최근 게시물 중 첫번쨰 게시물 선택하기
# time.sleep(3)
# feed = browser.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a')
# feed.send_keys(Keys.ENTER)
# nextFeed()

# for a in range(10):
#     # 좋아요 누르기

#     time.sleep(randint(random_wait_min, random_wait_max))
#     try:
#         like_list = browser.find_elements_by_xpath(
#             '//article//section/span/button')
#         like_list[0].click()  # list 중 0번째 버튼을 선택
#     except:
#         print("exception!")

#     # 다음 피드로 이동하기
#     for b in range(randint(random_next_min, random_next_max)):
#         nextFeed()


# for a in range(10):
#     # 좋아요 누르기
#     time.sleep(3)
#     like_list = browser.find_elements_by_xpath(
#         '//article//section/span/button')
#     like_list[0].click()  # list 중 0번째 버튼을 선택

#     # 다음 피드로 이동하기
#     nextFeed()


# for b in range(refresh_count):

#     # 최근 게시물 중 첫번쨰 게시물 선택하기
#     time.sleep(5)
#     feed = browser.find_element_by_xpath(
#         '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a')
#     feed.send_keys(Keys.ENTER)
#     nextFeed()
