import cv2 as cv
import time
Conf_threshold = 0.4
NMS_threshold = 0.4
COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class_name = []
with open('classes.txt', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]
# print(class_name)
net = cv.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')  #weights==모델 #cfg==모델정의서(설정파일)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

cap = cv.VideoCapture(0)
starting_time = time.time()
frame_counter = 0
while True:
    ret, frame = cap.read()
    frame_counter += 1
    if ret == False:
        break
    frame = cv.resize(frame, (768, 768))
    classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)
    for (classid, score, box) in zip(classes, scores, boxes):
        # classid == 예측한 라벨 score == pred 1에 가까움에 따라 정확도 box = 감지된 box 정보
        
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_name[classid[0]], score)
        print(label)  # class == 예측 대상 : 확률
        cv.rectangle(frame, box, color, 1)
        cv.putText(frame, label, (box[0], box[1] - 10),
                   cv.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
    endingTime = time.time() - starting_time    
    print(endingTime)
    fps = frame_counter / endingTime
    cv.putText(frame, f'FPS: {fps}', (20, 50),
               cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
