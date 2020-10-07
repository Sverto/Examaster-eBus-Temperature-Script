# Set Bulex Examaster Temperature
Basic Python script to overwrite heating temperature setpoint.  
Created for a 2-circuit heating system.  
  
**This script writes values to the registers of your heating system and can result in unexpected behaviour.**  
**!!! USE AT YOUR OWN RISK !!!**

## Requirements
- eBus connection to Examaster (using a Raspberry connected to an [eBus Koppler](https://www.esera.de/produkte/ebus/135/1-wire-hub-platine) for example)
- [ebusd](https://github.com/john30/ebusd)
- Knowledge of the `ebusctl` command that comes with `ebusd` to find the correct registers to write to

## Setup
Edit the script
```bash
nano ebus_set_temperature.py
```
Put in the correct register values specific to your situation
```python
register_temp_setpoint_downstairs = "9700" # Example value
register_temp_setpoint_upstairs = "FE00" # Example value
```
Note: The values written to the registers are converted to type D2C by the script.

## Usage
```bash
python ebus_set_temperature.py downstairs 22.0
```