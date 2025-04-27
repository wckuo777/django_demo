const MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
];

const COLORS = [
    '#4dc9f6',
    '#f67019',
    '#f53794',
    '#537bc4',
    '#acc236',
    '#166a8f',
    '#00a950',
    '#58595b',
    '#8549ba'
];

var Utils = (function () {
    function rand(min = 0, max = 1) {
        return Math.random() * (max - min) + min;
    }

    function numbers(config) {
        var cfg = config || {};
        var min = cfg.min ?? 0;
        var max = cfg.max ?? 100;
        var from = cfg.from ?? [];
        var count = cfg.count ?? 8;
        var decimals = cfg.decimals ?? 8;
        var continuity = cfg.continuity ?? 1;
        var dfactor = Math.pow(10, decimals) || 0;
        var data = [];

        for (var i = 0; i < count; ++i) {
            var value = (from[i] || 0) + rand(min, max);
            if (rand() <= continuity) {
                data.push(Math.round(dfactor * value) / dfactor);
            } else {
                data.push(null);
            }
        }

        return data;
    }

    // 回傳可以使用的物件
    return {
        rand,
        numbers
    };
})();
