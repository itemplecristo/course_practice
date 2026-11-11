# Study Notes: Proactive Practices

**Course:** Google IT Automation with Python — Course 4: Troubleshooting and Debugging Techniques  
**Module:** Module 4 — Managing Resources & Dealing with Hard Problems  

---

## 1. Reactive vs. Proactive Operations
Troubleshooting isn't just about fixing fires after users complain; mature IT operations prevent outages before they impact production:

* **Reactive Troubleshooting:** Waiting for a service to crash or a user to file a ticket before investigating. Results in downtime, stress, and emergency firefighting.
* **Proactive Practices:** Designing systems, monitoring, and workflows to detect degradation early, prevent recurring failures, and build long-term resilience.

---

## 2. Core Pillars of Proactive IT Management

### 1. Continuous Monitoring & Alerting
* **Metrics & Telemetry:** Track key health indicators continuously (CPU load, RAM usage, disk space, network latency, HTTP error rates, and queue depth) using tools like Prometheus, Nagios, or cloud monitoring agents.
* **Actionable Alerts:** Configure alerts to trigger *before* a resource hits 100% exhaustion (e.g., warning at 80% disk usage, critical alert at 90%).
* **Avoid Alert Fatigue:** Only page on-call engineers for actionable, urgent symptoms; route non-urgent anomalies to logs or daily dashboards so critical alerts aren't ignored.

### 2. Capacity Planning & Load Testing
* **Trend Analysis:** Analyze historical growth in traffic, storage, and memory to forecast when current hardware or quotas will hit limits—and upgrade ahead of time.
* **Load & Stress Testing:** Simulate peak traffic (e.g., Black Friday spikes) in staging environments using tools like `locust` or `ab` (Apache Bench) to discover bottlenecks safely before users do.

### 3. Automated Testing & CI/CD Safeguards
* **Unit & Integration Tests:** Automatically verify code changes before deployment to catch regressions early.
* **Canary Deployments & Rollbacks:** Roll out updates to a small subset of servers first (e.g., 5% of traffic). If error rates spike, automatically roll back before affecting the entire fleet.

### 4. Disaster Recovery & Backups
* **Regular Backups:** Automate encrypted backups of critical databases and configurations.
* **Test Your Restores:** An untested backup is not a backup—periodically verify that backups can actually be restored within your Recovery Time Objective (RTO).

### 5. Blameless Postmortems
* **Culture of Learning:** After any significant outage, write a **blameless postmortem** documenting:
  1. Timeline of events.
  2. Root cause(s).
  3. What went well vs. what went wrong.
  4. Concrete action items to prevent recurrence.
* **Focus on Systems, Not Individuals:** Assume engineers acted with good intentions based on the information they had; fix broken processes, missing guardrails, or unclear documentation rather than punishing people.

---

## 3. Practical Python Tool: Proactive System Health & Threshold Monitor
Below is a Python script implementing proactive threshold monitoring—checking disk space, memory consumption, and CPU load, and triggering tiered warnings before critical exhaustion occurs.

```python
import shutil
import psutil
import logging
from dataclasses import dataclass
from typing import List

# Configure structured logging for proactive audit trails
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


@dataclass
class ThresholdConfig:
    """Defines warning and critical percentage thresholds for system resources."""
    cpu_warn: float = 75.0
    cpu_crit: float = 90.0
    mem_warn: float = 80.0
    mem_crit: float = 92.0
    disk_warn: float = 80.0
    disk_crit: float = 90.0


class ProactiveHealthMonitor:
    """Checks vital system metrics and flags early degradation before outages."""

    def __init__(self, config: ThresholdConfig, disk_path: str = "/"):
        self.config = config
        self.disk_path = disk_path

    def check_cpu(self) -> str:
        usage = psutil.cpu_percent(interval=1.0)
        return self._evaluate("CPU Usage", usage, self.config.cpu_warn, self.config.cpu_crit)

    def check_memory(self) -> str:
        usage = psutil.virtual_memory().percent
        return self._evaluate("Memory Usage", usage, self.config.mem_warn, self.config.mem_crit)

    def check_disk(self) -> str:
        total, used, _ = shutil.disk_usage(self.disk_path)
        usage = (used / total) * 100
        return self._evaluate(f"Disk Usage ({self.disk_path})", usage, self.config.disk_warn, self.config.disk_crit)

    @staticmethod
    def _evaluate(metric_name: str, value: float, warn: float, crit: float) -> str:
        if value >= crit:
            msg = f"CRITICAL: {metric_name} at {value:.1f}% (threshold: {crit}%)"
            logging.critical(msg)
            return msg
        elif value >= warn:
            msg = f"WARNING: {metric_name} at {value:.1f}% (threshold: {warn}%)"
            logging.warning(msg)
            return msg
        else:
            msg = f"OK: {metric_name} at {value:.1f}%"
            logging.info(msg)
            return msg

    def run_all_checks(self) -> List[str]:
        logging.info("Starting proactive system health check...")
        return [
            self.check_cpu(),
            self.check_memory(),
            self.check_disk()
        ]


# -------------------------------------------------------------
# Execution (Designed to run periodically via cron or systemd)
# -------------------------------------------------------------
if __name__ == "__main__":
    thresholds = ThresholdConfig()
    monitor = ProactiveHealthMonitor(config=thresholds, disk_path="/")
    results = monitor.run_all_checks()

    alerts = [r for r in results if not r.startswith("OK")]
    if alerts:
        print("\n[!] Action Required — Early Warnings Triggered:")
        for alert in alerts:
            print(f"  - {alert}")
    else:
        print("\n[+] All systems operating within healthy proactive thresholds.")
```

---

## 4. Quick Exam & Review Checklist
* **Why do we write blameless postmortems?** To uncover systemic weaknesses and prevent similar outages in the future without discouraging engineers from reporting mistakes honestly.
* **What is the goal of proactive monitoring?** Detecting resource saturation or error trends *early* (via warning thresholds) so fixes can be applied before users experience downtime.
* **Why test backups regularly?** To verify data integrity and confirm recovery procedures work reliably under real conditions before an actual emergency hits.

===========

## Effective troubleshooting

When troubleshooting distributed systems, it's important to look beyond logical behavior. It takes well-established methods and a deep understanding of system behavior to troubleshoot effectively. Making observations, formulating hypotheses, and then systematically testing those hypotheses are all steps in the hypothetico-deductive method. It's crucial to avoid common pitfalls, such as fixating on unrelated symptoms or confusing correlation with causation. As you transition from theoretical concepts to practical implementation, using metrics, logs, and tracing exposes the subtle intricacies of the system's behavior. With defined strategies, well-informed diagnostic tools, and a thorough understanding of system dynamics, troubleshooting becomes a structured process supported by clear strategies.

To learn more about using a systematic approach to troubleshooting effectively in distributed computing environments, read more 
here - https://sre.google/sre-book/effective-troubleshooting/
