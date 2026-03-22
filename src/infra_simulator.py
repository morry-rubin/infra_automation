from main_helper import get_user_input, save_machine_to_file
import run_bash_script

if __name__ == "__main__":
    instances = get_user_input()
    print(f"{instances} \n")
    save_machine_to_file(instances)
    run_bash_script.run_setup_script()