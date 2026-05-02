class TaskPool:
    def __init__(self):
        self.tasks = [
            {"id": 1, "name": "每日数据统计", "type": "data", "status": "等待"},
            {"id": 2, "name": "服务器状态巡检", "type": "monitor", "status": "等待"},
            {"id": 3, "name": "自动发送运营报告", "type": "report", "status": "等待"},
            {"id": 4, "name": "用户活跃度分析", "type": "data", "status": "等待"},
        ]

    def has_task(self):
        return len(self.tasks) > 0

    def get_next_task(self):
        if self.tasks:
            return self.tasks.pop(0)
        return None