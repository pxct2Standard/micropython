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
def noic(np):
    n = np.n
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
def eins(np):
    n = np.n
    np[0] = (0, 0, 255, 128)
    np.write()
    np[1] = (0, 0, 255, 128)
    np.write()
def zwei(np):
    n = np.n
    np[2] = (0, 0, 255, 128)
    np.write()
    np[3] = (0, 0, 255, 128)
    np.write()
def drei(np):
    n = np.n
    np[4] = (0, 0, 255, 128)
    np.write()
    np[5] = (0, 0, 255, 128)
    np.write()
def fier(np):
    n = np.n
    np[6] = (0, 0, 255, 128)
    np.write()
    np[7] = (0, 0, 255, 128)
    np.write()
def funf(np):
    n = np.n
    np[8] = (0, 0, 255, 128)
    np.write()
    np[9] = (0, 0, 255, 128)
    np.write()
def sechs(np):
    n = np.n
    np[10] = (0, 0, 255, 128)
    np.write()
    np[11] = (0, 0, 255, 128)
    np.write()
def siben(np):
    n = np.n
    np[12] = (0, 0, 255, 128)
    np.write()
    np[13] = (0, 0, 255, 128)
    np.write()
def eins2(np):
    n = np.n
    np[14] = (0, 0, 255, 128)
    np.write()
    np[15] = (0, 0, 255, 128)
    np.write()
def zwei2(np):
    n = np.n
    np[16] = (0, 0, 255, 128)
    np.write()
    np[17] = (0, 0, 255, 128)
    np.write()
def drei2(np):
    n = np.n
    np[18] = (0, 0, 255, 128)
    np.write()
    np[19] = (0, 0, 255, 128)
    np.write()
def fier2(np):
    n = np.n
    np[20] = (0, 0, 255, 128)
    np.write()
    np[21] = (0, 0, 255, 128)
    np.write()
def funf2(np):
    n = np.n
    np[22] = (0, 0, 255, 128)
    np.write()
    np[23] = (0, 0, 255, 128)
    np.write()
def sechs2(np):
    n = np.n
    np[24] = (0, 0, 255, 128)
    np.write()
    np[25] = (0, 0, 255, 128)
    np.write()
def siben2(np):
    n = np.n
    np[26] = (0, 0, 255, 128)
    np.write()
    np[27] = (0, 0, 255, 128)
    np.write()
def punkte(np):
    n = np.n
    np[28] = (0, 0, 255, 128)
    np.write()
    np[29] = (0, 0, 255, 128)
    np.write()
def eins3(np):
    n = np.n
    np[30] = (0, 0, 255, 128)
    np.write()
    np[31] = (0, 0, 255, 128)
    np.write()
def zwei3(np):
    n = np.n
    np[32] = (0, 0, 255, 128)
    np.write()
    np[33] = (0, 0, 255, 128)
    np.write()
def drei3(np):
    n = np.n
    np[34] = (0, 0, 255, 128)
    np.write()
    np[35] = (0, 0, 255, 128)
    np.write()
def fier3(np):
    n = np.n
    np[36] = (0, 0, 255, 128)
    np.write()
    np[37] = (0, 0, 255, 128)
    np.write()
def funf3(np):
    n = np.n
    np[38] = (0, 0, 255, 128)
    np.write()
    np[39] = (0, 0, 255, 128)
    np.write()
def sechs3(np):
    n = np.n
    np[40] = (0, 0, 255, 128)
    np.write()
    np[41] = (0, 0, 255, 128)
    np.write()
def siben3(np):
    n = np.n
    np[42] = (0, 0, 255, 128)
    np.write()
    np[43] = (0, 0, 255, 128)
    np.write()
def eins4(np):
    n = np.n
    np[44] = (0, 0, 255, 128)
    np.write()
    np[45] = (0, 0, 255, 128)
    np.write()
def zwei4(np):
    n = np.n
    np[46] = (0, 0, 255, 128)
    np.write()
    np[47] = (0, 0, 255, 128)
    np.write()
def drei4(np):
    n = np.n
    np[48] = (0, 0, 255, 128)
    np.write()
    np[49] = (0, 0, 255, 128)
    np.write()
def fier4(np):
    n = np.n
    np[50] = (0, 0, 255, 128)
    np.write()
    np[51] = (0, 0, 255, 128)
    np.write()
def funf4(np):
    n = np.n
    np[52] = (0, 0, 255, 128)
    np.write()
    np[53] = (0, 0, 255, 128)
    np.write()
def sechs4(np):
    n = np.n
    np[54] = (0, 0, 255, 128)
    np.write()
    np[55] = (0, 0, 255, 128)
    np.write()
def siben4(np):
    n = np.n
    np[56] = (0, 0, 255, 128)
    np.write()
    np[57] = (0, 0, 255, 128)
    np.write()
def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  html = """<html><head> <title>ESP Web Server</title></head></html>"""
  return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
noic(np)
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  clearval = request.find('/?clear=on')
  if clearval == 6:
    clear(np)
  einsval = request.find('/?eins=on')
  if einsval == 6:
    eins(np)
  zweival = request.find('/?zwei=on')
  if zweival == 6:
    zwei(np)
  dreival = request.find('/?drei=on')
  if dreival == 6:
    drei(np) 
  fierval = request.find('/?fier=on')
  if fierval == 6:
    fier(np)
  funfval = request.find('/?funf=on')
  if funfval == 6:
    funf(np)
  sechsval = request.find('/?sechs=on')
  if sechsval == 6:
    sechs(np)
  sibenval = request.find('/?siben=on')
  if sibenval == 6:
    siben(np)
  eins2val = request.find('/?eins2=on')
  if eins2val == 6:
    eins2(np)
  zwei2val = request.find('/?zwei2=on')
  if zwei2val == 6:
    zwei2(np)
  drei2val = request.find('/?drei2=on')
  if drei2val == 6:
    drei2(np) 
  fier2val = request.find('/?fier2=on')
  if fier2val == 6:
    fier2(np)
  funf2val = request.find('/?funf2=on')
  if funf2val == 6:
    funf2(np)
  sechs2val = request.find('/?sechs2=on')
  if sechs2val == 6:
    sechs2(np)
  siben2val = request.find('/?siben2=on')
  if siben2val == 6:
    siben2(np)
  eins3val = request.find('/?eins3=on')
  if eins3val == 6:
    eins3(np)
  zwei3val = request.find('/?zwei3=on')
  if zwei3val == 6:
    zwei3(np)
  drei3val = request.find('/?drei3=on')
  if drei3val == 6:
    drei3(np) 
  fier3val = request.find('/?fier3=on')
  if fier3val == 6:
    fier3(np)
  funf3val = request.find('/?funf3=on')
  if funf3val == 6:
    funf3(np)
  sechs3val = request.find('/?sechs3=on')
  if sechs3val == 6:
    sechs3(np)
  siben3val = request.find('/?siben3=on')
  if siben3val == 6:
    siben3(np)
  eins4val = request.find('/?eins4=on')
  if eins4val == 6:
    eins4(np)
  zwei4val = request.find('/?zwei4=on')
  if zwei4val == 6:
    zwei4(np)
  drei4val = request.find('/?drei4=on')
  if drei4val == 6:
    drei4(np) 
  fier4val = request.find('/?fier4=on')
  if fier4val == 6:
    fier4(np)
  funf4val = request.find('/?funf4=on')
  if funf4val == 6:
    funf4(np)
  sechs4val = request.find('/?sechs4=on')
  if sechs4val == 6:
    sechs4(np)
  siben4val = request.find('/?siben4=on')
  if siben4val == 6:
    siben4(np)
  nice = request.find('/?nice=on')
  if nice == 6:
    noic(np)
  punkte = request.find('/?punkte=on')
  if punkte == 6:
    punkte(np)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()