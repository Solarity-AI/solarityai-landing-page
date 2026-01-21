# Ansible Deployment Guide

This directory contains Ansible playbooks and configurations to deploy the optimized Solarity AI landing page to EC2 instances.

## 📋 Updated Deployment Strategy

The Ansible playbook now:

1. **Builds optimized assets** locally using `npm run build`
2. **Deploys from `build/` folder** with optimized CSS, JS, and minified HTML
3. **Creates backups** of previous deployments
4. **Verifies deployment** with status confirmation

## 🗂️ Directory Structure

```
ansible/
├── deploy.yml                 # Main deployment playbook (updated for build/)
├── deploy-landing-page.sh     # Optional shell deployment script
├── reload-nginx.sh            # Quick Nginx reload script
├── sync-terraform-outputs.sh  # Auto-sync domain configuration
├── update-nginx-config.yml    # Standalone Nginx config update
├── ansible.cfg                # Ansible configuration
├── inventory/
│   ├── hosts.yml              # EC2 instance inventory
│   └── hosts.yml.bak          # Backup of hosts.yml
├── group_vars/
│   ├── all.yml                # Global variables (landing_page_root, domains)
│   └── all.yml.bak            # Backup of all.yml
├── roles/
│   └── landing_page/
│       └── tasks/
│           └── main.yml       # Updated: Syncs optimized build/ folder
└── templates/
    └── nginx.conf.j2          # Nginx configuration template
```

## 🚀 Quick Deploy

### Prerequisites

- Node.js and npm installed locally (for building assets)
- Ansible installed: `pip install ansible`
- SSH access to EC2 instances configured
- Inventory file updated with your EC2 hosts

### One-Command Deploy

```bash
ansible-playbook -i inventory/hosts.yml deploy.yml
```

### Deploy to Specific Host

```bash
ansible-playbook -i inventory/hosts.yml deploy.yml -l production
```

### Check What Would Change

```bash
ansible-playbook -i inventory/hosts.yml deploy.yml --check
```

## 📦 Deployment Flow

```
Local Machine              EC2 Instance
     │                          │
     ├─ npm run build           │
     │  └─ Creates build/       │
     │     ├─ index.html        │
     │     ├─ bundle.min.css    │
     │     ├─ bundle.min.js     │
     │     └─ assets/           │
     │                          │
     ├─ SSH connects ───────────→
     │                          │
     ├─ Backup current ────────→  Create backup-*.tar.gz
     │                          │
     ├─ Sync build/ ──────────→  /usr/share/nginx/html/solarityai/
     │   (rsync)                │
     │                          │
     ├─ Set permissions ──────→  nginx user permissions
     │                          │
     ├─ Verify HTML ──────────→  Check index.html exists
     │                          │
     └─ Reload Nginx ─────────→  Restart Nginx
```

## 🔄 Key Tasks

### 1. Build Optimizations

```yaml
- name: Build optimized landing page assets
  local_action:
    module: shell
    cmd: cd "{{ playbook_dir }}/.. && npm run build
```

- Creates minified HTML (-27.8%)
- Bundles CSS (-8.9%)
- Bundles JavaScript (-14.5%)
- Copies optimized images

### 2. Backup Current Deployment

```yaml
- name: Create backup of current landing page
  command: tar -czf "backup-{{ timestamp }}.tar.gz" ...
```

- Automatically backs up previous version
- Stored in `{{ landing_page_root }}/backups/`
- Allows easy rollback if needed

### 3. Deploy Build Files

```yaml
- name: Sync optimized landing page files from build/
  synchronize:
    src: "build/"
    dest: "{{ landing_page_root }}/"
    delete: yes
```

- Uses rsync for efficient file transfer
- Deletes old files not in build/
- Only transfers changed files

## 📊 Configuration Variables

Edit `group_vars/all.yml` to customize:

```yaml
# Landing page root directory (where files are served from)
landing_page_root: /usr/share/nginx/html/solarityai

# Enable/disable landing page deployment
landing_page_enabled: true

# Domain names (auto-synced from Terraform)
landing_domain_names:
  - "solarityai.com"
  - "www.solarityai.com"
```

## 🔐 Inventory Setup

Edit `inventory/hosts.yml` to define your EC2 hosts:

```yaml
[production]
web1 ansible_host=1.2.3.4 ansible_user=ec2-user
web2 ansible_host=5.6.7.8 ansible_user=ec2-user

[production:vars]
ansible_ssh_private_key_file=/path/to/key.pem
ansible_python_interpreter=/usr/bin/python3
```

## 🛠️ Advanced Usage

### Rollback to Previous Deployment

```bash
cd /usr/share/nginx/html/solarityai
tar -xzf backups/backup-[timestamp].tar.gz
sudo systemctl restart nginx
```

### Manual Nginx Reload

```bash
./reload-nginx.sh
```

### Update Only Nginx Configuration

```bash
ansible-playbook -i inventory/hosts.yml update-nginx-config.yml
```

### Sync Terraform Outputs

```bash
./sync-terraform-outputs.sh
```

## ✅ Deployment Verification

After deployment, Ansible will display:

```
✅ DEPLOYMENT COMPLETE!
Landing page deployed to: /usr/share/nginx/html/solarityai
Optimizations applied:
  - Minified HTML (-27.8%)
  - Bundled CSS (-8.9%)
  - Bundled JavaScript (-14.5%)
  - Image lazy loading
Access at: http://your-server-ip
```

## 🐛 Troubleshooting

### Issue: "nginx -t" fails

Check `/var/log/nginx/error.log` for configuration errors:

```bash
ansible-playbook -i inventory/hosts.yml deploy.yml -vvv
```

### Issue: Permission denied on landing page directory

The playbook automatically sets correct permissions:

```bash
# Manually fix if needed:
sudo chown -R root:nginx /usr/share/nginx/html/solarityai
sudo chmod 755 /usr/share/nginx/html/solarityai
```

### Issue: Files not syncing

Ensure rsync is installed on target:

```bash
ansible all -i inventory/hosts.yml -m shell -a "yum install rsync -y"
```

## 📋 Deployment Checklist

- [ ] Local build created: `npm run build`
- [ ] `build/` folder exists with optimized files
- [ ] Ansible inventory updated (`inventory/hosts.yml`)
- [ ] SSH key configured and working
- [ ] Domain names updated in `group_vars/all.yml`
- [ ] Run: `ansible-playbook -i inventory/hosts.yml deploy.yml`
- [ ] Verify deployment status message
- [ ] Test website in browser
- [ ] Check backup was created
- [ ] Monitor Nginx logs: `tail -f /var/log/nginx/error.log`

## 🔄 Continuous Deployment

For CI/CD integration (GitHub Actions, GitLab CI, etc.):

```yaml
# Example GitHub Actions workflow
- name: Deploy with Ansible
  run: |
    npm install
    npm run build
    ansible-playbook -i inventory/hosts.yml ansible/deploy.yml
```

## 📞 Support

For issues:

1. Check playbook syntax: `ansible-playbook --syntax-check deploy.yml`
2. Run with verbose output: `ansible-playbook -i inventory/hosts.yml deploy.yml -vvv`
3. Check Nginx logs on target: `sudo tail -f /var/log/nginx/error.log`
4. Review backups if needed: `ls /usr/share/nginx/html/solarityai/backups/`

---

**Last Updated**: January 2026
**Deployment Method**: Ansible with optimized build folder
**Assets**: Minified CSS/JS, lazy-loaded images, optimized HTML
