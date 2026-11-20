# Module 03: Cloud Concepts, VMs & Automation

## 1. Cloud Service & Deployment Models

### Cloud Service Models
* **IaaS (Infrastructure as a Service):**
  * Provides virtualized compute, storage, and networking resources (e.g., Google Compute Engine VMs).
  * **Responsibility:** You install, configure, and maintain the operating system, runtime dependencies, databases, and applications.
* **PaaS (Platform as a Service):**
  * Provides a managed platform and runtime environment where the cloud provider handles hardware, OS updates, database engines, and dependencies (e.g., Google BigQuery, App Engine).
  * **Best Use Case:** When a team wants to store, query, and analyze massive amounts of data—or deploy application code—without managing servers, OS patches, or database infrastructure.
* **SaaS (Software as a Service):**
  * Delivers complete, ready-to-use software applications over the internet (e.g., Gmail, Google Workspace).

### Cloud Environments
* **Public Cloud:** Cloud infrastructure owned and operated by a third-party provider and shared across tenants over the internet.
* **Private Cloud / On-Premises:** IT infrastructure owned, hosted, and managed exclusively by a single organization within its own data center.
* **Hybrid Cloud:** Combines **on-premises infrastructure** (owned/managed by the organization) with **public cloud services**, enabling data and workloads to operate across both environments.
* **Multi-Cloud:** Uses cloud services from multiple public cloud providers (e.g., GCP, AWS, and Azure) simultaneously.

---

## 2. Cloud Management Interfaces, Orchestration & IaC

### Two Main Interfaces for Managing Virtual Machines
1. **Web-Based Graphical User Interface (GUI):**
   * Example: Google Cloud Console.
   * Useful for visual exploration and one-off tasks, but slow and error-prone when managing dozens or hundreds of servers.
2. **Command-Line Interface (CLI):**
   * Example: `gcloud` CLI in Google Cloud Shell.
   * **Preferred for Automation:** CLI commands can be saved in scripts, parameterized, version-controlled, and executed repeatedly at scale.

### Orchestration & APIs
* **How Orchestration Tools Interact with Cloud Providers:**
  * Instead of clicking through a web GUI or typing manual CLI commands, orchestration tools (e.g., Terraform, Google Cloud Deployment Manager, Ansible) use **Application Programming Interfaces (APIs)** provided by the cloud vendor for direct, programmatic control.

### Infrastructure as Code (IaC)
* **Definition:** Managing and provisioning cloud infrastructure (VMs, networks, firewalls, load balancers) using declarative machine-readable configuration files rather than manual setup.
* **Primary Benefits:**
  * **Repeatable deployments** (eliminates manual configuration drift).
  * **Version control** (infrastructure definitions live in Git with full commit history).
  * **Easier rollbacks** (reverting to a previous working infrastructure state if a deployment breaks).

---

## 3. Execution Boundaries in GCP (VM SSH vs. Cloud Shell)

Understanding where your terminal commands execute prevents permission and scope errors:

| Terminal Environment | Prompt Example | Scope & Permissions | What to Run Here |
| :--- | :--- | :--- | :--- |
| **VM SSH Terminal** | `student@vm1:~$` | Runs **inside a single Linux VM**. By default, a VM's service account has restricted OAuth scopes (cannot create new cloud VMs). | Local OS tasks: installing packages, editing `/etc/systemd/system/` units, checking local ports (`curl http://localhost`). |
| **Google Cloud Shell** | `student@cloudshell:~$` | Runs at the **GCP project level** in your browser (`>_` icon). Pre-authenticated with your admin/student credentials. | Project-wide infrastructure orchestration: `gcloud compute instances create`, managing images, templates, and networks. |

> **Troubleshooting Note:** Running `gcloud compute instances create` inside `@vm1` throws `Request had insufficient authentication scopes`. Always switch to **Cloud Shell** (`@cloudshell`) to provision new VMs.

---

## 4. End-to-End Lab Workflow: Reference VM, Custom Image & Instance Template

To automate deploying identical web servers in GCP instead of configuring each VM manually:

### Step 1: Configure Auto-Start on the Reference VM (`vm1`)
* Use a Linux service manager (`systemd`) so your web server starts automatically on boot.
* Stop/disable conflicting web servers (like default `apache2`) if your custom service listens on port `80`.

```bash
# 1. Disable default Apache2 so port 80 is free
sudo systemctl disable --now apache2 2>/dev/null || true

# 2. Install the application and systemd unit file
cd ~/it-cert-automation-practice/Course5/Lab3
sudo cp hello_cloud.py /usr/local/bin/
sudo cp hello_cloud.service /etc/systemd/system/

# 3. Reload systemd, enable on boot, and start the service
sudo systemctl daemon-reload
sudo systemctl enable --now hello_cloud.service

# 4. Verify locally on port 80
curl -i http://localhost
