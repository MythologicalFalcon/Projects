# TestCaseReduction

Reduces a regression test suite so it runs faster while keeping comparable coverage.

Test cases are described by numeric features in a CSV. `reduceKNN.py` fits a
scikit-learn `NearestNeighbors` model over those features and selects a representative
subset, dropping cases that sit close to one already chosen. `reportGen.py` writes the
run out to `test_report.csv`, and `visual.py` plots the result.

`weather.py` and `testWeather.py` are the worked example: a small weather module with a
test suite to reduce.

## Layout

- `main.py` entry point
- `src/mainPackage/reduceKNN.py` the KNN reduction
- `src/mainPackage/reduce.py` alternative reduction pass
- `src/mainPackage/DataHandle.py` and `manageData.py` for CSV loading and cleaning
- `src/mainPackage/visual.py` matplotlib output
- `src/reportGen.py` report writer
- `src/resources/` input and output CSVs

## Running

```
pip install pandas scikit-learn matplotlib
python main.py
```

## Known limitation

`reduceKNN.py` selects `indices[:, 0]` from the fitted neighbour matrix. When a model is
fitted and queried on the same data, a point's nearest neighbour is itself, so that
column is just the original row order and the step returns the full set rather than a
reduced one. Selecting from column 1 onward, or de-duplicating the chosen indices, is the
fix.

Python, scikit-learn, pandas, matplotlib.
