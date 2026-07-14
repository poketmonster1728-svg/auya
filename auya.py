import streamlit as st
start = st.text_input("모드 선택(암호화/복호화): ")
if start == "암호화":
    code = st.text_input("암호화 하고 싶은 단어: ")
    for i in code:
        a = ord(i)
        encoding = []
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
        st.code(answer)
elif start == "복호화":
    decoding = st.text_area("암호문을 입력하세요:\n")
    for h in decoding:
        mda = ""
        for h1 in h:
            if h1 == "아":
                mda += "0"
            elif h1 == "으":
                mda += "1"
            else:
                mda += "2"
        st.code(chr(int(mda,3)),end="")
else:
    st.code("ㄲㅈ")
