# PK3.0 样片：安装后实际调用 video-shotcraft

交付：out/PK3-shotcraft-sample.mp4，7.5秒1920×1080@30，H.264/AAC。三张关键帧：第20、74、210帧。
已从Skill Gallery索引确认light-play-moves / sheen-sweep，并读取准确SheenSweepRetry.tsx参考实现。
本版采用单次115°光带、58–90帧（约1.93–3秒）、swift(.4,0,.2,1)、条件挂载/结束卸载、机身alpha遮罩。光层强度28%，避免改变白色外壳观感。非完整demo复制：用户禁止虚构角度，因此去掉rotateY、悬浮、模拟卡片材质；原屏幕保持静态、不亮屏、不补结构。
与上版差别：取消全程漂移的局部光斑，改为一次有明确起止的柔和反射；摄影机推进在5.5秒落定，5.5–7.5秒真静止hold，保留同一真实45°照片。标题沿用用户指定英文名，没有参数页、转场、BGM、额外CTA。已授权PK3男声仍0.45–7.05秒，无新增API调用或付费。
只让video-shotcraft承担镜头设计，没有自动安装其完整工作台依赖或启动完整宣传片模式。Remotion继续主渲染；未修改设备原像素来源与人工遮罩。
TypeScript和Remotion渲染通过，ffprobe参数匹配，完整解码返回0，blackdetect未见连续0.1秒以上黑帧，音频峰值见shotcraft-decode-audio.txt，未削波。程序检查不等于音色自然或品牌发音验收。
本机没有Gallery参考MP4，因此不能验证动态参考样片一致性；提供了准确demo源码与索引供独立审查。独立审片记录另见shotcraft-independent-review.md。
旧audit/审核报告.md是补装前版本的历史检查；video-shotcraft已安装可读取，缺失状态已解除。官网流道冲突、Remotion组织许可未知及npm审计10项high仍未因装Skill而解决，继续沿用历史报告对应限制。
仍是照片运动展示，不是设备运行录像；人工遮罩轮廓边缘和压缩后细节仍需人眼检查。未启动45秒完整片。

## 独立审核后修正
BOROMOND字号由24提升至46px，副标题由37提升至48px，已重渲染全部关键帧和MP4。WORKFLOW第1步安装状态已更新；render-metadata.json现指当前shotcraft版，旧metadata单独保留为render-metadata-before-shotcraft.json。白壳光效可感知度/细边与实际听感仍保留质量限制，未宣称全项通过。
