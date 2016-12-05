#!/usr/bin/env python
#! -*- encoding:utf-8 -*-
"""
注释
"""
import SocketServer
class myTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data=self.request.recv(1024)
        if self.data is list and self.data[0] == "get":
            f=open(self.data[1],"rb")
            data=f.read()
            self.request.sendall(data)
            print "send down"
        else:
            f1 = open(self.data,'rb',encoding="utf-8")
            data1 = self.request.recv(1024)
            f1.write(data1)
            f1.close()
            aa = "server have down"
            self.request.send(aa)



h,p="",9999
server=SocketServer.ThreadingTCPServer((h,p),myTCPHandler)
server.serve_forever()


