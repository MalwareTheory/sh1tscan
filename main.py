import socket

def main() :
    print("====== SH1T SCAN (Port scanner) ===")
    target_ip = input("Enter the target ip adress: ")
    common_tcp_ports = [
        21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 
        443, 445, 993, 995, 1433, 1521, 3306, 3389, 
        5432, 5900, 6379, 8080, 8443, 27017
    ]
    for ports in common_tcp_ports :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, ports))

        if result == 0 :
            print(f"Port {ports} open")
        else :
            print(f"Port {ports} closed")








        
main()