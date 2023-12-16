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
    "생물의 다양성"
]

성취기준: List[str] = [
    "[9과01-01] 지구계의 구성 요소를 알고, 지권의 층상 구조와 그 특징을 설명할 수 있다.",
    "[9과01-02] 지각을 이루는 암석을 생성 과정에 따라 분류할 수 있으며, 암석의 순환 과정을 설명할 수 있다."
]

학년도: List[str] = [
    "2022", 
    "2023", 
    "2024"
]

학기: List[str] = [
    "1학기", 
    "2학기", 
]

학년: List[str] = [
    "1학년", 
    "2학년", 
    "3학년", 
]

교과: List[str] = [
    "국어", 
    "과학",
    "",
]

class SubjecState(State):
    table_col: list = []
    table_data: list = []
    table_null: list = []

    # form_data: dict = {}
    # table_temp: dict = {}
    # table_temp2: list = []

    # table_col = [
    #     { "title": "학년도", "type": "str", "width": "80px" },
    #     { "title": "학기", "type": "str" , "width": "80px" },
    #     { "title": "학년", "type": "str" , "width": "80px" },
    #     { "title": "교과", "type": "str" , "width": "80px" },
    #     { "title": "단원(영역)", "type": "str" , "width": "160px" },
    #     { "title": "성취기준", "type": "str" , "width": "1320px" },
    # ]
    table_col = [
        { "title": "학년도", "type": "str", "width": 80 },
        { "title": "학기", "type": "str" , "width": 80 },
        { "title": "학년", "type": "str" , "width": 80 },
        { "title": "교과", "type": "str" , "width": 80 },
        { "title": "단원(영역)", "type": "str" , "width": 160 },
        # { "title": "성취기준", "type": "str" , "width": 800 },
        { "title": "성취기준", "type": "str" , "width": 1240 },
    ]
    table_null = ["","","","","",""]

    def handle_register(self, form_data: dict):
        """Handle the form append."""
        # self.form_data = form_data
        row = [form_data['학년도'], 
               form_data['학기'], 
               form_data['학년'], 
               form_data['교과'], 
               form_data['단원'], 
               form_data['성취기준']]
        self.table_data.append(row)

    def handle_delete(self, form_data: dict):
        """Handle the form delete."""
        # self.form_data = dict.copy(form_data)        
        # if form_data["current"] is None:
        #     for k in form_data["rows"]["items"]:
        #         s = k.pop(0)
        #         e = k.pop(0)
        #         while s < e:
        #             self.table_data.pop(s)
        #             s += 1
        while True:
            try:
                self.table_data.remove(self.table_null)
            except ValueError:
                break

    def handle_clear(self):
        while True:
            try:
                self.table_data.remove(self.table_null)
            except ValueError:
                break        

    def handle_update(self, pos, new_vaule):
        """Handle the form update."""
        col, row = pos
        # self.table_temp = new_vaule        
        self.table_data[row][col] = new_vaule["data"]

    def handle_sort(self):
        """Handle the form sort."""
        self.table_data.sort(key = lambda x:x[1])

@webpage(path="/input/subject_concept")
def subject_concept():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading("교과 성취 기준", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.text("교과 성취 기준을 구성하기 위해 학년도, 학기, 학년, 교과, 단원을 입력하세요.", color=tc["docs"]["body"]),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            rx.form(
                rx.vstack(                    
                    rx.select(
                        학년도,
                        placeholder="학년도",
                        id="학년도",
                        color_schemes="twitter",
                    ),
                    rx.select(
                        학기,
                        placeholder="학기",
                        id="학기",
                        color_schemes="twitter",
                    ),
                    rx.select(
                        학년,
                        placeholder="학년",
                        id="학년",
                        color_schemes="twitter",
                    ),
                    rx.select(
                        교과,
                        placeholder="교과",
                        id="교과",
                        color_schemes="twitter",
                    ),
                    rx.select(
                        단원,
                        placeholder="단원 선택",
                        id="단원",
                        color_schemes="twitter",
                    ),
                    rx.select(
                        성취기준,
                        placeholder="성취기준 선택",
                        id="성취기준",
                        color_schemes="twitter",
                    ),
                    rx.button("등록", type_="submit"),
                ),
                on_submit=SubjecState.handle_register,
            ),
            rx.box(
                rx.divider(),
                rx.heading("결과", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                # rx.text("Delete: " + SubjecState.form_data.to_string(), color=tc["docs"]["body"]),
                # rx.text("Select: " + SubjecState.table_temp.to_string(), color=tc["docs"]["body"]),
                # rx.text("Table: " + SubjecState.table_data.to_string(), color=tc["docs"]["body"]),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            rx.box(
                rx.button("빈 줄 삭제", on_click=SubjecState.handle_clear),
                text_align="left",
                width="100%",
            ),
            rx.box(
                rx.data_editor(
                    columns=SubjecState.table_col,
                    data=SubjecState.table_data,
                    row_height=40,
                    height="100vh",
                    smooth_scroll_x=True,
                    smooth_scroll_y=True,
                    draw_focus_ring=True,
                    get_cell_for_selection=True,
                    on_paste=True,
                    row_markers="both",
                    freeze_columns=5,
                    # row_marker_width=40,
                    column_select="multiple",               
                    on_cell_edited=SubjecState.handle_update,
                    # on_delete=SubjecState.handle_delete,
                ),
                width="100%"
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
