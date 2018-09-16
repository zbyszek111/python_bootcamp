import sys

user_total_time = {}
user_last_login = {}


wejscie = sys.argv[1]
with open(wejscie) as f:
    for line in f:
        print(line)
        login, action, time_str = line.split(";")
        time = int(time_str)
        if action == "LOGIN":
            user_last_login[login] = time
        elif action =="LOGOUT":
            user_total_time[login] = user_total_time.get(login,0) + time - user_last_login[login]

print(f"Czas przebywania w systemie :")

for user, time in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(f" -{user}: {time} s")