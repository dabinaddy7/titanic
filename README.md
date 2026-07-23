# 🚢 타이타닉 승객 요금(Fare)과 생존율 상관관계 분석

타이타닉 데이터를 활용해 승객이 지불한 운임(Fare)이 생존에 미친 영향을 다각도로 분석하고 시각화한 미니 프로젝트입니다.

---

## 📊 주요 분석 내용

### 1. 요금 데이터의 쏠림 현상 확인
* 승객의 대다수(90% 이상)가 0~50달러 사이의 저렴한 티켓을 이용했습니다.
* 최고가 티켓은 512달러로 극단적인 이상치(Outlier)가 존재하며, 전형적인 오른쪽으로 꼬리가 긴(Skewed to the right) 분포를 띱니다.

### 2. 구간화(Binning) 방식에 대한 비판적 접근
* **`pd.qcut` (인원수 기준 3등분):**
  * 그룹 간 인원 비율을 맞추기엔 좋으나, 경계선(29.9달러와 30.1달러 등) 근처의 승객들이 단 몇 센트 차이로 다른 그룹에 묶이는 '경계선 왜곡 문제'를 식별했습니다.
* **`pd.cut` (금액 기준 3등분):**
  * 절대적인 금액 기준으로 자를 수 있으나, 데이터 쏠림이 심해 특정 그룹에 승객이 과도하게 쏠리는 현상이 발생했습니다.

### 3. 연속형 확률 분석 (로지스틱 회귀 곡선)
* 구간화의 한계를 극복하기 위해 데이터를 쪼개지 않고 연속적인 흐름으로 분석했습니다.
* `seaborn.lmplot`의 `logistic=True` 옵션을 활용하여 요금이 올라갈수록 생존 확률이 완만한 S자를 그리며 상승하는 로지스틱 회귀 곡선을 도출했습니다.

---

## 🛠️ 해결한 이슈 (Troubleshooting)

### 🚨 `RuntimeError: logistic=True requires statsmodels...`
* **원인:** 로지스틱 곡선을 그리기 위한 통계 라이브러리(`statsmodels`)가 부재함.
* **해결:** Jupyter 환경에서 `%pip install statsmodels`를 실행한 후, **커널 재시작(Kernel Restart)**을 수행하여 패키지를 정상 인식시켰습니다.

---

## 💻 사용 기술 및 라이브러리
* Python 3.13
* Pandas (Data Manipulation)
* Seaborn & Matplotlib (Data Visualization)
* Statsmodels (Statistical Regression)

## 📅 TIL (Today I Learned)
매일매일 분석하고 배운 알짜배기 지식들을 기록하는 공간입니다.

* 📝 **[나의 일일 분석 일지(TIL) 보러가기](./TIL)**