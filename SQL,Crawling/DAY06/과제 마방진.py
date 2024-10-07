def create_magic_square(n):
    # 마방진 초기화
    magic_square = [[0] * n for _ in range(n)]

    # 시작 위치 설정
    row = 0
    col = n // 2
    magic_square[row][col] = 1

    for num in range(2, n * n + 1):
        # 다음 위치 설정
        new_row = (row - 1) % n
        new_col = (col + 1) % n

        # 첫 번째 if문: 다음 위치가 범위를 벗어나면
        if new_row < 0:
            new_row = n - 1
        if new_col == n:
            new_col = 0

        # 두 번째 if문: 다음 위치에 숫자가 이미 있으면 아래로 이동
        if magic_square[new_row][new_col] != 0:
            new_row = (row + 1) % n
            new_col = col

        # 세 번째 if문: 범위를 벗어난 경우 조정
        if new_row >= n:
            new_row = 0

        magic_square[new_row][new_col] = num
        row, col = new_row, new_col

    return magic_square

def print_magic_square(magic_square):
    n = len(magic_square)
    for row in magic_square:
        for num in row:
            print(f"{num:2}", end=" ")
        print()

def main():
    n = int(input("홀수차 배열의 크기를 입력하세요: "))
    if n % 2 == 0:
        print("짝수를 입력하였습니다. 다시 입력하세요.")
    else:
        magic_square = create_magic_square(n)
        print(f"Magic Square ({n}x{n})")
        print_magic_square(magic_square)

if __name__ == "__main__":
    main()





    ######################## Chat GPT 사용하였습니다.!!!!!!!!!!!죄송합니다!!!!!!!!!!!!!##################################################