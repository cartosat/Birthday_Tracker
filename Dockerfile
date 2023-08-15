FROM python:3.10.10-bullseye

ARG ENABLE_NONROOT_DOCKER="true"
ARG INSTALL_ZSH="false"
ARG UPGRADE_PACKAGES="false"
ARG USERNAME="vips"
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG USE_MOBY="true"
ARG INSTALL_ZSH="false"
ENV DOCKER_BUILDKIT=1

COPY .devcontainer/library-scripts/*.sh /tmp/library-scripts/

RUN apt-get update \
    && apt-get install -y dos2unix python3-dev default-libmysqlclient-dev build-essential \
    pkg-config graphviz\
    && dos2unix /tmp/library-scripts/common-debian.sh \
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "false" "true" \
    # Use Docker script from script library to set things up
    && dos2unix /tmp/library-scripts/docker-debian.sh \
    && /bin/bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}" \
    # Clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /workspace

ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]
