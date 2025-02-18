from netmiko import ConnectHandler
from config import NETWORK_DEVICES


def execute_commands_on_device(device_name, commands):
    """
    Executes a list of commands on a network device using Netmiko.

    Args:
        device_name (str): The name of the device (as defined in `config.py`).
        commands (list of str): A list of commands to execute.

    Returns:
        str: The output from the device.  Returns None if an error occurred.
    """
    if device_name not in NETWORK_DEVICES:
        print(f"Error: Device '{device_name}' not found in configuration.")
        return None

    device_params = NETWORK_DEVICES[device_name]

    try:
        net_connect = ConnectHandler(**device_params)
        output = net_connect.send_config_set(commands)  # Send as a configuration set
        net_connect.disconnect()
        return output
    except Exception as e:
        print(f"Error connecting to {device_name} or executing commands: {e}")
        return None


def get_device_facts(device_name):
    """
    Retrieves device facts using Netmiko.

    Args:
        device_name (str): The name of the device.

    Returns:
        dict: A dictionary containing device facts.  Returns None if an error occurred.
    """
    if device_name not in NETWORK_DEVICES:
        print(f"Error: Device '{device_name}' not found in configuration.")
        return None

    device_params = NETWORK_DEVICES[device_name]

    try:
        net_connect = ConnectHandler(**device_params)
        device_facts = net_connect.send_command("show version")  # or other command
        net_connect.disconnect()
        return device_facts # process and return as dictionary

    except Exception as e:
        print(f"Error connecting to {device_name} or retrieving facts: {e}")
        return None


if __name__ == '__main__':
    # Example Usage
    device_name = "SW1"  # Replace with your device name
    commands_to_execute = [
        "interface GigabitEthernet0/2",
        "description TEST_INTERFACE_FROM_SCRIPT",
        "no shutdown"
    ]

    output = execute_commands_on_device(device_name, commands_to_execute)

    if output:
        print(f"Output from {device_name}:\n", output)
    else:
        print(f"Failed to execute commands on {device_name}.")

    facts = get_device_facts(device_name)
    if facts:
        print(f"Device Facts: {facts}")
    else:
        print("Failed to retrieve device facts.")
