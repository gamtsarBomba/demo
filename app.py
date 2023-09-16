import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.write('1 + 1 = ', 2)
# # st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

# ### 5. 텍스트 출력
# ## Title
# st.title("Streamlit Tutorial")
# ## Header/Subheader
# st.header("This is header")
# st.subheader("This is subheader")
# ## Text
# st.text("Hello Streamlit! 이 글을 튜토리얼입니다.")

# ## Markdown syntax
# st.markdown("# This is a Markdown title")
# st.markdown("## This is a Markdown header")
# st.markdown("### This is a Markdown subheader")
# st.markdown("- item 1\n"
#             "    - item 1.1\n"
#             "    - item 1.2\n"
#             "- item 2\n"
#             "- item 3")
# st.markdown("1. item 1\n"
#             "   1. item 1.1\n"
#             "   2. item 1.2\n"
#             "2. item 2\n"
#             "3. item 3")

# ## Latex
# st.latex(r"Y = \alpha + \beta X_i")
# ## Latex-inline
# st.markdown(r"회귀분석에서 잔차식은 다음과 같습니다 $e_i = y_i — \hat{y}_i$")

# ### 6. 메세지와 에러메세지, 예외처리 메시지
# ## Error/message text
# st.success("Successful")
# st.info("Information!")
# st.warning("This is a warning")
# st.error("This is an error!")
# st.exception("NameError('Error name is not defined')")

# ### 7. 데이터 로딩
# ## Load data
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# # GitHub 에서 아이리스 데이터 다운로드
# url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
# iris_df = pd.read_csv(url)

# ### 8. 데이터프레임과 테이블 출력
# ## Return table/dataframe
# # table
# st.table(iris_df.head())
# # dataframe
# st.dataframe(iris_df)
# st.write(iris_df)
# st.markdown("* * *")

# ### 9. 위젯
# ## Checkbox
# if st.checkbox("Show/Hide"):
#     st.write("체크박스가 선택되었습니다.")
    
# ## Radio button
# status = st.radio("Select status.", ("Active", "Inactive"))
# if status == "Active":
#     st.success("활성화 되었습니다.")
# else:
#     st.warning("비활성화 되었습니다.")
    
# ## Select Box
# occupation = st.selectbox("직군을 선택하세요.", [
#     "Backend Developer",
#     "Frontend Developer",
#     "ML Engineer",
#     "Engineer",
#     "Database Administrator",
#     "Scientist",
#     "Data Analyst",
#     "Security Engineer"
# ])
# st.write(" 직군은 ", occupation, " 입니다.")

# ## MultiSelect
# location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
#                         (
#                         "운동",
#                         "IT 기기",
#                         "브이로그",
#                         "먹방",
#                         "반려동물",
#                         "맛집 리뷰"
#                         )
# )
# st.write(len(location), "가지를 선택했습니다.")

# ## Slider
# level = st.slider("레벨을 선택하세요.", 1, 5)

# ## Buttons
# if st.button("About"):
#     st.text("Streamlit 을 이용한 튜토리얼입니다.")
    
# # Text Input
# first_name = st.text_input("Enter Your First Name", "Type Here ...")
# if st.button("Submit", key='first_name'):
#     result = first_name.title()
#     st.success(result)
# # Text Area
# message = st.text_area("메세지를 입력하세요.", "Type Here ...")
# if st.button("Submit", key='message'):
#     result = message.title()
#     st.success(result)
    
# ## Date Input
# import streamlit as st
# import datetime
# today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
# the_time = st.time_input("시간을 입력하세요.", datetime.time())

# ## Display Raw Code — one line
# st.subheader("Display one-line code")
# st.code("import numpy as np")
# # Display Raw Code — snippet
# st.subheader("Display code snippet")
# with st.echo():
#     # 여기서부터 아래의 코드를 출력합니다.
#     import pandas as pd
#     df = pd.DataFrame()

# ## Display JSON
# st.subheader("Display JSON")
# st.json({"name" : "민수", "gender": "male", "Age": 29})

## Sidebars
# st.sidebar.header("사이드바 메뉴")
# st.sidebar.selectbox("메뉴를 선택하세요.",
#                     ["데이터",
#                     "EDA",
#                     "코드"])

# # GitHub 에서 아이리스 데이터 다운로드
# url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
# iris_df = pd.read_csv(url)
# ## Plotting
# st.subheader("Matplotlib 으로 차트 그리기")
# fig, ax = plt.subplots()
# ax = iris_df[iris_df['species']=='virginica']['petal_length'].hist()
# st.pyplot(fig)

# st.title("Registeration form")
# first, last = st.columns(2)
# first.text_input("First Name")
# last.text_input("Last Name")
# email, mob = st.columns([3, 1]) # 비율이 중요
# email.text_input("Email ID")
# mob.text_input("Mob Number")
# user, pw, pw2 = st.columns(3)
# user.text_input("Username")
# pw.text_input("Password", type="password")
# pw2.text_input("Retype your password", type="password")
# ch, bl, sub = st.columns(3)
# ch.checkbox("I Agree")
# sub.button("Submit")

# import time
# @st.cache_data
# def fetch_and_clean_data(url):
#  # Fetch data from URL here, and then clean it up.
#     data = pd.read_csv(url)
#     return data
# DATA_URL_1 = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
# DATA_URL_2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/raw/titanic.csv"
# # 시작 시간 기록
# start_time = time.time()
# d1 = fetch_and_clean_data(DATA_URL_1)
# # Actually executes the function, since this is the first time it was encountered.
# # 종료 시간 기록
# end_time = time.time()
# # 실행 시간 계산
# execution_time = end_time - start_time
# # 실행 시간 출력
# st.write(f"총 실행 시간: {execution_time:.6f} 초")
# st.write(d1.head())
# # 시작 시간 기록
# start_time = time.time()
# d2 = fetch_and_clean_data(DATA_URL_1)
# # Does not execute the function. Instead, returns its previously computed
# # value. This means that now the data in d1 is the same as in d2.
# # 종료 시간 기록
# end_time = time.time()
# # 실행 시간 계산
# execution_time = end_time - start_time
# # 실행 시간 출력
# st.write(f"총 실행 시간: {execution_time:.6f} 초")
# st.write(d2.head())
# # 시작 시간 기록
# start_time = time.time()
# d3 = fetch_and_clean_data(DATA_URL_2)
# # This is a different URL, so the function executes.
# # 종료 시간 기록
# end_time = time.time()
# # 실행 시간 계산
# execution_time = end_time - start_time
# # 실행 시간 출력
# st.write(f"총 실행 시간: {execution_time:.6f} 초")
# st.write(d3.head())

### 11. session

### 12. upload files
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

### 13. 예제 - 프로파일링
import platform
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')
# 스트림릿 앱 생성
st.title("데이터 프로파일링 실습")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("데이터 파일 업로드", type=["csv", "xlsx"])
if uploaded_file is not None:
    # 업로드한 파일을 DataFrame 으로 변환
    df = pd.read_csv(uploaded_file) # 엑셀 파일일 경우 pd.read_excel 사용
 
    # 데이터 프로파일링
    st.header("데이터 미리보기")
    st.write(df.head())
    st.header("기본 정보")
    st.write("행 수:", df.shape[0])
    st.write("열 수:", df.shape[1])
    st.header("누락된 값")
    missing_data = df.isnull().sum()
    st.write(missing_data)
    st.header("중복된 행 수")
    duplicated_rows = df.duplicated().sum()
    st.write(duplicated_rows)
    st.header("수치형 데이터 기술 통계량")
    numerical_stats = df.describe()

    st.write(numerical_stats)
    st.header("이상치 탐지 (상자 그림)")
    plt.figure(figsize=(10, 6))
    plt.boxplot(df.select_dtypes(include=['number']).values)
    plt.xticks(range(1, len(df.columns) + 1), df.columns, 
    rotation=45)
    plt.title("Outlier detection (box plot)")
    st.pyplot(plt)
    st.header("데이터 분포 시각화")
    column_to_plot = st.selectbox("열 선택", df.columns)
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_to_plot], bins=20, edgecolor='k')
    plt.xlabel(column_to_plot)
    plt.ylabel("빈도")
    plt.title(f"{column_to_plot} Data Distribution")
    st.pyplot(plt)
    
### 14. 예제 - IRIS 데이터 시각화
