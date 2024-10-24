// const num = 1;
// let num1 = 2;
// var num2 =3;
// // 再宣言、再代入不可
// // const num = 1;
// // 再宣言不可
// // let num1 = 2;
// // var num2 =3;
// if  (num1 % 2 == 0) {
//     console.log(num1 + "は偶数です");
//     console.log(`${num1}は偶数です`);
// }
// if (num1 % 2 == 0 && num1 % 3 == 0){
//     console.log(num1 + "は６の倍数");
// }
// else if (num1 % 2 == 0) {
//     console.log(num1 + "は2の倍数");
// }
// else {
//     console.log(num1 + "は3の倍数");
// }

// for (let i = 0; i < 5; i++){
//     if (i == 2) {
//         continue;
//     }
//     let s = i + 1
//     console.log(s + "回目の出力です");
//     console.log(`${i+1}回目の出力です`);
// } 

// let hairetu = [10, 20, 30, 40, 50]
// for (let i = 0; i < hairetu.length; i++){
//     let s = i  + 1
//     if (s == 4) {
//         break;
//     }
//     if (s % 2 == 0) {
//         hairetu[i] = hairetu[i] * 2
//     }
//     hairetu[i] = s % 2 == 0 ? hairetu[i] * 2 : hairetu[i];
// }

// const sum = (num3, num4=10, num5=10) => {
//     let result = num3 + num4
//     return result;
// }
// sum(10, 20);

window.onload = function(){
    const button = document.getElementById("button");
    const input = document.getElementById("input")
    
    console.log(button)
    button.addEventListener('click', () => {
        console.log(input.value);
    });
}
