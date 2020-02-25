def func(s, p):
    if len(s) == 0:
        print(p)
    else:
        for i in range(len(s)):
            func(s[:i]+s[i+1:], p+s[i])


func("DOUSES", "")
