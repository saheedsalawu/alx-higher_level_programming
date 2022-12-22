#!/usr/bin/python3

st = '"My_little " o"yun" place"'
print(st)
i = st.index('"')
while i and i != (len(st) - 1):
    en = st[i:]
    st = st[:i] + '\' + en
    if (i + 2) < len(st):
        try:
            i = st.index('"', i + 3)
        except Exception:
            break

st = st.replace("_", " ")
print(st)

flt = "100.4994"
print(flt)
flt = float(flt)
print(flt)
