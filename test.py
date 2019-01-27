import uiautomator2 as u2

# d = u2.connect_usb()
d = u2.connect_wifi('192.168.1.105')
d.make_toast('hello',3)
print(d.info)

d(resourceId="cn.nubia.weather:id/input_search").click()
d(resourceId="cn.nubia.browser:id/address_input").set_text("123")