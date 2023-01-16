# Quiz tool

## Instructions
* put the database in the `data` folder (for now just support `JSON format`)
* modify the `path` attribute in `setting.json` which is in the `config` folder 
* run the `main.py` or `main.exe`
***

## setting.json (config)
* `path` : the path of the database
* `width` : the width of the window
* `height` : the height of the window
* `font_ratio` : the size of the font
* `database` : the type of the database
* `model` : the type of the model
* `controller` : the type of the controller
* `view` : the type of the view

***

### Database format 

* JSON
    ```
    [
      {
        "front": "question1",
        "back": "answer1"
      },
      {
        "front": "question2",
        "back": "answer2"
      }
    ]
    ```
   `flashcards.json` is the example of the json database file

* CSV
  ```
  front,back
  question1,answer1
  question2,answer2
  ```
  `wordbank_1.csv` is the example of the csv database file



