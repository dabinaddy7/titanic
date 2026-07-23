# %%

import pandas as pd

df = pd.read_excel('titanic.xls')
df.head(3)
# %%
df['sex'].head()
# %%
df['survived'].head()
# %%
df['sex'].value_counts()
# %%
df['survived'].value_counts()
# %%
df.groupby('sex')['survived'].mean()
# %%
import matplotlib.pyplot as plt
import seaborn as sns

pclass_survival = df.groupby('pclass')['survived'].mean()
pclass_survival
# %%
plt.bar(pclass_survival.index, pclass_survival.values)
# %%
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.xticks([1, 2, 3])
plt.title('Survival Rate by Pclass')
plt.bar(pclass_survival.index, pclass_survival.values)
# %%
cross_tab = pd.crosstab(index=df['pclass'], columns=df['sex'], values=df['survived'], aggfunc='mean')
print(cross_tab)
# %%
sns.heatmap(cross_tab, annot=True, cmap='coolwarm')
# %%
# %% [3] 등급별 성별 생존율 교차 분석
import pandas as pd

# pd.crosstab을 사용해 pclass와 sex를 교차시키고 survived의 평균을 구합니다.
survival_table = pd.crosstab(
    index=df['pclass'],       # 행(세로축)에는 객실 등급을 둔다
    columns=df['sex'],        # 열(가로축)에는 성별을 둔다
    values=df['survived'],    # 칸에 채워질 데이터는 생존 여부로 한다
    aggfunc='mean'            # 그 데이터들을 묶어서 '평균(생존율)'을 낸다
)

print(survival_table)
# %%
# %% [4] 등급별 성별 생존율 시각화 (막대그래프)
import matplotlib.pyplot as plt

# 판다스 데이터프레임 자체에 내장된 plot 기능을 쓰면 matplotlib으로 자동 연동됩니다.
# kind='bar'는 막대그래프, rot=0은 x축 글씨(pclass)를 회전하지 않고 똑바로 세우는 옵션입니다.
survival_table.plot(kind='bar', rot=0, figsize=(8, 5))

# 차트 디테일 설정 (질문자님이 아까 쓰신 문법 활용!)
plt.title('Survival Rate by Pclass and Sex')
plt.xlabel('Pclass (Passenger Class)')
plt.ylabel('Survival Rate')
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 가로 눈금선 추가로 가독성 높이기

plt.show()
# %%
# %% [5] 등급별 성별 생존율 시각화 (히트맵)
import matplotlib.pyplot as plt

# matshow를 쓰면 표 형태의 데이터를 색상으로 표현해 줍니다.
plt.figure(figsize=(6, 5))
plt.matshow(survival_table, cmap='Blues', fignum=1)  # 파란색 농도로 표현
plt.colorbar(label='Survival Rate')                  # 우측에 색상 기준바 표시

# 축 레이블 매칭하기
plt.xticks([0, 1], labels=['Female', 'Male'])
plt.yticks([0, 1, 2], labels=['1st', '2nd', '3rd'])
plt.title('Survival Rate Heatmap', pad=20)

# 칸 마다 실제 숫자 적어주기 (디테일)
for i in range(len(survival_table.index)):
    for j in range(len(survival_table.columns)):
        val = survival_table.iloc[i, j]
        plt.text(j, i, f'{val:.2f}', ha='center', va='center', 
                 color='white' if val > 0.5 else 'black')

plt.show()
# %%
# %% [5] seaborn으로 히트맵 깔끔하게 그리기
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 5))

# annot=True: 칸 안에 숫자 적기
# fmt='.2f': 소수점 둘째 자리까지 표시
# cmap='Blues': 파란색 테마 적용
sns.heatmap(survival_table, annot=True, fmt='.2f', cmap='Blues')

plt.title('Survival Rate Heatmap by Pclass and Sex')
plt.show()
# %%
# %% [1] 성별 생존율 기본 그래프
import seaborn as sns
import matplotlib.pyplot as plt

# data에 데이터프레임을 넣고, x축과 y축에 컬럼 이름만 문자열로 쏙 넣어주면 끝!
sns.barplot(data=df, x='sex', y='survived')
plt.show()
# %%
sns.countplot(data=df, x='sex')
# %%
sns.histplot(data=df, x='age', kde = True)
# %%
sns.scatterplot(data = df, x = 'age', y = 'fare')
# %%
plt.figure(figsize = (8,5))

sns.barplot(data = df, x = 'pclass', y = 'survived', hue = 'sex')
plt.title('Survival Rate by Pclass and Sex (Seaborn)')
plt.show()
# %%
sns.set_theme(style="whitegrid")

sns.barplot(data = df, x = 'pclass', y = 'survived', hue = 'sex')
plt.title('Survival Rate by Pclass and Sex (Seaborn)')
plt.show()
# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

sns.histplot(data = df, x = 'age', hue = 'survived',
            multiple = 'stack', kde = True, palette = 'Set2')
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Passenger Count')
plt.show()
# %%
# %% [2] 결측치(NaN) 확인하고 중간값으로 채우기

# 1. 현재 나이 컬럼에 비어있는 값(결측치)이 몇 개인지 확인
print("채우기 전 비어있는 나이 데이터 개수:", df['age'].isnull().sum())

# 2. 승객들의 나이 중간값(Median) 구하기
median_age = df['age'].median()
print(f"승객들의 나이 중간값: {median_age}세")

# 3. 비어있는 값(.fillna)을 중간값으로 채워 넣기
df['age'] = df['age'].fillna(median_age)

# 4. 잘 채워졌는지 다시 확인
print("채운 후 비어있는 나이 데이터 개수:", df['age'].isnull().sum())
# %%

plt.figure(figsize=(10,5))

sns.histplot(data = df, x = 'age', hue = 'survived',
            multiple = 'stack', kde = True, palette = 'Set2')
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Passenger Count')
plt.show()
# %%
# %% [3] 나이 구간(Age Group) 나누고 시각화하기

# 나이를 나눌 기준점(bins)과 각 구간의 이름(labels) 정하기
bins = [0, 5, 19, 35, 60, 100]
labels = ['Baby', 'Teenager', 'Young Adult', 'Middle Aged', 'Senior']

# pd.cut을 이용해 'age_group'이라는 새로운 컬럼 만들기
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# 새로 만든 연령대 그룹별로 생존율 시각화하기!
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='age_group', y='survived', palette='muted')

plt.title('Survival Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.show()
# %%
# %% [4] 등급별, 성별 중간값으로 스마트하게 나이 채우기
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 원본 데이터 다시 불러오기 (이전의 왜곡된 데이터 초기화)
df = pd.read_excel('titanic.xls')

# 2. 각 그룹(pclass, sex)별 나이 중간값 확인해보기
# 1등석 남성(42세)과 3등석 여성(22세)의 차이가 엄청납니다!
medians = df.groupby(['pclass', 'sex'])['age'].transform('median')

# 3. 비어있는(NaN) 나이만 쏙 골라 해당 그룹의 중간값으로 정교하게 매칭하여 채우기
df['age'] = df['age'].fillna(medians)

# 4. 스마트하게 채운 뒤 나이 분포 다시 그려보기!
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='age', hue='survived', multiple='stack', kde=True, palette='Set2')
plt.title('Age Distribution (Smart Imputation by Pclass & Sex)')
plt.show()
# %%
# %% [5] 결측치를 채우지 않고 'Unknown' 카테고리로 다루기
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 원본 데이터 다시 깨끗하게 불러오기
df = pd.read_excel('titanic.xls')

# 2. 나이대를 자르되, 결측치(NaN)는 그대로 둡니다.
bins = [0, 5, 19, 35, 60, 100]
labels = ['Baby', 'Teenager', 'Young Adult', 'Middle Aged', 'Senior']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# 3. 판다스 카테고리 데이터에 'Unknown'이라는 방을 하나 더 만들어주고, 빈 곳을 채웁니다.
df['age_group'] = df['age_group'].cat.add_categories('Unknown')
df['age_group'] = df['age_group'].fillna('Unknown')

# 4. 시각화 해보기 (순서는 보기 좋게 정렬)
plt.figure(figsize=(9, 5))
group_order = ['Baby', 'Teenager', 'Young Adult', 'Middle Aged', 'Senior', 'Unknown']
sns.barplot(data=df, x='age_group', y='survived', order=group_order, palette='Set2')

plt.title('Survival Rate by Age Group (Including Unknown)')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.show()
# %%
df['fare'].describe()
# %%
sns.histplot(df, x = 'fare', kde = True)
plt.show()
# %%
df['fare_group'] = pd.qcut(df['fare'], q=3, labels= ['Low', 'Medium', 'High'])
sns.barplot(data=df, x = 'fare_group', y = 'survived')
plt.show()
# %%
%pip install statsmodels
# 요금이 올라갈수록 생존 확률(로지스틱 곡선)이 어떻게 변하는지 쪼개지 않고 그대로 보기
sns.lmplot(data=df, x='fare', y='survived', logistic=True, y_jitter=0.03)
# %%
# 역사적 기준이나 요금 분포의 명확한 절단면을 직접 숫자로 지정하기
# 0~15달러(서민형), 15~40달러(중산층), 40~512달러(자산가)
custom_bins = [0, 15, 40, 512]
df['fare_group_custom'] = pd.cut(df['fare'], bins=custom_bins, labels=['Low', 'Medium', 'High'])
# %%
sns.histplot(data=df, x='fare_group_custom', hue='survived', multiple='stack', palette='Set2')
# %%
# %% [7] 범주형 데이터에 맞게 kde를 빼고 깔끔한 스택 막대그래프로 보기
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

# kde=True만 쏙 뺐습니다!
sns.histplot(data=df, x='fare_group_custom', hue='survived', multiple='stack', palette='Set2')

plt.title('Passenger Count by Custom Fare Group and Survival')
plt.xlabel('Custom Fare Group')
plt.ylabel('Passenger Count')
plt.show()
# %%
