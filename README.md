# Face Recognition and Blur Project
일반 대중의 사생활을 침해하는 무단 영상 배포가 많은 이슈가 되고 있음. <br>
수작업 모자이크 편집을 기술은 많은 시간과 비용의 투자가 필요함. <br>
이를 개선하기 위해 본 프로젝트를 진행. <br>

#### 1. 데이터 수집 및 전처리
영화 '분노의 질주 : 더 세븐'의 영상 중 일부를 frame화. <br>
원본 50 frames을 다양한 Data Augmentation 작업을 통해서 최대 1,000 frames까지 증강하였음. <br>
Frame별로 주인공 'Dom'과 그외 인물들 'else'를 구분하여 라벨링. <br><br>
<img src="https://user-images.githubusercontent.com/72846750/110194874-35e34d00-7e7e-11eb-888e-1f0dce3bf612.JPG" width="600" height="400"/>
 <br>

#### 2. 평가 기준
IoU, mAP
