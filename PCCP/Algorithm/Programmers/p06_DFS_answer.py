def solution(k, dungeons):
    # 지금까지 클리어한 던전의 개수
    answer = -1
    # 전체 던전의 수
    dungeons_count = len(dungeons)
    # 던전 번호(idx)로 클리어 여부를 저장
    visited = [False] * dungeons_count

    def play(n, current_hp):
        nonlocal answer
        '''
        이 함수에 진입 => 던전을 클리어 했다! 
        (n이 0일 경우, 튜토리얼 종료의 느낌)
        '''
        # 지금까지 클리어한 던전의 수가 최대라면,
        if answer < n:
            # answer 갱신
            answer = n

        # 지금까지 깬 던전의 수가, 던전 개수와 같으면, 더 볼게 없음.
        # 깨고나서 남은 hp가 없으면 (==0) 더 볼 게 없음.
        if n == dungeons_count or current_hp <= 0:
            # 이 뒤의 코드는 실행하지 않고 이번 play를 종료하겠다.
            return

            # 던전 번호 순서대로 순회
        for dungeon_idx in range(dungeons_count):
            # 해당 던전을 방문한 적이 없다면,
            if not visited[dungeon_idx]:
                # 일단은 도전!
                visited[dungeon_idx] = True
                # 요구 피로도, 데미지
                require_hp, damage = dungeons[dungeon_idx]
                # 깰 수 있으면,
                if current_hp >= require_hp:
                    # 깼기 때문에 n+1, 체력은 감소한 채로 다음 던전 탐험
                    play(n + 1, current_hp - damage)
                # ** 다음 순회(for)를 위해 트라이 하지 않은걸로 초기화 **
                visited[dungeon_idx] = False

    play(0, k)
    return answer


# 3
print(solution(80, [[80, 20], [50, 40], [30, 10]]))


from itertools import permutations, combinations


# 순열
def solution_permutations(k, dungeon):
    for case in permutations(dungeon, len(dungeon)):
        count = 0
        for x, y in case:
            pass


solution_permutations(80, [[80, 20], [50, 40], [30, 10]])


# 조합
def solution_combinations(k, dungeons):
        answer = -1
        for case in permutations(dungeons, len(dungeons)):
            hp = k
            count = 0
            for require_hp, damage in case:
                if hp >= require_hp:
                    hp -= damage
                    count += 1
            if count > answer:
                answer = count
        return answer


solution_combinations(80, [[80, 20], [50, 40], [30, 10]])
