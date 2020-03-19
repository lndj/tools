# tools
Some tools, for my life.



## 1. tesla

自动检测国产长续航 model 3 车型是否上架官网，自动微信通知。已构建 docker 镜像，push 到 docker hub。

使用： 

### 1. docker

```shell
docker pull luoning/check-tesla
docker run -e NOTIFY_SECRET='your serverChan secret' -e CHECK_INTERVAL=60 luoning/check-tesla
````

### 2. python
```shell
cd tesla
pip install requests
export NOTIFY_SECRET='your serverChan secret' && export CHECK_INTERVAL=60 && python tesla.py
```

> 微信通知使用了 Server Chan 服务，服务地址： http://sc.ftqq.com/3.version
