import cv2
import mediapipe as mp
print("🔍 MediaPipe 的真身藏在这里：", mp.__file__) # 加上这行查岗
import math

print("🚀 1. 正在加载 MediaPipe 模型，请稍候...")
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
print("✅ MediaPipe 加载完成！")

print("🎥 2. 正在呼叫摄像头 (如果一直卡在这里，记得去改系统权限或把 0 改成 1)...")
# 尝试把这里的 0 改成 1 或 2 试试
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("❌ 完蛋，摄像头打不开！")
    exit()
else:
    print("✅ 3. 摄像头已成功启动！画面加载中...")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("忽略空帧")
        continue

    # 将图像水平翻转，这样画面就像照镜子一样，操作更直观
    image = cv2.flip(image, 1)
    
    # OpenCV 默认是 BGR 格式，MediaPipe 需要 RGB 格式
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 将图像传给模型进行处理
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 在画面上画出手部骨骼连线（为了看着酷炫且方便调试）
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 获取画面长宽，用于计算像素坐标
            h, w, c = image.shape
            
            # MediaPipe 中，大拇指尖是 4 号点，食指尖是 8 号点
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]

            # 将比例坐标转换成实际的像素坐标
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)

            # 核心算法 1：用勾股定理计算两个指尖的直线距离
            distance = math.hypot(tx - ix, ty - iy)

            # 核心算法 2：判断是否捏合 (阈值设定为 40 像素，可根据你的摄像头远近微调)
            pinch_threshold = 40
            is_pinched = distance < pinch_threshold

            # 准备输出给娃娃机的数据
            claw_x = ix  # 爪子的水平位置跟着食指走
            
            # 视觉反馈：在屏幕上显示当前状态
            status_text = "ACTION: Drop Claw! (抓!)" if is_pinched else "Status: Moving..."
            color = (0, 0, 255) if is_pinched else (0, 255, 0) # 捏合时变红，松开时变绿

            cv2.putText(image, f"Claw X Position: {claw_x}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, status_text, (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
            # 在指尖画两个圆，并连一条线，直观感受距离
            cv2.circle(image, (tx, ty), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(image, (ix, iy), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(image, (tx, ty), (ix, iy), color, 3)

    # 显示画面
    cv2.imshow('Gesture Controller Test', image)

    # 侦听键盘，按下 ESC 键退出循环
    if cv2.waitKey(5) & 0xFF == 27:
        break

# 释放资源，关闭窗口
cap.release()
cv2.destroyAllWindows()