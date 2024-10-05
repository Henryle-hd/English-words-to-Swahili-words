import data
data=data.get_data()

def ksw_to_eng(word:str):
    """Translate a Swahili word into to English word, Print and return the meaning"""
    for dic in data:
        if word==dic["ksw"].replace(" ",""):
            meaning=f"\x1b[36m{dic["eng"].upper()}\x1b[0m"
            print_box(word.upper(),meaning,"Ksw-Eng")
            for key,value in dic.items():
                if key =="id":
                    continue
                if key =="ksw" or key =="eng":
                    continue
                if key =="type":
                    print("\n\x1b[32mAina: \x1b[0m")
                if key =="example":
                    print("\n\x1b[32mMifano: \x1b[0m")
                    for key, value in value.items():
                        print(key,": ",value)
                else:
                    print(key,": ",value)
    # else:
    #     print("\x1b[31m-Neno halikuonekana\x1b[0m")
            return meaning

def eng_to_ksw(word:str):
    """Translate a English word into to Swahili word, print and return the meaning"""
    for dic in data:
        if word== dic["eng"].replace(" ",""):
            meaning=f"\x1b[36m{dic["ksw"].upper()}\x1b[0m"
            print_box(word.upper(),meaning,"Eng-Ksw")
            for key,value in dic.items():
                if key =="id":
                    continue
                if key =="eng" or key =="ksw":
                    continue
                if key =="type":
                    print("\n\x1b[32mTypes: \x1b[0m")
                if key =="example":
                    print("\n\x1b[32mExample: \x1b[0m")
                    for key, value in value.items():
                        print(key,": ",value)
                else:
                    print(key,": ",value)
    # else:
    #     print("\x1b[31m-Word not found\x1b[0m")
            return meaning

def print_box(word,meaning,title):
    print(f"""
┌──────────────────────┐
│    📝 {title}        │
├──────────────────────┤
│  {word} -{meaning}   
└──────────────────────┘
""")
