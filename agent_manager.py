import time
from agents.task_agent import TaskAgent
from agents.data_agent import DataAgent
from agents.exec_agent import ExecAgent
from agents.monitor_agent import MonitorAgent
from agents.report_agent import ReportAgent

class AgentManager:
    def __init__(self, task_pool):
        self.task_pool = task_pool
        self.agents = {}

    def start_all_agents(self):
        self.agents['task'] = TaskAgent(self.task_pool)
        self.agents['data'] = DataAgent()
        self.agents['exec'] = ExecAgent()
        self.agents['monitor'] = MonitorAgent()
        self.agents['report'] = ReportAgent()
        print("[AgentManager] 所有智能体已启动\n")

    def run(self):
        while True:
            if self.task_pool.has_task():
                task = self.task_pool.get_next_task()
                self.agents['task'].dispatch_task(task)
                task = self.agents['data'].process(task)
                result = self.agents['exec'].execute(task)
                self.agents['monitor'].record(task, result)
                self.agents['report'].make_report(task, result)
                print("-" * 60)
            else:
                print("[系统] 暂无任务，等待新任务...")
                time.sleep(3)
            time.sleep(1)