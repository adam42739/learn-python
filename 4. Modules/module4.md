# Modules

In Python we can separte our code in different files called _Modules_. Suppose we have a project that analyzes financial statements for a company. We might want to create a module for each type of financial statement. This way, all the codes that work on the same type of financial statement can be grouped together.

```
|__ FinanceProj
      |__ balance_sheet.py
      |__ income_statement.py
      |__ cash_flow.py
      |__ equity.py
      |__ main.py
```

Now inside our `main.py` file we can import all the other modules all call their functions.

```python
import balance_sheet
import income_statement
import cash_flow
import equity

print(balance_sheet.analyze())
print(income_statement.analyze())
print(cash_flow.analyze())
print(equity.analyze())
```

This is exactly how a library like `pandas` works. When we call `import pandas`, we're loading in the module called `pandas` which written by the `pandas` developers. When we call a function like `pandas.read_csv()`, we're simply calling a function that was written inside the `pandas` module.