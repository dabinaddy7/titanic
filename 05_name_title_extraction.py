#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('titanic.xls')
df
# %%
df['title'] = df['name'].str.extract(r' ([A-Za-z]+)\.', expand = False)
print(df['title'].value_counts())
# %%
df['title'] = df['title'].replace({
    'Mlle' : 'Miss',
    'Ms': 'Miss',
    'Mme' : 'Mrs'
})

race_titles = ['Dr', 'Rev', 'Col', 'Major', 'Capt', 'Lady', 'Sir', 'Don', 'Dona', 'Jonkheer', 'Countess']
df['title'] = df['title'].replace(race_titles, 'Rare')

print(df['title'].value_counts())
# %%
name_group = pd.crosstab(df['title'], df['survived'], normalize='index')
print(name_group)
# %%
name_group = pd.crosstab(df['title'], df['survived'], normalize=True)
print(name_group)
# %%
name_group = pd.crosstab(df['title'], df['survived'], normalize='columns')
print(name_group)
# %%
print(df.groupby('title')['age'].mean())
print("\n" + "="*40 + "\n")

print(df[df['age'].isna()]['title'].value_counts())
# %%
print("나이 결측치 수", df['age'].isna().sum())

df['age'] = df['age'].fillna(df.groupby('title')['age'].transform('mean'))

print("대체 후 나이 결측치 수:", df['age'].isna().sum())
print("\n" + "="*40 + "\n")

print("대체 완료된 데이터 상단 샘플:")
print(df[['name', 'title', 'age']].head(10))
# %%
# %% [4] 실제로 나이가 비어있던 승객들의 대체 결과만 콕 집어서 확인하기

# 타이타닉 원본 데이터셋을 다시 한번 불러와서 결측치 위치(인덱스)를 찾습니다.
raw_df = pd.read_excel('titanic.xls')
missing_age_indices = raw_df[raw_df['age'].isna()].index

# 우리가 결측치를 채운 df에서, 원래 비어있던 승객들의 인덱스만 필터링해 출력합니다.
print("=== 실제 결측치였던 승객들의 대체된 나이 ===")
print(df.loc[missing_age_indices, ['name', 'title', 'age']].head(10))
# %%
df['is_mother'] = (df['sex'] == 'female') & (df['title'] == 'Mrs') & (df['parch'] >0) & (df['age'] > 18)

print(df['is_mother'].value_counts())

female_df = df[df['sex'] =='female']
mother_survival = pd.crosstab(female_df['is_mother'], female_df['survived'], normalize='index')
print(mother_survival)
# %%
mother_survival = pd.crosstab(female_df['is_mother'], female_df['survived'], normalize='all')
print(mother_survival)
# %%
# %% [6] 객실 등급(pclass)별 엄마의 생존율 확인하기
# 여성 승객만 대상으로, 객실 등급과 엄마 여부에 따른 생존율을 구합니다.
mother_pclass_survival = pd.crosstab(
    index=[female_df['pclass'], female_df['is_mother']], 
    columns=female_df['survived'], 
    normalize='index'
)
print("=== 객실 등급 및 엄마 여부별 생존율 ===")
print(mother_pclass_survival)
# %%
