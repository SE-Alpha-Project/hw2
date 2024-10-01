<div align="center">
   
![Static Badge](https://img.shields.io/badge/python-3.13-brightgreen)
![Static Badge](https://img.shields.io/badge/platform-linux-blue)
![Static Badge](https://img.shields.io/badge/license-MIT-purple)
[![Test Cases](https://github.com/SE-Alpha-Project/hw2/actions/workflows/test.yml/badge.svg)](https://github.com/SE-Alpha-Project/hw2/actions/workflows/test.yml)
[![Coverage Status](https://we-cli.github.io/jayin/badges/coverage.svg)](https://github.com/SE-Alpha-Project/hw2/actions)
[![Code Style]([https://we-cli.github.io/jayin/badges/coverage.svg](https://img.shields.io/badge/code%20style-pep8-yellow.svg))](https://github.com/SE-Alpha-Project/hw2/actions)
<img src="https://img.shields.io/badge/linting-pylint-violet">
<img src="https://microsoft.github.io/pyright/img/pyright_badge.svg">

</div>
<div>Hi Everyone! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="20px"></div>

We are Team Alpha & welcome to our HW2 Repository!
<div align="center">
  
</div>

<h1 align="center">Debugging</h1>

## What is Merge Sort?

Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.

Merge sort is efficient with a time complexity of \( O(n \log n) \), making it suitable for large datasets. It is also a stable sorting algorithm, meaning it preserves the relative order of equal elements from the original input.



<div align="center">
<img src="https://willrosenbaum.com/assets/img/2022f-cosc-311/merge-sort.gif" width="600">
</div>

## Auto test generation
1. **Python Pre-requisite:** Python 3.x
2. **Navigate to the code directory**
```sh
cd hw2
```
3. **Install Dependencies**
```sh
pip install -r requirements.txt
```
4. **Adding a virtual machine enviroment (Optional)**
```sh
python3 -m pip install --user virtualenv   #installing the vm
python3 -m venv myenv                      #creating vm
source myenv/bin/activate                  #activating vm
```
5. **Python Run Command:** You can use the following commmand for running the Python code
```sh
python hw2_debugging.py
```
6. **Python auto-test Run Command:** You can use the following commmand for generating the files for pyright and pylint


-> Debugging file
```sh
autopep8 hw2_debugging.py > post_traces/autopep8_hw2_debugging_trace.txt
pylint hw2_debugging.py > post_traces/pylint_hw2_debugging_trace.txt
pyright hw2_debugging.py > post_traces/pyright_hw2_debugging_trace.txt
```
-> Rand file
```sh
autopep8 rand.py > post_traces/autopep8_rand_trace.txt
pylint rand.py > post_traces/pylint_rand_trace.txt
pyright rand.py > post_traces/pyright_rand_trace.txt
```
7. **Python Test Code Coverage:** You can use the following commmand for checking the overall code coverage
```sh
coverage run -m pytest
```

## Error fixes

1. **Debugging:** Check for the errors as produced in the auto test files
2. **Verification through report generation:** Re-run the commands & check the result for errors as the files get updated post changes and the report is generated

## Authors
[Chaitralee Datar](https://www.linkedin.com/in/cd2001/)

[Yash Shah](https://www.linkedin.com/in/yash2705/)

[Ananya Patankar](https://www.linkedin.com/in/ananya-patankar/)

## References
1. GeekforGeeks
2. W3Schools
3. Willrosenbaum

