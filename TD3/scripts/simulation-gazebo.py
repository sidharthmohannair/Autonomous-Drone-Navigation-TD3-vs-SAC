#!/usr/bin/env python3

import argparse
import subprocess
import os
import shutil

def run(cmd):
    process_handle = subprocess.Popen(['bash', '-c', cmd], cwd='.')
    return process_handle

def main():
    parser = argparse.ArgumentParser(description='Gazebo simulation')

    parser.add_argument('--world', help='World to run in Gazebo', required=False, default="warehouse")
    parser.add_argument('--gz_partition', help='Gazebo partition to run in', required=False)
    parser.add_argument('--gz_ip', help='Outgoing network interface to use for traffic', required=False)
    parser.add_argument('--interactive', help='Run in interactive mode', required=False, default=False, action='store_true')
    parser.add_argument('--model_source', help='Path to directory containing model files', required=True , default="/home/colcon_ws/src/drl_x500")
    parser.add_argument('--overwrite', help='Overwrite existing model directories', required=False, default=False, action='store_true')
    parser.add_argument('--dryrun', help='Test in dryrun. Do not launch gazebo', required=False, default=False, action='store_true')
    parser.add_argument('--headless', help='Run Gazebo without GUI', required=False, default=False, action='store_true')

    args = parser.parse_args()

    # Set up environment variables to look for models for simulation
    args.model_source = os.path.expanduser(args.model_source)

    # Check whether the model source directory exists.
    if not os.path.exists(args.model_source):
        print(f"Model source directory {args.model_source} does not exist.")
        exit(1)

    model_count = int(subprocess.check_output(f'find {args.model_source} -type f | wc -l', shell=True, text=True))
    models_exist = True if model_count > 0 else False
    print(f"Found: {model_count} files in {args.model_source}")

    if not models_exist:
        print("Model directory is empty. Please provide a valid model source directory.")
        exit(1)

    if models_exist and args.overwrite:
        try:
            subdirectories = [os.path.join(args.model_source, d) for d in os.listdir(args.model_source) if os.path.isdir(os.path.join(args.model_source, d))]
            for directory in subdirectories:
                shutil.rmtree(directory)
            print("Overwrite set. Removed existing model subdirectories.")
        except:
            print("No models dir present, overwrite did not remove a directory.")

    world_file = os.path.join(args.model_source, "worlds", f"{args.world}.sdf")
    if not os.path.isfile(world_file):
        print(f"World file {world_file} does not exist.")
        exit(1)

    # Launch gazebo simulation
    print('> Launching gazebo simulation...')
    if not args.dryrun:
        cmd = f'GZ_SIM_RESOURCE_PATH={args.model_source}/models gz sim -r {world_file}'
        if args.headless:
            cmd = f'{cmd} -s'

        if args.gz_partition:
            cmd = f'GZ_PARTITION={args.gz_partition} {cmd}'
        if args.gz_ip:
            cmd = f'GZ_IP={args.gz_ip} {cmd}'

        try:
            process_handle = run(cmd)

            while process_handle.poll() is None:
                process_handle.wait()

        except KeyboardInterrupt:
            exit(0)

if __name__ == "__main__":
    main()
