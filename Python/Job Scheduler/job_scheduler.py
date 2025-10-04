"""
Task Scheduler (Single File Project)
------------------------------------
A mini background job scheduler with retry logic, logging, and decorators.

Demonstrates:
- OOP design
- Logging
- Decorators
- Error handling
- Configuration via dataclass
"""

import time
import logging
import random
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Any


# ----------------------------
# Logging Configuration
# ----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("Scheduler")


# ----------------------------
# Configuration Management
# ----------------------------
@dataclass
class SchedulerConfig:
    """
    Configuration for the scheduler.
    """
    interval_check: int = 2  # seconds between job checks
    max_retries: int = 3     # max retries per job
    jobs: List[Dict[str, Any]] = field(default_factory=list)


# ----------------------------
# Job Wrapper
# ----------------------------
@dataclass
class Job:
    """
    Represents a registered job.
    """
    name: str
    func: Callable
    interval: int
    retries: int = 0
    max_retries: int = 3
    last_run: float = field(default_factory=lambda: 0.0)

    def should_run(self) -> bool:
        """Check if job should run based on interval."""
        return (time.time() - self.last_run) >= self.interval

    def run(self):
        """Run the job safely with retry mechanism."""
        try:
            logger.info(f"🔁 Running job: {self.name}")
            self.func()
            self.last_run = time.time()
            self.retries = 0
            logger.info(f"✅ Job '{self.name}' completed successfully.")
        except Exception as e:
            self.retries += 1
            logger.error(f"❌ Job '{self.name}' failed: {e}")
            if self.retries < self.max_retries:
                logger.warning(f"Retrying '{self.name}' ({self.retries}/{self.max_retries})...")
            else:
                logger.critical(f"🚨 Job '{self.name}' exceeded max retries. Skipping further attempts.")


# ----------------------------
# Scheduler Class
# ----------------------------
class TaskScheduler:
    """
    A simple background job scheduler.
    """

    def __init__(self, config: SchedulerConfig):
        self.config = config
        self.jobs: Dict[str, Job] = {}

    def job(self, name: str, interval: int, max_retries: int = 3):
        """
        Decorator to register a job.
        """
        def decorator(func: Callable):
            job = Job(name=name, func=func, interval=interval, max_retries=max_retries)
            self.jobs[name] = job
            logger.info(f"📝 Registered job '{name}' (every {interval}s, max_retries={max_retries})")
            return func
        return decorator

    def start(self):
        """Start the scheduler loop."""
        logger.info("🚀 Scheduler started. Press Ctrl+C to exit.\n")
        try:
            while True:
                for job in self.jobs.values():
                    if job.should_run() and job.retries < job.max_retries:
                        job.run()
                time.sleep(self.config.interval_check)
        except KeyboardInterrupt:
            logger.info("🛑 Scheduler stopped by user.")


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    config = SchedulerConfig(interval_check=2, max_retries=3)
    scheduler = TaskScheduler(config)

    @scheduler.job(name="send_email", interval=5)
    def send_email():
        """Mock email sending task."""
        if random.choice([True, False]):
            raise RuntimeError("SMTP connection failed.")
        logger.info("📧 Email sent successfully!")

    @scheduler.job(name="clean_temp", interval=10)
    def clean_temp_files():
        """Mock cleaning temporary files."""
        logger.info("🧹 Temporary files cleaned.")

    @scheduler.job(name="sync_data", interval=7)
    def sync_data():
        """Mock data synchronization."""
        if random.randint(0, 3) == 0:
            raise ValueError("Data sync timeout.")
        logger.info("🔄 Data synchronized with server.")

    scheduler.start()
