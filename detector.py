import cv2
import imutils

def detector(input_queue, output_queue):
    counter = 0
    prev_frame = None
    while True:
        frame = input_queue.get()
        if frame is None:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        boxes = []
        if counter == 0:
            prev_frame = gray_frame
        else:
            diff = cv2.absdiff(gray_frame, prev_frame)
            thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            for c in cnts:
                x, y, w, h = cv2.boundingRect(c)
                boxes.append((x, y, w, h))
            prev_frame = gray_frame
        counter += 1
        output_queue.put((frame, boxes))
    output_queue.put(None)
