# PyQt-Contact-Book

This Contacts Book app was built using Python, [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html), and [SQLite](https://www.sqlite.org/docs.html). Check out the tutorial where the idea for this project came from [here](https://realpython.com/python-contact-book/).

## Running the App

To run this application, please download the source code. Then open a terminal or command-line window and run the following steps:

1. Create and activate a Python virtual environment:

```sh
$ cd contacts/
$ python -m venv env
$ source env/bin/activate
(env) $
```

2. Install the dependencies:

```sh
(env) $ python -m pip install -r requirements.txt
```

3. Run the application!

```sh
(env) $ python contacts.py
```

## Future Improvements

- Add dropdown element for 'status' field.
- Perform data validation upon updating an entry.
- Add an icon to the window's title bar.
- Implement a way to perform a bulk import of entries via a CSV file.
