from PIL import Image,ImageDraw,ImageFilter
from pathlib import Path
p=Path(r'D:/codex/BDD/pk3-remotion-workflow');im=Image.open(p/'public/pk3-source.jpg').convert('RGBA');mask=Image.new('L',im.size);d=ImageDraw.Draw(mask)
points=[(273,343),(598,305),(598,282),(627,212),(638,208),(797,181),(822,179),(839,182),(879,249),(1265,274),(1269,320),(1277,323),(1307,813),(711,934),(698,945),(655,941),(643,927),(304,813),(298,789),(280,782)]
d.polygon(points,fill=255);d.polygon([(647,251),(786,232),(789,244),(680,250),(678,300),(646,305)],fill=0)
mask=mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.45));im.putalpha(mask);im.crop((250,165,1330,980)).save(p/'public/pk3-hero.png')
