import socket


def get_ip_addresses(domain: str) -> dict[str, list[str]] | None:

    final_dict = {}
    ip_v4_list = []
    ip_v6_list = []

    try:
        result = socket.getaddrinfo(domain, None, type=socket.SOCK_STREAM)
        for item in result:
            if item[0] == socket.AF_INET:
                if item[4][0] not in ip_v4_list:
                    ip_v4_list.append(item[4][0])
            elif item[0] == socket.AF_INET6:
               if item[4][0] not in ip_v6_list:
                    ip_v6_list.append(item[4][0])

        final_dict["IPv4"] = ip_v4_list
        final_dict["IPv6"] = ip_v6_list

    except socket.gaierror:
        return None
    
    return final_dict
