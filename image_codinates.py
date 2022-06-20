# # basically image number find wich place

# from cv2 import imshow
# import numpy   as np
# import cv2 as cv



# # events = [i for i in dir(cv)]

# # print(events)


# def click_event(event , x,y, flags, parms):
#     if  event == cv.EVENT_LBUTTONDOWN:
#         print(x ,' , ', y)
#         font = cv.FONT_HERSHEY_SIMPLEX
#         strxy = str(x) + ', '+ str(y)
#         cv.putText(img, strxy , (x,y), font, .5 , (255,255,0),2)
#         cv.imshow('image', img)
#         print()

#     if event == cv.EVENT_RBUTTONDOWN:
#         blue =  img(y,x,0)
#         green =  img(y,x,1)
#         red =  img(y,x,2)

#         font = cv.FONT_HERSHEY_SIMPLEX
#         strbgr = str(blue) + ', '+ str(green) + ", " + str(red)
#         cv.putText(img, strbgr , (x,y), font, .5 , (0,255,255,),2)
#         cv.imshow('image', img)

# img = np.zeros((512,512,3), np.uint8)
# img = cv.imread('images.jpg')
# cv.imshow('image', img)

# cv.setMouseCallback('image', click_event)

# cv.waitKey(0)
# cv.destroyAllWindows()


import numpy as np
import cv2



# # mouse callback function
# def draw(event,x,y,flags,param):
    
#     if event == cv2.EVENT_LBUTTONDBLCLK:
        
#         cv2.circle(img,(x,y),100,(125,0,255),5)
        
#     if event == cv2.EVENT_RBUTTONDBLCLK:
        
#         cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
# cv2.namedWindow(winname = "res")    
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.setMouseCallback("res",draw)

# while True:
#     cv2.imshow("res",img)
#     if cv2.waitKey(1) & 0xFF == 'q':
#         break

# cv2.destroyAllWindows()



def mouse_event(event, x, y, flg, param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flg==",flg)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN 
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
           
        cord = ". "+str(x) + ', '+ str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125 ,100), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[y, x, 0] #for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2] #for red channel is 2
        
        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
        cv2.imshow('image', img)
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('images.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()