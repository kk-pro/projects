# Secure Digest files based on Blockchain

Digest files are essential for digital forensics and data integrity.

## what problem does this project solve?

From a cyber security perspective, losing or tempering the digest files (intentional or unintentional) is a disaster for the cybersecurity team. The cost of maintaining digest files security is high for most organizations. Using Blockchain to store digest files made it almost impossible to delete the files since the data cant be modified or deleted on Blockchain unless you control 51% of the nodes

## Instructions to run
first, we need the Blockchain up and running

Install the dependencies,

```sh
$ cd python_blockchain_app
$ pip install -r requirements.txt
```

Start a blockchain node server,

```sh
# Windows users can follow this: https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery
$ export FLASK_APP=node_server.py
$ flask run --port 8000
```

One instance of our blockchain node is now up and running at port 8000.

Run the Blockchain application on a different terminal session,

```sh
$ python run_app.py
```

Run the main application,

```sh
$ cd secure_digestfile
$ python run_app.py /digestfiles_path/
```

To restore digest files 

```sh
$ cd secure_digestfile
$ python restore.py
```






Blockcahin was made by  https://github.com/satwikkansal

