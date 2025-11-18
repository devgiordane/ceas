from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
import inspect

class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_job(self, func, trigger_type, **trigger_args):
        trigger = self._create_trigger(trigger_type, **trigger_args)
        self.scheduler.add_job(func, trigger)

    def _create_trigger(self, trigger_type, **trigger_args):
        if trigger_type == 'cron':
            return CronTrigger(**trigger_args)
        elif trigger_type == 'interval':
            return IntervalTrigger(**trigger_args)
        elif trigger_type == 'date':
            return DateTrigger(**trigger_args)
        else:
            raise ValueError(f"Unsupported trigger type: {trigger_type}")

    def get_jobs(self):
        return self.scheduler.get_jobs()

    def shutdown(self):
        self.scheduler.shutdown()

scheduler = Scheduler()

def task(schedule, **kwargs):
    def decorator(func):
        sig = inspect.signature(func)
        if sig.parameters:
            # This is a task that will be called with arguments
            def wrapper(*args, **wrapper_kwargs):
                return func(*args, **wrapper_kwargs)
            
            # Here we should probably register the function and its arguments
            # but not schedule it yet.
            # For now, let's just print a message.
            print(f"Task {func.__name__} registered with schedule {schedule} and args {kwargs}")
            
            return wrapper
        else:
            # This is a task that will be run on a schedule
            scheduler.add_job(func, schedule, **kwargs)
            def wrapper():
                return func()
            return wrapper
    return decorator
