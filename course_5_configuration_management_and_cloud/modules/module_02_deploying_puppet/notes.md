# Module 02: Deploying Puppet, Manifests & Rules

## 📖 Overview
Key concepts, course lecture notes, and practical takeaways for Deploying Puppet, Manifests & Rules.

## 🔑 Key Concepts

1. Applying Rules Locally vs. Client-Server Architecture
Standalone / Local Mode (puppet apply):

Used to test and apply manifests locally on a single machine without needing a Puppet master server.

Command: sudo puppet apply -v <manifest.pp> (-v prints verbose output).

Client-Server Architecture (Puppet Agent & Puppet Master):

Puppet Master (Server): Stores all manifests, modules, and Hiera data; compiles node-specific catalogs.

Puppet Agent (Managed Node): Runs as a background daemon on client machines; collects system facts via Facter, sends them to the master over port 8140, downloads its compiled catalog, and enforces the desired state.

Catalog: A customized list of resources and dependency relationships compiled by the Puppet master specifically for one individual node after evaluating all functions, conditionals, and variables.

2. Puppet Modules & Directory Structure
A module is a self-contained, reusable directory bundle that organizes all Puppet code, files, templates, and plugins needed to manage a specific component or service (e.g., apache, ntp, users).

Plaintext
my_module/
├── manifests/          # Puppet DSL (.pp) code files
│   └── init.pp         # Main entry point defining class my_module
├── files/              # Static files copied directly to nodes (puppet:///modules/...)
├── templates/          # Dynamic templates (.epp or .erb) populated using system facts
├── lib/                # Ruby plugins: custom facts (lib/facter/) & functions
├── spec/               # Automated RSpec unit tests
└── metadata.json       # Module metadata: name, version, author, dependencies, OS support
Key Rules for Modules:
Manifest File Extension: All Puppet manifest files end in .pp.

Templates: Allow you to embed variables and $facts inside configuration files so Puppet dynamically generates customized configs per machine.

Puppet Forge: An online repository of community- and vendor-built modules that can be installed using puppet module install <author-module>.

3. Resource Relationships & Ordering
Puppet does not automatically execute resources in top-to-bottom order unless you define dependencies. When referring to an existing resource inside a dependency attribute, capitalize the resource type (e.g., Package['ntp']).

require: Ensures the referenced resource is applied before the current resource.

before: Ensures the current resource is applied before the referenced resource.

notify: Applies the current resource first, and if it changes, triggers a refresh/restart on the referenced resource (e.g., restarting a service when its config file changes).

subscribe: Listens for changes in the referenced resource and refreshes the current resource when a change occurs.

Puppet
class ntp {
  package { 'ntp':
    ensure => installed,
  }

  file { '/etc/ntp.conf':
    ensure  => file,
    source  => 'puppet:///modules/ntp/ntp.conf',
    require => Package['ntp'], # Install package before placing config
    notify  => Service['ntp'], # Restart service if config changes
  }

  service { 'ntp':
    ensure => running,
    enable => true,
  }
}
4. Managing Nodes & SSL/TLS Security (PKI)
Node Definitions (site.pp):

Stored in the main manifest (manifests/site.pp) on the Puppet master.

Specific machines are identified using their Fully Qualified Domain Name (FQDN) (or default as a fallback for unmatched nodes).

Puppet
node 'webserver01.example.com' {
  include apache
  include ntp
}

node default {
  include ntp
}
Authentication & Encryption via PKI:

Puppet uses Public Key Infrastructure (PKI) with its own built-in Certificate Authority (CA) to authenticate nodes and encrypt all communication.

First-Time Connection Workflow:

A new Puppet agent connects to the Puppet master and generates a Certificate Signing Request (CSR).

On the Puppet master, an admin inspects pending requests (sudo puppetserver ca list) and signs the certificate (sudo puppetserver ca sign --certname <node_fqdn>).

Once signed, the agent retrieves its certificate and can securely request catalogs (sudo puppet agent --test).

5. Safe Testing, Environments & Deployment Practices
Environments:

Development: Local sandboxes where engineers write and test new Puppet manifests.

Testing / Staging: Pre-production environment mirroring production to verify changes safely.

Canary Environment: Deploying changes to a small, isolated subset of production nodes first to catch bugs before rolling out fleet-wide.

Production: The live infrastructure serving end users.

Three Safe Ways to Validate Manifests Before Production:

puppet parser validate <file.pp>: Checks .pp files for syntax errors immediately without compiling a catalog or altering the system.

rspec tests (rspec-puppet): Automated unit tests that compile manifests in isolation and verify the resulting catalog contains expected resources and attributes.

No-Operations Simulation (--noop): Running sudo puppet agent --test --noop (or puppet apply --noop) simulates a full Puppet run and logs what would change without making any actual system modifications.

## 💡 Cheatsheet & Patterns
```python
# Code snippets and syntax patterns
```

## 📝 Practice Tasks
- [ ] **Exercise 1**: Description
- [ ] **Exercise 2**: Description
