import pytest
from pages.tutorial_page import TutorialPage

class TestBlueArchive:
    def test_full_tutorial(self):
        """블루아카이브 초반 튜토리얼 전체 자동화"""
        tutorial = TutorialPage()

        # 1. 챕터별 순차 실행
        tutorial.chapter_1() # 계정 생성
        tutorial.chapter_2() # 스킬 카드
        tutorial.chapter_3() # 엄폐/탱크
        tutorial.chapter_4() # 가챠
        tutorial.chapter_5() # 임무
        tutorial.chapter_6() # 로비
        
        print("\n>>> 초반 튜토리얼 테스트 완료")
        
 
