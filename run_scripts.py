import subprocess

def run_commands(commands):
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with error code {e.returncode}")
            break
        except Exception as e:
            print(f"An error occurred while executing command '{command}': {e}")
            break

if __name__ == "__main__":
    # List of commands you want to run, replace these with your actual commands
    commands_to_run = [
        # "python train.py env=thrower_throw num_train_steps=2e6 seed=0",
        # "python train.py env=thrower_throw num_train_steps=2e6 seed=1",
        # "python train.py env=thrower_throw num_train_steps=2e6 seed=2",
        # "python train.py env=pusher_push num_train_steps=2e6 seed=0"
        # "python train.py env=pusher_push num_train_steps=2e6 seed=1",
        # "python train.py env=pusher_push num_train_steps=2e6 seed=2",
        # "python train.py env=walker_run num_train_steps=2e6 seed=0",
        # "python train.py env=walker_run num_train_steps=2e6 seed=1",
        # "python train.py env=walker_run num_train_steps=2e6 seed=2",
        # "python train.py env=cheetah_run num_train_steps=2e6 seed=0",
        "python train.py env=pendulum_swingup num_train_steps=3e6 seed=2 frame_skip=4",
        "python train.py env=cheetah_run num_train_steps=2e6 seed=1",
        "python train.py env=cheetah_run num_train_steps=2e6 seed=2",
    ]

    run_commands(commands_to_run)
