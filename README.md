#
# 🖥️ Infra Simulator

`infra_simulator.py` is a simple infrastructure simulation tool that allows users to create virtual "machine" objects by entering system specifications. The program stores all created instances in a JSON file and automatically installs and enabling NGINX via a bash script.

--- 

## 🚀 Features

- Interactive CLI for creating machine instances  
- Collects machine specs:
  - Name
  - Operating System
  - RAM
  - CPU  
- Continues creating machines until the user enters `done`  
- Stores all instances in `instances.json`  
- Automatically runs a provisioning script to:
  - Install NGINX  
  - Enable and start the service   

---

## ⚙️ Requirements

- Linux-based operating system 🐧  
- Python 3.x  
- Root privileges (`sudo`) — required for NGINX installation  

---

## 🧰 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/morry-rubin/infra_automation.git
cd infra_automation
````

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

> ⚠️ **Important:** This script must be run with `sudo` or as root.

```bash
For example:
sudo python3 src/infra_simulator.py
```

---

## 💡 How It Works

1. The program prompts the user to enter:

   * Machine name
   * Operating system
   * RAM
   * CPU

2. A machine object is created with the provided specs.

3. The process repeats until the user enters:

```
done
```

4. All created machines are saved into:

```
configs/instances.json
```

5. After creation, a bash script is executed which:

   * Installs NGINX
   * Starts and enables the service

---

## 📁 Input / Output Example

```txt
Enter machine name (or 'done' to finish): pc_1
Enter wanted OS (Ubuntu/CentOS): centos
Enter the number of wanted vCPUs (e.g., 2): 1
Enter wanted RAM in GB (e.g., 4): 8

Provisioning pc_1: centos, 1, 8

Enter machine name (or 'done' to finish): pc_2 
Enter wanted OS (Ubuntu/CentOS): ubuntu
Enter the number of wanted vCPUs (e.g., 2): 4
Enter wanted RAM in GB (e.g., 4): 7

Provisioning pc_2: ubuntu, 4, 7

Enter machine name (or 'done' to finish): done

[Machine(name='pc_1', os='centos', cpu=1, ram=8), Machine(name='pc_2', os='ubuntu', cpu=4, ram=7)]

all done saving the machines!

running...

Updating package list...
Starting installation of nginx...

completed installation of nginx!

Setting up nginx service and enableing it...
nginx service is up and running!
```

---

## ⚠️ Notes

* Must be run on **Linux only**
* Requires **root privileges** for provisioning (NGINX installation)
* Ensure your system has internet access for package installation
* The script will modify your system by installing NGINX

---
