
import cv2


cap = cv2.VideoCapture("woody.mp4")

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)   #total no of frames in a vedio

# frames per sec
fps = cap.get(cv2.CAP_PROP_FPS)

# height width of vedio
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# output VIDEO writer

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('reversed.avi', fourcc, fps, (int(width*0.5), int(height*0.5)))

print("No. of frames are: {}".format(frames))
print("FPS is :{}".format(fps))

frame_index = frames-1

if(cap.isOpened()):
    while(frame_index != 0):       #keep looping till last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)    #give position of frame
        ret, frame = cap.read()

        frame = cv2.resize(frame, (int(width*0.5), int(height*0.5)))

        cv2.imshow('winname', frame)  #to show the reversing video

        out.write(frame)    #writing the reversed video
        frame_index = frame_index-1     #decrementing frame index at each step


        if(frame_index%100 == 0):
            print(frame_index)
        
        if(cv2.waitKey(2) == ord('q')):
            break

out.release()
cap.release()
cv2.destroyAllWindows()





# check, vid = cap.read()

# counter = 0      #variable for counter frames

# check = True   #initializing check

# frame_list = []

# while(check == True):
#     cv2.imwrite("frame%d.jpg" %counter , vid)
#     check , vid = cap.read()
#     frame_list.append(vid)
#     counter += 1
#     frame_list.pop()

#     for frame in frame_list:
#         cv2.imshow("frame", frame)

#         if cv2.waitKey(27) & 0xFF == ord('q'):
#             break
        
#     cap.release
#     cv2.destroyAllWindows()

#     frame_list.reverse()

#     for frame in frame_list:
#         cv2.imshow("frame", frame)
#         if cv2.waitKey(25) & 0xff == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()




