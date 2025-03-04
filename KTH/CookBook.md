### Latent Space란?
Q: Latent Space(잠재 공간)이란?  
A:  
- 머신러닝에서 데이터를 압축된 형태로 표현하는 공간  
- 원본 데이터를 인코더를 통해 낮은 차원으로 변환하여 추상적으로 표현  

---

### Latent Space의 중요한 이유
Q: Latent Space가 중요한 이유 4가지는?  
A:  
1. 차원 축소: 고차원 데이터를 낮은 차원으로 줄여 계산량 감소  
2. 특징 추출: 데이터의 핵심 요소를 추출  
3. 생성 모델: GAN, VAE와 같은 모델에서 데이터 생성  
4. 데이터 구조 해석: 고차원 데이터의 분포와 관계를 분석  

---

### Autoencoder란?
Q: Autoencoder의 정의는?  
A:  
- 입력 데이터를 압축(Encoding)하고 다시 복원(Decoding)하는 신경망  
- 비지도 학습 방식 사용  
- 데이터의 중요한 특징을 Latent Space에 표현  

---

### Autoencoder의 구조
Q: Autoencoder의 구성 요소 3가지는?  
A:  
1. Encoder: 입력 데이터를 압축하여 Latent Space로 변환  
2. Latent Space: 데이터의 핵심 특징을 저장하는 공간  
3. Decoder: Latent Space의 정보를 이용해 원본 데이터 복원  

---

### Autoencoder의 활용 사례
Q: Autoencoder는 어떤 분야에서 활용될 수 있는가? (4가지 이상)  
A:  
1. 차원 축소: PCA보다 강력한 비선형 차원 축소 가능  
2. 노이즈 제거: Denoising Autoencoder(DAE)를 활용  
3. 이상 탐지: Reconstruction Error를 활용한 이상 감지  
4. 데이터 생성: Variational Autoencoder(VAE)를 활용  
5. 추천 시스템: 사용자 행동 데이터를 인코딩하여 추천 성능 향상  

---

### Variational Autoencoder(VAE)란?
Q: Variational Autoencoder(VAE)란?  
A:  
- Autoencoder의 한계를 보완한 모델  
- 잠재 공간을 해석 가능하고 연속적으로 만들어 더 나은 데이터 생성 가능  

---

### VAE가 Autoencoder의 한계를 극복하는 원리
Q: VAE는 Autoencoder의 어떤 한계를 어떻게 극복하는가?  
A:  
1. 잠재 공간을 확률적 형태로 변환  
   - 하나의 고정된 값이 아닌 확률 분포로 변환하여 연속적인 표현 가능  
2. 샘플링 과정에서 부드러운 변화 유도  
   - 학습한 데이터만 복원하는 기존 AE와 달리 새로운 데이터 생성 가능  
3. 잠재 공간 구조 유지  
   - 비슷한 데이터끼리 가까운 위치에 배치해 일관된 결과 생성  

---

### VAE의 장점
Q: VAE의 장점 3가지는?  
A:  
1. 잠재 공간을 해석 가능하게 변환  
2. 연속적인 데이터 변환이 가능  
3. 고품질의 새로운 데이터를 생성  

---
