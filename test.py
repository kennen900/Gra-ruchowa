import cv2
import mediapipe as mp
import random
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# obiekt do trafienia
target_x = random.randint(100, 500)
target_y = random.randint(100, 400)
radius = 30

score = 0
spawn_time = time.time()

game_duration = 120  
start_time = time.time()
game_over = False

# te dwa niżej mogą powodować długie wczytywanie 
# rozdzielczość kamery
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# full window
cv2.namedWindow("Gra ruchowa", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Gra ruchowa", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    elapsed_time = time.time() - start_time
    remaining_time = int(game_duration - elapsed_time)

    if remaining_time <= 0:
        game_over = True

    # rysuj cel
    cv2.circle(frame, (target_x, target_y), radius, (0, 0, 255), -1)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # czubek palca wskazującego
            index_tip = hand_landmarks.landmark[8]
            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            # rysuj punkt palca
            cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

            # sprawdzanie trafienia (kolizja)
            distance = ((x - target_x)**2 + (y - target_y)**2)**0.5
            if distance < radius and not game_over:
                score += 1
                target_x = random.randint(50, w-50)
                target_y = random.randint(50, h-50)
                spawn_time = time.time()

    # zmiana celu co kilka sekund
    if time.time() - spawn_time > 3:
        target_x = random.randint(50, w-50)
        target_y = random.randint(50, h-50)
        spawn_time = time.time()

    # wyświetlanie punktów
    cv2.putText(frame, f"Punkty: {score}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # wyświetlanie czasu
    cv2.putText(frame, f"Czas: {remaining_time}s", (10, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # wyświetlanie konica gry
    if game_over:
        cv2.putText(frame, "KONIEC GRY", (150, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        break

    cv2.imshow("Gra ruchowa", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    
        
cap.release()
cv2.destroyAllWindows()