# PythonHTTPDoSProbe

## Introduction

`PythonHTTPDoSProbe` is a Python tool designed to test server resilience and firewall rules against high-volume HTTP requests. It uses multi-threading to simulate concurrent HTTP traffic to a specified URL, providing a valuable resource for network administrators and security professionals to assess system performance and robustness.

## Prerequisites

Before running `PythonHTTPDoSProbe`, ensure your system meets these requirements:

- **Python Version**: Python 3.6 or higher.
- **Libraries**: Requires the `requests` library.

### Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the `requests` library using pip:

   ```
   pip install requests
   ```

### Setup

1. Clone the repository:

   ```
   git clone https://github.com/iyonr/PythonHTTPDoSProbe.git
   ```

2. Navigate to the repository directory:

   ```
   cd PythonHTTPDoSProbe
   ```

## Usage

Run the script from the command line, specifying the target URL and number of threads:

```
python http-dos-probe.py [target_url] [num_threads]
```

Example:

```
python http-dos-probe.py http://example.com 500
```

## Disclaimer

`PythonHTTPDoSProbe` is intended for educational and testing purposes only within environments where explicit authorization is granted. All activities must be conducted in a legal and ethical manner. The author is not responsible for misuse or any damage that may be caused by the script.

**Responsibility for Use**: Modifying this script and using it for threatening or illegal activities, including deployment in production environments or for committing crimes, is strictly prohibited. Users are fully responsible for their actions when using or modifying this script. It is the user's responsibility to comply with all applicable laws and regulations.

## License

[MIT License](LICENSE)

