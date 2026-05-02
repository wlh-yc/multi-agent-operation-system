import time

class ExecAgent:
    def execute(self, task):
        print(f"[执行Agent] 正在执行任务：{task['name']}")
        time.sleep(0.5)
        return {
            "code": 200,
            "msg": "执行成功",
            "data": f"任务【{task['name']}】已自动完成"
        }