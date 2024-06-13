# Section 1- Base Image
FROM python:3.10-slim

# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Section 2.1 - Set language to english
ENV LANG en_US. UTF-8  
ENV LANGUAGE en_us:en  

# Section 2.2 - Set variables and display them during build process
ARG CLUSTER="app"

RUN echo "CLUSTER=${CLUSTER}"

ENV CENTRAL="${CLUSTER}.central.arubanetworks.com"

RUN echo "${CENTRAL}"

# Section 3- Compiler and OS libraries
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Section 4- Project libraries and User Creation
COPY requirements.txt /tmp/requirements.txt

RUN pip install websocket-client

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U streamingapi \
    && install -d -m 0755 -o streamingapi -g streamingapi /streamingapi

# Section 5- Code and User Setup
WORKDIR /streamingapi
ADD . /streamingapi
USER streamingapi:streamingapi
COPY --chown=streamingapi:streamingapi . .

# Section 6- Docker Run Checks and Configurations
CMD python3 wsclient_public.py --hostname ${CENTRAL} --jsoninput input.json --decode_data