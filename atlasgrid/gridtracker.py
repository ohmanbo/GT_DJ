import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import atexit

def fetch_data(driver):
    
    WebDriverWait(driver, 300).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".col-lg-12.gridplayers.noselect.ng-star-inserted"))
    )
    
    data = []
    elements = driver.find_elements(By.CSS_SELECTOR, ".col-lg-12.gridplayers.noselect.ng-star-inserted")
    data = [element.text.strip() for element in elements]
    
    return data 

def start_gridtracker():

    # Chrome 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless 모드 활성화
    chrome_options.add_argument("--disable-gpu")  # GPU 가속 비활성화 (일부 시스템에서 필요)
    chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 비활성화 (리눅스 시스템에서 필요)
    chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 비활성화
    

    # WebDriver 객체 생성 시 경로 명시
    driver = webdriver.Chrome(options=chrome_options)
    
    def cleanup_driver():
        driver.quit()
    # 장고가 종료될때 드라이버자동종료 할수있도록 cleanup 호출
    atexit.register(cleanup_driver)
    
    url = "https://atlas-world.net/cluster/1";
    driver.get(url)

    # 데이터 파일 경로
    data_file = './griddata.json'    
    data_history = []
    retry_count = 0
    max_retries = 5  # 최대 재시도 횟수
    update_count = 0

    # 파일이 존재하면 기존 데이터 로드, 그렇지 않으면 빈 리스트 시작
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            data_history = json.load(file)
    else:
        data_history = []

    while True:
        try:
            current_data = fetch_data(driver)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_history.append({'time': current_time, 'data': current_data})

            # 오래된 데이터 제거
            if len(data_history) > 12:
                data_history.pop(0)

            # 데이터 파일에 저장
            with open(data_file, 'w') as file:
                json.dump(data_history, file)

            update_count += 1   
            print(f"그리드 데이터 업데이트완료! count ={update_count}")
            time.sleep(10)
        except Exception as e:
            print(f"gridtracker error@@@@ 1분후 재시도... error:{e}")
            retry_count += 1
            if retry_count >= max_retries:
                print("크롬드라이버 최대 재시도 횟수 도달, 프로그램 종료")
                break  # while 루프를 빠져나와 프로그램 종료
            time.sleep(60)

    driver.quit()
    
    

