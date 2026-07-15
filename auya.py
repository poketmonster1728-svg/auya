import streamlit as st
start = st.text_input("모드 선택(암호화/복호화): ")
if start == "암호화":
    final = ""
    code = st.text_input("암호화 하고 싶은 단어: ")
    for i in code:
        a = ord(i)
        encoding = []
        if a == 0:
            encoding.append(a)
        while a > 0:
            encoding.append(a%3)
            a = a//3
        answer = ""
        encoding.reverse()
        for j in encoding:
            if j == 0:
                answer += "아"
            elif j == 1:
                answer += "으"
            else:
                answer += "야"
        final += answer + "\n"
    st.code(final)
elif start == "복호화":
    final2 = ""
    decoding = st.text_area("암호문을 입력하세요(입력 완료 시 입력창 바깥 클릭):\n").split("\n")
    for h in decoding:
        mda = ""
        for h1 in h:
            if h1 == "아":
                mda += "0"
            elif h1 == "으":
                mda += "1"
            else:
                mda += "2"
        final2 += chr(int(mda,3))
    st.code(final2)
else:
    st.code("ㄲㅈ")
