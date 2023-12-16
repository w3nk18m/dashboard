import reflex as rx
# import flexdown

from pcweb.base_state import State

from pcweb import styles
from pcweb.styles import text_colors as tc
# from pcweb.styles import colors as c
from pcweb.templates.webpage import webpage
# from pcweb.flexdown import component_map

from typing import List

class SubjecGradeState(State):
    table_col: list = []
    table_data: list = []
    table_null: list = []

    table_col = [
        { "title": "주제", "type": "str", "width": 120 },
        { "title": "목표", "type": "str" , "width": 120 },
        { "title": "평가요소", "type": "str" , "width": 120 },
        { "title": "수준", "type": "str" , "width": 120 },
        { "title": "채점기준", "type": "str" , "width": 1240 },
    ]
    table_null = ["","","","",""]

    def handle_register(self, form_data: dict):
        """Handle the form append."""
        # self.form_data = form_data
        for i in range(1, 5):
            row = [
                    form_data['주제'], 
                    form_data['목표'], 
                    form_data['평가요소'],
                    str(i),
                    "",
            ] 
            self.table_data.append(row)

    def handle_delete(self, form_data: dict):
        """Handle the form delete."""
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
        self.table_data[row][col] = new_vaule["data"]
        
    def handle_sort(self):
        """Handle the form sort."""
        self.table_data.sort(key = lambda x:x[1])

@webpage(path="/input/subject_grading_criteria")
def subject_grading_criteria():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading("교과 채점 기준", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.text("교과 채점 기준을 구성하기 위해 주제, 목표, 평가요소를 입력하세요.", color=tc["docs"]["body"]),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="주제", id="주제",
                    ),
                    rx.input(
                        placeholder="목표", id="목표",
                    ),
                    rx.input(
                        placeholder="평가요소", id="평가요소",
                    ),
                    rx.button("등록", type_="submit"),
                ),
                on_submit=SubjecGradeState.handle_register,
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
                rx.button("빈 줄 삭제", on_click=SubjecGradeState.handle_clear),
                text_align="left",
                width="100%",
            ),
            rx.box(
                rx.data_editor(
                    columns=SubjecGradeState.table_col,
                    data=SubjecGradeState.table_data,
                    row_height=40,
                    height="100vh",
                    smooth_scroll_x=True,
                    smooth_scroll_y=True,
                    draw_focus_ring=True,
                    get_cell_for_selection=True,
                    on_paste=True,
                    row_markers="both",
                    # freeze_columns=5,
                    # row_marker_width=40,
                    column_select="multiple",        
                    on_cell_edited=SubjecGradeState.handle_update,
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
