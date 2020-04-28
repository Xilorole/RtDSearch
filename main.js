$(function () {
    searchWord = function () {
        var searchText = $(this).val(), // 検索ボックスに入力された値
            targetText;

        $('.target-area tr').each(function () {

            targetText = $(this).text();

            // 検索対象となるリストに入力された文字列が存在するかどうかを判断
            if (searchText.length < 2) {
                $(this).addClass('hidden');
            } else if (targetText.indexOf(searchText) != -1) {
                $(this).removeClass('hidden');
            } else {
                $(this).addClass('hidden');
            }
        });
    };

    // searchWordの実行
    $('#search-text').on('input', searchWord);
});