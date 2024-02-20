from django.apps import AppConfig
from threading import Thread
import time
import os
from django.conf import settings


class AtlasgridConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'atlasgrid'
    
    def ready(self):
        if os.environ.get('RUN_MAIN') or not settings.DEBUG:
            def run_gridtracker():
                while True:
                    try:
                        from . import gridtracker
                        gridtracker.start_gridtracker()
                    except Exception as e:
                        print(f"gridtracker 실행 중 오류 발생: {e}, 재시도...")
                        time.sleep(60)  # 에러 발생 시 잠시 대기 후 재시도

            Thread(target=run_gridtracker).start()
