# Face Detection and Blurring using YOLO and openCV

### 배경
Instagram, Youtube 등 소셜미디어, 영상 스트리밍 서비스 이용자 수가 지속적으로 증가함에 따라 일반 대중의 사생활을 침해하는 영상 및 사진 무단 배포가 많은 사회적 이슈로 제기되고 있으며, 
현재의 수작업 모자이크 편집 기술은 많은 시간과 비용이 요구되고 있어 이는 매우 비효율적임. 따라서 사생활 보호 및 작업의 효율성 향상을 위해 본 프로젝트를 진행하였음. <br>

### 1. 데이터 수집
영화 '분노의 질주 : 더 세븐'의 영상 중 일부를 frame화. <br>


### 2. 데이터 증강
일상적인 영상의 재생시간은 길지 않은 경우가 많으므로, 해당 프로젝트 또한 수집할 수 있는 데이터를 50 frames으로 제한하여 진행함. 원본 50 frames을 다양한 Data Augmentation 작업을 통해서 최대 1,000 frames까지 증강하였음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110194874-35e34d00-7e7e-11eb-888e-1f0dce3bf612.JPG" width="600" height="400"/>
 <br>

### 3. 모델 선정
CNN 기반의 다양한 모델이 존재하지만, 속도와 정확도면에 상대적으로 우수한 YOLO를 선정.<br><br>
<img src="https://user-images.githubusercontent.com/72846750/110199392-82895100-7e9b-11eb-9487-1cedc8368d28.png" width="300" height="200"/>
 <br>
 
### 4. 라벨링
LabelImg툴을 이용하여 주인공 'Dom'과 그외 인물들 'else'를 구분하여 라벨링. <br>
1차 라벨링후 YOLO Train 결과, 주인공 'Dom'의 헤어스타일과 유사한 인물 혹은 맨살이 많이 드러난 신체부위 일부를 'Dom'으로 인식하는 경우가 많았음. 헤어스타일을 제외한 이목구비 부분만 라벨링 진행.<br><br>
<img src="https://user-images.githubusercontent.com/72846750/110195809-5530a900-7e83-11eb-81b3-fc7d59afcdc6.png" width="550" height="310"/>
 <br>
 

### 5. 모델 Train
Darknet framework를 통해 YOLOv3, YOLOv4 모델링 진행. <br>

 
### 6. 평가
원본 50 frames으로만 YOLOv3 모델 Train후, Test 진행시 결과는 다음과 같음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110203338-f7b35100-7eb0-11eb-91d0-72846f198315.JPG" width="600"/><br><br><br>
여러 데이터 증강기법을 시도하여, 원본 50 frames보다는 높은 성능을 보이는 증강기법을 찾고자 하였으며, 결과는 다음과 같음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110203537-17974480-7eb2-11eb-82a9-d76eae2bb473.JPG" width="600"/><br><br><br>
최종적으로 가장 높은 성능을 보인 'Rotation, Flip, Zoom-out' 기법으로 YOLOv4 모델링을 추가적으로 진행하였으며, 그 결과는 다음과 같음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110203850-a9538180-7eb3-11eb-8e5d-84b7ef999de8.JPG" width="600"/><br>

### 5. 구조도 
<img src="https://user-images.githubusercontent.com/72846750/110202050-ace20b00-7ea9-11eb-998e-9b444cff468a.png" width="600" height="550"/>
 <br>

