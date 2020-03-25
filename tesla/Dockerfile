FROM python:3.7.7-alpine3.10

RUN pip install requests \
  && sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
  && apk update && apk add tzdata \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \ 
  && echo "Asia/Shanghai" > /etc/timezone
  
ADD . .

CMD [ "python", "tesla.py" ]
