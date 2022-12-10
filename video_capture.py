import cv2
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./path_output_frame1/%06d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print(success)
  count += 1
  if count > 1000:
    break