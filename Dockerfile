#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#
# Izzy Ganteng

FROM ayiinxd/ayiin:xd

RUN git clone -b Uputt-Userbot https://github.com/iamuput/Uputt-Userbot /home/uputtuserbot/ \
    && chmod 777 /home/uputtuserbot\
    && mkdir /home/uputtuserbot/bin/

#COPY ./sample.env ./.env* /home/darenucelbot/

WORKDIR /home/uputtuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
