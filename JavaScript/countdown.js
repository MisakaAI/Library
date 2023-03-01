/* 倒计时

# html 文件

<span class="hour">00</span>:<span class="minute">00</span>:<span class="second">00</span>

# css 字体推荐
@font-face {
    font-family: 'PUTHIAfont';
    src: url("PUTHIAfont.ttf");
}

*/

// 获取 html 中的天数
// var day = document.querySelector(".day");
// 获取 html 中的小时
var hour = document.querySelector(".hour");
// 获取 html 中的分钟
var minute = document.querySelector(".minute");
// 获取 html 中的秒
var second = document.querySelector(".second");
// 结束时间
var end_time = new Date("2023-06-22 00:00:00");

// 定时器 每秒钟执行一次
setInterval(countDown, 1000);

// 倒计时
function countDown() {
    // 获取当前时间的时间戳（单位毫秒）
    var now_time = new Date();
    // 把剩余时间毫秒数转化为秒
    var times = (end_time - now_time) / 1000;
    // 天 = 转化为整数 ÷ 60秒 ÷ 60分钟 ÷ 24小时
    // var d = parseInt(times / 60 / 60 / 24);
    // day.innerHTML = d;

    // 小时 = 转化为整数 ÷ 60秒 ÷ 60分钟（ ÷ 24小时的余数）
    // 如果要加入天数，则 var h = parseInt(times / 60 / 60 % 24);
    var h = parseInt(times / 60 / 60);
    // 赋值 时 : 如果小时数小于 10，要变成 0 + 数字的形式
    hour.innerHTML = h < 10 ? "0" + h : h;

    // 分钟 = 转化为整数 ÷ 60秒 ÷ 60分钟的余数
    var m = parseInt(times / 60 % 60);

    // 赋值 分 : 如果分钟数小于 10，要变成 0 + 数字的形式
    minute.innerHTML = m < 10 ? "0" + m : m;

    // 秒 转化为整数 ÷ 60秒的余数
    var s = parseInt(times % 60);
    // 赋值 秒 : 如果秒钟数小于 10，要变成 0 + 数字的形式
    second.innerHTML = s < 10 ? "0" + s : s;
}

// 打开网页立即执行一次计时器，否则会延迟 1s 开始倒计时
countDown()