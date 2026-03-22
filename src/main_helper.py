from machine import Machine
from pydantic import ValidationError
import json
import run_bash_script
import logging
import logger

logger = logging.getLogger("infra_sim")


def get_user_input() -> list[Machine]:
    """
    this func gets input from the user and creates new machines, \n
    user input is checked with pydantic (in the machine.py file)

    Returns:
        machines (list[Machine]): list of all the new machines created
    """

    machines = []
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            print()
            break

        while True:
            os = input("Enter wanted OS (Ubuntu/CentOS): ").lower()
            cpu = input("Enter the number of wanted vCPUs (e.g., 2): ")
            ram = input("Enter wanted RAM in GB (e.g., 4): ")

            print() # print new line for aesthetics
            try:
                new_machine = Machine(name=name, os=os, cpu=cpu, ram=ram)
                new_machine.log_creation()
                machines.append(new_machine)
                break
            except ValidationError as e:
                logger.error(f"{e} \n \nplease try again: ")                
    
    return machines

# no need for now cause of pydantic :)
def check_mechine_input(instance: dict) -> bool:
    if not (instance["os"].lower() == "ubuntu" or instance["os"].lower() == "centos"):
        print(f"invalid os chosen '{instance["os"]}', valid options are: Ubunto or CentOS")
        return False
    if (not instance["cpu"].isnumeric()) or int(instance["cpu"]) == 0:
        print(f"number of wanted cpu must be a positive integer (eg. 2), you entered - {instance['cpu']}")
        return False
    if (not instance["ram"].isnumeric()) or int(instance["ram"]) == 0:
        print(f"number of wanted RAM must be a positive integer (eg. 2), you entered - {instance['ram']}")
        return False
    return True


def save_machine_to_file(machines: list[Machine]):
    """
    This func saves the list of mashines thats given to the file "instances.json" 

    Parameters:
        machines (list[Mashine]): A list of Mashines to save

    Returns:
        None
    """

    machines_json = []
    with open("configs/instances.json", "w") as f:
        for machine in machines:
            machines_json.append(machine.to_dict())
        
        json.dump(machines_json, f, indent=4)
    logger.info("all mechines saved seccessfully!")
    print("all done saving the machines!\n")

if __name__ == "__main__":
    instances = get_user_input()
    print(f"{instances} \n")
    save_machine_to_file(instances)
    run_bash_script.run_setup_script()
