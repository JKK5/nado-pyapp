import pygame

pygame.init()  # 초기화

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')  # 게임 이름

# 이벤트 루프
running = True  # 게임 진행 중인지
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생하는지
            running = False  # 게임 진행중 아님

# pygame 종료
pygame.quit()
