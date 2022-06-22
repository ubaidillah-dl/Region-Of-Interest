import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    x1=20
    y1=10
    
    x2=200
    y2=150
    
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    
    roi=frame[y1:y2,x1:x2]
    
    cv2.imshow("Camera",frame)
    cv2.imshow("ROI",roi)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()