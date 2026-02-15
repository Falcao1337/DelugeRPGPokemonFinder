import pyautogui
import time

print("Coloque o mouse na posição desejada...")
time.sleep(3)

x, y = pyautogui.position()
print(f"Coordenadas: X={x} Y={y}")
