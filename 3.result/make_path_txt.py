# **********************************************************
# 변수 설명 :
#                   1. 대상 폴더 (txt파일에 입력될 path기 때문에 절대경로 추천, 마지막에 꼭 '/' 넣어줘야함.)
#                       image_directory = '/content/gdrive/MyDrive/~~~ img_path/'
#                   2. 확장자
#                       extension = "*.jpg"
#                   3. 텍스트 파일이 저장될 경로
#                       save_at = './re.txt'
# *********************************************************
def make_data_path(image_directory,extension, save_at):
    import glob
    import os

    #대상 폴더에서 지정한 확장자를 가진 파일들의 경로를 리스트화
    files = sorted(glob.glob(image_directory + extension))
    print(files)

    #파일들의 경로를 텍스트 파일에 추가 및 출력
    with open(save_at, 'w') as f:
        for file in files:
            f.write(file + '\n')
    print(file)

    txt_file_path = os.path.abspath(save_at)

    return txt_file_path
