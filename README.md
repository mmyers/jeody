# jeody

This is a web application that displays Jeopardy data on the web and uses data mining techniques to help hopeful candidates study for the game.

## How to get started

0. Install Django (https://docs.djangoproject.com/en/1.10/howto/windows/)
1. Clone or download the repository
2. Download the Jeopardy data in CSV format. I got the data from the Reddit page we started from (https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/ -- Look for the CSV link)
3. Run the following command `python importdata.py /path/to/CSV/file` replacing /path/to/csv/file with the path to the Jeopardy CSV file
4. This will output a data.json file. Then run `python manage.py loaddata /path/to/data.json`. This will take a while but eventually the data will import.
5. Then run `python manage.py runserver` to start the server. The URL is 127.0.0.1:8000/

## Run migration (Do this every time there's a new commit)

1. Run `python manage.py migrate`
