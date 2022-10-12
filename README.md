# Toy Robot Code Challenge

## Procedure for Execution

This requires Python 3.7 or above using python virtual environment.

Navigate to the extracted folder in your terminal and run the following commands.

Initiate venv env and Install dependencies:
```bash
python -m venv venv
pip install -r requirements.txt
```

`setup.py` is the build tool for Python.

```bash
python setup.py test # Run all the corresponding unit test
```

To run toyrobot commandline program, run the `main.py` file
```bash
python main.py
```

#### Sketches of important points of execution

##### Directions:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; North\
West <--|-->East\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; South

##### Table Structure:
<table>
  <tr>
    <td>0,4</td>
    <td>1,4</td>
    <td>2,4</td>
    <td>3,4</td>
    <td>4,4</td>
  </tr>
  <tr>
    <td>0,3</td>
    <td>1,3</td>
    <td>2,3</td>
    <td>3,3</td>
    <td>4,3</td>
  </tr>
  <tr>
    <td>0,2</td>
    <td>1,2</td>
    <td>2,2</td>
    <td>3,2</td>
    <td>4,2</td>
  </tr>
   <tr>
    <td>0,1</td>
    <td>1,1</td>
    <td>2,1</td>
    <td>3,1</td>
    <td>4,1</td>
  </tr>
   <tr>
    <td>0,0</td>
    <td>1,0</td>
    <td>2,0</td>
    <td>3,0</td>
    <td>4,0</td>
  </tr>
</table>

##### Available commands: PLACE, MOVE, LEFT, RIGHT, REPORT, EXIT
where PLACE command has three parameters x_position, y_position and Direction (NORTH, SOUTH, EAST, WEST)

##### Design & implementation
- Focused on Object Oriented approach
- Abstract & decoupled subsets
- Used standard libraries - `unittest`, `unittest.mock`, `map`, `filter`
- Handled mutable & immutable data
- Appropriate annotations

#### Assumptions
- *Python 3.7 or above* is already available in the end user system.
- A new command has been introduced *EXIT* - To quit the toyrobot execution, and it is recognized as `EXIT`

![Sample Execution](sample_screenshot.PNG?raw=true "Sample Testcases Screenshot")