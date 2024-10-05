import func

def get_input():
    """
    Ask the user to choose if need to translate English word(s) to Swahili word(s) or Swahili word(s) to English word(s),
    take user input, validate and return it
    """
    print("""
┌──────────────────────┐
│    DICTIONARY        │
├──────────────────────┤
│  1. Eng-Ksw          │
│  2. Ksw-Eng          │
└──────────────────────┘
""")
    while True:
        ans=input("(1/2): ")
        if ans.isdigit():
            ans=int(ans)
            if ans>2 or ans<1:
                print("🚫Valid input is only (1/2)\n")
                continue
            break
        else:
            print("🚫Valid input is only (1/2)\n")
            continue
    return ans

def get_word(choice:int):
    """Receive Language choice, take,validate and return user input (word)"""
    while True:
        if choice==1:
            ans=input("\nEnter Word (q to quit, c to change Language): ").lower()
        else:
            ans=input("\nWeka Neno (q kuacha, c kubadili Lugha ): ").lower()
        if ans.isdigit():
            print("🚫Number not allowed\n")
            continue
        else:
            if ans=="q":
                ans=1
            elif ans=="c":
                ans=2
            else:
                ans=ans.split()
            break
    return ans

def main():
    """
    Take user choice,word(s), translate word(s). If user input is multiple words then example sentence of combined words will be printed
    """
    choice=get_input()
    while True:
        word=get_word(choice)
        if word==1:
            quit()
        elif word==2:
            main()
        meanings=[]
        for word in word:
            if choice==1:
                meaning=func.eng_to_ksw(word)
                meanings.append(meaning)
            else:
                meaning=func.ksw_to_eng(word)
                meanings.append(meaning)
        if len(meanings)>=2:
            print("\n\x1b[32mSentence\x1b[33m(May be not correct!):\x1b[0m")
            print("—",end="")
            for meaning in meanings:
                if meaning==None:
                    print("\x1b[31m__\x1b[0m",end="")
                else:
                    print(meaning.lower(),end="")
            print("")

