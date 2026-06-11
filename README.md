# 2026-bdp

## 프로젝트 소개

본 프로젝트는 서울시 열린데이터광장의 버스 승하차 데이터를 활용하여 명지대학교 주변 버스 정류장의 이용 패턴을 분석하는 빅데이터 처리 시스템을 구현하는 것을 목표로 한다.

서울시 Open API를 통해 데이터를 자동 수집하고, HDFS에 저장한 뒤 Spark를 이용해 전처리하고 Hive를 활용하여 분석을 수행하였다. 또한 분석 결과를 시각화하여 이용 패턴을 직관적으로 확인할 수 있도록 구현하였다.

---

## 프로젝트 목표

* 서울시 Open API 기반 데이터 수집
* HDFS 기반 데이터 저장
* Spark를 이용한 데이터 전처리
* Hive를 이용한 데이터 분석
* 버스 이용 패턴 시각화
* 전체 분석 과정 자동화

---

## 사용 기술

### 빅데이터 플랫폼

* Hadoop HDFS
* Apache Spark
* Apache Hive

### 프로그래밍 언어

* Python
* PySpark

### 시각화

* Matplotlib

### 형상 관리

* Git
* GitHub

---

## 데이터 출처

서울 열린데이터광장

사용 데이터:

* 서울시 버스노선별 정류장별 승하차 인원 정보

---

## 분석 대상

### 대상 정류장

* 13195 (명지대)-DMC센트럴아이파크 방면
* 13194 (명지대)-명지대삼거리 방면

### 수집 기간

* 2025년 1월 ~ 2025년 6월 (각 월 1~15일 데이터만 수집)

---

## 분석 내용

### 1. 월별 이용량 분석

명지대학교 주변 버스 정류장의 월별 이용량 변화를 분석하였다.

### 2. 요일별 이용량 분석

평일과 주말의 이용 패턴 차이를 분석하였다.

### 3. 노선별 이용량 분석

버스 노선별 승차 인원을 비교하여 주요 이용 노선을 파악하였다.

### 4. 승차·하차 비교 분석

명지대 정류장과 명지대삼거리 정류장의 승차 및 하차 패턴을 비교하였다.

---

## 시스템 구조

```text
서울시 Open API
        ↓
collect_data.py
        ↓
HDFS 저장
        ↓
preprocess.py
        ↓
Apache Spark
        ↓
Hive 테이블 생성
        ↓
Hive 분석
        ↓
visualization.py
        ↓
그래프 생성
```

---

## 저장소 구조

```text
2026-bdp
├── README.md
├── collect_data.py
├── preprocess.py
├── hive_queries.sql
├── run_pipeline.sh
├── visualization.py
├── analysis_result/
│   ├── monthly.csv
│   ├── dayofweek.csv
│   ├── routes.csv
│   └── station.csv
├── result_images/
│   ├── monthly_analysis.png
│   ├── dayofweek_analysis.png
│   ├── top_routes.png
│   └── station_direction.png
└── .gitignore
```

---

## 실행 방법

전체 파이프라인 실행

```bash
./run_pipeline.sh
```

실행 과정

1. Open API 데이터 수집
2. HDFS 저장
3. Spark 전처리
4. Hive 분석
5. 시각화 결과 생성

---

## 분석 결과

### 월별 이용량 분석

* 3월 이후 이용량이 크게 증가하였다.
* 4월에 가장 높은 이용량을 기록하였다.

### 요일별 이용량 분석

* 평일 이용량이 주말보다 높게 나타났다.
* 목요일 이용량이 가장 높게 나타났다.

### 노선별 이용량 분석

* 7612번 노선의 이용량이 가장 높게 나타났다.

### 승차·하차 비교 분석

* 명지대 정류장(13195)은 승차 인원이 많았다.
* 명지대 정류장(13194)은 하차 인원이 많았다.

이를 통해 학생들의 통학 패턴을 확인할 수 있었다.

---

## 실행 환경

* HDP Sandbox
* Hadoop 3.x
* Spark 2.x
* Hive 3.x
* Python 3.6

```
```
