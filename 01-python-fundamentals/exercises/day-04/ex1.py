def analyze_string(text):
    if len(txt) > 0:
        print(f"{len(txt)}, {(txt[0])}, {txt[-1]}, {txt.upper()}, {txt.lower()}, {txt[::-1]}")
    else:
        print('empty string')

txt = str(input())
analyze_string(txt)