class TaskAgent:
    def __init__(self, task_pool):
        self.task_pool = task_pool

    def dispatch_task(self, task):
        print(f"[任务Agent] 正在分配任务：{task['name']}")
        task['status'] = "分配完成"