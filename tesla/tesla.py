import requests
from urllib import parse
import time
import os


def getPage():
  url = 'https://www.tesla.cn/model3/design#battery'
  r = requests.get(url)
  return r.text.encode('utf-8').decode('unicode_escape')


def diff(notify_secret):
  now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  new_content = getPage()
  if new_content:
    r = new_content.find('"range":"668"')
    if r == -1:
      print('[{}] 没有检测到续航 668 的车型'.format(now))
    else:
      msg = '[{}] 检测到了续航 668 的车型！！！！！！！赶紧的!!!!!'.format(now)
      notify(msg, notify_secret)
      print(msg)


def notify(text, notify_secret):
  while True:
    r = requests.get('https://sc.ftqq.com/{}.send?text={}'.format(notify_secret, text))
    if r.status_code == 200:
      return
    time.sleep(2)


if __name__ == "__main__":
  check_interval = int(os.getenv('CHECK_INTERVAL')) or 60
  notify_secret = os.getenv('NOTIFY_SECRET')
  health_check_interval = os.getenv('HEALTH_CHECK_INTERVAL') or 50
  if not notify_secret:
    print('Error! 请设置 Server 酱通知的密钥')
    exit(1)

  print('本次检测开始，检测间隔：{} , Server 酱密钥：{} '.format(check_interval, notify_secret))

  i = 0
  while True:
    try:
        diff(notify_secret)
        time.sleep(check_interval)
        if i > 0 and i % int(health_check_interval) == 0:
          notify('【第{}次检测】距离上次通知你，已经又跑了 {} 次了，没啥事，就是告诉你我还活着'.format(i, health_check_interval), notify_secret)
        i += 1
    except Exception as e:
      print(e)
