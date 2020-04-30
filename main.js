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

    CopyLink = function () {
        //p要素の文字列を取得
        var text = location.href + "?q=" + $("#search-text").val();
        //textareaを生成
        var area = document.createElement("textarea");
        //p要素の内容をtextareaに記述
        area.textContent = text;
        //生成したものをdocumentに追加
        document.body.appendChild(area);
        //選択/コピーして・・
        area.select();
        document.execCommand("copy");
        //すぐに消す。
        document.body.removeChild(area);
    };
    $('#copy-link').on('click', CopyLink);
    var param = decodeURI(location.search).replace("?q=", "")

    if (param.length > 0) {
        $("#search-text").val(param).trigger('input', [true]);
    }

});