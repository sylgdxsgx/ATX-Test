python3.6.0
0.导出所有包：pip freeze --all > requirements.txt
0.导出所有包：pip download -d D:\python\ATX\ATX-Test\whls -r requirements.txt
1.进入虚拟环境
2.安装所有包（进入whls目录安装，可能.要改成绝对路径)
    pip install --no-index --find-index= . -r requirements.txt     （也可能是 --find-link 或 --find-links）

(这步不要了)
2.安装atx:pip install -U --pre uiautomator2  
    如果失败则：pip install -U --pre uiautomator2 -i https://pypi.doubanio.com/simple
    安装获取元素库weditor：pip install --pre --upgrade weditor


3.初始化设备（每次连接手机都要执行一遍该命令来启动atx-agent）
    adb devices 连接成功后：python -m uiautomator2 init
    
    
截图： 
python -m uiautomator2 screenshot 192.168.1.105 ssss.jpg

截图：d.screenshot("home.jpg")
    