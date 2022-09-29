FROM centos:8

RUN cd /etc/yum.repos.d/ || exit
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

RUN dnf install -y python38

RUN pip install --no-cache-dir pytest
RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install pytest

ENTRYPOINT [ "/bin/bash" ]