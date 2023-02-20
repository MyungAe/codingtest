// 르탄이가 1000원을 가지고 편의점에서 물건을 사려고 한다. 편의점에는 500원, 100원, 50원, 10원이 충분히 있고, 편의점 직원은 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
// 르탄이가 편의점에서 물건을 사고 1000원 지폐 한 장을 냈을 때, 받을 잔돈의 개수를 구하는 프로그램을 작성하여라. (단, 물건의 가격은 10원 이상 1000원 미만이며, 1원 단위는 고려하지 않는다.)

function solution(num) {
  let count = 0;
  let money = 1000 - num;
  const unit_money = [500, 100, 50, 10];

  for (let i = 0; i < unit_money.length; i++) {
    count += Math.floor(money / unit_money[i]);
    money = money % unit_money[i];
  }

  return count;
}

// // 1
// console.log(solution(900));
// // 5
// console.log(solution(550));
// // 6
// console.log(solution(320));
// 8
console.log(solution(160));
