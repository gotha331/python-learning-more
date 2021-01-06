from distutils.core import setup

setup(name="dm_message",  # 包名
      version="1.0",
      description="自制的 发送和接收消息模块",
      long_description="完整描述 - 自制的 发送和接收消息模块",
      author="shuaishuai liu",
      author_email="123456789@qq.com",
      url="www.baidu.com",
      py_modules=["dm_message.send_message",
                  "dm_message.receive_message"]
      )
