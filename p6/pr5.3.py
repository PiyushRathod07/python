import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3])
print(s.describe, "\n")

s = pd.Series(['a', 'a', 'b', 'c'])
print(s.describe, "\n")

s = pd.Series([
  np.datetime64("2000-01-01"),
  np.datetime64("2010-01-01"),
  np.datetime64("2010-01-01")
])
print(s.describe)


