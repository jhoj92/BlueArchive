import os
from airtest.core.api import *
from airtest.core.cv import Template
from pages.base_page import BasePage

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
IMG_DIR = os.path.join(ROOT_DIR, "images.air")

class TutorialPage(BasePage):

    def path(folder, name):
        return os.path.join(IMG_DIR, folder, name)
    
    # =========================================================
    # [1] 튜토리얼 별 이미리 리스트 정리
    # =========================================================
    
    # 0. 공용 버튼 관련
    menu_btn = Template(path("00_common", "01_메뉴 버튼.png"))
    skip_btn = Template(path("00_common", "02_스킵 버튼.png"))
    skip_check_btn = Template(path("00_common", "03_스킵 확인 버튼.png"))
    tutorial_complete_btn = Template(path("00_common", "04_튜토리얼 임무 확인 버튼.png"))
    daily_01 = Template(path("00_common", "05_출석부1.png"))
    daily_02 = Template(path("00_common", "06_출석부2.png"))

    # 1. 타이틀 화면 진입 및 계정 생성
    user_name = "지쿠니"
    user_voice = "지쿠니"

    download_btn = Template(path("01_chapter", "01_다운로드 버튼.png"))
    k_voice_btn = Template(path("01_chapter", "02_한국어 음성 선택.png"))
    j_voice_btn = Template(path("01_chapter", "03_일본어 음성 선택.png"))
    voice_check_btn = Template(path("01_chapter", "04_음성 선택 확인 버튼.png"))
    guest_login = Template(path("01_chapter", "05_게스트 로그인.png"))
    guest_check_btn = Template(path("01_chapter", "06_게스트 계정 이용 안내 확인.png"))
    tos_btn = Template(path("01_chapter", "07_이용 약관 모두 동의.png"))
    tos_check_btn = Template(path("01_chapter", "08_동의 확인.png"))
    phone_confirm_btn = Template(path("01_chapter", "09_전화 이용 확인 버튼.png"))
    ad_close_btn_01 = Template(path("01_chapter", "10_광고 팝업01.png"))
    ad_close_btn_02 = Template(path("01_chapter", "11_광고 팝업02.png"))
    ad_close_btn_03 = Template(path("01_chapter", "12_광고 팝업3.png"))
    start_btn = Template(path("01_chapter", "13_TOUCH TO START.png"))
    alarm_btn = Template(path("01_chapter", "14_신규 계정 생성 확인.png"))
    name_input_btn = Template(path("01_chapter", "15_계정 이름 입력.png"))
    name_check_btn = Template(path("01_chapter", "16_계정 이름 확인.png"))
    name_voice_btn = Template(path("01_chapter", "17_이름 발음 입력.png"))
    name_voice_check_btn = Template(path("01_chapter", "18_이름 발음 입력 확인.png"))
    name_voice_file_btn = Template(path("01_chapter", "19_이름 발음 파일 다운.png"))
    name_voice_file_complete_btn = Template(path("01_chapter", "20_파일 다운 완료.png"))
    tutorial_prologue_btn = Template(path("01_chapter", "21_프롤로그 플레이.png"))
    tutorial_start_btn = Template(path("01_chapter", "22_튜토리얼 접속.png"))
    
    # 2. 스킬 카드 
    skill_card_01 = Template(path("02_chapter", "01_스킬 카드 시스템 안내.png"))
    skill_card_02 = Template(path("02_chapter", "02_스킬 카드 시스템 안내.png"))
    skill_card_03 = Template(path("02_chapter", "03_스킬 카드 시스템 안내.png"))
    skill_card_04 = Template(path("02_chapter", "04_스킬 카드 시스템 안내.png"))
    skill_card_05 = Template(path("02_chapter", "05_스킬 카드 시스템 안내.png"))
    skill_card_06 = Template(path("02_chapter", "06_스킬 카드 시스템 안내.png"))
    skill_card_07 = Template(path("02_chapter", "07_스킬 카드 시스템 안내.png"))
    skill_card_08 = Template(path("02_chapter", "08_스킬 카드 시스템 안내.png"))
    skill_card_09 = Template(path("02_chapter", "09_스킬 카드 시스템 안내.png"))
    skill_card_10 = Template(path("02_chapter", "10_스킬 카드 시스템 안내.png"))
    skill_card_11 = Template(path("02_chapter", "11_스킬 카드 시스템 안내.png"))
    skill_card_12 = Template(path("02_chapter", "12_스킬 카드 시스템 안내.png"))
    skill_card_13 = Template(path("02_chapter", "13_스킬 카드 시스템 안내.png"))
    skill_card_14 = Template(path("02_chapter", "14_스킬 카드 시스템 안내.png"))
    skill_card_15 = Template(path("02_chapter", "15_스킬 카드 시스템 안내.png"))
    skill_card_16 = Template(path("02_chapter", "16_스킬 카드 시스템 안내.png"))
    skill_card_17 = Template(path("02_chapter", "17_스킬 카드 시스템 안내.png"))

    # 3. 엄폐 및 탱크
    hide_01 = Template(path("03_chapter", "01_엄폐물 시스템 안내.png"))
    hide_02 = Template(path("03_chapter", "02_엄폐물 시스템 안내.png"))
    hide_03 = Template(path("03_chapter", "03_엄폐물 시스템 안내.png"))
    hide_04 = Template(path("03_chapter", "04_엄폐물 시스템 안내.png"))
    hide_05 = Template(path("03_chapter", "05_엄폐물 시스템 안내.png"))

    tank_01 = Template(path("03_chapter", "06_탱크 시스템 안내.png"))
    tank_02 = Template(path("03_chapter", "07_탱크 시스템 안내.png"))
    tank_03 = Template(path("03_chapter", "08_탱크 시스템 안내.png"))
    tank_04 = Template(path("03_chapter", "09_탱크 시스템 안내.png"))
    tank_05 = Template(path("03_chapter", "10_탱크 시스템 안내.png"))
    tank_06 = Template(path("03_chapter", "11_탱크 시스템 안내.png"))
    tank_07 = Template(path("03_chapter", "12_탱크 시스템 안내.png"))

    # 4. 가챠 (Gacha)
    gacha_01 = Template(path("04_chapter", "01_가챠 시스템 안내.png"))
    gacha_02 = Template(path("04_chapter", "02_가챠 시스템 안내.png"))
    gacha_03 = Template(path("04_chapter", "03_가챠 시스템 안내.png"))
    gacha_04 = Template(path("04_chapter", "04_모집 버튼.png"))
    gacha_05 = Template(path("04_chapter", "05_모집 무료 버튼.png"))
    gacha_06 = Template(path("04_chapter", "06_모집 확인 버튼.png"))
    gacha_07 = Template(path("04_chapter", "07_결제 스킵 버튼.png"))
    gacha_08 = Template(path("04_chapter", "08_3성 학생 확인.png"))
    gacha_09 = Template(path("04_chapter", "09_가챠 시스템 안내.png"))
    gacha_10 = Template(path("04_chapter", "10_가챠 시스템 안내.png"))
    gacha_11 = Template(path("04_chapter", "11_가챠 시스템 안내.png"))
    gacha_12 = Template(path("04_chapter", "12_가챠 시스템 안내.png"))
    gacha_13 = Template(path("04_chapter", "13_첫뽑 결과 저장.png"))
    gacha_14 = Template(path("04_chapter", "14_가챠 시스템 안내.png"))
    gacha_15 = Template(path("04_chapter", "15_가챠 시스템 안내.png"))
    gacha_16 = Template(path("04_chapter", "16_가챠 시스템 안내.png"))
    gacha_17 = Template(path("04_chapter", "17_가챠 시스템 안내.png"))
    gacha_18 = Template(path("04_chapter", "18_다시 하기 버튼.png"))
    gacha_19 = Template(path("04_chapter", "19_가챠 시스템 안내.png"))
    gacha_20 = Template(path("04_chapter", "20_결과 선택 버튼.png"))
    gacha_21 = Template(path("04_chapter", "21_가챠 시스템 안내.png"))
    gacha_22 = Template(path("04_chapter", "22_결과 저장 버튼.png"))
    gacha_23 = Template(path("04_chapter", "23_결과 저장 확인.png"))
    gacha_24 = Template(path("04_chapter", "24_뽑기 재진행.png"))
    gacha_25 = Template(path("04_chapter", "25_최종 결과 선택.png"))
    gacha_26 = Template(path("04_chapter", "26_결과 선택 확인.png"))
    gacha_27 = Template(path("04_chapter", "27_가챠 시스템 안내.png"))
    gacha_28 = Template(path("04_chapter", "28_가챠 시스템 안내.png"))
    gacha_29 = Template(path("04_chapter", "29_최종 결과 확인.png"))

    # 5. 임무 (Mission)
    mission_01 = Template(path("05_chapter", "01_임무 시스템 안내.png"))
    mission_02 = Template(path("05_chapter", "02_임무 입장 버튼.png"))
    mission_03 = Template(path("05_chapter", "03_임무 시작 버튼.png"))
    mission_04 = Template(path("05_chapter", "04_임무 시스템 안내.png"))
    mission_05 = Template(path("05_chapter", "05_임무 시스템 안내.png"))
    mission_06 = Template(path("05_chapter", "06_임무 시스템 안내.png"))
    mission_07 = Template(path("05_chapter", "07_임무 시스템 안내.png"))
    mission_08 = Template(path("05_chapter", "08_빠른 편성 버튼.png"))
    mission_09 = Template(path("05_chapter", "09_임무 시스템 안내.png"))
    mission_10 = Template(path("05_chapter", "10_임무 시스템 안내.png"))
    mission_11 = Template(path("05_chapter", "11_임무 시스템 안내.png"))
    mission_12 = Template(path("05_chapter", "12_임무 시스템 안내.png"))
    mission_13 = Template(path("05_chapter", "13_임무 시스템 안내.png"))
    mission_14 = Template(path("05_chapter", "14_임무 시스템 안내.png"))
    mission_15 = Template(path("05_chapter", "15_임무 시스템 안내.png"))
    mission_16 = Template(path("05_chapter", "16_임무 시스템 안내.png"))
    mission_17 = Template(path("05_chapter", "17_임무 시스템 안내.png"))
    mission_18 = Template(path("05_chapter", "18_임무 시스템 안내.png"))
    mission_19 = Template(path("05_chapter", "19_빠른 편성 자동.png"))
    mission_20 = Template(path("05_chapter", "20_빠른 편성 확인.png"))
    mission_21 = Template(path("05_chapter", "21_임무 시스템 안내.png"))
    mission_22 = Template(path("05_chapter", "22_임무 출격 버튼.png"))
    mission_23 = Template(path("05_chapter", "23_임무 시스템 안내.png"))
    mission_24 = Template(path("05_chapter", "24_임무 개시 버튼.png"))
    mission_25 = Template(path("05_chapter", "25_임무 시스템 안내.png"))
    mission_26 = Template(path("05_chapter", "26_임무 시스템 안내.png"))
    mission_27 = Template(path("05_chapter", "27_임무 시스템 안내.png"))
    mission_28 = Template(path("05_chapter", "28_스킬 오토 버튼.png"))
    mission_29 = Template(path("05_chapter", "29_임무 완료 확인 버튼.png"))
    mission_30 = Template(path("05_chapter", "30_랭크 획득 확인 버튼.png"))
    mission_31 = Template(path("05_chapter", "31_임무 시스템 안내.png"))
    mission_32 = Template(path("05_chapter", "32_임무 시스템 안내.png"))
    mission_33 = Template(path("05_chapter", "33_페이즈 종료 버튼.png"))
    mission_34 = Template(path("05_chapter", "34_임무 시스템 안내.png"))
    mission_35 = Template(path("05_chapter", "35_임무 시스템 안내.png"))
    mission_36 = Template(path("05_chapter", "36_임무 시스템 안내.png"))
    mission_37 = Template(path("05_chapter", "37_임무 완료 확인 버튼.png"))
    mission_38 = Template(path("05_chapter", "38_최종 임무 완료 확인 버튼.png"))
    mission_39 = Template(path("05_chapter", "39_임무 시스템 안내.png"))
    mission_40 = Template(path("05_chapter", "40_임무 시스템 안내.png"))
    mission_41 = Template(path("05_chapter", "41_임무 시스템 안내.png"))
    mission_42 = Template(path("05_chapter", "42_임무 시스템 안내.png"))

    # 6. 로비 (Lobby)
    lobby_01 = Template(path("06_chapter", "01_로비 안내.png"))
    lobby_02 = Template(path("06_chapter", "02_로비 안내.png"))
    lobby_03 = Template(path("06_chapter", "03_로비 안내.png"))
    lobby_04 = Template(path("06_chapter", "04_모모톡 시스템 안내.png"))
    lobby_05 = Template(path("06_chapter", "05_모모톡 시스템 안내.png"))
    lobby_06 = Template(path("06_chapter", "06_모모톡 시스템 안내.png"))
    lobby_07 = Template(path("06_chapter", "07_모모톡 시스템 안내.png"))
    lobby_08 = Template(path("06_chapter", "08_모모톡 시스템 안내.png"))
    lobby_09 = Template(path("06_chapter", "09_모모톡 시스템 안내.png"))
    lobby_10 = Template(path("06_chapter", "10_모모톡 시스템 안내.png"))
    lobby_11 = Template(path("06_chapter", "11_모모톡 시스템 안내.png"))
    lobby_12 = Template(path("06_chapter", "12_모모톡 시스템 안내.png"))
    lobby_13 = Template(path("06_chapter", "13_모모톡 시스템 안내.png"))
    lobby_14 = Template(path("06_chapter", "14_모모톡 시스템 안내.png"))
    lobby_15 = Template(path("06_chapter", "15_모모톡 시스템 안내.png"))
    lobby_16 = Template(path("06_chapter", "16_모모톡 시스템 안내.png"))
    
    # =========================================================
    # [2] 동작 로직
    # =========================================================

    def skip_story_action(self):
        """스토리 스킵 공통 동작"""
        self.step(self.menu_btn)
        self.step(self.skip_btn)
        wait(self.skip_check_btn)
        sleep(1.0)
        touch((1186, 753))

    def chapter_1(self):
        """타이틀 화면 진입 및 계정 생성"""
        print(">>> Chapter 1: 자동화 테스트를 시작합니다.")

        # 데이터 다운 및 계정 생성
        self.step(self.start_btn)
        self.step(self.alarm_btn)
        
        # 닉네임 입력
        self.step(self.name_input_btn)
        self.input_text(self.user_name)
        self.step(self.name_check_btn)
        
        # 닉네임 보이스 설정
        self.step(self.name_voice_btn)
        self.input_text(self.user_voice)
        sleep(1.0)
        self.step(self.name_voice_check_btn)
        
        # 튜토리얼 진입
        self.step(self.tutorial_start_btn)
        self.skip_story_action()

    def chapter_2(self):
        """스킬 카드 시스템"""
        print(">>> Chapter 2: 스킬 카드")
        
        # 스킬 카드 시스템 튜토리얼 진행
        cards = [
            self.skill_card_01, self.skill_card_02, self.skill_card_03,
            self.skill_card_04, self.skill_card_05, self.skill_card_06,
            self.skill_card_07, self.skill_card_08, self.skill_card_09,
            self.skill_card_10, self.skill_card_11, self.skill_card_12,
            self.skill_card_13, self.skill_card_14, self.skill_card_15,
            self.skill_card_16, self.skill_card_17
        ]
        
        for c in cards:
            self.step(c)

        self.step(self.tutorial_complete_btn)

        # 스킬 카드 시스템 튜토리얼 후 스토리 스킵
        self.skip_story_action()
        self.skip_story_action()


    def chapter_3(self):
        """엄폐 및 탱크"""
        print(">>> Chapter 3: 엄폐 및 탱크")
        
        # 엄폐 튜토리얼 진행
        hides = [
            self.hide_01, self.hide_02, self.hide_03,
            self.hide_04, self.hide_05
        ]
        for h in hides:
            self.step(h)
        
        # 엄폐 튜토리얼 후 스토리 스킵            
        self.skip_story_action()
        self.skip_story_action()
        self.skip_story_action()
        self.skip_story_action()

            
        # 탱크 튜토리얼 진행
        tanks = [
            self.tank_01, self.tank_02, self.tank_03, self.tank_04
        ]
        for t in tanks:
            self.step(t)
        
        sleep(1.0)
        touch((1410, 328))                    
        self.step(self.tutorial_complete_btn)

        # 탱크 튜토리얼 후 스토리 스킵
        self.skip_story_action()
        wait(self.tank_06)
        self.skip_story_action()

        sleep(5.0)
        touch((1410, 328))    
        self.step(self.tank_07)

    def chapter_4(self):
        """가챠 튜토리얼"""
        print(">>> Chapter 4: 가챠")
        
        # 가챠 뽑기 진행
        gacha_01 = [
            self.gacha_01, self.gacha_02, self.gacha_03,
            self.gacha_04, self.gacha_05, self.gacha_06,
            self.gacha_07, self.gacha_07
        ]

        for g in gacha_01:
            self.step(g)
            
        # 3성 연속 획득 가능성에 대한 대응(만일 2개 이상 획득 시 같은 코드 한 줄 더 추가)
        self.step_pass(self.gacha_08)
        self.step_pass(self.gacha_08)
            
        # 뽑기 재진행
        gacha_02 = [
            self.gacha_09, self.gacha_10, self.gacha_11,
            self.gacha_12, self.gacha_13, self.gacha_14,
            self.gacha_15, self.gacha_16, self.gacha_17,
            self.gacha_18, self.gacha_19, self.gacha_20,
            self.gacha_21, self.gacha_22, self.gacha_23,
            self.gacha_24
        ]
        for g in gacha_02:
            self.step(g)
            
        # 다시하기 후 스킵
        self.step(self.gacha_07)
        self.step(self.gacha_07)
        
        # 3성 연속 획득 가능성에 대한 대응(만일 2개 이상 획득 시 같은 코드 한 줄 더 추가)
        self.step_pass(self.gacha_08)
        self.step_pass(self.gacha_08)
        
        
        # 뽑기 최종 선택 및 다음 튜토리얼 진입
        gacha_03 = [
            self.gacha_22, self.gacha_23, self.gacha_25
        ] 
        for g in gacha_03:
            self.step(g)

        sleep(2.0)
        touch((1140, 815))
        
        gacha_04 = [
            self.gacha_27, self.gacha_28, self.gacha_29
        ]
        for g in gacha_04:
            self.step(g)

    def chapter_5(self):
        """임무 튜토리얼"""
        print(">>> Chapter 5: 임무")

        # 임무 튜토리얼 진행
        missions_01 = [
            self.mission_01, self.mission_02, self.mission_03, self.mission_04,
            self.mission_05, self.mission_06, self.mission_07, self.mission_08,
            self.mission_09, self.mission_10, self.mission_11, self.mission_12,
            self.mission_13, self.mission_14, self.mission_15, self.mission_16,
            self.mission_17, self.mission_18, self.mission_19, self.mission_20,
            self.mission_21, self.mission_22, self.mission_23, self.mission_24,
            self.mission_25, self.mission_26, self.mission_27, self.mission_28,
            self.mission_29, self.mission_30, self.mission_31, self.mission_32,
            self.mission_33, self.mission_34, self.mission_35, self.mission_36,
        ]
        for m in missions_01:
            self.step(m)

        wait(self.mission_37)
        sleep(2.0)
        touch((1688, 965))

        missions_02 = [    
            self.mission_38, self.mission_39, self.mission_40,
            self.mission_41, self.mission_42
        ]
        for m in missions_02:
            self.step(m)

    def chapter_6(self):
        """출석체크 및 로비 + 모모톡 튜토리얼"""
        print(">>> Chapter 6: 로비 and 모모톡")
        
        # 출석 체크
        self.step(self.daily_01)
        self.step(self.daily_02)
        
        # 로비 및 모모톡 튜토리얼 진행(최종)
        lobbies = [
            self.lobby_01, self.lobby_02, self.lobby_03,
            self.lobby_04, self.lobby_05, self.lobby_06,
            self.lobby_07, self.lobby_08, self.lobby_09,
            self.lobby_10, self.lobby_11, self.lobby_12,
            self.lobby_13, self.lobby_14, self.lobby_15,
            self.lobby_16
        ]
        
        for l in lobbies:
            self.step(l)
            
