import cv2

def FrameCapture(woody):

    vidObj = cv2.VideoCapture(woody)

    count = 0
    success = 1

    while success:
        success, image = vidObj.read()

        cv2.imwrite("framed.jpg" % count, image)

        count += 1
if __name__ == '__main__':
    FrameCapture("woody.mp4")
