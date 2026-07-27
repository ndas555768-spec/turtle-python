import time, os
os.system('cls' if os.name=='nt' else 'clear')
msg = "🎉🎂 Happy Birthday! 🎂🎉"
for ch in msg:
    print(ch, end='', flush=True)
    time.sleep(0.1)
print("\n🎈 Have a wonderful day! 🎈")
