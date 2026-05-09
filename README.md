# 2026-bdp
## 프로젝트 소개

본 프로젝트는 서울시 공공 버스 승하차 데이터를 활용하여  
명지대학교 주변 버스 정류장의 교통 이용 패턴을 분석하는 빅데이터 처리 시스템을 구현하는 것을 목표로 한다.

Hadoop 기반 환경에서 데이터를 수집·저장·처리·분석하며,  Spark와 Hive를 활용하여 대용량 교통 데이터를 분석한다.

---

## 프로젝트 목표

- 명지대학교 주변 버스 정류장 데이터 수집
- HDFS 기반 데이터 저장
- Spark / Hive 기반 데이터 처리 및 분석
- 월별 및 요일별 교통 패턴 분석
- 버스 노선별 이용량 분석 및 시각화

---

## 기술 스택

### Big Data
- Hadoop HDFS
- Apache Spark
- Apache Hive

### Language
- Python
- PySpark

### Visualization
- Matplotlib

---

## 데이터 출처

- 서울 열린데이터광장


사용 데이터:
- 서울시 버스노선별 정류장별 승하차 인원 정보

---

## 분석 목표

1. 명지대학교 주변 정류장의 월별 이용량 변화 분석
2. 요일별 승하차 패턴 분석
3. 버스 노선별 이용량 비교
4. 학기 중 / 방학 중 이용 패턴 비교

---

## 시스템 구조

```text
Public Data
    ↓
Data Collection
    ↓
HDFS Storage
    ↓
Spark / Hive Processing
    ↓
Traffic Pattern Analysis
    ↓
Visualization
```

---

## Repository Structure

```text
mju-bus-bigdata/
├── README.md
├── data/
├── src/
│   ├── ingest/
│   ├── pipeline/
│   └── analyze/
├── results/
└── infra/
```

---

## 실행 환경

- HDP Sandbox

---

