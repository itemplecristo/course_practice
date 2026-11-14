# Module 01: Automation at Scale with Config Management

## 📖 Overview
Key concepts, course lecture notes, and practical takeaways for Automation at Scale with Config Management.

## 🔑 Key Concepts
Study Notes: Automating with Configuration Management

Course: Google IT Automation with Python — Course 5: Configuration Management and the Cloud

Module: Module 1 — Automating with Configuration Management

1. Core Concepts of Configuration Management

As infrastructure scales from a handful of machines to thousands of servers across data centers and the cloud, manual setup becomes error-prone and unsustainable (configuration drift).

Configuration Management (CM): A systematic process for establishing and maintaining consistency in a system's performance, functional, and physical attributes with its requirements, design, and operational information throughout its life.

Infrastructure as Code (IaC): Managing and provisioning computing infrastructure through machine-readable definition files rather than physical hardware configuration or interactive configuration tools.

Declarative vs. Imperative:

Imperative (Procedural): You specify how to achieve the desired state step-by-step (e.g., a Bash or Python script: "Check if Apache is installed; if not, run apt install apache2; then edit config; then restart").

Declarative: You define what the final desired state should be, and the CM tool figures out the steps to get there (e.g., Puppet: "Ensure package apache2 is installed and service apache2 is running").

Idempotency: A critical property of CM operations—applying the same configuration multiple times produces the exact same result without unintended side effects. If the system is already in the desired state, Puppet does nothing.

Stateless vs. Stateful: Puppet runs use a stateless model where each catalog compilation evaluates the node's current facts (Facter) against the desired state defined in manifests, applying changes only where drift occurred.

2. Puppet Architecture & Workflow

Puppet uses a client-server architecture (or standalone puppet apply for local execution):

Puppet Agent (Client Node): Runs on every managed machine. Collects system information (Facts like OS, IP address, memory) via Facter and sends them to the master.

Puppet Master (Server): Compiles the node's Facts along with the Puppet Manifests (.pp files) into a Catalog—a complete blueprint of resources and dependencies for that specific node.

Catalog Application: The Agent receives the compiled Catalog, compares it against the actual machine state, enforces any needed changes, and sends a Report back to the Master.

3. Puppet Domain-Specific Language (DSL) Syntax

Puppet manifests are saved with the .pp extension. Every configuration block revolves around Resources.

Anatomy of a Resource Declaration

resource_type { 'title':
  attribute1 => value1,
  attribute2 => value2,
}


resource_type: Built-in or custom type (e.g., package, file, service, user, cron, exec).

'title': Unique identifier for the resource (often the package name or file path), always followed by a colon (:).

=> (Hash Rocket): Assigns values to attributes. Never use = or == inside a resource body.

Commas (,): Separate each attribute => value pair (including a trailing comma after the last attribute as best practice).

Common Core Resource Types

package: Manages software packages (apt, yum, pip, etc.).

ensure => installed (or latest, absent, '1.2.3').

file: Manages files, directories, symlinks, and permissions.

ensure => file (or directory, link, absent).

content => "text..." or source => 'puppet:///modules/...'.

mode => '0644', owner => 'root', group => 'root'.

service: Manages background daemons (systemd, init).

ensure => running (or stopped).

enable => true (starts automatically at boot) or false.

Grouping Resources with Classes

A Class groups related resources together into a reusable unit:

class webserver {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "<h1>Managed by Puppet</h1>\n",
    require => Package['nginx'],  # Explicit dependency ordering
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/var/www/html/index.html'], # Restarts service if file changes
  }
}


Conditionals & Facts

Puppet exposes system metadata via the $facts hash:

if $facts['os']['family'] == 'Debian' {
  $pkg_name = 'apache2'
} elsif $facts['os']['family'] == 'RedHat' {
  $pkg_name = 'httpd'
} else {
  fail("Unsupported OS family: ${facts['os']['family']}")
}

package { $pkg_name:
  ensure => present,
}


4. Hands-On Coding Practice

Try completing these three progressive Puppet manifest exercises on your own before checking the solutions below.

Exercise 1: Fix the Broken Manifest (Syntax & Logic Drill)

The following Puppet manifest has 5 syntax/logic bugs. Identify and fix all of them:

class security_baseline :
  package { 'ufw'
    ensure == installed,
  }
  file { '/etc/motd':
    ensure  => 'file',
    content => 'Authorized Access Only',
    mode    => 0644
  }
  program { 'ufw':
    ensure => running,
    enable => yes,
  }
}


Exercise 2: Write a Manifest from Scratch (NTP Time Sync)

Write a complete Puppet class named ntp_sync that accomplishes the following:

Ensures the package ntp is installed.

Creates/manages /etc/ntp.conf using a source file at 'puppet:///modules/ntp/ntp.conf', owned by root, group root, with permissions '0644'.

Ensures the ntp service is both running and enabled at boot (true), and automatically restarts whenever /etc/ntp.conf changes.

Exercise 3: Cross-Platform Conditionals

Write a Puppet snippet that inspects $facts['os']['family']:

On 'Debian' systems, installs python3-pip.

On 'RedHat' systems, installs python3-pip as well, but on any other OS, raises a failure message saying "OS not supported".

5. Practice Solutions

Solution 1: Fixed Manifest

Replaced colon : after class security_baseline with an opening curly brace {.

Added missing colon : after 'ufw' on line 2.

Replaced comparison operator == with hash rocket => on line 3.

Quoted file mode '0644' as a string (octal modes in Puppet should be strings) and added trailing comma.

Changed invalid resource type program to service and changed yes to boolean true.

class security_baseline {
  package { 'ufw':
    ensure => installed,
  }
  file { '/etc/motd':
    ensure  => 'file',
    content => 'Authorized Access Only',
    mode    => '0644',
  }
  service { 'ufw':
    ensure => running,
    enable => true,
  }
}


Solution 2: ntp_sync Class

class ntp_sync {
  package { 'ntp':
    ensure => installed,
  }

  file { '/etc/ntp.conf':
    ensure  => file,
    source  => 'puppet:///modules/ntp/ntp.conf',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    require => Package['ntp'],
  }

  service { 'ntp':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/ntp.conf'],
  }
}


Solution 3: Cross-Platform Conditional

if $facts['os']['family'] in ['Debian', 'RedHat'] {
  package { 'python3-pip':
    ensure => installed,
  }
} else {
  fail('OS not supported')
}


6. Quick Exam & CLI Reference

Test manifest syntax locally without applying changes: puppet parser validate manifest.pp

Dry-run a manifest (simulate changes without modifying the system): puppet apply --noop manifest.pp

Apply a manifest locally: sudo puppet apply manifest.pp

Inspect system facts available to Puppet: facter (or facter os)


## 💡 Cheatsheet & Patterns
```python
# Code snippets and syntax patterns
```

## 📝 Practice Tasks
- [ ] **Exercise 1**: Description
- [ ] **Exercise 2**: Description
