import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

st = speedtest.Speedtest()

start = input("Press Enter to Start")
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
ping = int(st.results.ping)

print('D/L: ' + down_speed + 'mb/s')
print('U/L: ' + up_speed + 'mb/s')
print(f"Ping: {ping} ms")
