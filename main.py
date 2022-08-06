import plotly.graph_objects as go
import csv

colorScheme = dict(
    red='rgba(225,87,89, 0.8)',
    orange='rgba(242,142,43, 0.8)',
    yellow='rgba(241,206,99, 0.8)',
    green='rgba(89,161,79, 0.8)',
    blue='rgba(78,121,167, 0.8)',
    gray='rgba(186,176,172, 0.8)'
)

dicts = [
    ["All"],
    ["Sent", "Not sent", "No contact"],
    ["Delivered", "Not delivered", "Blacklisted", "Unknown"],
    ["Read", "Ignored", "Not online", "Unknown"],
    ["No reaction", "Answered", "Promised", "Custom feedback", "Blacklisted"],
    ["Visited", "Not visited"],
    ["Edited", "Not edited"],
    ["Completed", "Not completed"]
]

values = [
            0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0,
            0, 0
        ]

with open('raw.csv', newline='') as csvfile:
    rawReader = csv.reader(csvfile, delimiter=',')
    for row in rawReader:
        initialIndex = 0
        for i in range(len(dicts[1])):
            if row[3]==dicts[1][i].lower():
                values[initialIndex+i]+=1

        initialIndex+=len(dicts[1])
        for i in range(len(dicts[2])):
            if row[4]==dicts[2][i].lower() and row[3]==dicts[1][0].lower():
                values[initialIndex+i]+=1

        initialIndex+=len(dicts[2])
        for i in range(len(dicts[3])):
            if row[5]==dicts[3][i].lower():
                if row[4]==dicts[2][0].lower():
                    values[initialIndex+i]+=1
                if row[4]==dicts[2][3].lower():
                    values[initialIndex+len(dicts[3])]+=1

        initialIndex += len(dicts[3])+1
        for i in range(len(dicts[4])):
            if row[6]==dicts[4][i].lower():
                if row[5] == dicts[3][0].lower():
                    values[initialIndex+i] += 1
                if row[5] == dicts[3][3].lower():
                    values[initialIndex+i+ len(dicts[4])] += 1

        initialIndex+=2*len(dicts[4])
        for i in range(len(dicts[5])):
            if row[7]==dicts[5][i].lower():
                for j in range(len(dicts[4])):
                    if row[6] == dicts[4][j].lower():
                        values[initialIndex + j*len(dicts[5])+i] += 1

        initialIndex+=2*len(dicts[4])
        for i in range(len(dicts[6])):
            if row[8]==dicts[6][i].lower() and row[7] == dicts[5][0].lower():
                    values[initialIndex + i] += 1

        initialIndex += len(dicts[6])
        for i in range(len(dicts[7])):
            if row[9] == dicts[7][i].lower() and row[8] == dicts[6][0].lower():
                values[initialIndex + i] += 1

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=[item for stage_dict in dicts for item in stage_dict],
        color=[
            colorScheme['gray'],
            colorScheme['blue'], colorScheme['gray'], colorScheme['gray'],
            colorScheme['green'], colorScheme['yellow'], colorScheme['red'], colorScheme['gray'],
            colorScheme['green'], colorScheme['orange'], colorScheme['yellow'], colorScheme['gray'],
            colorScheme['gray'], colorScheme['yellow'], colorScheme['green'], colorScheme['green'], colorScheme['red'],
            colorScheme['green'], colorScheme['red'],
            colorScheme['green'], colorScheme['red'],
            colorScheme['green'], colorScheme['red']
        ]
    ),
    link=dict(
        source=[
            0, 0, 0,
            1, 1, 1, 1,
            4, 4, 4, 4, 7,
            8, 8, 8, 8, 8, 11, 11, 11, 11, 11,
            12, 12, 13, 13, 14, 14, 15, 15, 16, 16,
            17, 17,
            19, 19
        ],
        target=[
            1, 2, 3,
            4, 5, 6, 7,
            8, 9, 10, 11, 11,
            12, 13, 14, 15, 16, 12, 13, 14, 15, 16,
            17, 18, 17, 18, 17, 18, 17, 18, 17, 18,
            19, 20,
            21, 22
        ],
        value=values,
        color=[
            colorScheme['blue'], colorScheme['gray'], colorScheme['gray'],
            colorScheme['green'], colorScheme['yellow'], colorScheme['red'], colorScheme['gray'],
            colorScheme['green'], colorScheme['orange'], colorScheme['yellow'], colorScheme['gray'], colorScheme['gray'],

            colorScheme['gray'], colorScheme['yellow'], colorScheme['green'], colorScheme['green'], colorScheme['red'],
            colorScheme['gray'], colorScheme['yellow'], colorScheme['green'], colorScheme['green'], colorScheme['red'],

            colorScheme['green'], colorScheme['red'], colorScheme['green'], colorScheme['red'], colorScheme['green'],
            colorScheme['red'], colorScheme['green'], colorScheme['red'], colorScheme['green'], colorScheme['red'],

            colorScheme['green'], colorScheme['red'],
            colorScheme['green'], colorScheme['red']
        ]
    ))])

fig.update_layout(title_text="Project Nietzsche's Feedback Acquisition Flow", font_size=35)
fig.show()
