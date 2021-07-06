# Ansible for setting Ubuntu Bastion Server!

![](ansible_bastion.png)

Ansible to configure Ubuntu Bastion Server
---

**`main.sh`** - script to configure Ubuntu Bastion Server for Gitlab Runner.

**There is an input of the necessary parameters with the ability to use the default parameters.**

**There are 8 installation options:**
* Full Setup Bastion Server and Register Gitlab Runner
* Only Install Gitalb Runner
* Only Install Docker and Docker Compose
* Only Install Docker Machine
* Only Register Gitlab Runner
* Only Install AWS CLI and AWS Login
* Only Add Cron AWS Login
* Only Setup Bastion Server

**Ansible must be installed on the server you need!**

 **To install, you need to download scripts and run `bash main.sh`**

**What is included in the server setup**
**System:**
* Install Gitlab Runner latest version!
* Install Docker and Docker-compose latest version!
* Install Docker-machine latest version!
* Install AWS cli latest version!
* Configure Gitalb Runner
* Configure AWS parameters
* Add AWS Login to Cron Job

## License
Configs is Copyright © 2015-2021 Codica. It is released under the [MIT License](https://opensource.org/licenses/MIT).

## About Codica

[![Codica logo](https://www.codica.com/assets/images/logo/logo.svg)](https://www.codica.com)

We love open source software! See [our other projects](https://github.com/codica2) or [hire us](https://www.codica.com/) to design, develop, and grow your product.