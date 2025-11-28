# %%
# diameter = 10
# pi = 3.1416
# circle = {
#     'diameter': diameter,
#     'radius': (radius := diameter / 2),
#     'area': pi * radius ** 2,
#     'circumference': 2 * pi * radius
# }
# # test
# diameter = 10
# pi = 3.1416
# radius = diameter / 2
# circle = {
#     'diameter': diameter,
#     'radius': radius,
#     'area': pi * radius ** 2,
#     'circumference': 2 * pi * radius
# }
# circle

# pytania
# losowenie pytan z puli
# gra
# Millionaires.py


questions = [
    {
        "text": "Pytanie 1.: W ilu stopnia Celsjusza woda wrze?",
        "answers": {
            "a": "90",
            "b": "95",
            "c": "100",
            "d": "105",
        },
        "correct": "c",
        "prize": 1000,
        "guaranteed": False,
        "fifty_fifty": ("a", "c"),  # zostaną a i c, c jest poprawne
    },
    {
        "text": "Pytanie 2.: W którym roku miała miejsce bitwa pod Waterloo?",
        "answers": {
            "a": "1795",
            "b": "1815",
            "c": "1813",
            "d": "1805",
        },
        "correct": "b",
        "prize": 2000,
        "guaranteed": True,  # gwarantowane 2 000 zł po poprawnej odpowiedzi
        "fifty_fifty": ("a", "b"),  # jak w Twoim Case 2
    },
    {
        "text": "Pytanie 3.: W którym roku miała miejsce bitwa pod Grunwaldem?",
        "answers": {
            "a": "996",
            "b": "1515",
            "c": "1410",
            "d": "1485",
        },
        "correct": "c",
        "prize": 5000,
        "guaranteed": False,
        "fifty_fifty": ("a", "c"),
    },
    {
        "text": "Pytanie 4.: W którym roku wybuchła II wojna światowa?",
        "answers": {
            "a": "1945",
            "b": "1933",
            "c": "1936",
            "d": "1939",
        },
        "correct": "d",
        "prize": 10000,
        "guaranteed": False,
        "fifty_fifty": ("c", "d"),
    },
    {
        "text": "Pytanie 5.: W którym roku zakończyła się II wojna światowa?",
        "answers": {
            "a": "1945",
            "b": "1933",
            "c": "1936",
            "d": "1939",
        },
        "correct": "a",
        "prize": 15000,
        "guaranteed": False,
        "fifty_fifty": ("a", "d"),
    },
    {
        "text": "Pytanie 6.: W którym roku wybuchła I wojna światowa?",
        "answers": {
            "a": "1918",
            "b": "1910",
            "c": "1914",
            "d": "1919",
        },
        "correct": "c",
        "prize": 25000,
        "guaranteed": False,
        "fifty_fifty": ("c", "a"),
    },
    {
        "text": "Pytanie 7.: W którym rozpoczęła się wojna secesyjna w Stanach Zjednoczonych?",
        "answers": {
            "a": "1861",
            "b": "1870",
            "c": "1850",
            "d": "1820",
        },
        "correct": "d",
        "prize": 50000,
        "guaranteed": True,
        "fifty_fifty": ("a", "c"),
    },
    {
        "text": "Pytanie 8.: W którym roku miała miejsce bitwa pod Austerlitz?",
        "answers": {
            "a": "1812",
            "b": "1809",
            "c": "1805",
            "d": "1801",
        },
        "correct": "b",
        "prize": 10000,
        "guaranteed": False,
        "fifty_fifty": ("b", "d"),
    },
    {
        "text": "Pytanie 9.: W jakich latach trwała Wojna Krymska?",
        "answers": {
            "a": "1850-1855",
            "b": "1853-1856",
            "c": "1860-1865",
            "d": "1870-1871",
        },
        "correct": "b",
        "prize": 500000,
        "guaranteed": False,
        "fifty_fifty": ("b", "c"),
    },
    {
        "text": "Pytanie 10.: W jakich latach trwała bitwa o Anglię?",
        "answers": {
            "a": "1940",
            "b": "1942",
            "c": "1941",
            "d": "1939",
        },
        "correct": "a",
        "prize": 1000000,
        "guaranteed": True,
        "fifty_fifty": ("a", "b"),
    },

]
