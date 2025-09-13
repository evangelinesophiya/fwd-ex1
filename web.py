from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <title>TCP/IP Protocol Table</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
    }
    th, td {
      border: 1px solid #444;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #ddd;
    }
  </style>
</head>
<body>
  <h2>TCP/IP Protocol Layers & Functions</h2>
  <table>
    <tr>
      <th>Layer</th>
      <th>Main Protocols</th>
      <th>Function</th>
    </tr>
    <tr>
      <td>Application Layer</td>
      <td>HTTP, FTP, SMTP, DNS, SNMP, POP3, IMAP</td>
      <td>Standardizes data exchange for user applications</td>
    </tr>
    <tr>
      <td>Transport Layer</td>
      <td>TCP, UDP</td>
      <td>Provides reliable end-to-end communication, flow control, error checking</td>
    </tr>
    <tr>
      <td>Internet Layer</td>
      <td>IP, ICMP, ARP</td>
      <td>Packet forwarding, addressing, routing across networks</td>
    </tr>
    <tr>
      <td>Network Access Layer</td>
      <td>Ethernet, Wi-Fi, PPP, ARP</td>
      <td>Physical transmission, framing, hardware addressing</td>
    </tr>
  </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()