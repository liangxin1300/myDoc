help links:
1) [PIL简明教程](https://liam0205.me/2015/04/22/pil-tutorial-basic-usage/) 
2) [PIL廖雪峰](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000)

```Python
from PIL import Image
picName = "sanpang.jpg"
picFd = Image.open(picName)
picFd.show()
print(picFd.format, picFd.size, picFd.mode)
```

```Python
import os, sys
from PIL import Image

def convert_pic_ext(pic_name, pic_ext):
    infile = os.path.basename(pic_name)
    f, e = os.path.splitext(infile)
    outfile = f + "." + pic_ext.strip('.')
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
            Image.open(outfile).show()
            os.remove(outfile)
        except IOError:
            print("cannot convert ", infile)

convert_pic_ext(sys.argv[1], "png")
```
