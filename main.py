from multiprocessing import Process, Queue
from streamer import streamer
from detector import detector
from presenter import presenter
from logger import Logger

logger = Logger.get_logger(__name__)

if __name__ == "__main__":
    logger.info("Starting video pipeline application")

    video_path = "People.mp4"
    logger.info(f"Using video file: {video_path}")

    q_video_to_frames = Queue()
    q_frames_to_viewer = Queue()

    logger.info("Creating processes...")
    p_streamer = Process(target=streamer, args=(video_path, q_video_to_frames))
    p_detector = Process(target=detector, args=(q_video_to_frames, q_frames_to_viewer))
    p_presenter = Process(target=presenter, args=(q_frames_to_viewer,))

    logger.info("Starting processes...")
    p_streamer.start()
    logger.debug("Streamer process started")

    p_detector.start()
    logger.debug("Detector process started")

    p_presenter.start()
    logger.debug("Presenter process started")

    logger.info("Waiting for processes to complete...")
    p_streamer.join()
    logger.debug("Streamer process joined")

    p_detector.join()
    logger.debug("Detector process joined")

    p_presenter.join()
    logger.debug("Presenter process joined")

    logger.info("All processes completed successfully")
    logger.info("Video pipeline application finished")
