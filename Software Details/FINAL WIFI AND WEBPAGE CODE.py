import network
import socket

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Mind Flayer', password='12345678')

print("Access Point Active")
print("IP Address:", ap.ifconfig()[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(1)
print("Web server running...")

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mind Flayer</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}

body{
background:#000;
color:#f0f0f0;
font-family:Georgia,serif;
min-height:100vh;
box-shadow:inset 0 0 120px rgba(180,0,0,0.35);
padding:0 0 40px 0;
}

@keyframes flicker{
0%  {text-shadow:0 0 10px #ff0000,0 0 30px #cc0000,0 0 60px #990000;}
15% {text-shadow:0 0 4px #ff0000,0 0 10px #cc0000;}
20% {text-shadow:0 0 10px #ff0000,0 0 30px #cc0000,0 0 60px #990000;}
45% {text-shadow:0 0 3px #ff0000;}
50% {text-shadow:0 0 10px #ff0000,0 0 30px #cc0000,0 0 60px #990000;}
80% {text-shadow:0 0 6px #ff0000,0 0 20px #cc0000;}
100%{text-shadow:0 0 10px #ff0000,0 0 30px #cc0000,0 0 60px #990000;}
}

@keyframes pulseborder{
0%  {border-left-color:#cc0000;}
50% {border-left-color:#ff4444;}
100%{border-left-color:#cc0000;}
}

.warning-banner{
background:#1a0000;
border-bottom:1px solid #cc0000;
text-align:center;
padding:10px;
letter-spacing:6px;
font-size:11px;
color:#cc0000;
text-transform:uppercase;
}

.hero{
text-align:center;
padding:40px 20px 20px 20px;
}

.title{
font-size:52px;
font-weight:900;
letter-spacing:10px;
text-transform:uppercase;
color:#ff1111;
animation:flicker 3s infinite;
line-height:1.1;
}

.subtitle{
margin-top:10px;
font-size:13px;
letter-spacing:5px;
color:#cc0000;
text-transform:uppercase;

/* REMOVE ANY ANIMATION EFFECT */
animation: none !important;
text-shadow: none !important;
}

.divider{
width:60%;
margin:24px auto;
border:none;
border-top:1px solid #330000;
}

.instructions-label{
text-align:center;
font-size:11px;
letter-spacing:4px;
color:#660000;
text-transform:uppercase;
margin-bottom:20px;
}

.cards{
padding:0 20px;
max-width:480px;
margin:0 auto;
}

.card{
background:#111;
border-left:4px solid #cc0000;
padding:22px 20px;
margin-bottom:16px;
animation:pulseborder 2.5s infinite;
}

.card-warning{
background:#130000;
border-left:4px solid #ff0000;
}

.card-number{
font-size:32px;
font-weight:900;
color:#cc0000;
line-height:1;
margin-bottom:8px;
letter-spacing:2px;
}

.card-text{
font-size:17px;
color:#e8e8e8;
line-height:1.5;
letter-spacing:0.5px;
}

.card-sub{
font-size:12px;
color:#666;
margin-top:6px;
letter-spacing:1px;
}

footer{
text-align:center;
margin-top:40px;
font-size:10px;
letter-spacing:3px;
color:#330000;
text-transform:uppercase;
padding:0 20px;
}
</style>
</head>
<body>

<div class="warning-banner">&#9888; &nbsp; Enter If You Dare &nbsp; &#9888;</div>

<div class="hero">
  <div class="title">Mind<br>Flayer</div>
  <div class="subtitle">The Upside Down Awaits</div>
</div>

<hr class="divider">

<div class="instructions-label">Ride Instructions</div>

<div class="cards">

  <div class="cards">

  <div class="card">
    <div class="card-number">01</div>
    <div class="card-text">Press the button to start</div>
    <div class="card-sub">Wait for the light and sound show to finish before continuing</div>
  </div>

  <div class="card">
    <div class="card-number">02</div>
    <div class="card-text">Wave your hand over the sensor near the scale</div>
    <div class="card-sub">Control the ride with your movement</div>
  </div>

  <div class="card card-warning">
    <div class="card-number">03</div>
    <div class="card-text">After 20 seconds, the buzzer and light show will play again</div>
    <div class="card-sub">&#9888; This is your signal to bring your hand back down to the bottom of the scale</div>
  </div>

  <div class="card">
    <div class="card-number">04</div>
    <div class="card-text">Watch how you control the ride with your mind</div>
    <div class="card-sub">The Flayer responds to your command</div>
  </div>

</div>

<footer>Hawkins National Laboratory &mdash; Authorised Personnel Only</footer>

</body>
</html>
"""

while True:
    conn, addr = server.accept()
    print("Client connected from", addr)
    request = conn.recv(1024)
    conn.send("HTTP/1.1 200 OK\r\n")
    conn.send("Content-Type: text/html\r\n")
    conn.send("Connection: close\r\n\r\n")
    conn.sendall(html)
    conn.close()