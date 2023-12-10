source = [
    "/*Test program */",
    "int main()",
    "{ ",
    "  // variable declaration ",
    "int a, b, c;",
    "/* This is a test",
    "   multiline  ",
    "   comment for ",
    "   testing */",
    "a = b + c;",
    "}",
]

s = "'".join(source)
ans = ""
l = 0

while l < len(s) - 1:
    r = l
    if s[l] == "/" and s[l + 1] == "*":
        r = l + 2
        while r < len(s) - 1 and s[r] != "*" and s[r + 1] != "/":
            r += 1
        r += 2
    elif s[l] == "/" and s[l + 1] == "/":
        r = l + 2
        while r < len(s) - 1 and s[r] != "'":
            r += 1
        r += 1

    ans += s[r]
    l = r
    l += 1
print(ans.split("'"))
