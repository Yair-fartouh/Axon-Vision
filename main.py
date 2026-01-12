from multiprocessing import Process, Queue
from streamer import streamer
from detector import detector
from presenter import presenter

if __name__ == "__main__":
    video_path = "People.mp4"
    q_video_to_frames = Queue()
    q_frames_to_viewer = Queue()

    p_streamer = Process(target=streamer, args=(video_path, q_video_to_frames))
    p_detector = Process(target=detector, args=(q_video_to_frames, q_frames_to_viewer))
    p_presenter = Process(target=presenter, args=(q_frames_to_viewer,))

    p_streamer.start()
    p_detector.start()
    p_presenter.start()

    p_streamer.join()
    p_detector.join()
    p_presenter.join()
