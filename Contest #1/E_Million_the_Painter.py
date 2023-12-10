def myfunc():
    m = int(input())
    N = input()
    #  Million The painter

    if "CC" in N or  "YY" in N or "MM" in N:
        return "No"
    elif N[0] == "?" or N[len(N)-1] == "?":
        return "Yes"
    elif ("??" in N) or ("C?C" in N) or ("Y?Y" in N) or ("M?M" in N):
        return "Yes"
    else:
        print("No")



print(myfunc())
