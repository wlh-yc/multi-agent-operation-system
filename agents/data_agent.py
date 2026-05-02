class DataAgent:
    def process(self, task):
        print(f"[数据Agent] 处理任务数据：{task['name']}")
        task['data_processed'] = True
        return task