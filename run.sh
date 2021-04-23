trap 'sudo kill 0' SIGINT
sudo /home/pi/projects/led_matrix_16x32_test/bin/ARM/Debug/led_matrix_16x32_test.out --led-no-hardware-pulse --led-gpio-mapping=custom --led-rows=16 --led-cols=32 --led-slowdown-gpio=5 --led-brightness=100 &
python3 src/matrix/media_dot.py &
python3 main.py

# omxplayer

# 토큰 만료 될때
# google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --scope https://www.googleapis.com/auth/gcm --save --headless --client-secrets client_secret_242001129964-hosauo8ih5avm66cv03dqsftfr4i0rfd.apps.googleusercontent.com.json