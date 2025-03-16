# NLP Advanced: NLP Pipeline

## 1. 환경설정
- 라이브러리 및 패키지 설치
- GPU/TPU 설정
- 랜덤 시드 고정

## 2. 데이터셋 구축
- 데이터 수집 및 정제
- 데이터 전처리 (토큰화, 정규화, 불용어 제거 등)
- 데이터 증강 및 분할 (Train/Validation/Test)

## 3. 모델 및 토크나이저 가져오기
- 사전 훈련된 모델 및 토크나이저 로드
- 커스텀 모델 설계 (필요 시)
- 모델 설정 (하이퍼파라미터 튜닝)

## 4. 모델 학습
### Model
- Huggingface에서 사전 학습된 분류 모델 불러오기
- 사전 학습된 토크나이저와 모델은 동일한 Checkpoint여야 학습 가능
- 다른 Checkpoint의 Tokenizer와 model 사용 시, 호환성 문제 발생

### Trainer
- 모델을 학습, 평가, 최적화하기 위한 간편하고 확장 가능한 인터페이스 제공
- 배치학습, 학습 스케줄러, 학습 조기종료 등의 기능 포함
  - 배치학습: 일정 크기의 데이터 묶음을 사용하여 학습 진행
  - 학습 스케줄러: 학습률을 점진적으로 조정하여 최적의 학습 성능 도출
  - 학습 조기종료: 성능이 향상되지 않을 경우 학습을 자동으로 중단하여 과적합 방지

## 5. 추론 및 평가
- 테스트 데이터셋에서 예측 수행
- 성능 평가 (정확도, F1-score, BLEU, ROUGE 등)
- 에러 분석 및 추가 개선 방향 탐색

---

# Encoder Model: Transfer Learning
## 1. 출현 배경
1. **데이터 부족 문제 해결**
   - 대량의 데이터 확보가 어려운 도메인(의료, 금융 등) 존재
   - 데이터 라벨링 비용이 높아 대규모 학습 어려움
   - 대규모 데이터셋에서 학습한 모델을 활용해 적은 데이터로도 높은 성능 가능

2. **학습 비용 절감**
   - 처음부터 모델 학습 시 높은 연산 비용과 긴 학습 시간 필요
   - 기존 학습된 모델의 가중치를 가져와 미세 조정(Fine-tuning)하여 연산 비용 절감

3. **모델의 일반화 성능 향상**
   - 작은 데이터셋에서 학습하면 과적합(Overfitting) 위험 증가
   - 다른 도메인에서 학습한 특징을 활용해 일반화된 패턴 학습 가능

## 2. Transfer Learning 방법
1. **Feature Extraction**
   - 사전 학습된 모델의 중간 층을 Feature Extractor로 활용
   - 새로운 데이터셋에서 분류기(classifier)만 변경하여 학습 진행

2. **Fine-Tuning**
   - 사전 학습된 모델의 일부 또는 전체 가중치를 미세 조정
   - 새로운 데이터셋에 맞게 모델의 일부 층을 다시 학습

## 3. Pretraining vs Fine-Tuning
- **Pre-training**: 대규모 데이터셋에서 일반적인 특징을 학습
- **Fine-Tuning**: 특정 도메인에 맞게 미세 조정

---

# ELMo (Embeddings from Language Models)
## 특징
- **양방향 LSTM(BiLSTM)**을 활용하여 문맥을 고려한 단어 임베딩 생성
- 문맥에 따라 단어의 의미가 변화
- 대규모 말뭉치에서 **사전 학습된 언어 모델** 활용
- Fine-tuning 없이도 다양한 NLP 작업에서 사용 가능

## 한계
- **계산 비용**: 높은 연산 자원 필요
- **긴 문장 처리 어려움**: 문맥을 길게 유지하기 어려움

---

# BERT (Bidirectional Encoder Representations from Transformers)
## 개요
- Transformer의 **인코더**만으로 구성된 언어 모델
- MLM (Masked Language Model)과 NSP (Next Sentence Prediction) 활용
- 위키피디아와 BooksCorpus와 같은 레이블이 없는 데이터로 Pre-training 수행
- Fine-tuning을 통해 다양한 NLP 작업에 적용 가능

## BERT 모델 구조
### ELMo vs BERT
- **ELMo**: 양방향 LSTM 기반
- **BERT**: Transformer 기반으로 병렬 처리 가능

### BERT-Base vs BERT-Large
- **BERT-Base**: 12개 층, 110M 파라미터
- **BERT-Large**: 24개 층, 340M 파라미터

### 입력 임베딩
- **[CLS] 토큰**: 문장 분류를 위한 임베딩 생성
- **[SEP] 토큰**: 문장 간 구분
- **Position Embedding**: 단어 위치 정보 학습

### Pretraining
1. **Masked Language Model (MLM)**
   - 문장에서 무작위로 토큰을 마스킹하여 예측
   - 80%는 `[MASK]`, 10%는 랜덤 단어, 10%는 원래 단어 유지
   - 양방향 단어 정보를 동시에 학습

2. **Next Sentence Prediction (NSP)**
   - 두 문장이 연속되는지 예측
   - 질의 응답, 자연어 추론 등의 문제 해결 가능

---

# Decoder Model: GPT
- Transformer의 **디코더**만 활용하는 모델
- Autoregressive(자가 회귀) 방식으로 학습하여 다음 단어 예측
- Zero-shot, Few-shot Learning 가능

# Encoder-Decoder Model
- Transformer 기반의 **Seq2Seq 모델**
- 번역, 요약, 문서 생성 등에 활용
- 대표 모델: T5, BART

# Next Encoder Model
- BERT 이후의 향상된 인코더 모델 연구
- 대표적인 모델: RoBERTa, ALBERT, ELECTRA

# NLP 최신 트렌드
- 대규모 멀티모달 모델 (예: GPT-4, Flamingo)
- 효율적인 경량 모델 연구 (예: DistilBERT, TinyBERT)
- Prompt Engineering 및 In-Context Learning
- Multilingual NLP 및 코드-스위칭 모델 연구

