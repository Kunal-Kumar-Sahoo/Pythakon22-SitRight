import csv
import cv2
import mediapipe as mp
import math
import os
import time


class PoseDetector:
    def __init__(self) -> None:
        self.__mp_pose = mp.solutions.pose
        # self.__mp_holistics = mp.solutions.holistic

        self.__colors = {
            # BGR Channels
            'blue': (255, 127, 0),
            'red': (50, 50, 255),
            'green': (127, 255, 0),
            'dark blue': (127, 20, 0),
            'light green': (127, 233, 100),
            'yellow': (0, 255, 255),
            'pink': (255, 0, 255)
        }

        self.__pose = self.__mp_pose.Pose()
        self.__file_name = None  # Also represents camera index in case of live video stream
        self.__cap = None  # VideoCapture Object
        self.__fps = None
        self.__frame_size = None
        self.__fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    def getVideoStream(self, filePath: str) -> None:
        self.__file_name = filePath
        print(filePath)
        self.__cap = cv2.VideoCapture(self.__file_name)
        self.__fps = int(self.__cap.get(cv2.CAP_PROP_FPS))
        self.__dimensions = (
            int(self.__cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.__cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )

    def processing(self):
        while self.__cap.isOpened():
            success, img = self.__cap.read()
            if not success:
                print('null video frames')
                break

            self.__fps = self.__cap.get(cv2.CAP_PROP_FPS)

            h, w = img.shape[:2]

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            keypoints = self.__pose.process(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            lm = keypoints.pose_landmarks
            lmPose = self.__mp_pose.PoseLandmark
            dic = {'name': self.__file_name}
            dic['leftShoulderX'] = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
            dic['leftShoulderY'] = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
            dic['rightShoulderX'] = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
            dic['rightShoulderY'] = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
            dic['leftEarX'] = int(lm.landmark[lmPose.LEFT_EAR].x * w)
            dic['leftEarY'] = int(lm.landmark[lmPose.LEFT_EAR].y * h)
            dic['leftHipX'] = int(lm.landmark[lmPose.LEFT_HIP].x * w)
            dic['leftHipY'] = int(lm.landmark[lmPose.LEFT_HIP].y * h)
            fieldnames = ['name', 'leftShoulderX', 'leftShoulderY', 'rightShoulderX', 'rightShoulderY', 'leftEarX', 'leftEarY', 'leftHipX', 'leftHipY']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dic)
            writer.writeheader()


if __name__ == '__main__':
    pd = PoseDetector()
    di = os.fsencode(r'C:\Users\Kishan Pipaliya\Desktop\Sitting posture')
    csvfile = open('data.csv', 'w', newline='\n')
    for f in os.listdir(di):
        pd.getVideoStream('C:\\Users\\Kishan Pipaliya\\Desktop\\Sitting posture\\'+f.decode('utf-8'))
        pd.processing()
        break
