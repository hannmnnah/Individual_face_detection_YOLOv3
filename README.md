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


 
### 3. 라벨링
LabelImg툴을 이용하여 주인공 'Dom'과 그외 인물들 'else'를 구분하여 라벨링. <br>
1차 라벨링후 YOLO Train 결과, 주인공 'Dom'의 헤어스타일과 유사한 인물 혹은 맨살이 많이 드러난 신체부위 일부를 'Dom'으로 인식하는 경우가 많았음. 헤어스타일을 제외한 이목구비 부분만 라벨링 진행.<br><br>
<img src="https://user-images.githubusercontent.com/72846750/110195809-5530a900-7e83-11eb-81b3-fc7d59afcdc6.png" width="550" height="310"/>
 <br>
 
### 4. 모델 선정
CNN 기반의 다양한 모델이 존재하지만, 속도와 정확도면에 상대적으로 우수한 YOLO를 선정.<br><br>
<img src="https://user-images.githubusercontent.com/72846750/110199392-82895100-7e9b-11eb-9487-1cedc8368d28.png" width="300" height="200"/>
 <br>
 

### 5. 모델 Train 

YOLOv3
- Darknet framework로 진행.
- Parameter 수정
  - filters = 21
  - max_batches = 6000
  - steps = 4800, 5400
  - classes = 2

YOLOv4
- Darknet framework로 진행.
- Parameter 추가 수정
  - width = 512
  - height = 512

 
### 6. 모델 평가
YOLOv3 모델을 기반으로 성능 평가를 먼저 진행하였음. <br>
원본 50 frames으로만 Train하였을때, 결과는 다음과 같음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110204454-6941ce00-7eb6-11eb-84a0-9cfa6d5bfd60.JPG" width="600"/><br>

여러 데이터 증강기법을 시도하였으며, 그 중에서 'Rotation, Flip, Zoom-out'가 가장 높은 성능을 보였으며, 그 결과는 다음과 같음. 
(Rotation의 각도는 10도이하로 하였음. 각도를 그 이상 다양화할 경우 오히려 성능 저하) <br>
<img src="https://user-images.githubusercontent.com/72846750/110204466-765ebd00-7eb6-11eb-9146-61f1d3b55595.JPG" width="600"/><br>

위의 데이터셋으로 YOLOv4 모델링을 추가적으로 진행하였으며, 그 결과는 다음과 같음. <br>
<img src="https://user-images.githubusercontent.com/72846750/110204472-7f4f8e80-7eb6-11eb-9d87-2d00ea3e6c56.JPG" width="600"/><br>



bounding box를 통해서 확인할 수 있듯이, 모델 성능과 함께 점차적으로 모든 인물을 인식해냈으나, 분류에는 어려움을 겪음. <br>

원본 with YOLOv3<br>
<img src="https://user-images.githubusercontent.com/72846750/110206497-5bde1100-7ec1-11eb-8277-61fc493829bf.jpg" width="600"/><br><br><br>
<img src="https://user-images.githubusercontent.com/72846750/110206894-c728e280-7ec3-11eb-8a53-3ed26527f5da.png" width="600"/><br><br><br>

Rotation, Flip, Zoom-out with YOLOv3<br>
<img src="https://user-images.githubusercontent.com/72846750/110206568-d7d85900-7ec1-11eb-8fc5-99dc859aec3e.jpg" width="600"/><br><br><br>
　　　　　　　　　　　　🔻<br>
Rotation, Flip, Zoom-out with YOLOv4<br>
<img src="https://user-images.githubusercontent.com/72846750/110206576-e757a200-7ec1-11eb-9534-22b6801dc016.jpg" width="600"/><br><br><br>





### 7. 구조도 
<img src="https://user-images.githubusercontent.com/72846750/110202050-ace20b00-7ea9-11eb-998e-9b444cff468a.png" width="600" height="550"/>
 <br>

