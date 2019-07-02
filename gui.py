import numpy as np
import cv2  
import tkinter as tk   
import tkinter.font 
import sys
class Gui():  
    def __init__(self):
        self.copyright = tk.Tk()
        self.copyright.title('Vision Termproject') 
        label = tk.Label(self.copyright,text="21311758 정우영")
        label.config(font=("맑은고딕", 20))
        label.pack()

        # 이미지 선택 객체
        self.image = tk.Tk()
        self.image.withdraw() 
        self.image.title('Confirm image') 
        # 안내 메세지 객체
        self.message = tk.Tk() 
        self.message.withdraw()  
        self.message.title('Message') 
        # 원본 및 합성 이미지 변수
        self.origin = ""
        self.change = ""  
    # 얼굴 혹은 눈 영역 미탐색시 콜백 함수
    def error_closing(self):
        sys.exit(1) 
    # original image 선택 함수
    def origin_select(self):
        self.image.filename = tk.filedialog.askopenfilename(title = "Select image")
        self.origin = cv2.imread(self.image.filename)
    # 눈 미탐색시 함수
    def eye_error(self):
        eye = tk.Tk()
        eye.title('Message') 
        label = tk.Label(eye,text="눈을 찾지 못했습니다. 다른 이미지를 사용해주세요")
        label.config(font=("맑은고딕", 20))
        label.pack()
        exit_btn = tk.Button(eye, text ="종료", command = self.error_closing)
        exit_btn.config(font=("맑은고딕", 20))
        exit_btn.pack()
        eye.protocol("WM_DELETE_WINDOW", self.error_closing)
        eye.mainloop() 
    # 얼굴 미탐색시 함수
    def face_error(self):
        face = tk.Tk() 
        face.title('Message') 
        label = tk.Label(face,text="얼굴을 찾지 못했습니다. 다른 이미지를 사용해주세요")
        label.config(font=("맑은고딕", 20))
        label.pack()
        exit_btn = tk.Button(face, text ="종료", command = self.error_closing)
        exit_btn.config(font=("맑은고딕", 20))
        exit_btn.pack()
        face.protocol("WM_DELETE_WINDOW", self.error_closing)
        face.mainloop()
    # 안내메세지 닫기 함수
    def message_closing(self):
        self.message.withdraw() 
        self.message.quit()
    # 안내메세지 생성 함수
    def create_message(self):
        label = tk.Label(self.message,text="영역확인 후 esc를 눌러주세요")
        label.config(font=("맑은고딕", 20))
        label.pack()
        exit_btn = tk.Button(self.message, text ="닫기", command = self.message_closing)
        exit_btn.pack()
        self.message.protocol("WM_DELETE_WINDOW", self.message_closing)
    # 안내메세지 활성화 함수
    def view_message(self):
        self.message.deiconify() 
        self.message.mainloop()
    # 합성할 이미지 선택 함수
    def change_select(self):
        self.select_img = tk.Tk()
        self.select_img.title('Select image')
        # 라벨 생성 및 폰트 설정
        label = tk.Label(self.select_img,text="합성할 이미지를 선택해 주세요.")
        label.config(font=("맑은고딕", 20))
        label.pack()
        # 버튼 생성 및 폰트 설정 및 활성화
        select_1 = tk.Button(self.select_img, text ="직접선택", command = self.select1,width=20)
        select_1.config(font=("맑은고딕", 20))
        select_1.pack()
        select_2 = tk.Button(self.select_img, text ="박보검", command = self.select2,width=20)
        select_2.config(font=("맑은고딕", 20))
        select_2.pack()
        select_3 = tk.Button(self.select_img, text ="김수현", command = self.select3,width=20)
        select_3.config(font=("맑은고딕", 20))
        select_3.pack()
        select_4 = tk.Button(self.select_img, text ="이승기", command = self.select4,width=20)
        select_4.config(font=("맑은고딕", 20))
        select_4.pack()
        select_5 = tk.Button(self.select_img, text ="박서준", command = self.select5,width=20)
        select_5.config(font=("맑은고딕", 20))
        select_5.pack()
        select_6 = tk.Button(self.select_img, text ="차은우", command = self.select6,width=20)
        select_6.config(font=("맑은고딕", 20))
        select_6.pack()
        select_11 = tk.Button(self.select_img, text ="서강준", command = self.select11,width=20)
        select_11.config(font=("맑은고딕", 20))
        select_11.pack()
        select_7 = tk.Button(self.select_img, text ="수지", command = self.select7,width=20)
        select_7.config(font=("맑은고딕", 20))
        select_7.pack()
        select_8 = tk.Button(self.select_img, text ="사나", command = self.select8,width=20)
        select_8.config(font=("맑은고딕", 20))
        select_8.pack()
        select_9 = tk.Button(self.select_img, text ="나연", command = self.select9,width=20)
        select_9.config(font=("맑은고딕", 20))
        select_9.pack()
        select_10 = tk.Button(self.select_img, text ="김태희", command = self.select10,width=20)
        select_10.config(font=("맑은고딕", 20))
        select_10.pack()
        self.select_img.mainloop()
    # image select button callbakc functions
    def select1(self): 
        self.image.filename = tk.filedialog.askopenfilename(title = "Select file")
        self.change = cv2.imread(self.image.filename)
        self.select_img.quit() 
        self.select_img.destroy()
    def select2(self): 
        self.change = cv2.imread("img/face1.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select3(self): 
        self.change = cv2.imread("img/face2.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select4(self): 
        self.change = cv2.imread("img/face3.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select5(self): 
        self.change = cv2.imread("img/face4.jpeg")
        self.select_img.quit()
        self.select_img.destroy()
    def select6(self): 
        self.change = cv2.imread("img/face5.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select7(self): 
        self.change = cv2.imread("img/face6.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select8(self): 
        self.change = cv2.imread("img/face7.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select9(self): 
        self.change = cv2.imread("img/face8.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select10(self): 
        self.change = cv2.imread("img/face9.jpg")
        self.select_img.quit()
        self.select_img.destroy()
    def select11(self): 
        self.change = cv2.imread("img/face10.jpeg")
        self.select_img.quit()
        self.select_img.destroy()