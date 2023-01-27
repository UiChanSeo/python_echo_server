# echo_server_python
```
이 프로그램은 파이썬에서 RAW 소켓을 이용하여 텍스트 문자를 수신하여 바로 전송하는 에코 프로그램입니다.
통신 프로그램의 기본인 소켓을 이용하여 클라이언트/서버가 통신을 합니다.
```
# 사용법
```
python main.py
```
# 작성자
```
seouichan@naver.com
```
# 테스트 예
## 서버
```
~echo_server_python % python main.py 
Socket is created.[<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>]
Socket is now listening.
Connected with 127.0.0.1:58016
Received : hi!

Received : My name is chan.

```
## 클라이언트
```
~echo_server_python % telnet localhost 8888
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Welcome to the server. Type something and hit enter.
hi!
OK... : hi!
My name is chan.
OK... : My name is chan.
```
