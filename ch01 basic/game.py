import tkinter as tk
import random

# 게임 상태
found_clues = 0
TOTAL_CLUES = 3

# 창 생성
root = tk.Tk()
root.title("🔍 미스터리 방 탈출!")

# 캔버스 생성
WIDTH, HEIGHT = 600, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# 메시지 표시
message = canvas.create_text(WIDTH // 2, 30, text="단서를 찾아 탈출하세요!", font=("Arial", 16), fill="white")

# 단서 위치 (랜덤 배치)
clue_positions = [(random.randint(50, 550), random.randint(50, 350)) for _ in range(TOTAL_CLUES)]
clue_objects = []

# 문(탈출구)
door_x1, door_y1, door_x2, door_y2 = 500, 150, 580, 250
canvas.create_rectangle(door_x1, door_y1, door_x2, door_y2, fill="brown", tags="door")
canvas.create_text(540, 200, text="🚪", font=("Arial", 30), tags="door_text")

# 단서 클릭 시 실행되는 함수
def find_clue(event):
    global found_clues

    # 단서 찾기
    for clue in clue_objects[:]:  # 리스트 복사하여 반복 중 삭제 가능하도록 처리
        x1, y1, x2, y2 = canvas.coords(clue)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            canvas.delete(clue)
            clue_objects.remove(clue)
            found_clues += 1
            canvas.itemconfig(message, text=f"단서 발견! ({found_clues}/{TOTAL_CLUES})")
            break

    # 모든 단서를 찾았을 때 문을 열 수 있도록 안내
    if found_clues == TOTAL_CLUES:
        canvas.itemconfig(message, text="모든 단서를 찾았습니다! 문을 클릭하세요!")

    # 문 클릭 시 탈출 체크
    if found_clues == TOTAL_CLUES and door_x1 <= event.x <= door_x2 and door_y1 <= event.y <= door_y2:
        escape()

# 탈출 성공 함수
def escape():
    canvas.itemconfig(message, text="🎉 탈출 성공! 🎉", font=("Arial", 20), fill="yellow")
    root.unbind("<Button-1>")  # 더 이상 클릭 이벤트가 작동하지 않도록 함

# 단서 배치
for x, y in clue_positions:
    clue = canvas.create_oval(x, y, x + 20, y + 20, fill="yellow", tags="clue")
    clue_objects.append(clue)

# 클릭 이벤트 바인딩 (캔버스 전체에서 클릭 감지)
canvas.bind("<Button-1>", find_clue)

# 게임 실행
root.mainloop()
