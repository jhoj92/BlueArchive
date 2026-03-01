import pytest
from airtest.core.api import *
import logging

logging.getLogger("airtest").setLevel(logging.WARNING)

@pytest.fixture(scope="session", autouse=True)
def setup_automation():
    print("\n[Setup] 기기 연결 중...")

    try:
        # 1. 기기 연결
        connect_device("Android:///emulator-5554")
        
    except Exception as e:
        print(f"\n[Error] 연결 실패: {e}")
        raise e

    # 3. Airtest 설정
    auto_setup(__file__)

    ST.THRESHOLD = 0.9
    ST.FIND_TIMEOUT = 120
    
    print("[Setup] 기기 연결 완료")
    
