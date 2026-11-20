# ==============================================================================
# Module 02: Deploying Puppet, Manifests & Rules - Practice Manifest (.pp)
# ==============================================================================
# Useful CLI commands (if puppet is installed):
#   Validate syntax:   puppet parser validate practice.pp
#   Dry-run (no-op):   sudo puppet apply --noop -v practice.pp
#   Apply locally:     sudo puppet apply -v practice.pp
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Resource Relationships & Ordering (require, notify, subscribe, before)
# ------------------------------------------------------------------------------
# Remember:
#   - Use lowercase when declaring a resource: package { 'ntp': ... }
#   - Use Capitalized type when referencing a resource: Package['ntp']

class ntp_config {
  package { 'ntp':
    ensure => installed,
  }

  file { '/etc/ntp.conf':
    ensure  => file,
    source  => 'puppet:///modules/ntp/ntp.conf',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    require => Package['ntp'], # Apply Package['ntp'] BEFORE creating this file
    notify  => Service['ntp'], # Restart Service['ntp'] whenever this file changes
  }

  service { 'ntp':
    ensure => running,
    enable => true,
  }
}

# ------------------------------------------------------------------------------
# 2. Using System Facts ($facts) & Cross-Platform Conditionals
# ------------------------------------------------------------------------------

class web_server {
  if $facts['os']['family'] == 'Debian' {
    $web_pkg     = 'apache2'
    $web_service = 'apache2'
  } elsif $facts['os']['family'] == 'RedHat' {
    $web_pkg     = 'httpd'
    $web_service = 'httpd'
  } else {
    fail("Unsupported OS family: ${facts['os']['family']}")
  }

  package { $web_pkg:
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "Managed by Puppet on ${facts['networking']['fqdn']} (${facts['os']['family']})\n",
    mode    => '0644',
    require => Package[$web_pkg],
  }

  service { $web_service:
    ensure    => running,
    enable    => true,
    subscribe => File['/var/www/html/index.html'],
  }
}

# ------------------------------------------------------------------------------
# 3. Node Definitions (Typically placed in manifests/site.pp on Puppet Master)
# ------------------------------------------------------------------------------

node 'webserver01.example.com' {
  include ntp_config
  include web_server
}

node default {
  include ntp_config
}

# ==============================================================================
# 4. Hands-On Practice Exercises (Try writing your solutions below!)
# ==============================================================================

# Exercise 1: Create a class named 'docker_setup' that:
#   1. Ensures the 'docker.io' package is installed.
#   2. Manages '/etc/docker/daemon.json' as a file with mode '0644',
#      requiring Package['docker.io'].
#   3. Ensures the 'docker' service is running and enabled at boot,
#      and subscribes to File['/etc/docker/daemon.json'].
#
# Write your code below:


# Exercise 2: Create a class named 'reboot_on_kernel_update' or a 'machine_info'
# resource that writes '/etc/machine_info.txt' containing the OS family and
# kernel version using $facts['kernel'], and only runs if $facts['kernel'] == 'Linux'.
#
# Write your code below:

class sys_setup {
  $motd_path = '/etc/motd'

  if $facts['os']['family'] == 'Debian' {
    package { 'curl':
      ensure => installed,
    }
  }

  file { $motd_path:
    ensure  => file,
    content => "Managed by Puppet on ${facts['networking']['hostname']}\n",
    mode    => '0644',
  }
}

======

""" 

Drill 1: Fix the Resource Reference & Dependency Chain
Task: Spot and fix the 3 syntax/logic bugs in this Puppet class:

"""

class webserver {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    source  => 'puppet:///modules/webserver/nginx.conf',
    require => package['nginx'],
    before  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

"""

package['nginx'] must be capitalized as Package['nginx'].

Using before => Service['nginx'] only enforces ordering; to make nginx automatically reload when nginx.conf is updated, replace before with notify => Service['nginx'].

Ensure the file is placed inside webserver/manifests/init.pp and the static config is placed inside webserver/files/nginx.conf.

Drill 2: Write a site.pp Node Definition
Task: Write a site.pp manifest that applies class base_tools and class ssh_server to app01.corp.local, and applies only class base_tools to all other nodes.

"""

node 'app01.corp.local' {
  include base_tools
  include ssh_server
}

node default {
  include base_tools
}
