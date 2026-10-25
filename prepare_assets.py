from PIL import Image,ImageDraw,ImageFilter
from pathlib import Path
import shutil,json,hashlib,urllib.request
p=Path(r'D:/codex/BDD/pk3-remotion-workflow');o=p/'audit';o.mkdir(exist_ok=True);pub=p/'public';pub.mkdir(exist_ok=True)
s=Image.new('RGB',(1500,480),'white');inv=[]
for i in range(1,6):
 src=Path(r'D:/codex/BDD/PK3-design/assets')/f'{i}.jpg';im=Image.open(src);inv.append({'file':str(src),'size':im.size,'sha256':hashlib.sha256(src.read_bytes()).hexdigest()});im.thumbnail((300,450));s.paste(im,((i-1)*300,0))
s.save(o/'five-product-images.jpg');(o/'assets.json').write_text(json.dumps(inv,indent=2),encoding='utf-8')
im=Image.open(r'D:/codex/BDD/PK3-design/assets/4.jpg').convert('RGBA');mask=Image.new('L',im.size);d=ImageDraw.Draw(mask)
points=[(265,342),(595,305),(595,281),(625,211),(637,207),(796,179),(822,177),(841,181),(882,249),(1267,272),(1271,319),(1279,321),(1309,817),(1308,838),(1308,851),(1279,863),(1186,939),(1090,963),(1042,964),(697,949),(654,942),(641,927),(303,814),(296,790),(279,785)]
d.polygon(points,fill=255)
d.polygon([(647,251),(786,232),(789,244),(680,250),(678,300),(646,305)],fill=0)
mask=mask.filter(ImageFilter.GaussianBlur(.5));im.putalpha(mask);im=im.crop((250,165,1330,980));im.save(pub/'pk3-hero.png')
shutil.copyfile(r'D:/codex/BDD/PK3-design/assets/4.jpg',pub/'pk3-source.jpg')
# Use the existing authorized PK3 narration. This is not the MC088 audio.
import subprocess,static_ffmpeg
static_ffmpeg.add_paths();r=subprocess.run(['ffmpeg','-i',r'D:/codex/BDD/PK3-huashu/film/output/PK3-narration.wav','-ss','0.75','-t','6.6','-af','afade=t=in:d=0.035,afade=t=out:st=6.5:d=0.1,loudnorm=I=-16:TP=-1.5:LRA=7','-ar','48000','-c:a','pcm_s16le','-y',str(pub/'pk3-voice.wav')],capture_output=True);print('Audio excerpt',r.returncode)
try:(o/'official-pk3.html').write_bytes(urllib.request.urlopen('https://boromond.com/test-module/pk3/').read())
except Exception as e:print(type(e).__name__)
