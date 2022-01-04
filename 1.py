s = '()'
st = []
st.append(s[0]) 
for i in range(1, len(s)):
    print(s[i], st[len(st) - 1])
    if (s[i] == ')' and st[len(st) - 1] == '(') or (s[i] == ']' and st[len(st) - 1] == '[') or (s[i] == '}' and st[len(st) - 1] == '{'):
        st.pop()
    else:
        st.append(s[i])

if len(st) == 0:
    print("True")
else:
    print("False")