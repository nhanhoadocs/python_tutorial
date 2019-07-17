import shodan

def get_port(hostname):
    api_key = "PcNh5rvG630TK0EiHAeZf2NT0Vo9RbfU"
    api = shodan.Shodan(api_key)
    try:
        info = api.host(hostname)
        datas = info["data"]
        #ports = "Port đang sử dụng\n"
        data = datas[0]
        port = str(data["port"])
        service = str(data["_shodan"]["module"])
        ports = port + ":" + service
          
    except:
        ports = "Error!!!"
    return ports
