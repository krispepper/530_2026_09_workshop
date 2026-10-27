# Workshop Management Application

Follow the steps below to set up and run our Flask application on your local machine.

## How to Run the App (Manual Setup)

**Step 1: Clone the repository**
You need to clone our repository from GitHub to grab all the project files. Run this command in your terminal:
```bash
git clone [https://github.com/krispepper/530_2026_09_workshop.git](https://github.com/krispepper/530_2026_09_workshop.git)
```

**Step 2: Set up a Python virtual environment**
This is a good idea because it protects the packages you need for this project from having conflicts with other packages on your system. Run these commands:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Step 3: Install dependencies**
There is a file in this project called `requirements.txt` that tells your system exactly what packages you need to run our Flask app. Running this command installs all of them:
```bash
pip install -r requirements.txt
```

**Step 4: Run the app**
Now that you have installed the files, you can run our Flask app. When you run the command, it will ask you for a port number in the terminal. If you are not sure what to put, just type `5001`.
```bash
python3 app.py
```

---

## Alternative Option (Quick Setup)
If you prefer, you can use our `run.sh` script to set up and start the app automatically. 

**Step 1: Give permission to the file**
```bash
chmod +x run.sh
```

**Step 2: Run the script**
```bash
./run.sh
```

---

## Running Unit Tests
We use `pytest` for unit testing our backend modules (users, workshops, and enrollments). All unit tests are organized inside the `tests/` folder. 

You can run the tests using our test script:

**Step 1: Give execution permission to the test script**
```bash
chmod +x run_tests.sh
```

**Step 2: Run the tests**
```bash
./run_tests.sh
```
