# SolarityAI Landing Page Deployment

This directory contains Ansible playbooks and scripts to deploy the SolarityAI landing page to the EC2 frontend server.

## Overview

The deployment process:
1. Syncs Terraform outputs to Ansible configuration
2. Uploads static landing page files to the server
3. Configures Nginx to serve the landing page on `solarityai.com` and `www.solarityai.com`

## Prerequisites

- Ansible installed
- Terraform outputs available (for syncing configuration)
- SSH access to the EC2 frontend server
- Landing page files in the parent directory

## Quick Start

1. **Sync Terraform outputs** (optional, but recommended):
   ```bash
   ./sync-terraform-outputs.sh
   ```

2. **Deploy the landing page**:
   ```bash
   ./deploy-landing-page.sh
   ```

## Configuration

### Files Structure

- `ansible.cfg` - Ansible configuration
- `deploy.yml` - Main deployment playbook
- `deploy-landing-page.sh` - Deployment script
- `sync-terraform-outputs.sh` - Script to sync Terraform outputs
- `inventory/hosts.yml` - Server inventory (auto-synced from Terraform)
- `group_vars/all.yml` - Configuration variables
- `templates/nginx.conf.j2` - Nginx configuration template
- `roles/landing_page/tasks/main.yml` - Landing page deployment tasks

### Domain Configuration

The landing page is configured to serve on:
- `solarityai.com` (root domain)
- `www.solarityai.com` (www subdomain)

These domains are configured in `group_vars/all.yml` and can be auto-synced from Terraform outputs.

### Deployment Path

The landing page files are deployed to:
- `/usr/share/nginx/html/solarityai/` on the server

## Manual Deployment Steps

If you prefer to deploy manually:

1. **Run the main playbook**:
   ```bash
   ansible-playbook -i inventory/hosts.yml deploy.yml
   ```

2. **Upload files** (if not using the script):
   ```bash
   ansible-playbook -i inventory/hosts.yml -e "landing_page_source=/path/to/landing-page" deploy-landing-page.sh
   ```

## Troubleshooting

- **Check Nginx configuration**: `nginx -t` on the server
- **View logs**: Check `/var/log/nginx/solarityai_access.log` and `/var/log/nginx/solarityai_error.log`
- **Verify files**: SSH to server and check `/usr/share/nginx/html/solarityai/`

## Notes

- The deployment script automatically handles file uploads and Nginx configuration
- SSL/TLS is handled by the Application Load Balancer (ALB), not Nginx
- The configuration is designed to work with the existing infrastructure setup

