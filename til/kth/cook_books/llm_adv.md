
---

Q. Seq2Seq 모델에서 인코더(Encoder)의 역할은?  
A. 입력 시퀀스를 받아 고정된 크기의 컨텍스트 벡터(context vector)로 변환하는 역할을 수행하며, 주로 RNN, LSTM, GRU 등의 구조를 사용하여 입력을 처리하고 최종 히든 스테이트를 디코더에 전달한다.

---

Q. 디코더(Decoder)는 어떻게 동작하는가?  
A. 인코더에서 전달된 컨텍스트 벡터를 기반으로 출력 시퀀스를 생성하며, 처음에는 인코더의 최종 히든 스테이트를 받아 첫 번째 단어를 생성한 후, 생성된 단어를 다시 입력하여 다음 단어를 예측하는 방식으로 동작한다.

---

Q. Seq2Seq 모델에서 사용되는 주요 신경망 구조 3가지는?  
A. RNN (Recurrent Neural Network), LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit)

---

Q. Seq2Seq 모델에서 문맥(Context)을 유지하는 방식은?  
A. 인코더가 입력 시퀀스를 처리한 후 최종 히든 스테이트를 디코더에 전달하여 문맥을 유지한다.

---

Q. Seq2Seq 모델 학습 시 사용되는 기법 중 하나로, 정답 시퀀스를 일부 제공하여 학습을 돕는 방법은?  
A. Teacher Forcing

---

Q. Seq2Seq 모델에서 발생할 수 있는 긴 문장 처리 문제를 해결하기 위한 방법은?  
A. Attention Mechanism

---


---

Q. One-to-One 구조의 신경망 예시는?  
A. 일반적인 신경망 (예: 이미지 분류)

---

Q. One-to-Many 구조는 어떤 경우에 사용되며, 예시는?  
A. 하나의 입력으로 여러 개의 출력을 생성하는 구조로, 예시로 이미지 캡셔닝이 있다.

---

Q. Many-to-One 구조는 어떤 경우에 사용되며, 예시는?  
A. 여러 개의 입력이 하나의 출력으로 변환되는 구조로, 예시로 감정 분석이 있다.

---

Q. Many-to-Many 구조는 어떤 경우에 사용되며, 예시는?  
A. 여러 개의 입력이 여러 개의 출력으로 변환되는 구조로, 예시로 기계 번역과 챗봇이 있다.

---

Q. RNN이 순차 데이터 처리에 강한 이유는?  
A. 과거 정보를 유지하는 Hidden State를 사용하기 때문이다.

---

Q. RNN의 주요 장점 두 가지는?  
A.  
1. 순차 데이터 처리에 강점 (텍스트, 음성, 시계열 데이터 등)  
2. 과거 정보를 활용할 수 있음 (Hidden State 유지)  

---

Q. RNN의 주요 단점 두 가지는?  
A.  
1. Vanishing Gradient 문제 (기울기 소멸로 인해 장기 의존성 학습이 어려움)  
2. 긴 문장에서 기억력이 약함  

---

Q. RNN이 긴 문장에서 기억력이 약한 이유는?  
A. Vanishing Gradient 문제로 인해 장기 의존성을 학습하기 어렵기 때문이다.

---

Q. RNN의 단점을 해결하기 위한 대안은?  
A. LSTM(Long Short-Term Memory)과 GRU(Gated Recurrent Unit)

---

Q. LSTM이 RNN과 다른 점은?  
A. LSTM은 Cell State를 추가하여 장기 의존성을 유지할 수 있으며, RNN의 Vanishing Gradient 문제를 완화한다.

---

Q. LSTM이 사용하는 3가지 게이트는?  
A.  
1. Forget Gate: 불필요한 정보 삭제  
2. Input Gate: 새로운 정보 추가  
3. Output Gate: 최종 결과 계산  

---

Q. Forget Gate의 역할은?  
A. 불필요한 정보를 삭제하여 모델이 중요한 정보만 유지할 수 있도록 한다.

---

Q. Input Gate의 역할은?  
A. 새로운 정보를 Cell State에 추가하여 모델이 학습할 수 있도록 한다.

---

Q. Output Gate의 역할은?  
A. 최종 결과를 계산하여 다음 단계로 전달한다.

---

Q. LSTM의 주요 장점 두 가지는?  
A.  
1. 장기 의존성 문제 해결 (Vanishing Gradient 문제 완화)  
2. 긴 문장에서도 정보를 유지 가능  

---

Q. LSTM의 주요 단점 두 가지는?  
A.  
1. 계산량이 많음 (복잡한 구조)  
2. 학습 속도가 느림  

---

### GRU (Gated Recurrent Unit)

Q. GRU의 구조적 특징은?  
A. LSTM과 유사하지만 Gate 수가 2개로 단순화됨  
1. Reset Gate: 과거 정보를 얼마나 반영할지 결정  
2. Update Gate: 새로운 정보와 과거 정보를 어떻게 결합할지 결정  

---

Q. GRU가 LSTM보다 빠른 이유는?  
A. 게이트 수가 2개로 단순화되어 계산량이 적고 학습 속도가 빠름.

---

Q. GRU의 주요 장점 두 가지는?  
A.  
1. LSTM보다 빠르고 경량  
2. 계산량이 적어 학습 속도가 빠름  

---

Q. GRU의 주요 단점 두 가지는?  
A.  
1. LSTM보다 유연성이 낮음 (정보 삭제 방식이 단순함)  
2. 일부 문제에서는 LSTM보다 성능이 낮을 수 있음  

---

### Attention Mechanism

Q. Attention Mechanism이 Seq2Seq 모델에서 하는 역할은?  
A. 입력 시퀀스의 각 단어가 출력 단어와 얼마나 관련 있는지 가중치(weight)로 계산하여 중요한 정보에 집중할 수 있도록 함.

---

Q. Attention Mechanism이 Seq2Seq 모델을 어떻게 개선하는가?  
A. 디코더가 모든 입력을 동시에 참고할 수 있도록 하여 컨텍스트 벡터의 한계를 극복함.

---

Q. Attention Mechanism의 주요 장점 두 가지는?  
A.  
1. 긴 문장에서도 정보 손실이 적음  
2. 병렬 연산이 가능하여 Transformer에서 효과적으로 활용됨  

---

Q. Attention Mechanism의 주요 단점 두 가지는?  
A.  
1. 추가적인 계산 비용 발생  
2. 초반에는 최적의 가중치 학습이 어려울 수 있음  

---

Q. RNN 기반 Seq2Seq 모델에서 Attention을 적용하면 어떤 이점이 있는가?  
A. 기존 컨텍스트 벡터 하나만 사용하던 방식에서 벗어나, 입력 단어별로 가중치를 적용하여 보다 유연한 디코딩이 가능함.

---

### Transformer

Q. Transformer 모델의 주요 특징은?  
A.  
1. RNN 없이도 시퀀스를 처리할 수 있음  
2. Self-Attention Mechanism을 기반으로 동작  
3. Encoder-Decoder 구조 유지  
4. Multi-Head Attention과 Feed-Forward Networks 사용  

---

Q. Transformer의 주요 장점 두 가지는?  
A.  
1. 병렬 연산 가능하여 학습 속도가 빠름  
2. 긴 문장에서도 정보 손실이 없음  

---

Q. Transformer의 주요 단점은?  
A. 학습에 많은 데이터와 연산 자원이 필요함  

---

### Self-Attention Mechanism

Q. Self-Attention이란?  
A. 시퀀스 내 단어들이 서로 어떻게 관련되는지를 학습하는 메커니즘으로, 입력 문장의 각 단어가 다른 모든 단어들과 관계를 맺음.  

---

Q. Self-Attention의 주요 연산 과정은?  
A.  
1. Query, Key, Value 생성  
2. Query와 Key의 유사도 계산 (Attention Score)  
3. Score를 가중치로 활용하여 Value를 조합  

---

Q. Self-Attention에서 Query, Key, Value의 역할은?  
A.  
- Query (Q): 현재 단어가 어떤 정보를 찾을지 결정  
- Key (K): 모든 단어의 정보 저장  
- Value (V): 출력할 정보 저장  

---

Q. Self-Attention의 연산 공식은?  
A. $Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$  

---

### Multi-Head Attention

Q. Multi-Head Attention이란?  
A. Self-Attention을 여러 번 수행하여 다양한 관점에서 정보를 학습하는 기법  

---

Q. Multi-Head Attention이 정보를 효과적으로 학습하는 이유는?  
A. 여러 개의 Attention Head가 서로 다른 부분을 학습하여 정보 손실을 방지하기 때문  

---

### Feed-Forward Networks & Positional Encoding

Q. Position-wise Feed-Forward Networks의 역할은?  
A. 각 Attention 레이어의 출력값을 변환하는 비선형 변환 층으로, 모든 단어에 개별 적용되므로 연산이 독립적으로 수행됨.  

---

Q. Transformer에서 Positional Encoding이 필요한 이유는?  
A. RNN처럼 순서를 직접 학습하지 않으므로, 단어의 위치 정보를 추가하기 위해 사용됨.  

---

Q. Positional Encoding에서 사용되는 함수는?  
A. 사인(sin)과 코사인(cos) 함수  

---

### 자연어 처리 평가지표 (Evaluation Metrics)

Q. NLP 모델의 성능을 평가할 때 중요한 점은?  
A. 주어진 문제 유형에 따라 적절한 평가지표를 선택하는 것  

---

### 1. 분류 (Classification) 평가 지표

Q. 정확도(Accuracy)란?  
A. 전체 데이터 중에서 올바르게 분류된 샘플의 비율.  
$$ \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} $$  
그러나 데이터 불균형이 있을 경우 적절하지 않을 수 있음.  

---

Q. 정밀도(Precision)의 의미는?  
A. 모델이 양성으로 예측한 것 중에서 실제 양성의 비율.  
$$ \text{Precision} = \frac{TP}{TP + FP} $$  

---

Q. 재현율(Recall)이란?  
A. 실제 양성 샘플 중에서 모델이 올바르게 양성으로 예측한 비율.  
$$ \text{Recall} = \frac{TP}{TP + FN} $$  

---

Q. F1 Score를 계산하는 공식은?  
A. 정밀도와 재현율의 조화 평균.  
$$ F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} $$  

---

### 2. 회귀 (Regression) 평가 지표

Q. Mean Squared Error (MSE)의 정의는?  
A. 예측값과 실제값의 차이를 제곱하여 평균한 값.  

---

Q. Mean Absolute Error (MAE)의 정의는?  
A. 예측값과 실제값의 차이의 절대값 평균.  

---

Q. R-squared (R² Score)의 역할은?  
A. 모델이 데이터를 얼마나 잘 설명하는지 평가하는 지표.  

---

### 3. 언어 모델 평가 지표

Q. Perplexity (PPL)의 의미는?  
A. 언어 모델이 다음 단어를 얼마나 정확히 예측하는지 평가하는 지표로, 값이 낮을수록 성능이 좋음.  

---

Q. BLEU (Bilingual Evaluation Understudy)의 역할은?  
A. 기계 번역 성능 평가 지표로, 생성된 문장이 실제 문장과 얼마나 유사한지를 측정함.  

---

Q. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)의 목적은?  
A. 요약 및 생성된 텍스트가 참조 텍스트와 얼마나 유사한지 평가하는 지표.  

---

### 4. 자연어 처리 Pipeline

Q. 자연어 처리(NLP) 파이프라인의 첫 번째 단계는?  
A. 텍스트 수집(Data Collection): 원시 데이터를 수집하는 과정.  

---

Q. 전처리(Preprocessing)에서 수행하는 작업 세 가지는?  
A.  
1. 토큰화(Tokenization)  
2. 불용어 제거(Stopword Removal)  
3. 어간추출(Stemming)  

---

Q. 특징 추출(Feature Extraction)에서 사용되는 대표적인 단어 임베딩 기법 세 가지는?  
A. Word2Vec, FastText, BERT  

---

Q. NLP 모델 학습(Training Model) 단계에서 사용할 수 있는 모델 두 가지는?  
A.  
1. 딥러닝 모델 (Transformer, RNN)  
2. 전통적인 모델 (SVM, Naive Bayes)  

---

Q. NLP 파이프라인에서 마지막 평가(Evaluation) 단계의 목적은?  
A. 모델의 성능을 평가하고 조정하는 과정.  

---

### Transfer Learning (전이 학습)

Q. Transfer Learning(전이 학습)이란?  
A. 한 도메인에서 학습한 지식을 다른 도메인에 적용하는 기법으로, NLP 및 컴퓨터 비전에서 널리 사용됨.  

---

### 1. 출현 배경  

Q. Transfer Learning이 등장한 이유는?  
A. 기존 기계 학습 모델은 특정 데이터셋에서만 학습되었기 때문에 새로운 데이터에서 성능이 저하되는 문제가 있었음. 이를 해결하기 위해 대규모 데이터에서 사전 학습(Pre-training) 후, 특정 태스크에 미세 조정(Fine-tuning) 하는 방식이 등장함.  

---

### 2. 단어 임베딩의 한계  

Q. 기존 Word2Vec, GloVe 등 정적 단어 임베딩 방식의 문제점은?  
A. 문맥 정보를 반영하지 못해 같은 단어라도 문맥에 따라 다른 의미를 가지는 경우를 처리하지 못함.  

---

### 3. Transfer Learning in Computer Vision (CV)  

Q. 컴퓨터 비전(CV)에서 Transfer Learning이 어떻게 사용되는가?  
A. ImageNet에서 사전 학습된 모델을 다양한 태스크에 적용하는 방식이 일반적임.  

---

### 4. Pre-training & Fine-tuning  

Q. Pre-training(사전 학습)의 역할은?  
A. 대규모 데이터에서 일반적인 언어 구조 또는 패턴을 학습하는 과정.  

---

Q. Fine-tuning(미세 조정)의 역할은?  
A. 사전 학습된 모델을 특정 태스크에 맞게 추가 학습하는 과정.  

---

### 5. Transfer Learning의 효율성  

Q. Transfer Learning의 주요 장점 세 가지는?  
A.  
1. 데이터가 적어도 높은 성능을 달성할 수 있음  
2. 연산량 감소  
3. 기존의 모델보다 빠른 학습 속도  

---

### ELMo 관련
Q. ELMo(Embeddings from Language Models)의 핵심 개념은?  
A. 문맥을 반영한 단어 임베딩 기법으로, LSTM 기반 언어 모델을 활용하여 단어의 의미를 문맥에 따라 다르게 표현한다.  

Q. ELMo 모델의 구조에서 사용하는 핵심 기술은?  
A.  
- 양방향 LSTM(BiLSTM) 사용  
- 다층 언어 모델 적용  

Q. ELMo의 Pre-training 과정에서 수행하는 주요 작업은?  
A.  
- 대량의 텍스트에서 학습  
- 문맥을 고려하여 단어 임베딩을 생성  

Q. ELMo가 제공하는 Contextualized Word Embedding이란?  
A. 같은 단어라도 문맥에 따라 다른 벡터 표현을 가지는 임베딩 기법  

Q. 기존 단어 임베딩(Word2Vec, GloVe)과 ELMo의 차이점은?  
A.  
- Word2Vec, GloVe: 단어별로 고정된 벡터 사용  
- ELMo: 문맥에 따라 동적으로 변화하는 벡터 제공  

Q. Pretrained Language Model(PLM)의 역할은?  
A. 미리 학습된 언어 모델을 다양한 NLP 태스크에 활용 가능  

Q. ELMo의 주요 한계점은?  
A.  
- 계산량이 많고 느림  
- Transformer 기반 모델(BERT)의 등장으로 대체됨  

---

### BERT 관련
Q. BERT(Bidirectional Encoder Representations from Transformers)의 핵심 개념은?  
A. Transformer 기반의 양방향 언어 모델로, 문맥을 양방향으로 고려하여 더 강력한 언어 표현을 학습한다.  

Q. ELMo와 BERT의 주요 차이점은?  
A.  
- ELMo: LSTM 기반  
- BERT: Transformer 기반 → 더 깊은 문맥 정보 학습 가능  

Q. BERT의 두 가지 주요 버전과 차이점은?  
A.  
1. BERT-Base: 12-layer, 768 hidden size  
2. BERT-Large: 24-layer, 1024 hidden size  

Q. BERT의 Pre-training 과정에서 사용하는 두 가지 학습 기법은?  
A.  
1. Masked Language Model (MLM): 문장의 일부 단어를 마스킹하여 예측하는 방식  
2. Next Sentence Prediction (NSP): 두 문장이 연속적인지 예측  

Q. BERT가 다양한 NLP 태스크에 적용되는 방식은?  
A.  
- Fine-tuning  
- Single Sentence Classification  
- Sentence Pair Classification  
- Question Answering  
- Single Sentence Tagging  

Q. BERT의 단어 임베딩을 활용하는 방법은?  
A. Feature Extraction (특징 추출)  

---

### Tokenizer 관련
Q. Tokenization이란 무엇인가?  
A. 문장을 토큰 단위로 분리하는 과정  

Q. Subword Tokenizer란?  
A. 단어보다 작은 단위까지 분해하는 토크나이징 기법  

Q. BPE(Byte Pair Encoding) 알고리즘의 원리는?  
A. 자주 등장하는 문자 쌍을 결합하여 새로운 단위를 생성하는 방식  

---

### GPT-1 관련
Q. GPT란 무엇인가?  
A. "Generative Pre-trained Transformer"의 약자로, OpenAI에서 개발한 자연어 처리(NLP) 모델  

Q. GPT의 학습 과정 2단계는?  
A.  
1. Pre-training (사전 학습): 대량의 텍스트 데이터를 활용하여 언어 모델을 학습  
2. Fine-tuning (미세 조정): 특정 태스크(예: 감성 분석, QA)에 맞게 추가 학습  

Q. GPT-1이 기반으로 하는 Transformer의 구조는?  
A. Decoder 구조  

Q. Self-Attention과 Masked Self-Attention의 차이는?  
A.  
- Self-Attention: 모든 단어가 서로를 참조 가능  
- Masked Self-Attention: GPT에서는 예측할 단어 이후의 정보가 보이지 않도록 마스킹 처리  

---

### Pre-training 관련
Q. GPT-1의 Pre-training(사전 학습) 과정은 어떤 방식으로 진행되는가?  
A.  
- 대량의 비지도 학습 데이터(예: 위키백과, 웹 문서) 활용  
- Autoregressive Language Modeling: 주어진 문장에서 다음 단어를 예측하는 방식  

---

### Fine-tuning 관련
Q. GPT 모델에서 Fine-tuning이란?  
A.  
- 사전 학습된 모델을 특정 태스크에 맞게 조정하는 과정  
- Supervised learning 방식으로 추가 학습  
- 감성 분석, 번역, 요약 등 다양한 작업 수행 가능  

---

### Downstream Tasks 관련
Q. GPT 모델이 활용되는 주요 NLP 태스크 4가지는?  
A.  
1. Single Sentence Classification: 감성 분석, 주제 분류  
2. Textual Entailment: 두 문장이 논리적으로 연결되는지 판별  
3. Similarity: 두 문장의 의미적 유사도 비교  
4. Question Answering & Commonsense Reasoning: 질의응답 및 상식적 추론  

---

### GPT 모델 비교
Q. GPT-1, GPT-2, GPT-3의 주요 차이점은 무엇인가?  
A.  
- GPT-1: 1.17억 개의 파라미터, 제한된 데이터셋으로 학습됨.  
- GPT-2: 15억 개의 파라미터, 더 큰 데이터셋을 사용하여 학습됨.  
- GPT-3: 1750억 개의 파라미터, Few-Shot Learning 개념 도입.  

Q. GPT-2와 GPT-3의 공통점은 무엇인가?  
A.  
- Transformer 기반의 Decoder-only 모델  
- 대규모 코퍼스를 활용한 비지도 학습 (Pre-training)  
- Autoregressive Language Modeling 방식 사용  
- Zero-shot, One-shot, Few-shot Learning 지원  

---

### GPT-2와 이전 모델의 차이
Q. GPT-1의 주요 한계는 무엇인가?  
A.  
- 적은 양의 데이터와 파라미터로 학습되어 일반화 성능이 낮음  
- 특정 태스크를 수행하려면 Fine-tuning이 필요함  

Q. GPT-2의 핵심 개념은 무엇인가?  
A.  
- 비지도 학습을 통해 다양한 NLP 태스크 수행 가능  
- 사전 학습 데이터 크기와 모델 크기 증가  
- Fine-tuning 없이도 다양한 태스크 수행 가능  
- Zero-shot Learning 성능 향상  

---

### GPT-3의 발전
Q. GPT-3는 GPT-2보다 어떻게 발전했는가?  
A.  
- 파라미터 수 증가 (1750억 개)  
- Few-shot Learning 지원으로 훈련 없이도 예제만 제공해도 문제 해결 가능  
- API 기반으로 다양한 애플리케이션에서 활용 가능  

Q. Few-shot Learning이란 무엇인가?  
A.  
Few-shot Learning은 훈련 없이 몇 개의 예제만 제공해도 새로운 태스크를 해결할 수 있는 능력.  

Q. GPT-3가 다양한 태스크를 해결하는 방식은?  
A.  
- Prompt Engineering을 활용하여 적절한 입력을 제공  
- Zero-shot, One-shot, Few-shot Learning 방식 적용  

---

### Zero-shot, One-shot, Few-shot Learning
Q. Zero-shot Learning이란 무엇인가?  
A.  
예제 없이 태스크에 대한 설명만 제공하고 해결하는 방식.  

Q. One-shot Learning이란 무엇인가?  
A.  
예제 하나만 제공한 후 태스크를 해결하는 방식.  

Q. Few-shot Learning이란 무엇인가?  
A.  
여러 개의 예제를 제공한 후 태스크를 해결하는 방식.  

---

### GPT 모델의 한계
Q. GPT-2, GPT-3의 주요 한계는 무엇인가?  
A.  
1. 긴 문서의 문맥 유지 어려움 → 제한된 context window로 인해 문맥 유지가 어렵다.  
2. 계산 비용이 큼 → GPT-3는 1750억 개의 파라미터를 가지며 학습 및 추론 비용이 높다.  
3. 사전 학습된 데이터 편향 → 학습 데이터의 편향으로 인해 부적절한 답변이 생성될 가능성이 있다.  
4. 추론 가능성 부족 → 논리적 추론이나 사실 검증이 어려운 한계가 있다.  

---

