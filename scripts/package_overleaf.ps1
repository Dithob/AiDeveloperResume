<#
.SYNOPSIS
    把与主要简历相关的 LaTeX 内容打包成 zip，可直接导入 Overleaf 继续编辑（XeLaTeX 编译中文简历）。

.DESCRIPTION
    生成的 zip 只包含编译简历所需的最小文件集：
      - 选中的 main_*.tex 模板（默认四个全打）
      - tex\     共享版式与个人信息（真实 profile.tex / education.tex；加 -Sanitize 时改用 *.example 占位）
      - fonts\   内置中文字体（preamble 用 fonts\ 相对路径加载，Overleaf 无需另装字体）
      - images\  页眉、照片、校徽等图片素材
      - latexmkrc            Overleaf 专用最小配置（强制 XeLaTeX 引擎）
      - README-Overleaf.txt  导入说明
    刻意排除 scripts\（本地编译/打包脚本）、reference\、skills\、docs\ 与全部编译产物。
    仓库自带的 .latexmkrc（面向本地 latexmk：输出重定向到 .output\ 并给 PDF 改名）不打包，
    改为生成一个 Overleaf 专用最小 latexmkrc，强制使用 XeLaTeX（Overleaf 默认 pdfLaTeX 无法编译本模板）。

.PARAMETER Template
    打包范围：all（默认，四个模板全打）/ algorithm / backend / frontend / testdevelop。
    也接受 main_algorithm 等带 main_ 前缀的写法。

.PARAMETER Sanitize
    改用脱敏的 tex\data\*.tex.example 占位数据，并从 images\ 中剔除真实照片。
    当 zip 可能被分享、不希望带上真实个人信息时使用。

.PARAMETER OutDir
    zip 输出目录，默认 <仓库根>\overleaf。

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\package_overleaf.ps1
    powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\package_overleaf.ps1 -Template backend
    powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\package_overleaf.ps1 -Template algorithm -Sanitize

.NOTES
    默认打包 tex\data\ 下的真实个人信息与真实照片，生成的 zip 请勿随意传播；
    如需分享/留档脱敏版本，请加 -Sanitize。
#>

[CmdletBinding()]
param(
    [ValidateSet('all', 'algorithm', 'backend', 'frontend', 'testdevelop',
                 'main_algorithm', 'main_backend', 'main_frontend', 'main_testdevelop')]
    [string]$Template = 'all',

    [switch]$Sanitize,

    [string]$OutDir = ''
)

$ErrorActionPreference = 'Stop'

# 脚本位于仓库 script\ 子目录，仓库根取其父目录（无论在哪个目录调用都正确）
$root = Split-Path -Parent $PSScriptRoot

# ---- 1. 解析模板选择 ----
$base = $Template -replace '^main_', ''
switch ($base) {
    'all'         { $tplNames = @('main_algorithm.tex', 'main_backend.tex', 'main_frontend.tex', 'main_testdevelop.tex') }
    'algorithm'   { $tplNames = @('main_algorithm.tex') }
    'backend'     { $tplNames = @('main_backend.tex') }
    'frontend'    { $tplNames = @('main_frontend.tex') }
    'testdevelop' { $tplNames = @('main_testdevelop.tex') }
    default       { throw "Unknown template: $Template" }
}

foreach ($f in $tplNames) {
    if (-not (Test-Path -LiteralPath (Join-Path $root $f) -PathType Leaf)) {
        throw "Cannot find $f under $root"
    }
}

# ---- 2. 输出路径 ----
if ([string]::IsNullOrWhiteSpace($OutDir)) { $OutDir = Join-Path $root 'overleaf' }
if (-not (Test-Path -LiteralPath $OutDir -PathType Container)) {
    $null = New-Item -ItemType Directory -Path $OutDir -Force
}

if ($tplNames.Count -eq 1) {
    $zipLabel = [IO.Path]::GetFileNameWithoutExtension($tplNames[0])
} else {
    $zipLabel = 'all'
}
$zipName = 'resume-overleaf-{0}-{1:yyyyMMdd-HHmm}.zip' -f $zipLabel, (Get-Date)
$zipPath = Join-Path $OutDir $zipName

# ---- 3. 组装暂存目录 ----
$stage = Join-Path ([IO.Path]::GetTempPath()) ('ai-resume-overleaf-' + [guid]::NewGuid().ToString('N'))
$null = New-Item -ItemType Directory -Path $stage

try {
    Copy-Item -LiteralPath (Join-Path $root 'fonts') -Destination $stage -Recurse -Force
    Copy-Item -LiteralPath (Join-Path $root 'images') -Destination $stage -Recurse -Force
    Copy-Item -LiteralPath (Join-Path $root 'tex') -Destination $stage -Recurse -Force
    foreach ($f in $tplNames) {
        Copy-Item -LiteralPath (Join-Path $root $f) -Destination (Join-Path $stage $f) -Force
    }

    # ---- 4. 个人信息数据：真实 or 脱敏占位 ----
    $realProfile = Join-Path $root 'tex\data\profile.tex'
    $realEdu     = Join-Path $root 'tex\data\education.tex'
    $exProfile   = Join-Path $root 'tex\data\profile.tex.example'
    $exEdu       = Join-Path $root 'tex\data\education.tex.example'

    $useReal = (-not $Sanitize) -and (Test-Path -LiteralPath $realProfile) -and (Test-Path -LiteralPath $realEdu)

    if ($useReal) {
        Copy-Item -LiteralPath $realProfile -Destination (Join-Path $stage 'tex\data\profile.tex') -Force
        Copy-Item -LiteralPath $realEdu     -Destination (Join-Path $stage 'tex\data\education.tex') -Force
        $dataNotes = '打包的是你本地的真实个人信息（tex\data\profile.tex、education.tex，含真实姓名/联系方式/照片），导入后可直接编辑，请勿随意传播；如需脱敏版请加 -Sanitize。'
    } else {
        if (-not $Sanitize) {
            Write-Warning '未找到 tex\data\profile.tex / education.tex（首次克隆需按 readme「第 0 步」从 *.example 复制），本次回退为 *.example 脱敏占位数据。'
        }
        Copy-Item -LiteralPath $exProfile -Destination (Join-Path $stage 'tex\data\profile.tex') -Force
        Copy-Item -LiteralPath $exEdu     -Destination (Join-Path $stage 'tex\data\education.tex') -Force
        $dataNotes = '本次为脱敏版：tex\data\profile.tex、education.tex 来自 *.example 占位内容，导入 Overleaf 后请填入你的真实信息与照片。'
    }

    # 脱敏模式下的图片收尾：剔除真实照片，并为占位模板的默认照片路径补一个可用文件
    if ($Sanitize) {
        foreach ($p in @('images\me.jpg', 'images\photo_mine.jpg')) {
            $pp = Join-Path $stage $p
            if (Test-Path -LiteralPath $pp) { Remove-Item -LiteralPath $pp -Force }
        }
        $kunPng = Join-Path $stage 'images\kun.png'
        if (Test-Path -LiteralPath $kunPng) {
            Copy-Item -LiteralPath $kunPng -Destination (Join-Path $stage 'images\kun.jpg') -Force
        }
    }

    # ---- 4.5 Overleaf 专用 latexmkrc：强制 XeLaTeX（仓库根的 .latexmkrc 只面向本地 latexmk，不能带入）----
    $latexmkrc = @'
# AiDeveloperResume project rc for Overleaf.
# This resume must be typeset with XeLaTeX (xeCJK/fontspec + bundled .otf fonts);
# pdfLaTeX cannot compile it and stops with a fatal fontspec error.
# Overleaf compiles via latexmk; forcing $pdf_mode = 5 below auto-selects XeLaTeX,
# so no manual Menu -> Compiler change is needed in most cases.
# Note: the output directory is left at its default, so the PDF stays at the project root.
$pdf_mode = 5;    # 5 = xelatex -> PDF (xelatex + xdvipdfmx)
'@
    Set-Content -LiteralPath (Join-Path $stage 'latexmkrc') -Value $latexmkrc -Encoding ASCII

    # ---- 5. 写入 Overleaf 说明 ----
    $tplText = $tplNames -join '、'
    $readme = @"
AiDeveloperResume - Overleaf 导入说明
=====================================

本 zip 由 package_overleaf.ps1 生成，只含编译简历所需的最小文件集，
可在 Overleaf 直接导入并继续编辑（XeLaTeX 编译中文简历）。

一、包内内容
  - $tplText               简历主文档
  - tex\shared\            preamble.tex / components.tex（版式与通用组件）
  - tex\data\              profile.tex / education.tex（个人信息与教育背景，见「四」）
  - fonts\                 内置 Noto Serif SC 中文字体
  - images\                页眉、照片、校徽等图片素材
  - latexmkrc              Overleaf 专用最小配置：强制 XeLaTeX（见「三」）
  - 本说明文件

二、刻意排除（避免干扰 Overleaf 或带入无关内容）
  scripts\（本地编译/打包脚本）、reference\、skills\、docs\、.git 及编译产物等。
  仓库自带的 .latexmkrc（面向本地 latexmk：输出重定向到 .output\ 并给 PDF 加日期后缀）不打包——
  它会干扰 Overleaf 预览；取而代之的是本包根目录一个 Overleaf 专用最小 latexmkrc（强制 XeLaTeX）。

三、导入与修改步骤
  1. Overleaf 右上角 New Project -> Upload Project，上传本 zip。
  2. 若包内含多个 main_*.tex，先在左上角 Menu -> Main Document 选择本次要修改的模板
     （例如 main_algorithm.tex），Overleaf 会记住该选择。
  3. 直接 Recompile：根目录的 latexmkrc 已强制 XeLaTeX，多数情况下无需手动切换。
     若日志仍以 "This is pdfTeX" 开头并报 fontspec 致命错误（说明 Overleaf 未读取 latexmkrc），
     请打开 Menu -> Compiler 手动选一次 XeLaTeX（项目级记忆，只需一次）再 Recompile。
  4. Recompile 成功即可左侧改代码、右侧实时预览 PDF。

四、个人信息说明
  $dataNotes
  替换照片：直接覆盖 images\ 下的照片文件，或在 tex\data\profile.tex 中修改 \ResumePhoto 路径。
  说明：*.example 是脱敏模板，仅作参考；正常打包已自带 tex 数据，无需再复制 example 文件。

五、导出 PDF
  Overleaf 预览面板点击下载即可导出最终 PDF；或左侧文件树右键 PDF。
"@
    $readmePath = Join-Path $stage 'README-Overleaf.txt'
    Set-Content -LiteralPath $readmePath -Value $readme -Encoding UTF8

    # ---- 6. 压缩 ----
    Write-Host ''
    Write-Host 'Packing into zip:' -ForegroundColor Cyan
    foreach ($f in $tplNames) { Write-Host ('  - ' + $f) }
    Write-Host '  - tex\  fonts\  images\  latexmkrc  README-Overleaf.txt'

    Compress-Archive -Path (Join-Path $stage '*') -DestinationPath $zipPath -CompressionLevel Optimal -Force

    $item = Get-Item -LiteralPath $zipPath
    $sizeMb = '{0:N2}' -f ($item.Length / 1MB)
    Write-Host ''
    Write-Host ('Zip created: {0}  ({1} MB)' -f $zipPath, $sizeMb) -ForegroundColor Green

    if ($useReal) {
        Write-Warning '注意：本 zip 包含真实个人信息（tex\data\*.tex 与真实照片），请勿随意分享/上传公开仓库；需要脱敏版本请加 -Sanitize。'
    }

    Write-Host ''
    Write-Host 'Overleaf 使用提示：' -ForegroundColor Yellow
    $tips = @(
        '  1) New Project -> Upload Project，上传该 zip'
    )
    if ($tplNames.Count -gt 1) {
        $tips += '  2) 在 Menu -> Main Document 选择本次要修改的模板（本包含多个 main_*.tex）'
        $tips += '  3) 直接 Recompile：包内 latexmkrc 已强制 XeLaTeX；若日志仍以 pdfTeX/fontspec 报错，'
        $tips += '     请 Menu -> Compiler 手动选一次 XeLaTeX（仅需一次）再 Recompile'
    } else {
        $tips += '  2) 直接 Recompile：包内 latexmkrc 已强制 XeLaTeX；若日志仍以 pdfTeX/fontspec 报错，'
        $tips += '     请 Menu -> Compiler 手动选一次 XeLaTeX（仅需一次）再 Recompile'
    }
    $tips | ForEach-Object { Write-Host $_ }
}
finally {
    if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
}
