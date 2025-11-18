import yaml
import importlib
from ceas.core import scheduler
import time

def load_tasks_from_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    tasks = config.get('tasks', [])
    for task_str in tasks:
        module_name, task_name = task_str.rsplit('.', 1)
        try:
            module = importlib.import_module(module_name)
            task_func = getattr(module, task_name)
        except (ImportError, AttributeError) as e:
            print(f"Could not import task {task_str}: {e}")

def run():
    print("Starting CEAS...")
    load_tasks_from_config('ceas/config/config.yaml')
    print("Tasks loaded. Scheduler is running in the background.")
    
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler shut down.")

if __name__ == "__main__":
    run()
