# Contents
- [Transfer Learning](#transfer-learning)
    - [Transfer Learning 출현 배경](#transfer-learning-출현-배경)
    - [Transfer Learning 과정](#transfer-learning-과정)
    - [Transfer Learning 대표 모델](#transfer-learning-대표-모델)

<br>

# Transfer Learning

- Transfer Learning(전이 학습)은 한 번 학습한 모델을 다른 비슷한 작업(Task)에 적용하는 방법

- 즉, 새로운 작업(Task)을 수행할 때 처음부터 모델을 학습하는 것이 아니라, 이미 학습된 모델을 재사용하여 효율적으로 학습하는 방법

- 예시
    
    - 이미지 인식: 대량의 이미지 데이터셋(ex. ImageNet)에서 학습된 모델을 사용하여 새로운 이미지 분류 작업에 활용

    - 자연어 처리(NLP): 대량의 텍스트 데이터에서 미리 학습한 언어 모델(ex. BERT, GPT)을 가져와 감성 분석, 기계 번역 등에 활용

<br>

## Transfer Learning 출현 배경

- 기존 NLP 모델의 문제점

    1. 단어 임베딩의 한계

        - 기존 단어 임베딩(W2V, GloVe)은 문맥을 반영하지 못함
        
        - 다의어(ex. "bank"는 "은행"과 "둑" 두 가지 의미)가 구별되지 않음

    2. 대용량 학습 데이터 부족

        - 딥러닝 모델을 학습하려면 대량의 데이터가 필요하지만, 특정 Task에는 데이터가 부족할 수 있음

        - ex. 법률 문서 요약 모델을 만들려면 법률 문서 데이터가 많아야 함

    3. 모델 학습 비용이 큼

        - 처음부터 모델을 학습하면 시간과 비용(컴퓨팅 리소스)이 많이 듦

- 해결책: Transfer Learning (전이 학습) 활용

    - 대량의 데이터로 미리 학습(Pre-training)한 후, 작은 데이터셋에서 추가 학습(Fine-tuning)하여 빠르고 효율적으로 모델을 생성

<br>

## Transfer Learning 과정

1. Pre-training (사전 학습)

    - 대량의 텍스트 데이터에서 일반적인 언어 이해를 학습

    - ex. 문장 속에서 단어의 의미를 예측하는 방식으로 언어 모델 학습

    - 모델 예시: Word2Vec, GloVe, BERT, GPT, ELMo

2. Fine-tuning (미세 조정)

    - Pre-training된 모델을 가져와 특정 Task(감정 분석, 기계 번역, 질문응답 등)에 맞춰 추가 학습

    - 빠르게 모델을 학습할 수 있으며 적은 데이터로도 성능이 좋음

-> 즉, Pre-trianing에서 일반적인 언어 지식을 습득하고, Fine-tuning을 통해 특정 작업에 맞게 모델을 조정함

<br>

## Transfer Learning 대표 모델

1. ELMo (Embeddings from Language Models)

    - BiLSTM(양방향 LSTM) 기반의 문맥 임베딩 모델

    - 기존 Word2Vec, GloVe 보다 문맥을 잘 반영

    - 단점: RNN 계열이라 속도가 느림, 병렬 연산이 어려움

    - 한계: 이후 Transformer 기반 모델(BERT, GPT)이 등장하면서 덜 사용됨

2. BERT (Bidirectional Encoder Representations from Transformers)

    - Transformer 기반의 사전 학습 모델

    - 양방향으로 문맥을 학습하여 ELMo보다 뛰어난 성능

    - 감성 분석, 질문응답(QA), 개체명 인식(NER) 등 다양한 NLP Task에 활용

3. GPT (Generative pre-trained Transformer)

    - Transformer 기반의 생성형 언어 모델

    - BERT와 달리 한 방향으로 문장을 예측 (Autoregressive)

    - 대량의 데이터를 학습한 후, 추가 Fine-tuning 없이도 Zero-shot / Few-shot Learning 가능
