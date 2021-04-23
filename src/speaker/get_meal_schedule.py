import requests
import json
import time

# if __name__ == "__main__":
#     import env.env as env
# else:
#     import src.speaker.env.env as env
import os
os.chdir(os.path.dirname(os.path.abspath( __file__ )))

from .env import *

CurrentDate=time.strftime('%Y%m%d', time.localtime(time.time()))
CurrentHour=int(time.strftime('%H', time.localtime(time.time())))

# API 고유키
# KEY=env.KEY

# # 학교 정보
# SCHUL_NM=env.SCHUL_NM # 학교 이름

def get_school():
    global ATPT_OFCDC_SC_CODE
    global SD_SCHUL_CODE
    try:
        tmp=json.loads(requests.get("https://open.neis.go.kr/hub/schoolInfo", {
            'Type':'json',
            'KEY':KEY,
            'SCHUL_NM':SCHUL_NM,
        }).text)['schoolInfo'][1]['row'][0]
        ATPT_OFCDC_SC_CODE=tmp['ATPT_OFCDC_SC_CODE']
        SD_SCHUL_CODE=tmp['SD_SCHUL_CODE']
    except:
        print('학교 정보를 불러오지 못했습니다.')

# ( 급식일자, 식사코드 1:아침, 2:점심, 3:저녁)
def meal(MLSV_YMD='', MMEAL_SC_CODE=''):
    get_school()
    # 급식 일자가 없다면
    if MLSV_YMD=='':
        MLSV_YMD=CurrentDate
    # 식사코드가 없다면
    if MMEAL_SC_CODE=='':
        if 0<CurrentHour and CurrentHour<8:
            MMEAL_SC_CODE=1
        elif 8<=CurrentHour and CurrentHour<13:
            MMEAL_SC_CODE=2
        elif 13<=CurrentHour and CurrentHour<24:
            MMEAL_SC_CODE=3
    try:
        meal=json.loads(requests.get("https://open.neis.go.kr/hub/mealServiceDietInfo", {
            'Type':'json', 
            'ATPT_OFCDC_SC_CODE':ATPT_OFCDC_SC_CODE, 
            'SD_SCHUL_CODE':SD_SCHUL_CODE, 
            'KEY':KEY, 
            'MMEAL_SC_CODE':MMEAL_SC_CODE, 
            'MLSV_YMD':MLSV_YMD,
        }).text)['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        meal=meal.replace('*','').replace('.','').replace('<br/>',' ')
        meal=''.join([i for i in meal if not i.isdigit()])
        return meal+' 입니다'
    except:
        return '급식 정보를 불러오지 못했습니다.'

def same_schedule(data, i, length):
    global same_cnt
    if i<length-1 and data[i]['ITRT_CNTNT']==data[i+1]['ITRT_CNTNT']:
        same_schedule(data, i+1, length)
        same_cnt+=1

# (시간표 일자, 학년, 반)
def schedule(ALL_TI_YMD='', GRADE='', CLASS_NM='0'):
    get_school()
    # 시간표 일자가 없다면
    if ALL_TI_YMD=='':
        ALL_TI_YMD=CurrentDate
    if GRADE=='':
        GRADE='3'
    if CLASS_NM=='0':
        CLASS_NM='4'
    try:
        tmp=json.loads(requests.get("https://open.neis.go.kr/hub/hisTimetable", {
            'Type':'json',
            'KEY':KEY,
            'SCHUL_NM':SCHUL_NM,
            'ATPT_OFCDC_SC_CODE':ATPT_OFCDC_SC_CODE, 
            'SD_SCHUL_CODE':SD_SCHUL_CODE,
            'ALL_TI_YMD':ALL_TI_YMD,
            'GRADE':GRADE,
            'CLASS_NM':CLASS_NM,
        }).text)['hisTimetable'][1]['row']
        schedule=''

        # Shorten
        # 같은 수업이 연달아 존재한다면
        # 합쳐서 출력해주는 로직
        global same_cnt
        i=0
        while i<len(tmp):
            if '휴업' in tmp[i]['ITRT_CNTNT']:
                schedule+=tmp[i]['ITRT_CNTNT'].replace('*','')+' '
                break
            if '일본' in tmp[i]['ITRT_CNTNT'] or '중국' in tmp[i]['ITRT_CNTNT']:
                tmp[i]['ITRT_CNTNT']=' 외국어'
            if i<len(tmp)-1 and ('일본' in tmp[i+1]['ITRT_CNTNT'] or '중국' in tmp[i+1]['ITRT_CNTNT']):
                tmp[i+1]['ITRT_CNTNT']=' 외국어'
            same_cnt=0
            same_schedule(tmp,i,len(tmp))
            j=i+1
            while j<=i+1+same_cnt:
                schedule+=str(j)+' '
                j+=1
            schedule+='교시'+tmp[i]['ITRT_CNTNT'].replace('*','')+' '
            i+=same_cnt
            i+=1

        # Origin
        # for i in tmp:
        #     schedule+=i['PERIO']+'교시'+i['ITRT_CNTNT'].replace('*','')+' '
        
        return schedule+'입니다'
    except:
        return '시간표 정보를 불러오지 못했습니다.'

def main():
    get_school()
    print(meal())
    print(schedule())

if __name__ == '__main__':
    main()