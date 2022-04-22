var num = 1
var ol1 = document.getElementById('ol1');
var ol2 = document.getElementById('ol2');
var ol3 = document.getElementById('ol3');

function sdvig () {
  if (num == 1) {
    ol1.classList.add('vnepola');
  }
  if (num == 2) {
    ol2.classList.add('vnepola');
  }
  // if (num == 3) {
  //   ol3.classList.add("vnepola");
  // }
  if (num == 3) {
    ol1.classList.remove('vnepola');
    ol2.classList.remove('vnepola');
    ol3.classList.remove('vnepola');
    num = 0;
  }
  num++;
  console.log({ num: num });
}