import cv2
import mediapipe as mp
import math
import time
from plyer import notification

class PoseDetector:
    def __init__(self) -> None:
        self.__mp_pose = mp.solutions.pose
        # self.__mp_holistics = mp.solutions.holistic

        self.__good_frames = 0
        self.__bad_frames = 0

        self.__font = cv2.FONT_HERSHEY_SIMPLEX

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

        self.neckInclination = None
        self.torsoInclination = None

    @staticmethod
    def findDistance(x1:int, y1:int, x2:int, y2:int) -> float:
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    @staticmethod
    def findAngle(x1:int, y1:int, x2:int, y2:int) -> float:
        theta = math.acos((y1-y2) / PoseDetector.findDistance(x1, y1, x2, y2))
        thetaDegrees = 180 / math.pi * theta

        return thetaDegrees

    def sendWarning(self):
        f = open('./warning.txt', 'w')
        f.close()

    def getVideoStream(self, camIdx: int) -> None:
        self.__file_name = camIdx
        self.__cap = cv2.VideoCapture(self.__file_name)
        self.__fps = int(self.__cap.get(cv2.CAP_PROP_FPS))
        self.__dimensions = (
            int(self.__cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.__cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )

    def getVideoStream(self, filePath: str) -> None:
        self.__file_name = filePath
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

            leftShoulderX = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
            leftShoulderY = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
            rightShoulderX = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
            rightShoulderY = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
            leftEarX = int(lm.landmark[lmPose.LEFT_EAR].x * w)
            leftEarY = int(lm.landmark[lmPose.LEFT_EAR].y * h)
            leftHipX = int(lm.landmark[lmPose.LEFT_HIP].x * w)
            leftHipY = int(lm.landmark[lmPose.LEFT_HIP].y * h)



            if self.neckInclination < 40 and self.torsoInclination < 10:
                self.__bad_frames = 0
                self.__good_frames += 1

                cv2.putText(img, angleTextString, (10, 30), self.__font, 0.9, self.__colors['light green'], 2)
                cv2.putText(img, str(int(self.neckInclination)), (leftShoulderX+10, leftShoulderY), self.__font, 0.9,
                            self.__colors['light green'], 2)
                cv2.putText(img, str(int(self.torsoInclination)), (leftHipX + 10, leftHipY), self.__font, 0.9,
                            self.__colors['light green'], 2)

                cv2.line(img, (leftShoulderX, leftShoulderY), (leftEarX, leftEarY), self.__colors['green'], 4)
                cv2.line(img, (leftShoulderX, leftShoulderY), (leftShoulderX, leftShoulderY-100),
                         self.__colors['green'], 4)
                cv2.line(img, (leftShoulderX, leftShoulderY), (leftEarX, leftEarY), self.__colors['green'], 4)
                cv2.line(img, (leftShoulderX, leftShoulderY), (leftShoulderX, leftShoulderY - 100),
                         self.__colors['green'], 4)
            else:
                self.__good_frames = 0
                self.__bad_frames += 1

                cv2.putText(img, angleTextString, (10, 30), self.__font, 0.9, self.__colors['red'], 2)
                cv2.putText(img, str(int(self.neckInclination)), (leftShoulderX + 10, leftShoulderY), self.__font, 0.9,
                            self.__colors['red'], 2)
                cv2.putText(img, str(int(self.torsoInclination)), (leftHipX + 10, leftHipY), self.__font, 0.9,
                            self.__colors['red'], 2)

                cv2.line(img, (leftShoulderX, leftShoulderY), (leftEarX, leftEarY), self.__colors['red'], 4)
                cv2.line(img, (leftShoulderX, leftShoulderY), (leftShoulderX, leftShoulderY - 100),
                         self.__colors['red'], 4)
                cv2.line(img, (leftShoulderX, leftShoulderY), (leftEarX, leftEarY), self.__colors['red'], 4)
                cv2.line(img, (leftShoulderX, leftShoulderY), (leftShoulderX, leftShoulderY - 100),
                         self.__colors['red'], 4)

            good_time = self.__good_frames / self.__fps
            bad_time = self.__bad_frames / self.__fps

            if good_time > 0:
                cv2.putText(img, f'Good posture time: {round(good_time, 1)}s', (10, h-20),
                            self.__font, 0.9, self.__colors['green'])
            else:
                cv2.putText(img, f'Bad posture time: {round(bad_time, 1)}s', (10, h - 20),
                            self.__font, 0.9, self.__colors['red'])

            if bad_time >= 3:
                self.sendWarning()

            cv2.imshow('Video feed:', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('Quitting')
                break

if __name__ == '__main__':
    pd = PoseDetector()
    pd.getVideoStream('./media/input.mp4')
    pd.processing()