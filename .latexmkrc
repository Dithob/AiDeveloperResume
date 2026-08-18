# latexmk 配置：使用 XeLaTeX 编译中文简历模板
# 用法：在仓库根目录执行 latexmk main_algorithm.tex
# 行为：
#   1. 全部产物输出到 .output/ 目录
#   2. 编译成功后，PDF 自动重命名为 <文件名>-YYYYMMDD.pdf
#   3. 其余中间产物（.aux/.log/.xdv/.fls/.fdb_latexmk/.synctex.gz 等）自动删除
# 注意：直接用 xelatex 编译不走本配置，产物会留在当前目录

$pdf_mode = 5;                     # 5 = xelatex（先生成 .xdv 再转 PDF）
$xelatex = 'xelatex -interaction=nonstopmode -synctex=1 %O %S';

$out_dir = '.output';              # PDF 输出目录（不存在时 latexmk 自动创建）
$aux_dir = '.output';              # 中间文件目录

# 编译正常退出后：给 PDF 加日期后缀，并删除所有非 PDF 副产物
END {
    # 仅在 latexmk 成功退出（退出码 0）时执行；失败时保留 .log 等便于排错
    if ($? == 0) {
        my $out = $out_dir;
        if (opendir(my $dh, $out)) {
            my @files = readdir($dh);
            closedir($dh);
            my @t = localtime();
            my $date = sprintf('%04d%02d%02d', $t[5] + 1900, $t[4] + 1, $t[3]);
            for my $f (@files) {
                next if $f =~ /^\./;                          # 跳过 . .. 及隐藏文件（如 .DS_Store）
                if ($f =~ /\.pdf$/ && $f !~ /-\d{8}\.pdf$/) {
                    (my $dated = $f) =~ s/\.pdf$/-$date.pdf/;
                    rename "$out/$f", "$out/$dated";          # main_x.pdf -> main_x-YYYYMMDD.pdf
                }
            }
            # 删除全部非 PDF 中间产物
            unlink map { "$out/$_" } grep { !/^\./ && !/\.pdf$/ } @files;
        }
    }
}
