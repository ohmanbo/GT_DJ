import socket

# 셀 정보를 저장할 빈 리스트 생성
server_list = []

# A1부터 I9까지의 grid_name을 생성
for col in 'ABCDEFGHI':
    for row in range(1, 10):
        grid_name = f"{col}{row}"
        server_list.append({
            "cellid": len(server_list),  # 현재 리스트 길이를 cellid로 사용
            "grid_name": grid_name,
            "status": 0  # 기본 상태는 0으로 설정
        })

# 예시 출력
for server_list in server_list:
    print(server_list)