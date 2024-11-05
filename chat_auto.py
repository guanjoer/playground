# 채팅 자동 입력 프로그램
# 서버 요청 X, 활성화 된 입력 프롬프트에 chat 배열에 정의된 값 중 랜덤으로 입력 후, Enter 수행

# Windows
import time
import pyautogui
import pyperclip
import random
from datetime import datetime, timedelta, timezone

# 한국 시간대; UTC+9
KST = timezone(timedelta(hours=9))

# 5초 대기
for i in range(5, 0, -1):
    print(f"[*] {i}...")
    time.sleep(1)

print(f"[*] 메시지 자동 입력 시작 : {datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}")

# 채팅 메시지 리스트
chat = ["ㅋㅋㅋㅋㅋ ", "ㅋㅋㅋㅋㅋ ", "ㅋㅋㅋㅋㅋㅋㅋ ", "ㅋㅋㅋ ", "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ "]

while True:
    # 7초 ~ 15초
    delay = 7 + random.randint(0, 7)
    
    random_chat = random.choice(chat)
    

    pyperclip.copy(random_chat) # 클립보드에 복사
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")

    current_time = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')
    print(f"[+] 메시지 전송 완료: {current_time} - 메시지: {random_chat}")
    
    # delay의 값만큼 대기
    time.sleep(delay)



# Linux
# import time
# import random
# import subprocess
# from datetime import datetime, timedelta, timezone

# # 한국 시간대; UTC+9
# KST = timezone(timedelta(hours=9))

# # 5초 대기
# for i in range(5, 0, -1):
#     print(f"[*] {i}...")
#     time.sleep(1)


# print(f"[*] 메시지 자동 입력 시작 : {datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}")


# chat = [" ㅋㅋㅋㅋㅋ ", " ㅋㅋㅋㅋㅋ ", " ㅋㅋㅋㅋㅋㅋㅋ ", " ㅋㅋㅋ ", " ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ "]

# while True:
#     # 7초 ~ 15초
#     delay = 7 + random.randint(0, 7)
    
#     # chat 배열에서 랜덤 선택
#     random_chat = random.choice(chat)
    

#     subprocess.run(["xdotool", "type", random_chat])
#     time.sleep(1)
#     subprocess.run(["xdotool", "key", "Return"])
    

#     current_time = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')
#     print(f"[+] 메시지 전송 완료: {current_time} - 메시지: {random_chat}")
    
#     # delay 만큼 대기 후 다음 반복 동작 수행
#     time.sleep(delay)
