from pathlib import Path
import subprocess,json,numpy as np
from PIL import Image
import static_ffmpeg
p=Path(r'D:/codex/BDD/pk3-remotion-workflow');static_ffmpeg.add_paths();v=p/'out/PK3-hero-sample.mp4'
r=subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(v)],capture_output=True,text=True);(p/'audit/render-metadata.json').write_text(r.stdout,encoding='utf-8')
r=subprocess.run(['ffmpeg','-v','error','-i',str(v),'-f','null','-'],capture_output=True,text=True);decode=r.returncode
r=subprocess.run(['ffmpeg','-i',str(v),'-vf','blackdetect=d=0.1:pix_th=0.04','-af','volumedetect','-f','null','-'],capture_output=True,text=True);(p/'audit/black-audio-check.txt').write_text(r.stderr,encoding='utf-8');lines=[s for s in r.stderr.splitlines() if 'black_start:' in s or 'max_volume:' in s or 'mean_volume:' in s]
a=np.array(Image.open(p/'public/pk3-hero.png'));b=np.array(Image.open(p/'public/pk3-source.jpg').convert('RGB').crop((250,165,1330,980)));sel=a[:,:,3]>254;exact=bool(np.array_equal(a[:,:,:3][sel],b[sel]));(p/'audit/pixel-provenance.json').write_text(json.dumps({'opaque_pixel_RGB_exact_source_match':exact,'opaque_pixel_count':int(sel.sum()),'source_crop':[250,165,1330,980],'alpha_method':'manual polygon, one-pixel erosion, 0.45px feather','geometric_changes':'uniform 1.000–1.035 scale only; no rotation, warp or 3D','render_display_correction':'brightness 1.015 / contrast 1.015, low-opacity local lighting overlay'},indent=2),encoding='utf-8')
(p/'audit/审核报告.md').write_text('''# BOROMOND PK3.0 单镜样片审核

## 已交付
7.5秒、1920×1080、30fps、H.264/AAC横屏MP4；3张Remotion关键帧（第20/112/210帧）；可编辑源码、素材登记、技术参数JSON/Markdown和专用WORKFLOW.md。

## 第一阶段：Skill与运行能力
- 已读取Remotion best-practices/create/markup/compositions/render/studio说明，版本4.0.534；实际使用Remotion/CLI 4.0.538，包版本一致，TypeScript编译通过，Studio已可显示PK3Hero合成，MP4和关键帧均由Remotion生成。
- 未在本机skills和plugins/cache中找到video-shotcraft。因此不能声称其已安装或被调用。遵照用户要求，没有安装其他Skill。当前镜头采用明确指定的固定45°、轻微推进；待提供shotcraft路径后，仅纳入策划，不替换Remotion渲染。
- Node24.19.0/npm11.17.0/React19.2.3/TypeScript5.9.3；新建独立项目，不覆盖此前工程。脚手架尝试首次Git提交失败，项目已生成；没有替用户设置Git身份、提交或推送。
- 普通Chromium启动出现spawn UNKNOWN；改用本机Chromium Headless Shell1248后渲染成功。运行时自动下载浏览器不等于安装Skill。
- npm audit报告10项high，主要来自Zod<4.6.6内存耗尽公告及其Remotion依赖链。详见npm-audit.json。没有运行audit fix --force，没有声称安全审计通过。后续公开托管/接受外部输入前应处理，不把本地开发服务器作为已加固服务。
- 当前Remotion组织许可未知。官网免费范围为个人及最多3人的公司，更大组织需核对公司许可。技术可用不等于商业授权已经确认：https://www.remotion.dev/docs/license/pricing 。本任务不购买或注册许可。

## 第二阶段：产品与素材
五张真实JPG已读取并登记SHA256；另有历史第6张PNG，本样片未用。只采用第4张45°图，未导入MC088素材、参数或声音。
技术核对见技术参数核查.md：均明确为“官网公开值已核对”，不是独立实验确认。官网页首parallel与正文zigzag流道描述冲突，已HOLD；没有在片中使用。未使用处理效果、认证、结构示意或运行画面。页面直接抓取返回HTTPError，官网核查通过浏览工具读取完成；没有伪造HTML快照。

## 第三阶段：实际制作
人工轮廓遮罩替换照片背景为石墨灰；不使用生成式补画。去掉原照片环境和宣传条，仅保留实物RGB像素。原图中的设备、散热格栅、接口、屏幕状态不重绘。原背景的广告Logo未直接搬到新场景，品牌以BOROMOND文字标识呈现，产品本体PK3标识保留。
一个固定角度镜头，全程等比推进3.5%，无旋转、透视变化或假3D。轻微亮度/对比度及低强度局部照明，不增加机体部件。人工遮罩边缘仍可存在细小残边，属于需人工精修的质量项，不称为商业精修终稿。
画面标题：PK3.0 | Portable BDD Electro-Oxidation Kit。文字一次出现，不换页、不叠要点、不做模板转场。没有另加整句旁白字幕，以免字幕占据产品。
声音取自此前已授权生成并下载的PK3专用HeyGen Mike/Orca旁白0.75–7.35秒；不是MC088旁白，不冒充本轮新生成。对应文案：“PK3.0 from Boromond—a portable BDD electro-oxidation kit.” 0.45秒入场，约7.05秒结束；没有人为加速，没有背景音乐。

## 第四阶段：检查结论
- Remotion实际渲染完成；TypeScript通过；完整解码状态：'''+str(decode)+'''（0表示通过）。
- 透明设备图的完全不透明像素与原图裁切RGB逐像素一致：'''+str(exact)+'''。仅证明像素来源，不证明人工遮罩每个轮廓点完美。
- 三张关键帧已肉眼检查：型号/标题/机身与底脚未见裁切，图片等比，无新增结构；屏幕保持原图未通电状态，未伪造运行数据。
- 黑帧/峰值检查摘录：
'''+ '\n'.join(lines)+'''
- PPT感：与此前翻页片相比，本片只有一个实物主镜头，无卡片与参数页切换；但仍是照片运动展示，不是真实运行拍摄。是否足够高级，需要用户按正常速度观看判断，不以程序通过替代审美验收。
- 同步：音频区间按已返回的PK3原旁白逐词时码切段；标题在开始0.65秒内落定，声音约0.51秒起读。音轨存在和时间匹配已检查；未直接听取完整输出，不宣称品牌读音、男声自然度和实际听感已全面通过。

## 仍待核实
video-shotcraft的安装位置；Remotion公司许可；流道冲突；人工遮罩细边与最终听感。以上没有被悄悄省略或当成通过。没有启动45秒完整视频。
''',encoding='utf-8')
print('decode',decode,'pixels_exact',exact);print('\n'.join(lines))
