import numpy as np
import cv2  
from gui import Gui
from tkinter import *
from tkinter import filedialog  ,messagebox 
# trackbar callback function
def nothing(x):
    pass
# create object 
gui = Gui() 
gui.create_message()
# for face and eye detecting CascadeClassifier
face_cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cascade/eye22.xml") 
while 1:
    # select change image
    gui.change_select() 
    change = gui.change.copy()
    change_temp = change.copy()
    change_gray = cv2.cvtColor(change_temp,cv2.COLOR_BGR2GRAY)
    # face area detect
    change_face = face_cascade.detectMultiScale(change_gray) 
    # detect biggest area in face areas 
    change_face_len = len(change_face)
    # 정상처리
    try:
        if change_face_len==0:
            raise
        face_temp = change_face[0]  
        if change_face_len != 1:
            for face in change_face: 
                if face_temp[3] < face[3]:
                    face_temp = face
        change_face = face_temp
        # face area x,y,w,h
        # xy : starting point(col,row) , w : width , h : height
        x = change_face[0]
        y = change_face[1]
        w = change_face[2]
        h = change_face[3]
        # draw box half of face area
        cv2.rectangle(change_temp, (x,y), (x+w, y+int(h/2)), (255,0,0), 1)
        # image for eye detect 
        change_face_crop = change[y:y+h, x:x+w] 
        # image for face and eye confirm
        change_temp_crop_face = change_temp[y:y+int(h/2), x:x+w]
    # 예외처리
    except:
        gui.face_error()
    # eye area detect
    change_eyes = eye_cascade.detectMultiScale(change_temp_crop_face)
    change_eyes_len = len(change_eyes)
    # 정상처리
    try:    
        # 눈영역미검출시 예외상황 발생
        if change_eyes_len == 0:
            raise
        # detect area with high height in eye areas
        while change_eyes_len > 1:
            # variable for smallest index
            index = 0 
            # variable for smallest value
            small = change_eyes[0][3]
            # search index with smallest value
            for i,eye in enumerate(change_eyes):
                if small > eye[3]:
                    small = eye[3]
                    index = i
            # delete index with smallest value
            change_eyes = np.delete(change_eyes,index,0) 
        # 계속 진행하기 위해 esc 입력 요청 message 활성화
        gui.view_message()
        # create trackbar window
        cv2.namedWindow('Trackbar',cv2.WINDOW_NORMAL)
        cv2.createTrackbar('cx', 'Trackbar', 0, 100, nothing)
        cv2.createTrackbar('cy', 'Trackbar', 0, 100, nothing)
        cv2.createTrackbar('cw', 'Trackbar', 0, 100, nothing)
        cv2.createTrackbar('ch', 'Trackbar', 0, 100, nothing)
        # initialize trackbar variable
        cv2.setTrackbarPos('cx', 'Trackbar', 30)
        cv2.setTrackbarPos('cy', 'Trackbar', 30)
        cv2.setTrackbarPos('cw', 'Trackbar', 50)
        cv2.setTrackbarPos('ch', 'Trackbar', 50)
        # 작업용 이미지 copy
        temp = change_temp[y:y+int(h/2), x:x+w].copy()
        # draw box of eyes area
        while 1:
            # get track bar value
            tcx = cv2.getTrackbarPos('cx', 'Trackbar')
            tcy = cv2.getTrackbarPos('cy', 'Trackbar')
            tcw = cv2.getTrackbarPos('cw', 'Trackbar')
            tch = cv2.getTrackbarPos('ch', 'Trackbar')
            cx = tcx - 30
            cy = tcy - 30
            cw = tcw - 50
            ch = tch - 50
            change_temp_crop_face = temp.copy()
            # get eyes axis and size variable
            ex, ey, ew, eh = change_eyes[0]
            cv2.rectangle(change_temp_crop_face, (ex+cx,ey+cy), (ex+cx+ew+cw, ey+cy+eh+ch), (0,0,255), 2)
            change_temp[y:y+int(h/2), x:x+w] = change_temp_crop_face.copy()
            # ask face area and eyes area
            cv2.imshow("change_temp",change_temp)
            if cv2.waitKey(1) & 0xFF == 27:
                break 
        # create questionbox
        check = messagebox.askquestion("확인", "얼굴과 눈 영역이 정확한가요?")
        # continue if distinguished
        if check == "yes":
            cv2.destroyAllWindows()
            break
        # try other image if not distinguished
        elif check =="no": 
            cv2.destroyAllWindows() 
    # 예외처리
    except:
        gui.eye_error()
while 1:
    # select origin image
    gui.origin_select()
    origin = gui.origin.copy()
    origin_temp = origin.copy()
    # face area detect
    origin_gray = cv2.cvtColor(origin,cv2.COLOR_BGR2GRAY)
    origin_face = face_cascade.detectMultiScale(origin_gray) 
    origin_face_len = len(origin_face)
    # 정상처리
    try:
        # 얼굴영역 미검출시 예외상황발생
        if origin_face_len == 0:
            raise
        # detect biggest area in face areas
        # 얼굴 영역이 1개가 아니면 높이(너비)가 가장 긴 영역을 얼굴 영역으로 정한다.
        face_temp = origin_face[0]  
        if origin_face_len != 1:
            for face in origin_face: 
                if face_temp[3] < face[3]:
                    face_temp = face
        origin_face = face_temp 
        # face area x,y,w,h
        # xy : starting point(col,row) , w : width , h : height
        x = origin_face[0]
        y = origin_face[1]
        w = origin_face[2]
        h = origin_face[3]
        # draw box half of face area
        cv2.rectangle(origin_temp, (x,y), (x+w, y+int(h/2)), (255,0,0), 2)
        # image for eye detect working 
        origin_face_crop = origin[y:y+h, x:x+w] 
        # image for face and eye detect confirming
        origin_temp_crop_face = origin_temp[y:y+int(h/2), x:x+w].copy()
        
    # 예외처리
    except:
        gui.face_error()
    # eye area detect
    origin_eyes = eye_cascade.detectMultiScale(origin_temp_crop_face)
    origin_eyes_len = len(origin_eyes) 
    # 정상처리
    try:
        # 눈영역 미검출시 예외상황발생
        if origin_eyes_len == 0:
            raise 
        # detect area with high height in eye areas
        # 눈 영역이 1개가 아니면 높이(너비)가 가장 긴 영역을 눈 영역으로 정한다.
        while len(origin_eyes) > 1:
            # variable for smallest index
            index = 0 
            # variable for smallest value
            small = origin_eyes[0][3]
            # search index with smallest value
            for i,eye in enumerate(origin_eyes):
                if small > eye[3]:
                    small = eye[3]
                    index = i
            # delete index with smallest value
            origin_eyes = np.delete(origin_eyes,index,0) 
        # 계속 진행하기 위해 esc 입력 요청 message 활성화
        gui.view_message()
        # create trackbar window
        cv2.namedWindow('Trackbar',cv2.WINDOW_NORMAL)
        cv2.createTrackbar('ox', 'Trackbar', 0, 100, nothing)
        cv2.createTrackbar('oy', 'Trackbar', 0, 100, nothing)
        cv2.createTrackbar('ow', 'Trackbar', 0, 100, nothing)
        cv2.createTrackbar('oh', 'Trackbar', 0, 100, nothing)
        # initialize trackbar variable
        cv2.setTrackbarPos('ox', 'Trackbar', 30)
        cv2.setTrackbarPos('oy', 'Trackbar', 30)
        cv2.setTrackbarPos('ow', 'Trackbar', 50)
        cv2.setTrackbarPos('oh', 'Trackbar', 50)
        # 작업용 이미지 copy
        temp = origin_temp[y:y+int(h/2), x:x+w].copy()
        # draw box of eyes area
        while 1:
            # get track bar value
            tox = cv2.getTrackbarPos('ox', 'Trackbar')
            toy = cv2.getTrackbarPos('oy', 'Trackbar')
            tow = cv2.getTrackbarPos('ow', 'Trackbar')
            toh = cv2.getTrackbarPos('oh', 'Trackbar')
            ox = tox - 30
            oy = toy - 30
            ow = tow - 50
            oh = toh - 50   
            origin_temp_crop_face = temp.copy()
            # get eyes axis and size variable
            ex , ey, ew, eh = origin_eyes[0]
            cv2.rectangle(origin_temp_crop_face, (ex+ox,ey+oy), (ex+ox+ew+ow, ey+oy+eh+oh), (0,0,255), 2)
            origin_temp[y:y+int(h/2), x:x+w] = origin_temp_crop_face.copy()
            cv2.imshow("origin_temp",origin_temp)
            if cv2.waitKey(1) & 0xFF == 27:
                break 
        # create questionbox
        check = messagebox.askquestion("확인", "얼굴과 눈 영역이 정확한가요?")
        # continue if separated
        if check == "yes":
            cv2.destroyAllWindows() 
            break
        # try other image if not separated
        elif check =="no":
            cv2.destroyAllWindows() 
    # 예외처리
    except:
        gui.eye_error()
# create trackbar window
cv2.namedWindow('Trackbar',cv2.WINDOW_NORMAL) 
cv2.createTrackbar('kernel_size', 'Trackbar', 11, 101, nothing)
cv2.createTrackbar('ox', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('oy', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('ow', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('oh', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('cx', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('cy', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('cw', 'Trackbar', 0, 100, nothing)
cv2.createTrackbar('ch', 'Trackbar', 0, 100, nothing)
# initialize trackbar variable
cv2.setTrackbarPos('ox', 'Trackbar', tox)
cv2.setTrackbarPos('oy', 'Trackbar', toy)
cv2.setTrackbarPos('ow', 'Trackbar', tow)
cv2.setTrackbarPos('oh', 'Trackbar', toh)
cv2.setTrackbarPos('cx', 'Trackbar', tcx)
cv2.setTrackbarPos('cy', 'Trackbar', tcy)
cv2.setTrackbarPos('cw', 'Trackbar', tcw)
cv2.setTrackbarPos('ch', 'Trackbar', tch) 
origin_temp = origin_face_crop.copy() 
# show image for comparison
cv2.imshow("origin",origin)
while 1:
    # get track bar value
    ox = cv2.getTrackbarPos('ox', 'Trackbar')
    oy = cv2.getTrackbarPos('oy', 'Trackbar')
    ow = cv2.getTrackbarPos('ow', 'Trackbar')
    oh = cv2.getTrackbarPos('oh', 'Trackbar')
    cx = cv2.getTrackbarPos('cx', 'Trackbar')
    cy = cv2.getTrackbarPos('cy', 'Trackbar')
    cw = cv2.getTrackbarPos('cw', 'Trackbar')
    ch = cv2.getTrackbarPos('ch', 'Trackbar') 
    kernel_size = cv2.getTrackbarPos('kernel_size', 'Trackbar')   
    # 원본 이미지 눈 영역 crop
    oex = origin_eyes[0][0]+ox - 30
    oey = origin_eyes[0][1]+oy - 30
    oew = origin_eyes[0][2]+ow - 50
    oeh = origin_eyes[0][3]+oh - 50
    origin_eye = origin_face_crop[oey:oey+oeh, oex:oex+oew] 
    origin_eye_height = origin_eye.shape[0]
    origin_eye_width = origin_eye.shape[1]
    # 합성 이미지 눈 영역 crop
    cex = change_eyes[0][0]+cx - 30
    cey = change_eyes[0][1]+cy - 30
    cew = change_eyes[0][2]+cw - 50
    ceh = change_eyes[0][3]+ch - 50
    change_eye = change_face_crop[cey:cey+ceh, cex:cex+cew] 
    # 원본 눈영역에 합성 눈영역 size resize
    resize_change_eye = cv2.resize(change_eye,dsize=(origin_eye_width,origin_eye_height))  
    # 작업용 이미지 copy
    origin_face_crop[oey:oey+oeh, oex:oex+oew]  = origin_temp[oey:oey+oeh, oex:oex+oew].copy()
    # 실제눈영역 검출 과정
    # create kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    # get edge image 
    gray = cv2.cvtColor(resize_change_eye,cv2.COLOR_BGR2GRAY) 
    edge = cv2.Canny(gray, 150, 180)
    # edge morphology연산
    mask = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # get not mask 
    mask_inv = cv2.bitwise_not(mask) 
    # mask, 합성할 이미지 and 연산
    change_fg = cv2.bitwise_and(resize_change_eye, mask)
    # not mask, 원본 이미지 and 연산
    original_bg = cv2.bitwise_and(origin_face_crop[oey:oey+oeh, oex:oex+oew], mask_inv) 
    # kernel size 최솟값(3)으로 설정
    if kernel_size >= 3:
        result_eye = cv2.add(original_bg, change_fg)
    # kernel size가 3보다 작으면 원래 이미지 보여주기
    else:
        result_eye = origin_eye.copy()
    origin_face_crop[oey:oey+oeh, oex:oex+oew] = result_eye 
    # result image 출력
    cv2.imshow("result",origin) 

    if cv2.waitKey(1) & 0xFF == 27:
        break