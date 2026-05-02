class MonitorAgent:
    def record(self, task, result):
        print(f"[监控Agent] 任务状态记录：{result['msg']}")