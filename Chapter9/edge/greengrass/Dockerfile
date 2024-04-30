FROM amazonlinux:2023

ARG AWS_REGION
ARG AWS_DEVICE_NAME
ARG AWS_DEVICE_GROUP

ARG AWS_ACCESS_KEY_ID
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ARG AWS_SECRET_ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ARG AWS_SESSION_TOKEN
ENV AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN}

RUN yum update && yum install -y unzip wget sudo shadow-utils less systemd systemd-sysv kernel-libbpf which procps-ng
RUN yum install -y java


RUN curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip && unzip greengrass-nucleus-latest.zip -d GreengrassInstaller

RUN java -Droot="/greengrass/v2" -Dlog.store=FILE -jar ./GreengrassInstaller/lib/Greengrass.jar \ 
                --aws-region ${AWS_REGION} \
                --thing-name ${AWS_DEVICE_NAME} \
                --thing-group-name ${AWS_DEVICE_GROUP} \
                --component-default-user ggc_user:ggc_group --provision true --setup-system-service true --deploy-dev-tools true

CMD ["/usr/sbin/init"]