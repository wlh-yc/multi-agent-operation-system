
## 3. main.py
```python
from agent_manager import AgentManager
from tasks.task_pool import TaskPool

if __name__ == "__main__":
    print("=" * 50)
    print("  多Agent协同运营自动化系统 启动成功")
    print("=" * 50)

    task_pool = TaskPool()
    manager = AgentManager(task_pool)
    manager.start_all_agents()
    manager.run()