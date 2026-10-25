from pathlib import Path
import json
p=Path(r'D:/codex/BDD/pk3-remotion-workflow');o=p/'audit';url='https://boromond.com/test-module/pk3/'
rows=[('Product type','Portable BDD electro-oxidation kit','Product Description'),('Recommended test volume','2–5 L','At a Glance'),('Rated power','440 W','Nameplate'),('AC input','AC220 V / AC110 V','Nameplate; configuration, not verified auto switching'),('Frequency','50/60 Hz','Nameplate'),('DC output voltage','0–12 V','Nameplate'),('DC output current','0–35 A','Nameplate'),('Ambient temperature','10–45 °C','Operating Conditions'),('Ambient humidity','≤90%','Operating Conditions'),('Pump flow','0–3 L/min','Operating Conditions; not wastewater throughput'),('Weight','12.5 kg','Operating Conditions'),('Overall size','420 × 320 × 290 mm','Operating Conditions'),('Housing','Aluminum alloy + ABS','Operating Conditions'),('Module dimensions','220 × 180 × 160 mm','Module'),('Anode material','Nb/BDD','Anode'),('Anode dimensions','100 × 50 × 1 mm','Anode'),('Anode quantity','7','Anode'),('Sealed active area','540 cm²','Anode'),('Current density','0–55 mA/cm²','Anode'),('Cathode material','Titanium','Cathode'),('Cathode dimensions','100 × 50 × 1 mm','Cathode'),('Cathode quantity','8','Cathode')]
(o/'verified-parameters.json').write_text(json.dumps({'checked_date':'2026-10-25','source':url,'verification_level':'Manufacturer webpage agreement only; not independent testing or as-built nameplate verification','parameters':[{'name':n,'value':v,'evidence_section':s,'status':'OFFICIAL_PAGE_CONFIRMED'} for n,v,s in rows],'conflicts':[{'name':'Flow path','status':'HOLD','reason':'Intro: parallel / all seven plates equally fed; Product Description and Key Features: zigzag. Do not use until manufacturer resolves.'}],'excluded_claims':['No certification verified','No guaranteed COD removal or time to treatment','No virtual running screen','No throughput claim from pump flow']},indent=2,ensure_ascii=False),encoding='utf-8')
(o/'技术参数核查.md').write_text('# PK3.0 官网核查\n\n核查时间：2026-10-25。来源：'+url+'\n\n“已核对”仅指官网公开文字一致，不等于样机实测、出厂铭牌或第三方认证。\n\n| 参数 | 官网值 | 证据位置 |\n|---|---|---|\n'+''.join(f'|{n}|{v}|{s}|\n' for n,v,s in rows)+'\n## 暂停使用\n流道：页首写 parallel，正文和FAQ相关段落写 zigzag，存在内部冲突，待厂家确认。\n处理效果：葡萄糖模拟废水的条件试验不代表实际废水普遍结果；本样片不使用。\n电源AC110/220V不代表自动宽电压；0–3 L/min是泵流量，不代表处理量。\n无已核实认证资料。样片仅使用产品名称与类别，不展示参数表或性能承诺。\n',encoding='utf-8')
(p/'WORKFLOW.md').write_text('''# BOROMOND PK3.0 专用视频制作流程

1. Skill预检：读取本机Remotion入口、创建、markup、composition、render说明；查找video-shotcraft。缺失只记录，不安装。当前video-shotcraft未找到，不能声称调用；待用户提供已安装路径后，仅用于真实设备的镜头策划。
2. 素材锁定：五张JPG登记路径、分辨率、SHA256，6.png不计入五张。仅第4张正面45°用于本样片。MC088素材、参数及旁白禁止导入。本项目的历史PK3专用配音有独立来源记录。
3. 官网核查：保存结构化参数及冲突清单。OFFICIAL_PAGE_CONFIRMED不等于独立检测。flow-path冲突未解决前不写进画面、旁白。
4. 镜头约束：单镜7.5秒、真实照片固定角度；只等比缩放和平移，0%旋转，不虚构绕拍、内部、接口或通电运行。背景石墨灰，字号克制，标题一处。非生成式人工轮廓遮罩保留原始RGB像素；不重绘、不补全屏幕或设备。
5. Remotion主渲染：用frame/fps驱动动画，不用CSS时间动画。先Studio预览；MP4、关键帧均由Remotion渲染。同版Remotion/CLI版本锁定，package-lock.json记录依赖。FFmpeg仅用于音频取段和成片验证。
6. 声音：复用已经授权并下载的PK3.0 Mike/Orca旁白片段，不沿用MC088，不调用新的TTS、不额外生成试听。音频0.75–7.35秒取段，视频延迟0.45秒入场。没有背景音乐。未经听检不得声称美式发音及自然度已通过。
7. 检查：TypeScript/Remotion渲染、MP4参数、黑帧、音频峰值、三帧对照、遮罩像素来源与结构、文字安全区、声音时码。仍需用户正常速度试听；不以渲染通过证明审美质量。
8. 交付边界：只交付7.5秒16:9样片、三张关键帧、技术参数与审核报告。完整45秒片不启动。

## Skill与依赖边界
Remotion Skill版本4.0.534，项目运行时锁定4.0.538；这是说明包与运行包的补丁差异，使用公共稳定API并实际渲染验证。不装任何新Skill。huashu-art-motion不参与本次渲染和门禁，避免强制快速运动指标与单镜轻推进冲突。

## 授权待核实
原图由用户提供，技术信息来自官网；外部摄影权利归属仍为用户确认项。本样片本机渲染，没有付费API调用。
Remotion许可页 https://www.remotion.dev/docs/license/pricing ：个人/最多3人公司可适用免费许可，较大组织需要公司许可。当前组织规模与既有许可未知，不能宣称商业授权已核实；正式发布前需确认适用许可，不在本任务中购买授权。
''',encoding='utf-8')
