main_sec = int(input("Enter your time in seconds: "))

if main_sec > 86400:
    print("Error")
elif main_sec == 86400:
    print("00:00:00")
else:
    hour = int(main_sec / 3600)
    minutes = int((main_sec - (hour * 3600)) / 60)
    sec = int(main_sec - (hour * 3600) - (minutes * 60))
    if hour < 10:
        print(f"0{hour}:{minutes}:{sec}")
    else:
        print(f"{hour}:{minutes}:{sec}")




