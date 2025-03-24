### Latent Space 관련 카드  

Q: Latent Space란?  
A: 머신 러닝에서 데이터를 압축된 형태로 표현하는 잠재 공간. 원본 데이터를 인코더 등을 통해 저차원 또는 추상적인 형태로 변환한 공간.  

Q: 머신 러닝에서 데이터를 압축된 형태로 표현하는 공간을 무엇이라고 하는가?  
A: Latent Space (잠재 공간)  

Q: Latent Space가 중요한 이유 4가지는?  
A:  
1. 차원 축소: 계산량 감소 및 중요한 패턴 포착  
2. 특징 추출: 원본 데이터의 핵심 정보 내재화  
3. 생성 모델: GAN, VAE 등을 통해 새로운 데이터 생성  
4. 데이터 구조 해석: 데이터 간의 관계와 분포를 시각화 및 분석 가능  

Q: 다음 중 Latent Space의 역할이 아닌 것은?  
1. 데이터의 차원을 축소하여 복잡도를 줄임  
2. 데이터의 핵심 특징을 추출하는 공간  
3. 데이터를 손실 없이 원래 형태로 복원하는 공간  
4. GAN, VAE 등에서 활용되어 새로운 데이터 생성 가능  

A: 3번 (Latent Space는 압축된 표현을 가지므로 원래 데이터를 완벽하게 복원하는 것이 목적이 아님)

---

### Autoencoder 관련 카드  

Q: Autoencoder란?  
A: 입력 데이터를 압축(Encoding)하고 다시 복원(Decoding)하는 비지도 학습 기반 신경망.  

Q: Autoencoder의 핵심 목표는?  
A: 데이터를 저차원의 Latent Space에 효율적으로 표현하는 것.  

Q: Autoencoder의 주요 구성 요소 3가지는?  
A:  
1. 인코더 (Encoder): 입력 데이터를 압축하여 Latent Space로 변환  
2. 잠재 공간 (Latent Space): 데이터의 중요한 특징을 추출  
3. 디코더 (Decoder): 잠재 공간의 정보를 원본과 유사한 데이터로 복원  

Q: Autoencoder가 활용되는 대표적인 4가지 사례는?  
A:  
1. 차원 축소 (Dimensionality Reduction)  
2. 노이즈 제거 (Denoising)  
3. 이상 탐지 (Anomaly Detection)  
4. 데이터 생성 (Generative Models)  

Q: Autoencoder가 차원 축소에서 PCA보다 강력한 이유는?  
A: PCA는 선형 차원 축소만 가능하지만, Autoencoder는 비선형 관계까지 학습할 수 있기 때문.  

Q: Autoencoder가 Denoising에 효과적인 이유는?  
A: 원본 데이터를 압축했다가 복원하는 과정에서 노이즈를 자연스럽게 제거하기 때문.  

Q: Autoencoder 기반 이상 탐지(Anomaly Detection)의 원리는?  
A: 정상 데이터로 학습한 Autoencoder는 정상 데이터 복원 오류가 낮고, 이상 데이터는 복원 오류가 크게 나타나는 특징을 이용함.  

---

### VAE (Variational Autoencoder) 관련 카드  

Q: VAE(Variational Autoencoder)의 등장 이유는?  
A: 기존 Autoencoder의 한계를 보완하여, 잠재공간을 해석 가능하고 연속적으로 만들며 더 나은 데이터 생성을 가능하게 하기 위해.  

Q: 기존 Autoencoder의 한계 3가지는?  
A:  
1. 잠재공간(latent space)의 해석이 어려움  
2. 학습된 잠재공간이 연속적이지 않음  
3. 생성된 데이터의 품질이 낮거나 원본과 차이가 큼  

Q: VAE가 기존 Autoencoder보다 뛰어난 이유는?  
A: 확률 분포 기반 샘플링을 통해 더 자연스럽고 해석 가능한 Latent Space를 학습할 수 있기 때문.  

Q: VAE가 Autoencoder의 한계를 극복하는 3가지 원리는?  
A:  
1. 잠재공간을 확률적인 형태로 변환  
2. 샘플링 과정에서 부드러운 변화 유도  
3. 학습된 공간을 일정한 구조로 유지  

Q: VAE는 어떻게 잠재 공간을 확률적인 형태로 변환하는가?  
A: 데이터 포인트를 하나의 값이 아닌 범위(확률 분포)로 변환하여 특정 위치가 아닌 여러 가능성을 가진 공간에서 표현.  

Q: VAE가 새로운 데이터를 생성할 수 있는 이유는?  
A: 샘플링을 통해 기존 데이터와 유사하면서도 새로운 데이터 포인트를 만들어낼 수 있기 때문.  

---

### NLU(Natural Language Understanding) 관련 카드  

Q: NLU(Natural Language Understanding)란?  
A: 자연어 처리(NLP)의 하위 분야로, 컴퓨터 소프트웨어를 활용하여 음성이나 텍스트의 입력된 문장을 이해하는 기술  

Q: 자연어 처리(NLP)의 하위 분야 중 음성이나 텍스트의 입력된 문장을 이해하는 기술은?  
A: NLU(Natural Language Understanding)  

---

### NLG(Natural Language Generation) 관련 카드  

Q: NLG(Natural Language Generation)란?  
A: 컴퓨터가 자연어 텍스트를 생성하여 인간과 유사한 텍스트나 음성을 만들어내는 기술  

Q: 인간과 유사한 자연어 텍스트를 생성하는 기술은?  
A: NLG(Natural Language Generation)  

---

### 자연어 처리의 어려움 관련 카드  

Q: 자연어 처리(NLP)에서 어려운 점 3가지는?  
A:  
1. 문맥에 따른 모호성  
2. 표현의 중의성  
3. 규칙의 예외성  

Q: 문맥에 따라 다르게 해석될 수 있는 자연어의 특징은?  
A: 모호성  

Q: 하나의 표현이 여러 가지 의미를 가질 수 있는 자연어의 특징은?  
A: 중의성  

---

### 교착어, 굴절어, 고립어 관련 카드  

Q: 교착어란?  
A: 어간에 접사가 붙어 단어를 이루고 의미와 문법적 기능이 정해지는 언어 (예: 한국어, 일본어, 몽골어)  

Q: 단어의 형태가 변하면서 문법적 기능이 변하는 언어는?  
A: 굴절어 (예: 라틴어, 독일어, 러시아어)  

Q: 단어의 형태가 변하지 않고 단어의 위치나 문맥으로 문법적 기능을 구분하는 언어는?  
A: 고립어 (예: 영어, 중국어)  

---

### 한국어 자연어 처리의 어려움 관련 카드  

Q: 한국어가 자연어 처리에서 어려운 이유 3가지는?  
A:  
1. 교착어 특성으로 인해 같은 단어라도 다양한 조합이 존재함  
2. 주어 생략 및 단어 순서의 유연성이 높음  
3. 띄어쓰기가 정확하지 않아 분절 단계에서 혼란 발생  

Q: 한국어에서 단어의 형태가 변하면서 문법적 기능이 변하는 이유는?  
A: 한국어가 교착어이기 때문  

Q: 한국어에서 띄어쓰기 문제로 인해 자연어 처리가 어려운 이유는?  
A: 띄어쓰기가 제대로 지켜지지 않으면 단어 분절 과정에서 혼란이 발생하기 때문  

---

### 언어학의 접근 방법 관련 카드  

Q: 자연어 처리에서 규칙 기반 접근이란?  
A: 언어학적 지식을 활용하여 문법적인 규칙을 만들어 자연어를 처리하는 방식  

Q: 대량의 데이터를 활용하여 자연어 처리를 수행하는 접근 방식은?  
A: 통계 기반 접근  

Q: 인공신경망을 활용하여 자연어를 처리하는 접근 방식은?  
A: 신경망 기반 접근  

---

### 전통적인 자연어 처리 파이프라인 관련 카드  

Q: 전통적인 자연어 처리 파이프라인의 순서를 나열하시오.  
A:  
1. Document  
2. Pre-process  
3. Tokenize, Sentence Split  
4. Part of speech tagger  
5. Chunker  
6. Class Matching  
7. Querying  
8. Post-process  
9. Structured Data  

---

### 음절, 형태소, 어절, 품사 관련 카드  

Q: 형태소란?  
A: 의미를 가지는 최소 단위  

Q: 띄어쓰기 단위로 나뉘는 언어 요소는?  
A: 어절  

Q: 단어의 문법적 기능을 나타내는 분류는?  
A: 품사  

Q: 형태소를 분석하고 그 관계를 연구하는 언어학 분야는?  
A: 형태론 (Morphology)  

---

### 형태소의 종류 관련 카드  

Q: 자립형태소란?  
A: 독립적으로 사용될 수 있는 형태소로 문장에서 독자적인 의미를 가짐 (예: 명사, 동사, 형용사)  

Q: 독립적으로 사용되지 못하고 다른 형태소와 결합해야 의미를 가지는 형태소는?  
A: 의존 형태소  

Q: 사물이나 개념을 직접 지칭하며 실질적인 의미를 가진 형태소는?  
A: 실질 형태소(어휘 형태소)  

Q: 문법적 관계를 나타내며 독립적인 의미를 가지지 않는 형태소는?  
A: 형식 형태소(문법 형태소)  

---

### 통사론(Syntax) 관련 카드  

Q: 문장의 구조와 형식을 연구하는 언어학 분야는?  
A: 통사론(Syntax)  

Q: 동일한 문장이 여러 개의 해석을 가질 수 있는 현상은?  
A: 구조적 모호성 (Structural Ambiguity)  

Q: 문법 규칙이 자기 자신을 호출할 수 있는 성질로, 무한한 문장 생성을 가능하게 하는 것은?  
A: 반복(Recursion)  

Q: "철수가 책을 읽었다."를 수동태로 변환하면?  
A: "책이 철수에 의해 읽혔다."  

---

### 의미론(Semantics) 관련 카드  

Q: 개념적 의미(Conceptual Meaning)란?  
A: 단어의 기본적인 의미 요소  

Q: 연상적 의미(Associative Meaning)란?  
A: 개인적, 사회적 맥락에 따라 확장된 의미  

Q: 단어의 의미적 속성을 분석하여 의미를 구성하는 최소 단위를 나누는 방법은?  
A: 의미자질(Semantic Features)  

Q: 문장에서 각 성분이 담당하는 의미적 역할을 나타내는 개념은?  
A: 의미역(Semantic Roles)  

---

### 화용론(Pragmatics) 관련 카드  

Q: 문맥과 사회적 요인에 따라 의미가 어떻게 변화하는지를 연구하는 분야는?  
A: 화용론(Pragmatics)  

---

### 자연언어처리(NLP)에서의 언어학 관련 카드  

Q: 자연언어처리(NLP)에서 주요 분석 기법 7가지는?  
A:  
1. 토큰화(Tokenization)  
2. 품사 태깅(POS Tagging)  
3. 구문 분석(Syntax Parsing)  
4. 의미 분석(Semantic Analysis)  
5. 개체명 인식(NER)  
6. 문법 교정(GEC)  
7. 의존 구문 분석(Dependency Parsing)  

Q: 텍스트를 의미 단위로 나누는 과정을 무엇이라고 하는가?  
A: 토큰화(Tokenization)  

Q: 각 단어에 품사 정보를 부착하는 과정은?  
A: 품사 태깅(POS Tagging)  

Q: 문장의 문법적 구조를 분석하는 기법은?  
A: 구문 분석(Syntax Parsing)  

Q: 문장의 의미를 해석하는 분석 기법은?  
A: 의미 분석(Semantic Analysis)  

Q: 고유명사(사람, 장소, 조직 등)를 식별하는 기술은?  
A: 개체명 인식(NER)  

Q: 문장의 문법 오류를 수정하는 기법은?  
A: 문법 교정(GEC)  

Q: 단어 간의 종속 관계를 분석하는 기법은?  
A: 의존 구문 분석(Dependency Parsing)  

---

### BERT와 언어 구조 관련 카드  

Q: BERT 모델이 단어 간 관계를 학습하는 방식은?  
A: 문맥을 고려하여 다층적인 의미 표현을 학습함  

Q: 기존 BERT 모델에 언어학적 지식을 추가하여 성능을 향상시킨 모델은?  
A: LIMIT-BERT  

---

### 전처리(Preprocessing) 관련 카드  

Q: 자연어 처리에서 전처리(Preprocessing)의 주요 기법 4가지는?  
A:  
1. HTML 태그, 특수문자, 이모티콘 제거  
2. 정규표현식(Regular Expression) 사용  
3. 불용어(Stopword) 제거  
4. 어간추출(Stemming) vs. 표제어 추출(Lemmatization)  

Q: 불필요한 특수문자와 이모티콘을 제거하는 이유는?  
A: 비언어적 요소를 제거하여 데이터의 품질을 높이기 위해  

Q: 정규표현식(Regular Expression)의 역할은?  
A: 패턴 기반으로 텍스트를 정제하는 기법  

Q: 불용어(Stopword)란?  
A: 자주 등장하지만 의미가 적은 단어 (예: "그리고", "하지만")  

Q: 어간추출(Stemming)과 표제어 추출(Lemmatization)의 차이점은?  
A:  
- 어간추출: 단순 변환 (예: ‘running’ → ‘run’)  
- 표제어 추출: 문맥을 고려하여 정확한 기본형 반환 (예: ‘better’ → ‘good’)  

Q: 한국어 형태소 분석 라이브러리는?  
A: KoNLPy  

Q: 영어 자연어 처리 도구는?  
A: NLTK  

---

### Lemmatization (표제어 추출) 관련 카드  

Q: Lemmatization이란?  
A: 단어의 원형을 찾아주는 과정  

Q: "running"의 표제어 추출 결과는?  
A: "run"  

Q: 표제어 추출(Lemmatization)과 어간추출(Stemming)의 차이는?  
A:  
- Lemmatization: 문법적으로 정확한 원형 유지  
- Stemming: 단순한 형태 변환  

Q: 표제어 추출이 적용되는 대표적인 사례는?  
A: 검색 엔진, 텍스트 정규화  

---

### Levenshtein Distance (편집 거리) 관련 카드  

Q: Levenshtein Distance란?  
A: 두 문자열을 같게 만들기 위한 최소한의 편집 작업(삽입, 삭제, 치환)의 수  

Q: 편집 거리(Levenshtein Distance)에서 가능한 세 가지 작업은?  
A: 삽입, 삭제, 치환  

Q: Levenshtein Distance가 활용되는 대표적인 분야 3가지는?  
A:  
1. 오타 수정 (문서 작성 시 오타 교정)  
2. 자연어 처리 (문장 유사도 계산, 텍스트 검색)  
3. 생물정보학 (DNA, RNA 서열 비교)  

---

### 형태소 분석기 관련 카드  

Q: 형태소(Morpheme)란?  
A: 의미를 가지는 최소 단위  

Q: 자립형 형태소란?  
A: 혼자서도 쓰일 수 있는 형태소 (예: 명사, 동사, 형용사)  

Q: 의존형 형태소란?  
A: 혼자 사용될 수 없고, 다른 형태소와 결합해야 의미를 형성하는 형태소 (예: 조사, 접사, 어미)  

Q: 형태소 분석(Morphological Analysis)이란?  
A: 문장을 형태소 단위로 나누고 각 형태소의 품사를 분석하는 과정  

Q: 주요 한국어 형태소 분석 라이브러리 4가지는?  
A: MeCab, KoNLPy, Khaiii, ETRI  

---

### 품사 태깅(POS Tagging) 관련 카드  

Q: 품사 태깅(POS Tagging)이란?  
A: 문장에서 각 단어(형태소)의 품사를 분석하여 태그를 부착하는 과정  

Q: 품사 태깅의 주요 목적 3가지는?  
A:  
1. 문법 분석  
2. 문장 구조 이해  
3. NLP 모델 학습  

Q: 품사 태깅에서 활용되는 주요 기법 3가지는?  
A:  
1. 사전 기반 분석 (Dictionary-based)  
2. 규칙 기반 분석 (Rule-based)  
3. 통계 기반 모델 (Statistical-based)  

---

### 딥러닝 기반 형태소 분석 및 품사 태깅 관련 카드  

Q: 딥러닝 기반 품사 태깅에서 활용되는 주요 모델 4가지는?  
A:  
1. RNN  
2. LSTM  
3. BiLSTM-CRF  
4. Transformer & BERT  

Q: BiLSTM이 기존 LSTM보다 효과적인 이유는?  
A: 문장의 앞뒤 문맥을 모두 고려하여 품사 태깅 정확도를 향상시키기 때문  

Q: Transformer 모델이 NLP에서 혁신적인 이유는?  
A: Self-Attention을 사용하여 문맥을 효과적으로 학습할 수 있기 때문  

---

### HMM: Hidden Markov Model 관련 카드  

Q: Hidden Markov Model(HMM)이란?  
A: 관찰된 데이터 뒤에 숨겨진(hidden) 상태(State)들을 확률적으로 모델링하는 기법  

Q: HMM 기반 품사 태깅에서 숨겨진 상태(Hidden State)는 무엇을 의미하는가?  
A: 품사 (예: 명사, 동사, 조사 등)  

Q: HMM의 핵심 요소 5가지는?  
A:  
1. 상태 집합 (S)  
2. 관찰 집합 (O)  
3. 상태 전이 확률 (A)  
4. 방출 확률 (B)  
5. 초기 상태 확률 (π)  

---

### CRF (Conditional Random Field) 관련 카드  

Q: CRF(Conditional Random Field)란?  
A: 순차 데이터(sequence data)에서 문맥(Context)을 고려하여 태깅하는 지도 학습 기반의 확률 모델  

Q: CRF의 주요 활용 분야 3가지는?  
A:  
1. 품사 태깅(POS Tagging)  
2. 개체명 인식(NER)  
3. 형태소 분석  

Q: CRF가 HMM보다 더 정교한 태깅이 가능한 이유는?  
A: CRF는 문맥 전체를 활용하여 태깅할 수 있기 때문  

---

### HMM vs. CRF 비교 카드  

Q: HMM과 CRF의 차이점은?  
A:  
- HMM: 이전 한 개의 상태만 고려하여 품사 태깅 → 긴 문맥을 고려하기 어려움  
- CRF: 문맥 전체를 활용하여 태깅 가능 → 학습 데이터가 많아야 함  

Q: 이전 한 개의 상태만 고려하여 품사 태깅을 수행하는 모델은?  
A: HMM (Hidden Markov Model)  

Q: 문맥 전체를 반영하여 품사 태깅을 수행하는 모델은?  
A: CRF (Conditional Random Field)  

---

### CRF의 주요 요소 카드  

Q: CRF의 주요 요소 3가지는?  
A:  
1. X (Observation Sequence) - 관찰된 데이터 (예: 단어 시퀀스)  
2. Y (Label Sequence) - 예측해야 할 라벨 (예: 품사 태그)  
3. Feature Function (특징 함수) - 문맥적 특징을 반영하는 함수  

Q: 문장에서 CRF가 태깅할 때 사용하는 Feature Function의 역할은?  
A: 문맥 정보를 반영하여 최적의 태깅을 수행하는 함수  

---

### CRF vs. BiLSTM-CRF vs. BERT 기반 모델 비교 카드  

Q: CRF와 BiLSTM-CRF, BERT 기반 모델의 차이점은?  
A:  
- CRF: 문맥을 반영한 태깅 가능, 높은 해석 가능성  
- BiLSTM-CRF: LSTM이 문맥을 학습하고 CRF가 최적의 태깅 시퀀스 결정  
- BERT 기반 모델: 사전 학습된 언어 모델로 문맥을 완벽히 반영하여 최고 성능 제공  

Q: BiLSTM-CRF가 CRF보다 뛰어난 이유는?  
A: BiLSTM이 문맥(Context)을 학습한 후, CRF가 최적의 태깅을 결정하기 때문  

Q: BERT 기반 모델이 BiLSTM-CRF보다 높은 성능을 보이는 이유는?  
A: 사전 학습된 언어 모델을 활용하여 문맥을 더욱 깊이 반영할 수 있기 때문  

---

### Character-Level BiLSTM-CRF 관련 카드  

Q: Character-Level BiLSTM-CRF란?  
A: 단어가 아닌 문자(Character) 단위로 처리하는 BiLSTM-CRF 모델  

Q: Character-Level BiLSTM-CRF의 주요 장점 3가지는?  
A:  
1. OOV(Out-of-Vocabulary) 문제 해결 가능  
2. 띄어쓰기 오류 보완 가능  
3. 소형 데이터셋에서도 효과적  

Q: Character-Level BiLSTM-CRF가 OOV 문제를 해결할 수 있는 이유는?  
A: 단어가 아닌 문자 단위로 학습하기 때문  

---

### 개체명 인식 (NER) 관련 카드  

Q: 개체명 인식(NER)이란?  
A: 문장에서 특정 개체(이름, 장소, 조직, 날짜 등)를 식별하는 자연어 처리 기술  

Q: NER의 주요 응용 분야 3가지는?  
A:  
1. 검색 엔진 (Search Engine)  
2. 챗봇 (Chatbot)  
3. 금융 및 뉴스 분석  

Q: NER에서 개체명(Entity)의 주요 유형 3가지는?  
A:  
1. PER (Person) - 인물 이름 (예: 스티브 잡스)  
2. LOC (Location) - 지명 (예: 서울, 미국)  
3. ORG (Organization) - 기업 및 조직 (예: 애플, 삼성전자)  

Q: 문장에서 개체명을 인식하는 대표적인 딥러닝 기반 모델은?  
A: BiLSTM-CRF 및 BERT-CRF  

---

### 태깅 시스템 관련 카드  

Q: 태깅 시스템(Tagging System)이란?  
A: 데이터를 특정 범주(Category) 또는 속성(Attribute)으로 분류하여 관리하는 기법  

Q: 태깅 시스템의 주요 유형 3가지는?  
A:  
1. 수동 태깅 (Manual Tagging)  
2. 자동 태깅 (Auto Tagging)  
3. 하이브리드 태깅 (Hybrid Tagging)  

Q: 품사 태깅(POS Tagging)이란?  
A: 문장에서 각 단어에 품사(Part-of-Speech, POS) 정보를 부착하는 작업  

Q: 감성 분석 태깅(Sentiment Tagging)이란?  
A: 문장에서 감정을 분석하여 긍정/부정 태그를 부착하는 태깅 기법  

---

### 태깅 시스템의 주요 응용 분야 관련 카드  

Q: 태깅 시스템이 활용되는 주요 분야 3가지는?  
A:  
1. 검색 엔진 (Search Engine)  
2. 전자상거래 (E-commerce)  
3. 자연어 처리 (NLP)  

Q: 감성 분석 태깅(Sentiment Tagging)의 대표적인 딥러닝 모델 2가지는?  
A:  
1. LSTM + Attention  
2. BERT + Sentiment Classification  

Q: 텍스트 분류 태깅(Text Classification Tagging)이란?  
A: 문서를 특정 카테고리로 태깅하는 기법  

--- 

아래는 학습 노트를 기본 카드 (뒤집기 포함, Basic and reversed) 형식으로 변환한 Anki 카드 목록입니다.

---

### 정보추출 (Information Extraction, IE) 관련 카드  

Q: 정보추출(IE)이란?  
A: 비정형 텍스트에서 의미 있는 정보를 자동으로 식별하고 구조화하는 과정  

Q: 비정형 텍스트에서 의미 있는 정보를 자동으로 식별하고 구조화하는 과정은?  
A: 정보추출(Information Extraction, IE)  

Q: 정보추출(IE)에서 사용하는 주요 방법 3가지는?  
A:  
1. 개체명 인식(NER)  
2. 관계 추출(RE)  
3. 이벤트 추출(EE)  

Q: 개체명 인식(NER)이란?  
A: 문장에서 사람, 장소, 조직, 날짜, 수량 등의 개체(Entity)를 인식하는 과정  

Q: 문장에서 사람, 장소, 조직, 날짜, 수량 등의 개체(Entity)를 인식하는 기술은?  
A: 개체명 인식(NER, Named Entity Recognition)  

Q: 관계 추출(RE)이란?  
A: 문장에서 인식된 개체들 간의 관계(Relation)를 추출하는 과정  

Q: 문장에서 인식된 개체들 간의 관계(Relation)를 추출하는 기술은?  
A: 관계 추출(RE, Relation Extraction)  

Q: 이벤트 추출(EE)이란?  
A: 특정 이벤트(Event)와 관련된 정보를 추출하는 과정  

Q: 특정 이벤트(Event)와 관련된 정보를 추출하는 기술은?  
A: 이벤트 추출(EE, Event Extraction)  

---

### 정보추출(IE) 접근 방법 관련 카드  

Q: 정보추출(IE)에서 전통적인 접근법 2가지는?  
A:  
1. 규칙 기반(Rule-based) 방법  
2. 기계 학습 기반(Statistical) 방법  

Q: 정보추출(IE)에서 딥러닝 기반 접근법 2가지는?  
A:  
1. BiLSTM-CRF (Bidirectional LSTM + CRF)  
2. Transformer 기반 (BERT, GPT)  

---

### 텍스트 분류 (Text Classification) 관련 카드  

Q: 텍스트 분류란?  
A: 주어진 문장을 특정 카테고리로 자동 분류하는 NLP 기술  

Q: 텍스트 분류가 활용되는 대표적인 4가지 분야는?  
A:  
1. 뉴스 기사 분류  
2. 감성 분석  
3. 스팸 필터링  
4. 법률 문서 자동 분류  

Q: 텍스트 분류에서 전통적인 기법 2가지는?  
A:  
1. TF-IDF + 머신러닝 모델  
2. Word2Vec + 분류 모델  

Q: TF-IDF의 의미는?  
A: Term Frequency - Inverse Document Frequency, 단어의 빈도와 희귀성을 반영하여 벡터화하는 기법  

Q: 텍스트 분류에서 딥러닝 기반 기법 3가지는?  
A:  
1. CNN for Text Classification  
2. LSTM / BiLSTM for Text Classification  
3. Transformer 기반 (BERT, GPT)  

---

### 문서 요약 (Text Summarization) 관련 카드  

Q: 문서 요약이란?  
A: 긴 텍스트에서 핵심 정보를 자동으로 요약하는 NLP 기술  

Q: 문서 요약의 두 가지 주요 방법은?  
A:  
1. 추출 요약 (Extractive Summarization)  
2. 생성 요약 (Abstractive Summarization)  

Q: 추출 요약(Extractive Summarization)이란?  
A: 문장에서 중요한 문장을 직접 선택하여 요약하는 방식  

Q: 생성 요약(Abstractive Summarization)이란?  
A: 원문의 의미를 이해하고 새로운 문장으로 요약하는 방식  

---

### 통계 기반 NLP (Statistical NLP) 관련 카드  

Q: 통계 기반 NLP에서 사용되는 주요 기법 3가지는?  
A:  
1. n-그램 (n-gram)  
2. Hidden Markov Model (HMM)  
3. CRF (Conditional Random Field)  

Q: n-그램(n-gram)이란?  
A: 문장에서 연속된 n개의 단어를 묶어 분석하는 기법  

Q: 개체명 인식(NER) 등에 활용되는 확률 모델은?  
A: CRF (Conditional Random Field)  

---

### 뉴럴심볼릭 기반 자연어처리 (Neural-Symbolic NLP) 관련 카드  

Q: 뉴럴심볼릭 NLP란?  
A: 기호 기반(Symbolic AI)과 딥러닝(Neural Networks)을 결합한 자연어 처리 방식  

Q: 뉴럴심볼릭 NLP에서 결합되는 두 가지 요소는?  
A:  
1. 딥러닝(Neural Networks) → 데이터에서 패턴 학습  
2. 기호 논리(Semantic Logic) → 언어 규칙, 지식 그래프 활용  

---

### 딥러닝 기반 자연어 처리 관련 카드  

Q: RNN (Recurrent Neural Network)이란?  
A: 순차 데이터(문장, 음성 등)를 처리하는 인공신경망  

Q: LSTM (Long Short-Term Memory)이란?  
A: 장기 의존성(Long-term dependency) 문제를 해결한 RNN 모델  

Q: Transformer 모델이 RNN보다 뛰어난 이유는?  
A: 병렬 연산이 가능하여 학습 속도가 빠르고, 장기 의존성을 효과적으로 학습할 수 있기 때문  

Q: BERT (Bidirectional Encoder Representations from Transformers)의 주요 특징 2가지는?  
A:  
1. 양방향(Bidirectional) 학습을 통해 문맥을 깊이 이해  
2. MLM (Masked Language Modeling)과 NSP (Next Sentence Prediction) 활용  

Q: GPT(Generative Pretrained Transformer)의 특징은?  
A: 자연어 생성(Language Generation)에 특화된 모델  

Q: BART (Bidirectional Auto Regressive Transformers)의 특징은?  
A: BERT와 GPT의 개념을 결합하여 문서를 인코딩하고 자연스럽게 문장을 생성할 수 있도록 설계  

---

### 딥러닝 기반 개체명 인식 (NER) 관련 카드  

Q: 개체명 인식(NER)의 대표적인 딥러닝 모델은?  
A: BERT 기반 NER 모델  

Q: Transformer 기반 개체명 인식 모델의 장점은?  
A: 문맥 정보를 반영하여 높은 정확도를 제공  

---
