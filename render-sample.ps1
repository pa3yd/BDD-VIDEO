# Run from this project directory after npm ci.
$taskBrowser='C:/Users/Administrator/AppData/Local/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-win64/chrome-headless-shell.exe'
if(Test-Path -LiteralPath $taskBrowser){
  & npx.cmd remotion render src/index.ts PK3Hero out/PK3-shotcraft-sample.mp4 --codec=h264 --crf=18 --browser-executable=$taskBrowser
} else {
  & npx.cmd remotion render src/index.ts PK3Hero out/PK3-shotcraft-sample.mp4 --codec=h264 --crf=18
}

