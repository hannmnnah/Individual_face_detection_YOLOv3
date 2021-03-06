# Face Recognition and Blur Project
일반 대중의 사생활을 침해하는 무단 영상 배포가 많은 이슈가 되고 있음. <br>
수작업 모자이크 편집기술은 많은 시간과 비용의 투자가 필요함. <br>
이를 개선하기 위해 본 프로젝트를 진행. <br>

#### 1. 데이터 수집
영화 '분노의 질주 : 더 세븐'의 영상 중 일부를 frame화. <br>


#### 2. 데이터 증강
일상적인 영상의 재생시간은 길지 않은 경우가 많으므로, 해당 프로젝트 또한 수집할 수 있는 데이터를 50 frames으로 제한하여 진행함.<br>
원본 50 frames을 다양한 Data Augmentation 작업을 통해서 최대 1,000 frames까지 증강하였음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110194874-35e34d00-7e7e-11eb-888e-1f0dce3bf612.JPG" width="600" height="400"/>
 <br>

#### 3. 모델 선정
CNN 기반의 다양한 모델이 존재하지만, 속도와 정확도면에 상대적으로 우수한 YOLO를 선정.<br><br>
<img src="https://user-images.githubusercontent.com/72846750/110195466-94112f80-7e80-11eb-997f-7cdb36b287aa.JPG" width="300" height="200"/>
 <br>
 
#### 4. 라벨링 작업
LabelImg툴을 이용하여 주인공 'Dom'과 그외 인물들 'else'를 구분하여 라벨링. <br><br>
<img src="https://user-images.githubusercontent.com/72846750/110195809-5530a900-7e83-11eb-81b3-fc7d59afcdc6.png" width="600" height="300"/>
 <br>
 
#### 5. 평가 기준
IoU, mAP

