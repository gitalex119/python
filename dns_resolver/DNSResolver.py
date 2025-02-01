import socket


class DNSResolver():
    def __init__(self):
        self.cache = {}

    def resolve_dns(self, dns_name):
        try:
            ip_address = socket.gethostbyname(dns_name)
            self.cache[dns_name] = ip_address
            return ip_address
        except socket.gaierror as e:
            print(repr(e))

    def __call__(self, dns_name):
        if dns_name in self.cache:
            print(f"Name {dns_name} exists in DNS Cache")
            return self.cache[dns_name]
        else:
            return self.resolve_dns(dns_name)


dns = DNSResolver()
print(dns("www.google.com"))
print(dns("www.facebook.com"))
print(dns("www.google.com"))
