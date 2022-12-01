import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2
FILENAME= "20221110_134425642.exr"
# img = cv2.imread(FILENAME, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
img = cv2.imread(FILENAME)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('EXR viewer',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
