import cv2
import imutils
from logger import Logger

logger = Logger.get_logger(__name__)

def detector(input_queue, output_queue):
    logger.info("Starting detector process")

    counter, motion_frames_detected = 0, 0
    prev_frame = None
    while True:
        logger.debug("Waiting for frame from input queue...")
        frame = input_queue.get()

        if frame is None:
            logger.info("Received termination signal from streamer")
            break

        logger.debug(f"Processing frame {counter + 1}")
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        boxes = []

        if counter == 0:
            prev_frame = gray_frame
            logger.debug("First frame, skipping motion detection")
        else:
            diff = cv2.absdiff(gray_frame, prev_frame)
            thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)

            if cnts:
                motion_frames_detected += 1
                logger.debug(f"Motion detected in frame {counter}. Contours found: {len(cnts)}")

            for c in cnts:
                if int(cv2.contourArea(c)) > 80:
                    x, y, w, h = cv2.boundingRect(c)
                    boxes.append((x, y, w, h))
            prev_frame = gray_frame
        counter += 1
        output_queue.put((frame, boxes))

        if counter % 100 == 0:
            logger.info(f"Processed {counter} frames, motion detected in {motion_frames_detected} frames")

    output_queue.put(None)
    logger.info(f"Detector process completed. Total frames: {counter}, Motion frames: {motion_frames_detected}")
