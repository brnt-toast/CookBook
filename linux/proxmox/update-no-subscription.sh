# add pve-no-subscription to /etc/apt/sources.list
deb http://download.proxmox.com/debian/pve bullseye pve-no-subscription

# comment-out pve-enterprise in /etc/apt/sources.list.d/pve-enterprise.list
# update and upgrade 
apt update -y && apt upgrade -y
