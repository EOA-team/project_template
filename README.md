# Unit Tests
python -m pytest 
python -m pytest tests/test_calculator.py 
python -m pytest tests/test_calculator.py::test_add_floats 

# Code Style
pylint code
pylint code/calculator.py 
pylint tests
pylint tests/test_calculator.py
# Static Type Checking 
mypy code 
mypy code/pywinauto_helpers_new.py

# Run a script
python -m code.scripts.automate_hyspexrad

# Autopep 8
autopep8 --in-place code/myfile.py 


 mypy .                                                                                                                                                                                                                            
 pylint $(git ls-files '*.py') --fail-under=8.0                                                                                                                                                                                    
 pytest --cov=. --cov-fail-under=80          