// получить доступ к кнопке

const topBtn = document.querySelector(".go-top");

// скроллинг окна
window.addEventListener("scroll", trackScroll);

// реакция на нажатие
topBtn.addEventListener("click", goTop);

function trackScroll() {
    //вычисляем положение от верхушки окна
    const scrolled = window.pageYOffset;
    // высота окна браузера
    const wh = document.documentElement.clientHeight;
    // в прокрутке вышли за пределы одного экрана
    if(scrolled > wh) {
    // должна показаться кнопка
    topBtn.classList.add("go-top--show");
    } else {
    // или исчезает если прокрутили больше чем один экран
    //topBtn.classList.remove("go-top--show");
    topBtn.style.display = 'block';
    }
}

function goTop() {
 // пока не дошли до верха страницы (конец скролла)
 if (window.pageYOffset > 0) {
 // скроллим к верху
 window.scrollBy(0, -50); // по Y на 28 пикселей
 setTimeout(goTop, 0);    // рекурсивный вызов через задержку

 }
}