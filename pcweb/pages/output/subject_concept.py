import reflex as rx
# import flexdown

from pcweb.base_state import State

from pcweb import styles
from pcweb.styles import text_colors as tc
# from pcweb.styles import colors as c
from pcweb.templates.webpage import webpage
# from pcweb.flexdown import component_map

from typing import List

단원: List[str] = [
    "지권의 변화", 
    "여러 가지 힘", 
    "생물의 다양성"]

성취기준: List[str] = [
    "[9과01-01] 지구계의 구성 요소를 알고, 지권의 층상 구조와 그 특징을 설명할 수 있다.",
    "[9과01-02] 지각을 이루는 암석을 생성 과정에 따라 분류할 수 있으며, 암석의 순환 과정을 설명할 수 있다."]

class SubjecOouputState(State):
    table_subject_concept_col: list = []
    table_subject_concept_data: list = []
    table_subject_criteria_col: list = []
    table_subject_criteria_data: list = []
    table_ability_criteria_col: list = []
    table_ability_criteria_data: list = []

    table_subject_concept_col = ["학년도", "학기", "학년", "교과", "단원(영역)", "성취기준"]
    table_subject_concept_data = [
        ["2023", "1", "1", "과학", 단원[0], 성취기준[0]],
        ["2023", "2", "1", "과학", 단원[1], 성취기준[1]],
        ["2023", "3", "1", "과학", 단원[1], 성취기준[1]],
    ]
    table_subject_criteria_col = ["주제", "목표", "평가요소", "수준", "채점기준"]
    table_subject_criteria_data = [
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],    
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "문제 상황 개선", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "문제 상황 개선", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "문제 상황 개선", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "문제 상황 개선", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 아이디어 투자 설명회", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 아이디어 투자 설명회", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 아이디어 투자 설명회", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],    
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 아이디어 투자 설명회", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 제안서 작성", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 제안서 작성", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 제안서 작성", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "처리 및 평가", "유니버셜디자인 제안서 작성", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],    
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],    
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "1", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "2", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "3", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],    
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "4", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
    ]
    table_ability_criteria_col = ["주제", "목표", "평가요소", "역량", "수준", "입력", "채점기준"]
    table_ability_criteria_data = [
        ["유니버셜디자인", "지식과이해", "여러 가지 힘 적용", "", "", "ㅁㅁㅁㅁㅁㅁㅁㅁㅁ"],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "지식정보처리 역량", "4", "ㅁㅁㅁ", "학습 기대치 이상의성과를 지속적으로 달성함."],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "지식정보처리 역량", "3", "ㅁㅁㅁ", "학습 기대치를 충족하여, 때로는 넘어서는 성과를 달성함."],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "지식정보처리 역량", "2", "ㅁㅁㅁ", "학습 기대치를 충족하기 위해 노력하고 있으며, 지속적으로 성장하고 있음."],
        ["유니버셜디자인", "탐구 및 설계", "힘을 이용한 문제 상황 선정", "지식정보처리 역량", "1", "ㅁㅁㅁ", "이해력 습득 초기 과정 중에 있거나 학습 기대치에 아직 도달하지 못함."],
    ]

@webpage(path="/output/subject_concept")
def subject_concept():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading("교과 성취 기준", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            rx.box(
                rx.data_table(
                data=SubjecOouputState.table_subject_concept_data,
                columns=SubjecOouputState.table_subject_concept_col,
                pagination=True,
                search=True,
                sort=True,
                ),
            ),
            rx.box(
                rx.heading("교과 채점 기준", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            rx.box(
                rx.data_table(
                data=SubjecOouputState.table_subject_criteria_data,
                columns=SubjecOouputState.table_subject_criteria_col,
                pagination=True,
                search=True,
                sort=True,
                ),
            ),
            rx.box(
                rx.heading("역량 채점 기준", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            rx.box(
                rx.data_table(
                data=SubjecOouputState.table_ability_criteria_data,
                columns=SubjecOouputState.table_ability_criteria_col,
                pagination=True,
                search=True,
                sort=True,
                ),
            ),
            align_items="stretch",
            min_height="80vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
        # max_width="960px",
        max_width="1800px",
    )    
