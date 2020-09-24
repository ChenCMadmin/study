import datetime
import time


def get_week_day(date):
    '''
        获取date时间的星期几
    '''
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]


time1 = time.strftime("%Y%m%d", time.localtime())
print("当前日期：%s"%(time1))


start = time.strftime('%Y-%m-%d %H:%M:%S ')
print("当前时间：%s"%(start))

now = datetime.datetime.now()  #当前时间
def end1(now):
    if get_week_day(now) == '星期一' :
        delta = now + datetime.timedelta(days=-3) #周五
        end = delta.strftime('%Y-%m-%d 17:00:00')
    else:
        delta = now + datetime.timedelta(days=-1) #昨天
        end = delta.strftime('%Y-%m-%d 17:00:00')
    return end

print('上一个交易日：%s'%end1(now))
