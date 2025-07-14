// Скрипт sample.js
/***********************************
Здесь некоторые элементы языка подробнее здесь: https://learn.javascript.ru
************************************/
// Функция
function sayHello(name) {
document.writeln("Вас зовут " + name);              //получаем доступ к нашему документу
}
/*
// переменная (var или let)
let name = prompt("Ваше имя: "); //тоже что и и input в python
sayHello(name);
**/ //конец функции
//-----------------------------------------------------------------------------------------------------
// Массивы
let colors = ["Красный", "Синий","Голубой"]

/*document.writeln("<h1>Цвета</h1><ul>");
for(let i=0; i<colors.length; i++) {
    document.writeln("<li>" + colors[i] +"</li>");
}
document.writeln("</ol>");*/

//-----------------------------------------------------------------------------------------------------

function changeColor() {
//document.getElementById('alive').style.color = 'red';
const txt = document.getElementById('alive');
if (txt.style.display === 'none') { //=== - совпадают по типу и значению
txt.style.display = block;
} else {
    txt.style.display = 'none';
}
}
//подключаюсь к документу в DOM
const txt = document.getElementById('alive').onclick = changeColor;