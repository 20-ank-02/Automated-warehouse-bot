from ultralytics import YOLO
# from ultralytics.utils.plotting import Annotator
import cv2 as cv 

model = YOLO('./runs/detect/train/weights/best.pt')

# print('this is also getting called')   

def detect():
    vidObj = cv.VideoCapture(0)

    # vidObj = cv.VideoCapture() 
    # img = cv.imread('./test.jpg')
    
    c,img=vidObj.read()
    img = img[0:480,0:400]    

    # print(type(img))
    cv.imwrite('frame.jpg',img)
    results=model(img)

    center=tuple()
    # print(results[0].boxes[0].conf)

    for r in results:
        for box in r.boxes:
            print(box.conf.item())
            i=0
            xy1=(int(box.xyxy[0][0].item()),int(box.xyxy[0][1].item()))  #top left
            xy2=(int(box.xyxy[0][2].item()),int(box.xyxy[0][3].item()))  #bottom right
            
            cv.rectangle( img, xy1 , xy2 , (255,0,0), 2)
            
            center=( ( xy1[0]+xy2[0])//2 , (xy1[1]+xy2[1])//2 )
            cv.circle( img , center, 1 , (0,0,255*(box.conf.item()*100)), 2)
            cv.imwrite(f'd{i}.jpg',img) 
            i+=1   
            
    return center
    
print(detect()) 
 
# cv.imshow('result',img)
# cv.waitKey(0)
# cv.destroyAllWindows()
