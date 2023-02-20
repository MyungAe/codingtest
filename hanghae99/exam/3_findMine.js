// windows에서 지원하는 지뢰 찾기 게임을 한번쯤은 해 보았을 것이다.
// 특히 르탄이는 지뢰찾기의 매니아로 알려져 있다. 지뢰 찾기 map은 N*N의 정사각형 모양으로 각 칸에는 숫자가 들어가 있거나 지뢰가 들어가 있다. 빈 칸에는 숫자 0이 들어있다고 생각하자.
// map의 어떤 칸에 적혀 있는 숫자는, 그 칸과 인접해 있는 여덟 개의 칸 중에서 지뢰가 들어 있는 칸이 몇 개인지를 나타내 준다. 물론 인접한 칸이 map 내부에 있는 경우에 대해서만 생각하면 된다.

// 예제를 보면 더 잘 이해할 수 있을 것이다.
// 이번 문제는 조금 업그레이드 된 지뢰 찾기로, 한 칸에 한 개의 지뢰가 있는 것이 아니고, 한 칸에 여러 개(1 이상 9 이하)의 지뢰가 묻혀 있는 게임이다.
// 따라서 map의 어떤 칸에 적혀 있는 숫자는, 그 칸과 인접해 있는 여덟 개의 칸들에 들어 있는 지뢰의 총 개수가 된다.
// 이미 windows 지뢰찾기 같은 것을 마스터한 르탄이는, map에서 지뢰에 대한 정보만이 주어졌을 때, 르탄이는 map을 완성하고 싶다고 한다.
// N과 지뢰의 위치가 주어졌을 때, 르탄이를 도와서 지뢰 찾기 map을 완성하는 프로그램을 작성하시오.

// (단, 1 ≤ N ≤ 1,000 이며, 배열의 각 요소에는 지뢰 찾기 map에 대한 정보가 주어지는데 '.' 또는 숫자로 이루어진 문자열이 들어온다.
// '.'는 지뢰가 없는 것이고 숫자는 지뢰가 있는 경우로 그 칸의 지뢰의 개수이다. 한 줄은 N개의 문자로 이루어져 있다.)

function solution(N, arr1) {
  const x = [1, -1, 0, 0, 1, 1, -1, -1];
  const y = [0, 0, 1, -1, 1, -1, 1, -1];

  let mineMap = Array.from(Array(N), () => Array(N).fill(0));
  let targetArea = '';

  // 순회하면서 지뢰를 찾고, 그 숫자만큼 주변에 더해준다
  for (let column = 0; column < N; column++) {
    for (let row = 0; row < N; row++) {
      targetArea = arr1[column][row];
      if (isMine(targetArea)) {
        for (let i = 0; i < x.length; i++) {
          if (isLowerIndex(row + x[i], column + y[i], N))
            mineMap[column + y[i]][row + x[i]] += parseInt(targetArea);
        }
      }
    }
  }

  // 순회하면서 10이 넘는 숫자를 M으로 변환
  for (let column = 0; column < N; column++) {
    for (let row = 0; row < N; row++) {
      if (mineMap[column][row] > 9) mineMap[column][row] = 'M';
    }
  }

  // 순회하면서 지뢰를 *로 변환
  for (let column = 0; column < N; column++) {
    for (let row = 0; row < N; row++) {
      targetArea = arr1[column][row];
      if (isMine(targetArea)) mineMap[column][row] = '*';
    }
  }

  return mineMap;
}

function isMine(char) {
  if (char != '.') return true;
  return false;
}

function isLowerIndex(row, column, N) {
  if (row > -1 && row < N) {
    if (column > -1 && column < N) {
      return true;
    }
  }
  return false;
}

// [[*, M, 9, 9],
// [5, M, *, M],
// [7, *, M, *],
// [7, *, 9, 2]]

console.log(
  solution(4, [
    ['2', '.', '.', '.'],
    ['.', '.', '9', '.'],
    ['.', '3', '.', '2'],
    ['.', '4', '.', '.'],
  ])
);

// [[*, 4, 3, 3, 0],
// [1, 4, *, 3, 0],
// [4, 7, 7, 3, 0],
// [4, *, M, 9, 9],
// [4, 4, M, *, 9]]

console.log(
  solution(5, [
    ['1', '.', '.', '.', '.'],
    ['.', '.', '3', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '4', '.', '.', '.'],
    ['.', '.', '.', '9', '.'],
  ])
);
