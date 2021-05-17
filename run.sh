trap 'sudo kill 0' SIGINT
sudo ../Cpp/main.out --led-no-hardware-pulse --led-gpio-mapping=custom --led-rows=16 --led-cols=32 --led-slowdown-gpio=3 --led-brightness=100 &
python3 src/matrix/media_dot.py &
python3 main.py