# Python

## Create Google Assistant API
### Access the Google Console: https://console.actions.google.com  
### Add project: Click “Add/import project”
<img src="./img/1.png" height=400>
<img src="./img/2.png" height=400>

### Click "Are you looking for device registration?"
<img src="./img/3.png" height=400>

### Visit https://console.developers.google.com/apis
<img src="./img/4.png" height=400>

<img src="./img/5.png" height=400>

<img src="./img/6.png" height=400>

<img src="./img/7.png" height=400>

### Download OAuth 2.0 credentials
<img src="./img/8.png" height=400>

### Copy credentials to Raspberry Pi
```sh
~ $ google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --scope https://www.googleapis.com/auth/gcm --save --headless --client-secrets /home/pi/Downloads/[your client oauth file name].json
```

## Create Dialogflow

### Access the Dialogflow: https://dialogflow.cloud.google.com/

### Create Project
<img src="./img/9.png" height=400>

### Write like this and press CREATE button
<img src="./img/10.png" height=400>

### [Click to Download Dialogflow File](https://github.com/Hi-Class/Python/blob/main/dialogflow_settings/speaker.zip) and Import From ZIP
<img src="./img/11.png" height=400>

## Install
```sh
[Respeaker Setting]
~ $ git clone https://github.com/respeaker/seeed-voicecard.git
~ $ cd seeed-voicecard
~/seeed-voicecard $ sudo ./install.sh
~ $ sudo apt-get update
~ $ sudo apt-get install portaudio19-dev libffi-dev libssl-dev ~ $ libmpg123-dev

[Source Clone and Install Python modules]
~ $ mkdir Hi-Class
~ $ cd Hi-Class
~/Hi-Class $ git clone https://github.com/Hi-Class/Python.git
~/Hi-Class $ cd Python 
~/Hi-Class/Python $ pip3 install -r requirements.txt
```

## Run
```sh
~ $ cd Hi-Class
~/Hi-Class $ cd Python
~/Hi-Class/Python $ python3 main.py
```