# 🧮 Scientific Calculator
A bare-bones scientific calculator made using python that internally uses Polish Notation Algorithm, more commonly known as Postfix Algorithm.

The implementation is done using an incremental stack which acts as a wrapper over python's list and provides normal naming conventions.

The project is a fun group project made in UG semester 4 for python programming skill based lab course. So it's not a full-blown scientific calculator but rather a cheap imitation of one.

#### 📒 Note:
- The project is built using Python3 so any references to python defaults to Python3 otherwise a version will be specified.

### 🫂 Group Members:
- Danyl Fernandes - Layout
- Boris Misquitta - Assets
- Celestyn Kinny - Logic
- Raymun Victor - Presentation

## 💽 To Run:

As described the project only relies on 2 external dependencies namely, `Tkinter` and `sqlite3` which are both available in python's standard library. Keep in mind that `sqlite3` was added to standard library in `Python 2.5` and `Tkinter` has been added since `Python 3.1`.

Now to run, just enter the following command.
```commandline
py calculator.py
```

Make sure that your current working directory is the project directory. Even if you are in the correct directory and command doesn't work try one of the following commands.

```commandline
python3 calculator.py
```

```commandline
python calculator.py
```

```commandline
py3 calculator.py
```

If an error shows up during the launch, please raise an issue.

## 🖼️ Screenshots

![Expression: 2^(78-3!-70)+12.5*(9/3)](screenshots/calculator_snap_1.png?raw=true "Expression Screenshot")

As you can see you may use a wide variety of expressions from the basic feature this calculator provides.

Just try not to press the maximize button as it will make the layout messy.

![Answer: 41.5](screenshots/calculator_snap_1_ans.png?raw=true "Expression Screenshot")

Yes, every answer is logged along with the expression that made it happen, but on the interface you can only see the answer using the arrow keys on your keyboard or on the calculator.

### 🧑‍💻 Have Fun!!! 🎉




