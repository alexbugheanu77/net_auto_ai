from flask import Flask, render_template, request
from ai_engine import generate_network_commands
from network_operations import execute_commands_on_device, get_device_facts

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None  # Initialize output
    device_facts = None

    if request.method == 'POST':
        user_prompt = request.form['prompt']
        device_name = request.form['device_name'] #get the device name from user input

        # 1. Generate Commands using AI Engine
        commands = generate_network_commands(user_prompt)

        if commands:
            # 2. Execute Commands using Network Operations
            # Split the commands string into a list of commands
            command_list = [cmd.strip() for cmd in commands.splitlines() if cmd.strip()] #split by lines
            output = execute_commands_on_device(device_name, command_list)

            # 3. Retrieve device facts
            device_facts = get_device_facts(device_name)

            if output:
                output = "Commands executed successfully:\n" + output
            else:
                output = "Failed to execute commands. Check the console for errors."
        else:
            output = "Failed to generate commands. Check the console for errors."

    return render_template('index.html', output=output, device_facts = device_facts)


if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development