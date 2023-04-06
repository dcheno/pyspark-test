# INSTRUCTIONS

1. Follow the installation steps below to get everything up and running.
2. From within the virtual environment, run `python run.py`. You should see
   a return like this if everything was installed properly:
   ```
   +----------+-----+
   |   pokemon| type|
   +----------+-----+
   |charmander| fire|
   |charmeleon| fire|
   | bulbasaur|grass|
   |   starmie|water|
   |    lapras|water|
   +----------+-----+    
   ```
3. Go to `edit.py`, follow the instructions in the method docstring to
   re-implement the method as described. You can use `python run.py` to
   check your logic, but you should write the function as if your pipeline
   was moving millions of records, not just the test data included here.

## Installation (mac/linux)

1. clone this repository `git clone git@github.com:dcheno/pyspark-test.git`
   (or whatever your preferred method)
2. Move into the directory: `cd pyspark-test`
3. Create a virtual environment: `python3 -m venv .venv`
4. Activate that virtual environment (all steps from here on should take
   place within the virtual environment):  `source .venv/bin/activate`
5. Install dependencies (this will take a few minutes): `pip install -r requirements.txt`
