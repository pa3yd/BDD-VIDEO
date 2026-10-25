# BOROMOND PK3.0 产品视频工作流

使用真实 PK3.0 产品照片制作可编辑、可复用的英文产品视频样片。

- **主渲染：** Remotion 4.0.538，1920×1080，30fps。
- **镜头设计：** video-shotcraft，仅采用适合真实工业设备的运动与光影语法。
- **当前样片：** 7.5 秒，固定正面45°照片、轻微推进、单次柔和高光、英文男声。
- 不使用MC088素材或参数，不生成设备结构、认证、运行画面或性能数据。

## 交付

[最新版 MP4](deliverables/PK3-shotcraft-sample.mp4) · [关键帧1](deliverables/shotcraft-frame-01.png) · [关键帧2](deliverables/shotcraft-frame-02.png) · [关键帧3](deliverables/shotcraft-frame-03.png)

[制作工作流](WORKFLOW.md) · [当前审核摘要](audit/shotcraft-review-summary.md) · [独立审核](audit/shotcraft-independent-review.md) · [官网参数核查](audit/技术参数核查.md)

## 本机运行

需要 Node.js 24（或package.json指定的兼容版本）。

```powershell
npm ci
npm run dev
npx remotion render src/index.ts PK3Hero out/PK3-shotcraft-sample.mp4 --codec=h264 --crf=18
```

如自动浏览器启动失败，可用已安装的 Chromium Headless Shell，并传入 `--browser-executable`；本机示例见 `render-sample.ps1`。不要把绝对路径当成其他电脑也存在的依赖。

`public/`包含用户提供的第4张产品原图、人工背景遮罩和已授权PK3专用旁白片段。`audit/assets.json`登记五张原图指纹，`audit/five-product-images.jpg`为素材总览。

## 状态与限制

video-shotcraft现已安装并实际使用。较早的审核文件是历史记录；以`shotcraft-*`文件为当前版本依据。

设备保持原图角度和结构，没有生成3D模型。人工遮罩细边、白壳光效观感、声音自然度仍需人工观看试听；自动检查通过不等于审美或发音全部合格。

官网的流道文字存在parallel/zigzag冲突，未写入成片。参数核查仅说明官网一致性，不是样机独立实测或认证。来源：https://boromond.com/test-module/pk3/

Remotion商业许可仍需按组织情况核实。npm依赖审计记录见`audit/npm-audit.json`，10项high没有因视频渲染成功而被视为已解决。

不提交node_modules、缓存、环境变量文件、历史打包ZIP。第三方Skill安装目录不复制进本仓库；项目资料记录选卡、索引和引用来源。
