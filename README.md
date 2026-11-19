# Ask your Mario

### This is a simple running game with Q&A


<img width="364" height="240" alt="1117 (1)" src="https://github.com/user-attachments/assets/b522c848-6cc0-46bd-b731-13b6ca80071d" />


A small character running forward. Jump over traps and firepillars to survive. 
A sage will appear after some distance. Answer his question.

You have 3 hearts. If you hit traps 3 times then game over. But if you answer wrong once, it's over. 

Controls: 
It moves forward automatic so it only needs to jump
Click anything among `Space` `W` and `Up` to jump

## How to run it:

* Download this repo
* open `mario.py` python script in your code editor
* In the quiz array write your questions and answers replacing the dots.
  <img width="491" height="178" alt="image" src="https://github.com/user-attachments/assets/33645876-c1e5-43c0-b2f7-1f59c992765f" />
* save the file
* Downolad pygame library
```
   pip install pygame
```
* Run the python script
```
   python mario.py
```

## Demo:

For demo to check how it runs - 
* GO to the release section and download the `.exe` file
* Go to your downloads and run the application
* The game will work automatically. Use `Space` or `W` or `Up` key to jump over traps
* For the demo answer `......` to the sage's questions. 
* If you want to modify sage questions and answers then follow the [How to run it guideline](https://github.com/Adnanosman9/Ask-Your-Mario/blob/main/README.md#how-to-run-it)

  <img width="414" height="240" alt="1115" src="https://github.com/user-attachments/assets/a134ae4d-5cac-4821-acdb-df3316860c91" />


## Architecture:

This game uses one external python library `pygame`
different parts of this game are made in different files to make debugging easier.
I tried to make the 2d background and design good but it was hard for me to place everything properly. Some bugs are here like 
* Trees placement, 
* Traps placement, sometimes traps are so close that it becomes impossible to jump over. 

<img width="897" height="547" alt="Screenshot 2026-11-17 124609" src="https://github.com/user-attachments/assets/c8e8609d-5ff9-4c3e-9557-76c464da6740" />


## Debugging:

A big part of this game was combining all files in one piece. A big issue I faced during debugging was variable and function names. I messed up variable function and classes names by using short single word as variable. 

Another issue was drawing sage and some syntax and placing errors. 

## AI Usage (Kiro CLI)

- Debugging messed up same variable names across all classes.
- Made a `reference.md` file using AI to keep track of the names so that i don't forget again and make debugging easier
- debugging syntax and font errors while connecting all pieces together.
- The `words()` word-wrap function in `dialogue.py` was written with AI help. Without this here was an error while sage question appears. 

Took suggestions from AI to draw the sage chaarcter. 

## Built with
  
- Python 3.12
- Pygame 2.6
