#%%
import time
import streamlit as st
import numpy as np
import pandas as pd
import base64
from PIL import Image
## code on terminal: streamlit run streamlit_py.py 

# 網頁配置設定(要寫在所有 Streamlit 命令之前，而且只能設定一次)
st.set_page_config(
    page_title="算錢錢",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="collapsed",
)
image = Image.open('wallpaper-1652017.jpg')
st.image(image, caption='Hello World')
## 加入標題
st.title('階段1: 總重量x區費率x0.9')

# # ## 設定背景





# 使用 Magic commands 指令，顯示 Markdown
df高屏台南 = pd.read_csv("高屏台南_csv.csv")
df雲嘉南 = pd.read_csv("雲嘉南_csv.csv")
df中彰投 = pd.read_csv("中彰投_csv.csv")
df桃竹苗 = pd.read_csv("桃竹苗_csv.csv")
df北基宜花東=pd.read_csv("北基宜花東_csv.csv")


area_select1 = ['高屏台南','雲嘉南','中彰投','桃竹苗','北基宜花東']



## 選地區
# st.sidebar.header("請選擇地區!")
# # select area
# areas = st.sidebar.selectbox(
#     "步驟一:選範圍",
#     options=area_select1,
# )
# areas = st.sidebar.selectbox(
areas = st.selectbox(
    "步驟一:選範圍",
    options=area_select1,
)


if areas == area_select1[0]:
    # get area data
    area_selection = df高屏台南['地區']
    first_area = df高屏台南
    
if areas == area_select1[1]:
    # get area data
    area_selection = df雲嘉南['地區']
    first_area = df雲嘉南
    
    
if areas == area_select1[2]:
    # get area data
    area_selection = df中彰投['地區']
    first_area = df中彰投
    
    
if areas == area_select1[3]:
    # get area data
    area_selection = df桃竹苗['地區']
    first_area = df桃竹苗    
    
    
if areas == area_select1[4]:
    # get area data
    area_selection = df北基宜花東['地區']
    first_area = df北基宜花東
    
# # select store
# 縣市區域 = st.sidebar.selectbox(
#     "步驟二: 選區名:",
#     options=area_selection)

縣市區域 = st.selectbox(
    "步驟二: 選區名:",
    options=area_selection)

area_rate = first_area[first_area['地區']==縣市區域]
area_rate = int(area_rate['費率'])

## 輸入總重量
sum_重量 = st.number_input('輸入總重量')
result = str(int(sum_重量)*area_rate*0.9)
# st.write("您選擇",areas,"-",縣市區域,"  費率:",str(area_rate),"  總重量:",sum_重量,"根據總重量計算結果1為:",result)
st.write("您選擇 ",areas," - ",縣市區域)
st.write("費率:   ",str(area_rate))
st.write("總重量:",sum_重量)
st.write("階段1計算結果為:",result)

# ## 超長寬
# 超長寬計算次數 = st.number_input('輸入超長寬計算次數')
# 超長寬費率 = st.number_input('輸入超長寬費率')


# cal_idx = 1
# stage2_res = 0
# for _ in 超長寬計算次數:
#     prod_x = st.number_input('輸入第',str(cal_idx),'個板金的長')
#     prod_y = st.number_input('輸入第',str(cal_idx),'個板金的寬')
#     each_res2 = (int(prod_x)+int(prod_y))
    
#     stage2_res=stage2_res+prod_x+prod_y
    
#     cal_idx+=1






# st.write("嘗試創建**表格**：")

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
# # 單行只有變數，不需要使用 st.write()，它會自動套用
# df


# # 繪製折線圖
# # 使用 Numpy 生成一個隨機樣本，然後將其繪製成圖表。
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

# # 使用複選框顯示/隱藏數據
# if st.checkbox('顯示地圖圖表'):
#     # 繪製地圖
#     # 使用 Numpy 生成一個隨機樣本，繪製到地圖上。
#     map_data = pd.DataFrame(
#         np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
#         columns=['lat', 'lon'])
#     st.map(map_data)

# # 使用選擇框進行選擇(選擇框移至側邊欄中)
# option = st.sidebar.selectbox(
#     '你喜歡哪種動物？',
#     ['狗', '貓', '鸚鵡', '天竺鼠'])
# '你的答案：', option

# '---'

# # 左右排列
# left_column, right_column = st.beta_columns(2)

# pressed = left_column.button('不要按!')
# if pressed:
#     left_column.write("就叫你不要按了!")

# with right_column:
#     chosen = st.radio(
#         '你住在哪裡？',
#         ("地球", "月亮", "火星"))
#     st.write(f"我是 {chosen} 人！！")

# # 隱藏大量內容來節省空間。
# expander = st.beta_expander("點擊來展開...")
# expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")


# 加入進度條
# 增加一個空白元件，等等要放文字
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'目前進度 {i+1} %')
#     bar.progress(i + 1)
#     time.sleep(0.1)


# @st.cache(suppress_st_warning=True)
# def expensive_computation(a):
#     st.write(f"沒有快取：expensive_computation({a})")
#     time.sleep(2)
#     return a * 2

# a = st.slider("選擇一個數字", 0, 10)
# result = expensive_computation(a)
# st.write("結果：", result)


# 更多元件請參考官方說明：https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
# st.title('My title')
# st.header('My header')
# st.subheader('My sub')
# st.text('Fixed width text')
# st.markdown('_Markdown_')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.code('for i in range(8):\n    foo()')
# st.video('https://www.youtube.com/watch?v=0rp3pP2Xwhs', start_time=100)

# st.button('Hit me')
# st.checkbox('Check me out')
# st.radio('Radio', [1,2,3])
# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])
# st.text_input('Enter some text')
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.color_picker('Pick a color')
# %%
