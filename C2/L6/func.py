def standardize(s):
    s=s.strip()
    while " " in s:
        s = s.replace(" ","")
    return s.lower()