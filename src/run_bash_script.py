import subprocess
import logging
from pathlib import Path

logger = logging.getLogger("infra_sim")

def run_setup_script():
    try:
        curr_dir = Path(__file__).resolve().parent.parent # to get to the infra dir
        script = curr_dir / "scripts/setup_nginx.sh"
        logger.info("running scripts/setup_nginx.sh...")
        print("running script... \n")
        subprocess.run([str(script)], check=True, shell=True)
        logger.info("Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"[ERROR] Failed to install Nginx")

# Example call:
if __name__ == "__main__":
    run_setup_script()
