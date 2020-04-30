import os

findex = open("index.html", "w")
findex.write("""<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ロードラ軽量ストーリー検索</title>

<head>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/earlyaccess/notosansjp.css">
</head>

<body>
    <div class="wrapper">
        <div class="search-area">
            <input type="text" id="search-text" placeholder="検索キー(2文字以上)">
            <button id="copy-link">copy link to this page</button>
            <div class="search-result">
                <div class="search-result__hit-num"></div>
                <div id="search-result__list"></div>
            </div>
        </div>
        <table class="table table-bordered table-hover table-condensed">
            <thead>
                <tr>
                    <th title="Field #1">no</th>
                    <th title="Field #2">name</th>
                    <th title="Field #3">rarity</th>
                    <th title="Field #4">attribute</th>
                    <th title="Field #5">story</th>
                    <th title="Field #6">cutin1</th>
                    <th title="Field #7">cutin2</th>
                    <th title="Field #8">cutin3</th>
                    <th title="Field #9">cutin4</th>
                </tr>
            </thead>
            <tbody class="target-area">""")

for filename in sorted(os.listdir("./rawcsv")):
    if "csv" not in filename:
        continue
    with open(f"./rawcsv/{filename}") as f:
        # 先頭行を読んでおく
        f.readline()
        for line in f.readlines():
            if len(line.split(",")) < 5:
                continue

            no, name, star, attr, story = line.split(",")[:5]
            cutins = line.split(",")[5:]

            # storyの中に半角カンマが含まれるものをcatch
            if int(no) in {883, 952, 989, 1400, 1577, 1600}:
                no, name, star, attr, story1, story2 = line.split(",")[:6]
                story = f"{story1},{story2}"
                cutins = line.split(",")[6:]

            cutin_str = "</td><td>".join([f"{text}" for text in cutins])
            findex.write(
                f"<tr class=\"hidden\"><td>{no}</td><td>{name}</td><td>{star}</td><td>{attr}</td><td class=\"story\">{story}</td><td>{cutin_str}</td></tr>\n")
findex.write("""</tbody></table></div><!-- /.wrapper -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
    <script src="main.js"></script>
</body>
</html>""")
findex.close()
