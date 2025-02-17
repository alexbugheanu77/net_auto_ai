# AI-Powered Network Automation Tool

This tool allows you to automate network configuration, troubleshooting, and other tasks using natural language prompts. It leverages OpenAI's API for natural language processing and network libraries like Netmiko for device interaction.

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Configure `config.py` with your OpenAI API key and network device credentials.
6. Run the web interface: `python web_interface.py`

## Usage

1. Open the web interface in your browser (usually `http://127.0.0.1:5000/`).
2. Enter a natural language prompt in the text box (e.g., "Configure VLAN 10 on switch SW1").
3. Click the "Run" button.
4. The tool will process your prompt, interact with the network device(s), and display the results.

## Dependencies

*   Python 3.7+
*   Flask
*   OpenAI Python Library
*   Netmiko (or other network device interaction library)
*   ... (other dependencies)

## Configuration

Edit the `config.py` file to provide your OpenAI API key and network device credentials.  **DO NOT COMMIT THIS FILE WITH SENSITIVE INFORMATION!**

## Contributing

... (Contribution guidelines)

## License

... (License information)