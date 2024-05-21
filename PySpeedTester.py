import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return round(float(bytes/MB),2)

st = speedtest.Speedtest()

start = input("Press Enter to Start: ")
st.get_best_server()
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
ping = int(st.results.ping)

server = st.results.server
server_name = server['sponsor']
server_location = server['name']
server_country = server['country']

print("------------------------------")
print(f'Server: {server_name}, {server_location}, {server_country}')
print('D/L:  ' +  down_speed + ' Mbps')
print('U/L:  ' + up_speed + ' Mbps')
print(f"Ping: {ping} ms")
print("------------------------------")

