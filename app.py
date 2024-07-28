import streamlit as st

# button
st.write("# st.button() 사용 예시")
if st.button("노크하기"):
  st.write("여기 사람 있어요")

# slider
st.title("st.slider() 사용 예시")
age = st.slider("당신은 몇 살인가요?", min_value=0, max_value=130, value=25, step=1)
st.write(f"저는 {age}살 입니다.")

# selectbox
st.title("st.selectbox() 사용 예시")
option = st.selectbox("어떤 음식을 좋아하세요?", ("초밥", "피자", "치킨", "햄버거"), placeholder="선택하세요", index=None)
st.write("당신이 좋아하는 음식은", option, "입니다.")

# checkbox
st.title("st.checkbox() 사용 예시")
st.write("동의하시면 아래 내용에 체크해 주세요.")
checked = st.checkbox("동의합니다.")

if checked:
  st.write("동의해주셔서 감사합니다.")

# form (columns, form, text_input, text_area, form_submit_button)
st.title("st.form() 사용 예시 (st.columns()와 함께 사용)")
col1, col2 = st.columns(2) # 두 개의 컬럼 생성. 표현하고 싶은 내용을 열 데이터로 나눠 보여주고 싶을 떄 사용합니다.

with col1:
    text1 = st.text_input("form을 이용하지 않는 경우")
    text2 = st.text_area("form을 이용하지 않는 경우")
    st.write("1번 입력값: " + text1)
    st.write("2번 입력값: " + text2)

with col2:
    with st.form("form을 사용합니다"):
        text3 = st.text_input("form을 이용하는 경우")
        text4 = st.text_area("form을 이용하는 경우")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.write("1번 입력값: " + text3)
            st.write("2번 입력값: " + text4)
        else:
            st.write("1번 입력값: ")
            st.write("2번 입력값: ")

# write
st.title('동물 이미지 찾아주기 😎')

name = st.text_input('영어로 동물을 입력하세요')

if st.button('이미지 찾아보기'):
    st.image(f'https://edu.spartacodingclub.kr/random/?{name}')

# markdown
st.write("""
# 리팩터링 목록

| 리팩터링 기법 | 리팩터링 기법(영문) | 참조 |
| --- | --- | --- |
| 값을 참조로 바꾸기 | Change Value to Reference | 9.5 |
| 객체 통째로 넘기기 | Preserve Whole Object | 11.4 |
| 계층 합치기 | Collapse Hierarchy | 12.9 |
| 기본형을 객체로 바꾸기 | Replace Primitive with Object | 7.3 |
| 단계 쪼개기 | Split Phase | 6.11 |
| 레코드 캡슐화하기 | Encapsulate Record | 7.1 |
| 매개변수 객체 만들기 | Introduce Parameter Object | 6.8 |
| 매개변수를 질의 함수로 바꾸기 | Replace Parameter with Query | 11.5 |
| 매직 리터럴 바꾸기 | Replace Magic Literal | 9.6 |
| 메서드 내리기 | Push Down Method | 12.4 |
| 메서드 올리기 | Pull Up Method | 12.1 |
| 명령을 함수로 바꾸기 | Replace Command with Function | 11.10 |
| 문장 슬라이드하기 | Slide Statements | 8.6 |
| 문장을 함수로 옮기기 | Move Statements into Function | 8.3 |
| 문장을 호출한 곳으로 옮기기 | Move Statements to Callers | 8.4 |
| 반복문 쪼개기 | Split Loop | 8.7 |
| 반목문을 파이프라인으로 바꾸기 | Replace Loop with Pipeline | 8.8 |
| 변수 이름 바꾸기 | Rename Variable | 6.7 |
| 변수 인라인하기 | Inline Variable | 6.4 |
| 변수 쪼개기 | Split Variable | 9.1 |
| 변수 추출하기 | Extract Variable | 6.3 |
| 변수 캡슐화하기 | Encapsulate Variable | 6.6 |
| 생성자 본문 올리기 | Pull Up Constructor Body | 12.3 |
| 생성자를 팩터리 함수로 바꾸기 | Replace Constructor with Factory Method | 11.8 |
| 서브 클래스 제거하기 | Remove Subclass | 12.7 |
| 서브클래스 위임으로 바꾸기 | Replace Subclass with Delegate | 12.10 |
| 세터 제거하기 | Remove Setter Method | 11.7 |
| 수정된 값 반환하기 | Return Modified Value | 11.11 |
| 슈퍼클래스 추출하기 | Extract Superclass | 12.8 |
| 슈퍼클래스를 위임으로 바꾸기 | Replace Superclass with Delegate | 12.11 |
| 알고리즘 교체하기 | Substitue Algorithm | 7.9 |
| Assertion 추가하기 | Introduce Assertion | 10.6 |
| 여러 함수를 변환 함수로 묶기 | Combine Functions into Transfrom | 6.10 |
| 여러 함수를 클래스로 묶기 | Combine Functions into Class | 6.9 |
| 예외를 사전확인으로 바꾸기 | Replace Exception with Precheck | 11.13 |
| 오류 코드를 예외로 바꾸기 | Replace Error Code with Exception | 11.12 |
| 위임 숨기기 | Hide Delegate | 7.7 |
| 인라인 코드를 함수 호출로 바꾸기 | Replace Inline Code with Function Call | 8.5 |
| 임시 변수를 질의 함수로 바꾸기 | Replace Temp with Query | 7.4 |
| 제어 플래그를 탈출문으로 바꾸기 | Replace Control Flag with Break | 10.7 |
| 조건문 분해하기 | Decompose Conditional | 10.1 |
| 조건문 로직을 다형성으로 바꾸기 | Replace Conditional with Polymorphism | 10.4 |
| 조건식 통합하기 | Consolidate Conditional Expression | 10.2 |
| 죽은 코드 제거하기 | Remove Dead Code | 8.9 |
| 중개자 제거하기 | Remove Middle Man | 7.8 |
| 중첩 조건문을 보호 구문으로 바꾸기 | Replace Nested Conditional with Guard Clauses | 10.3 |
| 질의 함수를 매개변수로 바꾸기 | Replace Query With Parameter | 11.6 |
| 질의 함수와 변경 함수 분리하기 | Separate Query From Modifier | 11.1 |
| 참조를 값으로 바꾸기 | Change Reference to Value | 9.4 |
| 컬렉션 캡슐화하기 | Encapsulate Collection | 7.2 |
| 클래스 인라인하기 | Inline Class | 7.6 |
| 클래스 추출하기 | Extract Class | 7.5 |
| 타입 코드를 서브클래스로 바꾸기 | Replace Type Code with Subclasses | 12.6 |
| 특이 케이스 추가하기 | Introduce Special Case | 10.5 |
| 파생 변수를 질의 함수로 바꾸기 | Replace Derived Variable with Query | 9.3 |
| 플래그 인수 제거하기 | Remove Flag Argument | 11.3 |
| 필드 내리기 | Push Down Field | 12.5 |
| 필드 올리기 | Pull Up Field | 12.2 |
| 필드 옮기기 | Move Field | 8.2 |
| 필드 이름 바꾸기 | Rename Field | 9.2 |
| 함수 매개변수화하기 | Parameterize Function | 11.2 |
| 함수 선언 바꾸기 | Change Function Declaration | 6.5 |
| 함수 옮기기 | Move Function | 8.1 |
| 함수 인라인하기 | Inline Function | 6.2 |
| 함수 추출하기 | Extract Function | 6.1 |
| 함수를 명령으로 바꾸기 | Replace Function with Command | 11.9 |

# 악취 제거 기법

| 악취 | 탈취용 리팩터링 기법 |
| --- | --- |
| 가변 데이터 | 변수 캡슐화하기, 변수 쪼개기, 문장 슬라이드하기, 함수 추출하기, 질의 함수와 변경 함수 분리하기, 세터 제거하기, 파생 변수를 질의 함수로 바꾸기, 여러 함수를 클래스로 묶기, 여러 함수를 변환 함수로 묶기, 참조를 값으로 바꾸기 |
| 거대한 클래스 | 클래스 추출하기, 슈퍼클래스 추출하기, 타입 코드를 서브클래스로 바꾸기 |
| 기능 편애 | 함수 옮기기, 함수 추출하기 |
| 기본형 집착 | 기본형을 객체로 바꾸기, 타입 코드를 서브클래스로 바꾸기, 조건부 로직을 다형성으로 바꾸기, 클래스 추출하기, 매개변수 객체 만들기 |
| 기이한 이름 | 함수 선언 바꾸기, 변수 이름 바꾸기, 필드 이름 바꾸기 |
| 긴 매개변수 목록 | 매개변수를 질의 함수로 바꾸기, 객체 통째로 넘기기, 매개변수 객체 만들기, 플래그 인수 제거하기, 여러 함수를 클래스로 묶기 |
| 긴 함수 | 함수 추출하기, 임시 변수를 질의 함수로 바꾸기, 매개변수 객체 만들기, 객체 통째로 넘기기, 함수를 명령으로 바꾸기, 조건문 분해하기, 조건부 로직을 다형성으로 바꾸기, 반복문 조깨기 |
| 내부자 거래 | 함수 옮기기, 필드 옮기기, 위임 숨기기, 서브클래스를 위임으로 바꾸기, 슈퍼클래스를 위임으로 바꾸기 |
| 데이터 뭉치 | 클래스 추출하기, 매개변수 객체 만들기, 객체 통째로 넘기기 |
| 데이터 클래스 | 레코드 캡슐화하기, 세터 제거하기, 함수 옮기기, 함수 추출하기, 단계 쪼개기 |
| 뒤엉킨 변경 | 단계 쪼개기, 함수 옮기기, 함수 추출하기, 클래스 추출하기 |
| 메시지 체인 | 위임 숨기기, 함수 추출하기, 함수 옮기기 |
| 반복되는 switch문 | 조건부 로직을 다형성으로 바꾸기 |
| 반복문 | 반복문을 파이프라인으로 바꾸기 |
| 산탄총 수술 | 함수 옮기기, 필드 옮기기, 여러 함수를 클래스로 묶기, 여러 함수를 변환 함수로 묶기, 단계 쪼개기, 함수 인라인하기, 클래스 인라인하기 |
| 상속 포기 | 메서드 내리기, 필드 내리기, 서브 클래스를 위임으로 바꾸기, 슈퍼클래스를 위임으로 바꾸기 |
| 서로 다른 인터페이스의 대안 클래스들 | 함수 선언 바꾸기, 함수 옮기기, 슈퍼클래스 추출하기 |
| 성의 없는 요소 | 함수 인라인하기, 클래스 인라인하기, 계층 합치기 |
| 임시 필드 | 클래스 추출하기, 함수 옮기기, 특이 케이스 추가하기 |
| 전역 데이터 | 변수 캡슐화하기 |
| 주석 | 함수 추출하기, 함수 선언 바꾸기, Assertion 추가하기 |
| 중개자 | 중개자 제거하기, 함수 인라인하기, 서브클래스 위임으로 바꾸기, 슈퍼클래스 위임으로 바꾸기 |
| 중복 코드 | 함수 추출하기, 문장 슬라이드하기, 메서드 올리기 |
| 추측성 일반화 | 계층  합치기, 함수 인라인하기, 클래스 인라인하기, 함수 선언 바꾸기, 죽은 코드 제거하기 |
""")