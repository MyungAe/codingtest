// Problem

// 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
// 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
// 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
// 다음 예를 보자. 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
// 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
// N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

// 9348kb, 148ms

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split();

const n = Number(input);

return solution(n);

function solution(n) {
  // 입력값 : 0 <= n:int <= 99
  // 결과값 : cycle length

  let repeatCount = 0;
  let lastNumber = 0;
  let targetNumber = n;

  do {
    lastNumber = targetNumber % 10;
    targetNumber = ((targetNumber % 10) + Math.floor(targetNumber / 10)) % 10;
    targetNumber += lastNumber * 10;
    repeatCount++;
    // console.log(
    //   `repeat : ${repeatCount}, target : ${targetNumber}, last : ${lastNumber}`
    // );
  } while (targetNumber != n);

  console.log(repeatCount);
  return repeatCount;
}

// // 4
// console.log(solution(26));

// // 3
// console.log(solution(55));

// // 60
// console.log(solution(1));

// // 1
// console.log(solution(0));

// // 12
// console.log(solution(71));
