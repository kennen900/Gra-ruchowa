import cv2
import mediapipe as mp
import random
import time

# funkcja sprawdzająca istniejące kamery
def list_Camera(max_device = 10):
    available = []
    for i in range(max_device):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                available.append(i)
            cap.release()
    return available
    


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# wczytanie obrazka delfina
dolphin = cv2.imread("Delfin.png", cv2.IMREAD_UNCHANGED)

# zmiana rozmiaru
dolphin = cv2.resize(dolphin, (100, 80))

dolphin_h, dolphin_w = dolphin.shape[:2]

# obiekt do trafienia
target_x = random.randint(100, 500)
target_y = random.randint(100, 400)


score = 0
spawn_time = time.time()

cameras = list_Camera()
print("Dostepne kamer: ", cameras)
if not cameras:
    print("Brak kamer")
    exit()

which_camera = int(input("Podaj ktora kamere wybierasz: "))
cap = cv2.VideoCapture(which_camera)

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

# obramówka ekranu
flash = False
flash_start = 0
flash_color = (0, 255, 255)

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
    y1 = target_y - dolphin_h // 2
    y2 = y1 + dolphin_h
    x1 = target_x - dolphin_w // 2
    x2 = x1 + dolphin_w

    # sprawdzanie czy obraz mieści się w ekranie
    if y1 >=0 and y2 <= h and x1 >= 0 and x2 <=w:
        # kanał alpha (przezroczystość)
        alpha = dolphin[:, :, 3] / 255.0

        # nakładanie obrazka
        for c in range(3):
            frame[y1:y2, x1:x2, c] = (
                alpha * dolphin[:,:,c] +
                (1 - alpha) * frame[y1:y2, x1:x2, c]
            )

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # czubek palca wskazującego
            index_tip = hand_landmarks.landmark[8]
            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            # rysuje punkt palca
            cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

            # sprawdzanie trafienia (kolizja)
            distance = ((x - target_x)**2 + (y - target_y)**2)**0.5
            if distance < 40 and not game_over:
                score += 1
                # nowy cel
                target_x = random.randint(50, w-50)
                target_y = random.randint(50, h-50)
                spawn_time = time.time()

                # uruchomienie flasha
                flash = True
                flash_start = time.time()

                # losowy kolor obramówki
                flash_color = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)
                )

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

    if flash:
        cv2.rectangle(frame, (0,0), (w,h), flash_color, 25)

        # obramówka znika po 0.3 sekundy
        if time.time() - flash_start > 0.3:
            flash = False

    cv2.imshow("Gra ruchowa", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    
        
cap.release()
cv2.destroyAllWindows()