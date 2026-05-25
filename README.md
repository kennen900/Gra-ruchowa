Gra-ruchowa 

Interaktywna gra ruchowa napisana w Pythonie, która wykorzystuje kamerę internetową oraz technologię śledzenia dłoni do sterowania grą za pomocą ruchu palca wskazującego.

Gracz zdobywa punkty poprzez dotykanie delfina wyświetlanego na ekranie. System wykrywa pozycję dłoni w czasie rzeczywistym przy użyciu biblioteki MediaPipe.

✨ Funkcje
📷 Wykrywanie dłoni z kamery internetowej
☝️ Śledzenie palca wskazującego w czasie rzeczywistym
🐬 Losowo pojawiający się cel (delfin)
🎯 System punktacji
⏱️ Limit czasu gry
🌈 Efekt kolorowej obramówki po trafieniu
🖥️ Tryb pełnoekranowy
🔍 Automatyczne wykrywanie dostępnych kamer
🛠️ Technologie

Projekt został stworzony przy użyciu:

Python
MediaPipe
OpenCV
📦 Wymagania
Python 3.11.9
Kamera internetowa
System Windows / Linux / macOS
🚀 Instalacja
1. Sklonuj repozytorium
git clone https://github.com/TWOJ_LOGIN/movement-game.git
cd movement-game
2. Utwórz środowisko virtualenv (opcjonalnie)
python -m venv venv
3. Aktywuj środowisko
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
4. Zainstaluj wymagane biblioteki
pip install opencv-python mediapipe==0.10.9
▶️ Uruchomienie gry
python test.py

Po uruchomieniu:

Program wyświetli listę dostępnych kamer
Wybierz numer kamery
Gra uruchomi się w trybie pełnoekranowym
Dotykaj delfina palcem wskazującym, aby zdobywać punkty
🎮 Sterowanie
Akcja	Opis
Ruch dłoni	Sterowanie kursorem
Palec wskazujący	Wykrywanie trafienia
ESC	Wyjście z gry
📂 Struktura projektu
movement-game/
│
├── test.py
├── Delfin.png
└── README.md
🧠 Jak działa?

Gra wykorzystuje model wykrywania dłoni z biblioteki MediaPipe.

Pozycja czubka palca wskazującego jest pobierana z landmarku:

hand_landmarks.landmark[8]

Następnie program oblicza odległość między palcem a delfinem:

distance = ((x - target_x)**2 + (y - target_y)**2)**0.5

Jeżeli odległość jest odpowiednio mała — gracz zdobywa punkt.

📸 Gameplay

Możesz dodać tutaj screeny lub GIF-y z gry:

![Gameplay](screenshot.png)
🔮 Możliwe rozszerzenia
🔊 Efekty dźwiękowe
🏆 Tablica wyników
👥 Multiplayer
🎨 Więcej obiektów do trafiania
📱 Wersja mobilna
🤖 Śledzenie całej sylwetki
