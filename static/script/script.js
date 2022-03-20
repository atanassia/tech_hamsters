
const btnReg = document.querySelector('.btn_reg');
btnReg.addEventListener('click', btnRegClick);

const btnBack = document.querySelector(".line_back");
btnBack.addEventListener('click', btnBackClick);
/*Подсветка карточек при клике */
const cardsRow1 = document.querySelector(".line1");
let cards1 = cardsRow1.childNodes;
for (let i = 0; i < cards1.length; i++) {
    let card = cards1[i];
    card.addEventListener("click", function () {
        card.classList.toggle('active');
    });
}
const cardsRow2 = document.querySelector(".line2");
let cards2 = cardsRow2.childNodes;
for (let i = 0; i < cards2.length; i++) {
    let card = cards2[i];
    card.addEventListener("click", function () {
        card.classList.toggle('active');
    });
}
/* */

var lvl = 1;
function btnRegClick() {
    let cardsPortf = document.querySelectorAll(".card");
    for (let i = 0; i < cardsPortf.length; i++) {
        let cardPortf = cardsPortf[i];
        cardPortf.classList.add("hidden");
    }
    let cardsHorizont = document.querySelectorAll(".card_horisont");
    for (let i = 0; i < cardsHorizont.length; i++) {
        let cardHorizont = cardsHorizont[i];
        cardHorizont.classList.add("visit");
    }
    var progresLine = document.querySelector('.progress_line_green');
    var widthGreen = progresLine.offsetWidth;
    var widthFluib = document.querySelector('.progress_line').offsetWidth;
    var width = widthGreen / widthFluib * 100;
    progresLine.style.width = width + 33.333 + "%";
    lvl++;
    let txt = document.querySelector(".step-desc");
    let txtTitle = document.querySelector(".title_desc");
    if (lvl == 2) {
        txt.innerHTML = 'Шаг 2 из 3';
        txtTitle.innerHTML = 'Горизонт инвестирования';

    }
    if (lvl == 3) {
        txt.innerHTML = 'Шаг 3 из 3';
        txtTitle.innerHTML = 'Сколько готовы инвестировать в месяц';
        let range = document.querySelector(".line3");
        range.classList.add("visit");
        for (let i = 0; i < cardsHorizont.length; i++) {
            let cardHorizont = cardsHorizont[i];
            cardHorizont.classList.remove("visit");
        }
        let btnSend = document.querySelector('.send');
        let btnNext = document.querySelector('.next');
        btnSend.classList.add('active');
        btnNext.classList.add('hidden');
    }
}


function btnBackClick() {
    lvl--;
    let txt = document.querySelector(".step-desc");
    let txtTitle = document.querySelector(".title_desc");
    if (lvl == 1) {
        let cardsPortf = document.querySelectorAll(".card");
        for (let i = 0; i < cardsPortf.length; i++) {
            let cardPortf = cardsPortf[i];
            cardPortf.classList.remove("hidden");
        }
        let cardsHorizont = document.querySelectorAll(".card_horisont");
        for (let i = 0; i < cardsHorizont.length; i++) {
            let cardHorizont = cardsHorizont[i];
            cardHorizont.classList.remove("visit");
        }
        txt.innerHTML = 'Шаг 1 из 3';
        txtTitle.innerHTML = 'Выберите портфель';

    }
    if (lvl == 2) {
        txt.innerHTML = 'Шаг 2 из 3';
        txtTitle.innerHTML = 'Горизонт инвестирования';
        let range = document.querySelector(".line3");
        range.classList.remove("visit");
        let cardsHorizont = document.querySelectorAll(".card_horisont");
        for (let i = 0; i < cardsHorizont.length; i++) {
            let cardHorizont = cardsHorizont[i];
            cardHorizont.classList.add("visit");
        }
        let btnSend = document.querySelector('.send');
        let btnNext = document.querySelector('.next');
        btnSend.classList.remove('active');
        btnNext.classList.remove('hidden');
    }

    var progresLine = document.querySelector('.progress_line_green');
    var widthGreen = progresLine.offsetWidth;
    var widthFluib = document.querySelector('.progress_line').offsetWidth;
    var width = widthGreen / widthFluib * 100;
    progresLine.style.width = width - 33.333 + "%";
}

function fun1() {
    var rng = document.getElementById('r1'); //rng - это Input
    var p = document.getElementById('one'); // p - абзац
    p.innerHTML = rng.value + " &#8381;";
}
