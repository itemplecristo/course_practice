# Study Notes: Dealing with Hard Problems

**Course:** Google IT Automation with Python — Course 4: Troubleshooting and Debugging Techniques  
**Module:** Module 4 — Managing Resources & Dealing with Hard Problems  

---

## 1. Mindset & Strategy for Complex Issues
When a bug isn't obvious—such as an intermittent race condition, an undocumented legacy system failure, or a multi-service outage—standard quick fixes won't work. Approaching hard problems requires structured discipline:

1. **Don't Guess—Formulate Hypotheses:** Avoid randomly changing settings or code ("shotgun debugging"). Always state *why* you think something is broken and design a test to prove or disprove that specific theory.
2. **Change One Variable at a Time:** If you modify three configuration files and restart two services simultaneously, you won't know which action fixed (or broke) the system.
3. **Keep a Troubleshooting Log:** Write down every command run, configuration altered, log snippet found, and hypothesis tested. This prevents repeating dead ends and provides clear handoff notes if you need to escalate.
4. **Take Strategic Breaks:** Stepping away from a screen after hitting a wall resets cognitive tunnel vision, often allowing you to spot obvious clues upon return.

---

## 2. Divide and Conquer: Isolating the Problem
Complex systems have many moving parts (client $\rightarrow$ network $\rightarrow$ load balancer $\rightarrow$ web server $\rightarrow$ database $\rightarrow$ disk). Use **binary search / bisection** to shrink the problem space:

* **Test Boundaries:** Check the midpoint of your architecture first. For example, if a web app fails to load user profiles, query the database directly from the server. 
  * If the DB query is fast, the bottleneck is in the application or network layer.
  * If the DB query hangs, you've eliminated the web server and frontend entirely.
* **Minimize the Reproduction Case:** Strip away unrelated code, configurations, or data until you have the smallest possible script or dataset that still triggers the failure.
* **Git Bisect (for Code Regressions):** If a bug appeared recently in a codebase, use `git bisect` to perform a binary search across commit history and automatically pinpoint the exact commit that introduced the issue.

---

## 3. Effective Communication & Escalation
Hard problems often require collaboration across teams or vendors. When asking for help or escalating a ticket, maximize signal and minimize noise:

* **Provide Context & Impact:** State what system is affected, who is impacted, and how severe the issue is.
* **Summarize What You Have Already Tried:** Share your troubleshooting log—list the hypotheses tested and the exact results/errors observed so colleagues don't waste time repeating your steps.
* **Include Actionable Artifacts:** Attach exact error messages, relevant log timestamps, stack traces, and steps to reproduce (avoid vague summaries like *"the server is acting weird"*).
* **Rubber Duck Debugging:** Explain the problem, line-by-line or step-by-step, out loud to an inanimate object or a colleague. Verbalizing assumptions frequently exposes the flaw in your own logic before the other person even speaks.

---

## 4. Practical Example: Isolating Intermittent / Hard-to-Reproduce Bugs
Hard problems often involve **intermittent failures** (Heisenbugs) that only occur under specific concurrency, timing, or input conditions. Below is a Python diagnostic wrapper pattern used to capture detailed state snapshots *only* when an elusive failure occurs.

```python
import functools
import logging
import traceback
import time
import random

# Configure detailed logging to capture context when a rare bug triggers
logging.basicConfig(
    filename="hard_problem_trace.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def capture_failure_context(func):
    """
    Decorator to isolate intermittent bugs by logging exact inputs,
    execution duration, and full stack traces only when an exception occurs.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            elapsed = time.perf_counter() - start_time
            logging.error(
                f"Failure in '{func.__name__}' after {elapsed:.4f}s | "
                f"Args: {args} | Kwargs: {kwargs} | Error: {repr(exc)}\n"
                f"Stack Trace:\n{traceback.format_exc()}"
            )
            raise
    return wrapper


# -------------------------------------------------------------
# Simulated Hard Problem: Intermittent Timing / Input Bug
# -------------------------------------------------------------

@capture_failure_context
def process_transaction(transaction_id: int, payload: dict):
    """Simulates a rare failure triggered by specific edge-case state."""
    # Simulate variable network/IO latency
    time.sleep(random.uniform(0.01, 0.05))

    # Simulated edge-case bug: fails only when a rare key combination occurs
    if payload.get("retry_count", 0) > 2 and transaction_id % 7 == 0:
        raise RuntimeError("Deadlock detected during shard commit")

    return f"Transaction {transaction_id} committed."


if __name__ == "__main__":
    print("Running stress test to reproduce intermittent bug...")
    failures = 0

    for i in range(1, 51):
        sample_payload = {
            "user": f"user_{i}",
            "retry_count": random.randint(0, 4)
        }
        try:
            process_transaction(i, sample_payload)
        except RuntimeError:
            failures += 1

    print(f"Completed 50 runs. Caught {failures} intermittent failure(s).")
    print("Check 'hard_problem_trace.log' for exact inputs that triggered the crash.")
```

---

## 5. Quick Exam & Review Checklist
* **What should you do when stuck on a hard problem?** Step back, review your assumptions, check your troubleshooting log, use divide-and-conquer to isolate components, or explain the problem to someone else (Rubber Duck Debugging).
* **Why document failed troubleshooting attempts?** It prevents duplicating effort, creates a clear audit trail, and gives teammates immediate context if the issue needs escalation.
* **How do you tackle intermittent bugs?** Automate reproduction via stress testing/looping and add targeted logging to capture the exact system state and inputs at the moment of failure.