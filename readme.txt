1.进入虚拟环境
2.安装atx:pip install -U --pre uiautomator2  
    如果失败则：pip install -U --pre uiautomator2 -i https://pypi.doubanio.com/simple
    安装获取元素库weditor：pip install --pre --upgrade weditor
3.初始化设备
    adb devices 连接成功后：python -m uiautomator2 init
    
    
截图： 
python -m uiautomator2 screenshot 192.168.1.105 ssss.jpg
    