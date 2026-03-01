from airtest.core.api import *

class BasePage:
    """모든 페이지가 공통으로 사용할 도구함"""

    def step(self, img):
        """이미지 확인 및 터치"""
        pos = wait(img)
        sleep(2.0)
        touch(pos)

    def step_pass(self, img, timeout=10):
        """이미지 확인 및 터치, 없을 시 패스"""
        try:
            pos = wait(img, timeout=timeout)
            sleep(7.0)
            touch(pos)
        except:
            pass

    def input_text(self, content):
        """계정 정보 입력"""
        text(content)
