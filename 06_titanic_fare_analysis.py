#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('titanic.xls')
df.head()
# %%
df['fare'].describe()
# %%
zero_fare_group = df['fare'] == 0
print(df[zero_fare_group][[ 'name', 'pclass', 'sex', 'survived']])
print('='*100)
rich_fare_group = df['fare'] >= 500
print(df[rich_fare_group][[ 'name', 'pclass', 'sex', 'survived']])
# %%
df['fare'].skew()
# %%
sns.histplot(data = df,x='fare', y = 'survived')
plt.show()
# %%
import numpy as np
df['fare_log'] = np.log1p(df['fare'])
df['fare_log'].skew()
# %%
sns.histplot(data = df,x='fare_log', y = 'survived')
plt.show()
# %%
sns.histplot(data = df,x='fare_log',kde=True)
plt.show()
# %%
sns.histplot(data=df, x='fare_log', hue='survived', multiple='stack', kde=True)
# %%
import matplotlib.ticker as mtick

# 1. 그래프 그리기 (multiple='fill'로 변경, 비율이라 kde는 제외하는 게 깔끔합니다)
ax = sns.histplot(data=df, x='fare_log', hue='survived', multiple='fill', bins=15)

# 2. y축을 0~100% 포맷으로 변경 (실무용 팁)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_ylabel("Percentage (%)")
# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
# 그래프를 그리고 ax 객체를 받아옵니다.
ax = sns.histplot(data=df, x='fare_log', hue='survived', multiple='stack', bins=10)

# 🔥 각 막대 위에 숫자를 자동으로 달아주는 마법의 함수
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', padding=3)
# %%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 샘플 데이터 플롯 세팅 (선 그래프로 연습해봐요!)
plt.figure(figsize=(8, 5))

# 임의의 데이터 (시간에 따른 요금 변화 추이라고 가정)
x_days = ['Day 1 (Departure)', 'Day 2 (Atlantic)', 'Day 3 (Iceberg Warning)', 'Day 4 (Disaster)']
y_price = [10, 25, 45, 90]

# 🔥 1. 마커('o'), 선 스타일('--'), 색상, 두께(lw) 커스텀
plt.plot(x_days, y_price, 
         marker='o',         # 마커는 동그라미
         markersize=10,      # 마커 크기 키우기
         linestyle='--',     # 선은 대시(점선) 형태
         color='#e74c3c',    # 고급진 세련된 빨간색 hex code
         linewidth=3,        # 선 두께
         label='Average Fare Trend')

# 🔥 2. x축 글자가 길어서 겹치니까 30도 회전 (오른쪽 정렬 적용해서 깔끔하게)
plt.xticks(rotation=30, ha='right')

# 제목과 레이블 추가
plt.title("Titanic Voyage Timeline & Status", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Timeline")
plt.ylabel("Fare Value")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6) # 배경에 연한 땡땡이 격자 추가

plt.tight_layout() # 글자 안 잘리게 여백 자동 조절 (실무 필수 팁!)
plt.show()
# %%
