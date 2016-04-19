import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program starts at "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=SR6iYWJxHqs")
    break_count += 1
