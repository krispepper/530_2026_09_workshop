enter commands in the following order to run our app

**Step 1: You need to clone our repository from git hub to grab the files you need**

run the command below

git clone https://github.com/krispepper/530_2026_09_workshop.git

**Step 2: You need to setup a python virtual enviroment.**

This is a good idea because it protects the packages you need from having conflicts with other packages on a given system.

Run the following commands below

python -m venv .venv

source .venv/bin/activate

**Step 3: Install dependencies.**

There is a file in this project called requirements.txt that tells you what pacakges you need to run our flask app.
running this file installs the needed packages that are listed

run this command

pip install -r requirements.txt

**Step 4: Run app**

Now that you have installed the files you can run our flask app.
When you run the command it will ask you for a port number.
If you are not sure what to put do 5001

run this command

python3 app.py

**Alterantive Option:**

You can our run.sh file to setup our app


**Step 1: give permission to file run.sh**

run this command

chmod +x run.sh

**Step 2: Run file**
run this command

./run.sh

**Step 5: Run Unit Tests**

We use `pytest` for unit testing our backend modules (users, workshops, and enrollments). 
All unit tests are organized in the `tests/` folder.

You can run the test script using your exact terminal workflow:

**Step 1: Give execution permission to the test script**
```bash
chmod +x run_tests.sh