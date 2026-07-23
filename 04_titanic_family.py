#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('titanic.xls')

df['family_size'] = df['sibsp'] + df['parch'] + 1
print(df[['sibsp', 'parch', 'family_size']].head())

# %%
sns.barplot(data=df, x='family_size', y='survived')
plt.show()
# %%
sns.barplot(data=df, x='family_size', y='survived', hue='pclass')
plt.show()
# %%
family_pclass_counts = pd.crosstab(df['family_size'], df['pclass'])
print(family_pclass_counts)
# %%
# %% 행(Row) 기준 비율 구하기 (소문자 'index'에 따옴표 꼭!)
print(pd.crosstab(df['family_size'], df['pclass'], normalize='index'))
# %%
# %% 전체 기준 비율 구하기 (첫 글자 대문자 True!)
print(pd.crosstab(df['family_size'], df['pclass'], normalize=True))
# %%
# %% 소수점을 깔끔한 % 형식으로 변환해서 출력하기
crosstab_pct = pd.crosstab(df['family_size'], df['pclass'], normalize='index')

# 출력 형식을 소수점 첫째 자리 %로 포맷팅합니다.
crosstab_pct.style.format('{:.1%}')
# %%
sns.lineplot(data=df, x='family_size', y='survived', hue='sex')
plt.show()
# %%
sns.barplot(data=df, x='family_size', y='survived')
# %%
def get_family_group(size):
    if size ==1:
        return 'Solo'
    elif 2 <= size <= 4:
        return 'Small'
    else:
        return 'Large'
    
df['family_group'] = df['family_size'].apply(get_family_group)
group_survival = pd.crosstab(df['family_group'], df['survived'], normalize='index')
print(group_survival)
# %%
import numpy as np

def get_age_group(age):
    if pd.isna(age):
        return 'Unknown'
    
    if age<15:
        return 'Child'
    elif 15 <= age < 35:
        return 'Young'
    elif 35 <= age < 60:
        return 'Middle'
    else:
        return 'Senior'
    
df['age_group'] = df['age'].apply(get_age_group)
age_survival = pd.crosstab(df['age_group'], df['survived'], normalize='index')
print(age_survival)
# %%
desired_order = ['Child', 'Young', 'Middle', 'Senior', 'Unknown']

# 3. reindex를 사용해 순서를 강제로 정렬합니다!
age_survival_sorted = age_survival.reindex(desired_order)

print(age_survival_sorted)
# %%
# %% [11] 객실 등급(pclass)과 나이대(age_group)를 동시에 고려한 생존율 분석
# 행(index)에 객실 등급과 나이대를 동시에 넣어서 입체적으로 분석합니다.
pclass_age_survival = pd.crosstab(
    index=[df['pclass'], df['age_group']], 
    columns=df['survived'], 
    normalize='index'
)

# 우리가 원하는 순서대로 행을 다시 정렬합니다.
# 1, 2, 3등석 각각 안에서 Child -> Young -> Middle -> Senior -> Unknown 순으로 정렬되도록 합니다.
desired_multi_order = []
for p in [1, 2, 3]:
    for age in ['Child', 'Young', 'Middle', 'Senior', 'Unknown']:
        desired_multi_order.append((p, age))

print(pclass_age_survival.reindex(desired_multi_order))
# %%
