![Python](https://img.shields.io/badge/Python-3.11.9-blue.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.9-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Najnowsza-orange.svg)

Interaktywna gra ruchowa zręcznościowa wykorzystująca kamerę internetową oraz algorytmy sztucznej inteligencji do śledzenia dłoni w czasie rzeczywistym. Zadaniem gracza jest kontrolowanie kursora za pomocą palca wskazującego i "wskazywanie" pojawiającego się na ekranie delfina.

---

## 🎮 O grze

Gra uruchamia się w trybie pełnoekranowym. Po wybraniu odpowiedniej kamery, program zaczyna analizować obraz:
1. **Wykrywanie dłoni:** Algorytm śledzi dłoń użytkownika i nakłada na nią mapę punktów (szkielet).
2. **Mechanika rozgrywki:** Głównym punktem interakcji jest czubek palca wskazującego (oznaczony niebieską kropką).
3. **Zasady:** Gra trwa **120 sekund**. Gracz musi dotknąć palcem losowo pojawiającego się delfina. Każde trafienie to 1 punkt, zmiana pozycji delfina oraz efektowne, kolorowe mignięcie ramki ekranu. 
4. **Dynamika:** Jeśli gracz nie trafi w delfina w ciągu 3 sekund, ten zmienia swoje położenie.

---

## 🛠️ Wymagania systemowe i technologiczne

Projekt został stworzony i przetestowany na konkretnych wersjach bibliotek, co gwarantuje jego stabilne działanie:

* **Python:** Wersja `3.11.9`
* **MediaPipe:** Wersja `0.10.9` (odpowiedzialna za detekcję dłoni)
* **OpenCV:** Do obsługi kamery wideo, renderowania grafiki oraz interfejsu gry.

---

## 🚀 Uruchomienie projektu

### 1. Klonowanie repozytorium
Sklonuj projekt na swój dysk lokalny:
```bash
git clone [https://github.com/TWOJ-LOGIN/movement-game.git](https://github.com/TWOJ-LOGIN/movement-game.git)
cd movement-game
