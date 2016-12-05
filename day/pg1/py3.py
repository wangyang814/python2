#!/usr/bin/env python
#!-*- coding:utf -8-*-
import SocketServer
import datetime
import pickle
host_status = {}
with open("pypy1","r+") as f:
    while True:
        line = f.readline().split()
        if len(line) == 0:break
        host_status[line[0]] = []


class myclass(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)

        if self.client_address[0] in host_status.keys():
            host_status[self.client_address[0]].append([datetime.datetime.now(),data])

        else:
            print "sorry %s is not in monitor" % (self.client_address[0])
        if self.client_address[0] == "192.168.137.50":
            with open("py2","r+") as f:
                pickle.dump(host_status,f)

        print "from %s : %s" % (self.client_address,data)
        for t,m in host_status.items():
            print t,m


if __name__ == "__main__":
    host,port = "",18000
    server = SocketServer.ThreadingTCPServer((host,port),myclass)
    server.serve_forever()




