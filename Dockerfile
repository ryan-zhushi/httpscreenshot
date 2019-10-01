FROM markadams/chromium-xvfb

RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean && apt-get update && apt-get install -y \
    python3 python3-pip nginx curl unzip

ENV CHROMEDRIVER_VERSION 76.0.3809.126
RUN curl -SLO "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip "chromedriver_linux64.zip" -d /usr/local/bin \
    && rm "chromedriver_linux64.zip"

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY . /opt/httpscreenshot

WORKDIR /opt/httpscreenshot
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

EXPOSE 80
ENTRYPOINT ["./entrypoint.sh"]

