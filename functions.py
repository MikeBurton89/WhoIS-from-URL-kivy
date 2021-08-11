import socket
import whois

# takes a url in form ofa string and returns the ip address
def ip_from_url(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

#takes the ip address and looks for the whois informations
def who_is(ip_address):
    who_is_result = whois.whois(ip_address)
    return who_is_result

