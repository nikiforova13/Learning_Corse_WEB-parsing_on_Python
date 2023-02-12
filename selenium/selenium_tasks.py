import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# task 1
url = 'https://parsinger.ru/selenium/4/4.html'
browser = webdriver.Chrome()
browser.get(url=url)
f = browser.find_elements(By.XPATH, '//input[@class="check"]')
for i in f:
    i.click()
browser.find_element(By.XPATH, '//input[@class="btn"]').click()
print(browser.find_element(By.ID, 'result').text)
# task 2
url = 'https://parsinger.ru/selenium/5/5.html'
browser = webdriver.Chrome()
browser.get(url=url)
f = browser.find_elements(By.XPATH, '//input[@class="check"]')
numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
           39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
           74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
           119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
           154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
           187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
           208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
           234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
           256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
           292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
           318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
           353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
           419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
           452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
           480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
for i in f:
    if int(i.get_attribute('value')) in numbers:
        i.click()

browser.find_element(By.XPATH, '//input[@class="btn"]').click()
print(browser.find_element(By.ID, 'result').text)
# task 3
url = 'https://parsinger.ru/selenium/7/7.html'
a = []
with webdriver.Chrome() as webrowser:
    webrowser.get(url)
    f = webrowser.find_elements(By.TAG_NAME, 'option')
    for i in f:
        a.append(int(i.text))
    print(a)
    webrowser.find_element(By.XPATH, '//input[@type="text"]').send_keys(sum(a))
    webrowser.find_element(By.XPATH, '//input[@class="btn"]').click()
    print(webrowser.find_element(By.XPATH, '//p[@id="result"]').text)
    time.sleep(5)
# task 4
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/6/6.html')
    num = eval(browser.find_element(By.ID, 'text_box').text)
    f = browser.find_elements(By.TAG_NAME, 'option')
    for i in f:
        if int(i.text) == num:
            i.click()
    browser.find_element(By.XPATH, '//input[@class="btn"]').click()
    print(browser.find_element(By.ID, 'result').text)
# task 5
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while browser.find_element(By.ID, 'result').text == 'refresh page':
        browser.refresh()
    print(browser.find_element(By.ID, 'result').text)
# task 6
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    a = browser.get_cookies()
    count = 0
    for i in a:
        count+= int(i['value'])
print(count)
# task 7
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    a = browser.get_cookies()
    c =0
    for i in a:
        print(i)
        b = i['name'][-2::].strip('_')
        print(b)
        if int(b) % 2 == 0:

            print(i['name'][-2::])
            print(i['value'])
            c += int(i['value'])
print(c)
# task 8
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    a = [i.get_attribute('href') for i in browser.find_elements(By.TAG_NAME, 'a')]
    b = []
    t = ''
    l = ''
    for i in a:
        print(i)
        browser.get(i)
        k = browser.get_cookies()
        for j in k:
            r = time.strftime('%Y-%m-%d', time.localtime(j['expiry']))
            print(r)
            if r > t:
                t = r
                l = browser.find_element(By.ID,'result' ).text
                print(t)
print(t, l)
# task 9
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.execute_script("window.scrollBy(0,10000)")
    time.sleep(10)
# task 10
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    for i in range(10):
        browser.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)
# task 11
with webdriver.Chrome() as browser:
    m = []
    browser.get('https://parsinger.ru/scroll/4/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'btn')
    for i in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", i)
        i.click()
        search = browser.find_element(By.ID, 'result').text
        m.append(int(search))
print(sum(m))
# task 12
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')

    list_input = []
    while True:
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
        for tag_input in input_tags:
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)
                tag_input.click()
                time.sleep(1)
                list_input.append(tag_input)
# task 13
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    while True:
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
# task 14
# with webdriver.Chrome() as browser:
#     c = []
#     browser.get('https://parsinger.ru/scroll/3/')
#     a = browser.find_elements(By.CLASS_NAME, 'checkbox_class')
#
#     for i in a:
#         i.click()
#
#     g = browser.find_elements(By.XPATH, '//span["@id"]')
#     for i in g:
#         if i.text != '':
#             c.append(int(i.text))
#     print(sum(c))
# task 15
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    b = browser.find_elements(By.TAG_NAME, 'input')
    for i in b:
        i.send_keys(Keys.DOWN)
        time.sleep(2)
# task 16
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    tags_input = browser.find_elements(By.TAG_NAME, 'input')

    for input in tags_input[20:]:
        input.send_keys(Keys.DOWN)
        time.sleep(1)
# task 17
with webdriver.Chrome() as browser:
    a = []
    browser.get('https://parsinger.ru/blank/modal/2/index.html')
    all_elements = browser.find_elements(By.XPATH, '//input[@type="button"]')
    for current_element in all_elements:
        current_element.click()
        window_alert = browser.switch_to.alert
        window_alert.accept()
        search_elem = browser.find_element(By.ID, 'result').text
        if len(search_elem) > 0:
            a.append(search_elem)
print(a)
# task 18
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/4/index.html')
    all_elements = browser.find_elements(By.CLASS_NAME, 'pin')
    button = browser.find_element(By.XPATH, '//input[@type="button"]')
    button2 = browser.find_element(By.XPATH, '//p[@id="result"]')
    for current_elem in all_elements:
        b = current_elem.text

        button.click()

        a1 = browser.switch_to.alert
        a1.send_keys(b)
        a1.accept()
        if button2.text != 'Неверный пин-код':
            print(button2.text)
# task 19
with webdriver.Chrome() as browser:
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    browser.get('https://parsinger.ru/window_size/2/index.html')
    for i in window_size_x:
        for j in window_size_y:
            browser.set_window_size(i + 16, j + 133)
            if browser.find_element(By.ID, 'result').text.isdigit():
                print(browser.find_element(By.ID, 'result').text)
                print(browser.get_window_size())
# task 20
with webdriver.Chrome() as browser:
    result = []
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
    time.sleep(2)
    print(browser.window_handles)
# task 21
for x in range(len(browser.window_handles)):  #reversed(range(len(browser.window_handles))) Для итерирования по порядку
    browser.switch_to.window(browser.window_handles[x])
    for y in browser.find_elements(By.CLASS_NAME, 'check'):
        y.click()
# task 22
for x in range(len(browser.window_handles)):
     browser.switch_to.window(browser.window_handles[x])
     time.sleep(1)
     print(browser.execute_script("return document.title;"), browser.window_handles[x])

# task 23
with webdriver.Chrome() as browser:
    browser.get("https://stepik.org/course/104774/promo")
    print(browser.execute_script("return document.title;"))
with webdriver.Chrome() as b:
    a = []
    for i in range(1, 11):
        b.get(f'https://parsinger.ru/blank/3/{i}.html')
        a.append(int(b.execute_script("return document.title;")))

    print(sum(a))
# task 24

with webdriver.Chrome() as browser:
    count = 0
    browser.get('http://parsinger.ru/blank/3/index.html')
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'buttons')]
    tabs = browser.window_handles
    for tab in range(len(tabs)):
        browser.switch_to.window(browser.window_handles[tab])
        title = browser.execute_script("return document.title;")
        if title.isdigit():
            count += int(title)
    print(count)
# task 25
# from math import sqrt
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
with webdriver.Chrome() as browser:
    b = []
    for i in sites:
        browser.execute_script(f'window.open("{i}");')
        time.sleep(1)
        a = browser.window_handles
    for j in range(1,len(a)):
        browser.switch_to.window(browser.window_handles[j])
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        b.append(sqrt(int(browser.find_element(By.ID, 'result').text)))
# task 26
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    element = WebDriverWait(browser, 10).until(EC.title_is('title changed'))
    print(element)
# task 27
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    element = WebDriverWait(browser, 10).until(EC.title_contains('tle'))
    print(element)
# task 28
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    if WebDriverWait(browser, 30).until(EC.title_is('345FDG3245SFD')):
        print(browser.find_element(By.ID, 'result').text)
# task 29
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/4/index.html')
    WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'btn'))).click()
    if WebDriverWait(browser, 30).until(expected_conditions.title_contains('JK8HQ')):
        print('da')
        print(browser.execute_script("return document.title;"))
# task 30
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'btn'))).click()
    print((WebDriverWait(browser, 30).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'Y1DM2GR')))).text)
# task 31
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    time.sleep(3)
    red_block = browser.find_element(By.ID, 'draggable')
    grey_block = browser.find_element(By.ID, 'field2')
    actions = ActionChains(browser)
    actions.drag_and_drop(red_block, grey_block).perform()
    # actions.click_and_hold(red_block).perform()
    # actions.move_to_element(grey_block).release().perform()
    print(browser.find_element(By.ID, 'result').text)
# task 32
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    red_block = browser.find_element(By.ID, 'draggable')
    all_blocks = browser.find_elements(By.CLASS_NAME, 'box')
    actions = ActionChains(browser)
    actions.click_and_hold(red_block).perform()
    for i in all_blocks:
        actions.drag_and_drop(red_block, i).release().perform()
    print(browser.find_element(By.ID, 'message').text)
# task 33
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    point = browser.find_elements(By.CLASS_NAME, 'controlPoint')
    elem = browser.find_element(By.ID, 'block1')
    actions = ActionChains(browser)
    for i in range(6):
        actions.click_and_hold(elem).move_by_offset(50, 0)
    actions.perform()

    time.sleep(1)
    print(browser.find_element(By.ID, 'message').text)
