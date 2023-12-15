import pandas as pd
import numpy as np
from unicodedata import normalize

def parsing_data(filename:str):
    df = pd.read_excel(filename,'성취기준')
    values = df.values
    rownum = values.shape[0]
    lectures = list(df.columns)[1::2]

    temp = []

    for j,lecture in enumerate(lectures):
        lecture_dict = {"교과": lecture, "단원": []}
        partname = ""

        part_dict = lecture_dict["단원"]

        for i in range(rownum):
            val = values[i, j * 2:j * 2 + 2]


            if pd.isna(val[0]) and pd.isna(val[1]):
                continue
            elif pd.isna(val[0]):
                part_dict[-1]["성취기준"].append(normalize("NFKD",val[1]))
            else:
                partname = val[0]
                part_dict.append({"단원명":partname, "성취기준":[normalize("NFKD",val[1])]})

        temp.append(lecture_dict)
    return temp



if __name__ == "__main__":
    #mongodb + bunnet init
    from pcweb.backend.mongodb import init
    init()

    #엑셀파일 파싱
    data = parsing_data('./피드백지 구상_231208.xlsx')

    # mongo db에 있는 지 확인
    from pcweb.backend.SubjectModel import SubjectModel
    for d in data:
        if SubjectModel.find(SubjectModel.label == d['교과']).count() == 0:
            sm = SubjectModel.parse_obj(d)
            sm.create()
    #표현
    from rich import print
    for sm in SubjectModel.find(SubjectModel.label == "수학").to_list():
        print(sm)