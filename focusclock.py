import time

# 定义工作时间和休息时间（单位为分钟）
work_time = 25
rest_time = 5

# 定义提醒语句
work_message = "Keep working! The Pomodoro timer is on."
rest_message = "Time to take a break! The Pomodoro timer is on."

# 循环计时器
while True:
    
    # 工作时间
    print("Work starts now...")
    print(work_message)
    time.sleep(work_time * 60)  # 延时时间以秒为单位
    
    # 休息时间
    print("Time for a break...")
    print(rest_message)
    time.sleep(rest_time * 60)

