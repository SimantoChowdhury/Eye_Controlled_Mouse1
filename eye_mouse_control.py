import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)

        # Blink detection using left eye landmarks
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)

        # Check blink
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye controlled Mouse', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()






# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# import math

# # Initialize
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)
# screen_w, screen_h = pyautogui.size()

# def euclidean_distance(point1, point2):
#     return math.hypot(point2.x - point1.x, point2.y - point1.y)

# prev_click_time = 0

# while True:
#     success, frame = cam.read()
#     if not success:
#         continue

#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     frame_h, frame_w, _ = frame.shape

#     if output.multi_face_landmarks:
#         landmarks = output.multi_face_landmarks[0].landmark

#         # Right eye for cursor control (landmark 474:478)
#         eye_landmarks = landmarks[474:478]
#         x = int(eye_landmarks[1].x * frame_w)
#         y = int(eye_landmarks[1].y * frame_h)
#         cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

#         screen_x = screen_w * eye_landmarks[1].x
#         screen_y = screen_h * eye_landmarks[1].y
#         pyautogui.moveTo(screen_x, screen_y, duration=0.05)

#         # Left eye for blink detection (landmark 145 and 159)
#         left_top = landmarks[145]
#         left_bottom = landmarks[159]
#         dist = euclidean_distance(left_top, left_bottom)

#         # Visual debug
#         cx = int(left_top.x * frame_w)
#         cy = int(left_top.y * frame_h)
#         cy2 = int(left_bottom.y * frame_h)
#         cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)
#         cv2.circle(frame, (cx, cy2), 4, (0, 255, 255), -1)

#         # Blink threshold ~ empirically tuned
#         if dist < 0.018:
#             current_time = time.time()
#             if current_time - prev_click_time > 1:  # 1-second delay between clicks
#                 pyautogui.click()
#                 prev_click_time = current_time

#     cv2.imshow('Eye Controlled Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()




