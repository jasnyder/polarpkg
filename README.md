This is a pip-installable package containing all the code needed to run the cell polarity model, with all the modifications I've made of it.

Code (the bulk of `polarcore.py`) comes from this repo: [https://github.com/juliusbierk/polar](https://github.com/juliusbierk/polar)

To download and install this package, you can do:
1. Navigate to an empty folder
2. Run `gh repo clone jasnyder/polarpkg`
3. Run `python3 -m pip install .`

This should install the package. You should then be able to import it in Python by doing
```python
import polaritymodel
```