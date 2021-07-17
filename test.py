import socket
import time
time.sleep_ms(25)
import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(2), 58)
    
def clear(np):
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    
def runneos(np, number, c, cc, ccc, cccc):
    np[number] = (c, cc, ccc, cccc)
    np.write()

def web_page():
  html = ""
  return html

def page():
    import socket
    print("HI-THERE")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    
    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)
      print('Content = %s' % request)
      clearval = request.find('/?clear=on')
      if clearval == 6:
        clear(np)
      print("...................................................................................")
      print(request.split("!"))
      
      test = request.split("!")
      
      runneos(np, int(test[1]), int(test[2]), int(test[3]), int(test[4]), int(test[5]))
      
      response = web_page()
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
      
clear(np)
page()
