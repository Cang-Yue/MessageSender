import random
import pyperclip
from time import sleep
from pynput.keyboard import Key, Controller
from tqdm import tqdm

#Get Data
def get_data():
    send_text = str(input("发送文字> "))
    send_count = int(input("发送次数> "))
    random_time_start = float(input("随机间隔时间 始> "))
    random_time_end = float(input("随机间隔时间 末> "))
    random_str_count = int(input("随机字符数量> "))
    start = input("按Enter将在5s后开始执行> ")
    return send_text,send_count,random_time_start,random_time_end,random_str_count

#Get Random String
def random_str(num):
    random_all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random_text = "".join(random.sample(random_all, num))
    random_text = "[" + random_text + "]"
    return random_text

#Get Random Time
def random_time(start, end):
    time = random.uniform(start, end)
    return time

#Send Function
def send(send_text, random_num, count, start, end):
    for i in tqdm(range(count)):
        if random_num != 0 :
            send = random_str(random_num) + " " + send_text + " " + random_str(random_num)
        else :
            send = send_text
        sleep(float(random_time(start, end)))
        pyperclip.copy(send)
        keyboard = Controller()
        keyboard.press(Key.ctrl_l)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl_l)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # print("\r" + str(i + 1) + "/" + str(send_count), end = "")

#Main
def main():
    send_text, send_count, random_time_start, random_time_end, random_str_count = get_data()
    sleep(5)
    send(send_text, random_str_count, send_count,random_time_start, random_time_end)
    return 0

#Run
if __name__ == "__main__":
    main()