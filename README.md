
## Description

This project demonstrates how the Elliptic Curve Digital Signature Algorithm (ECDSA) works. It includes a simple Python application that implements the ECDSA algorithm to show its functionality in creating and verifying digital signatures. ECDSA is widely used in various security protocols and applications, making this project useful for developers and students looking to understand or implement ECDSA in their own projects.

## Requirements

- Python 3.6 or higher
- The following Python packages (can be installed via `pip`):
  - `ecdsa`

## Mode of Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/ecdsa-poc.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ecdsa-poc
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Implementation Details

The `app.py` file contains the main implementation of the ECDSA algorithm, showcasing how to generate a key pair, create a digital signature, and verify it. The project uses the `ecdsa` Python library to facilitate these operations.
