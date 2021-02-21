#!/usr/bin/env python
# coding: utf-8

# # Pandas cheatsheet

# This cheatsheet lists out important and most used pandas functionality.

# In[102]:


get_ipython().run_cell_magic('html', '', '<style>\n.dataframe th {\n    font-size: 10.5px;\n    color: #3b3b3b;\n}\n.dataframe td {\n    font-size: 10.5px;\n    color: #3b3b3b;\n}\n</style>')


# In[103]:


import pandas as pd

# Setting optimal options for cheatsheet.
pd.set_option('display.max_rows', 10)


# ## Input & Output

# Pandas input and output functions.

# ```{list-table}
# :header-rows: 1
# 
# * - Function
#   - Description
# * - `pd.read_csv()`
#   - reads data from csv file
# * - `pd.to_csv()`
#   - writes data to csv file
# * - `pd.read_sql`
#   - reads from sql
# ```

# ### Snippets

# **Reading from mysql**

# ```python
# from sqlalchemy import create_engine
# import pymysql
# 
# db_connection_str = 'mysql+pymysql://user_name:password@mysqlhost/database_name'
# db_connection = create_engine(db_connection_str)
# 
# df = pd.read_sql('SELECT * FROM customers', con=db_connection)
# ```

# ## Selecting & Indexing

# ```{csv-table}
# :header-rows: 1
# :delim: ;
# 
# Code; Description
# ``df['col']``; Selects a single column
# ``df[['col1', 'col2']]``; Selects multiple columns. Pass in a list of columns.
# ``df.loc[index]``; selects single row
# ``df.loc[[index1,index2], [col1, col2]]``; selects specified rows and columns
# ``df.loc[start_index:end_index, start_col:end_col]``; slices rows and slices columns (end value is included unlike Python). Standard slicing is supported e.g. ``dfl.loc['index':,::-1]``
# ``df.sort_index()``; sorts row based on index
# ``df.iloc[]``; selects by position not label
# ``df.index[position]``; gives index for a position
# ``df.index[[pos1, pos2, .., posn]]``; gives index for requested positions
# ``df.set_index[[col, col]]``; Ability to set single or multi-index.
# ``df.sample()``; gives back a random sample. You can pass in the count or the fraction.
# ``df.columns.get_loc('col_name')``; returns location for a particular column
# ``df.columns.get_indexer(['col_name', 'col_name'])``; returns location for a particular columns
# ``| & ~``; used for boolean indexing
# ``series.isin(iterable)``; returns True if value is in iterable
# ``series/df.where(filter_condition, default value)``; returns the same shape as original df and not a subset like boolean indexing
# ``df.query('expression')``; querys based on string experssion
# ``df.duplicated([col, col])``; duplicacy checks
# ``df.drop_duplicates([col, col], keep='first')``; drop duplicate where keep can be last or first or False
# ``series.get(index, default=___)``; dict like get method
# ```

# ### Snippets

# **Using conditionals on a single row to filter out columns. The below example would work on row which has all integers**

# In[104]:


import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,4), index=list('abcdef'), columns=list('ABCD'))

df1


# In[105]:


# Creates a mask for a single row to filter out the cols ==> df1.loc['a'] > 0

df1.loc[:, df1.loc['a'] > 0]


# #### Using functions's for selection
# 
# The function should take one argument.
# 
# Selecting rows from DataFrame where the column *base_salary* has value greater than 50K.

# In[106]:


import pandas as pd

emp = pd.read_csv('data/employee.csv', index_col='unique_id')
emp


# In[107]:


emp.loc[lambda x: emp['base_salary'] > 150000]


# #### Combine positional and label to select data

# In the below example `df.index[0:10:4]` provides the index for every 4th row from 0 to 10 position.

# In[108]:


emp.loc[emp.index[0:10:4], ['gender', 'base_salary']]


# In the below example ``df.columns.get_loc('base_salary')`` returns the integer position of the column base_salary.

# In[109]:


emp.iloc[[0,4], emp.columns.get_loc('base_salary') ]


# In the below example ``df.columns.get_indexer(['base_salary', 'gender' ])`` returns the integer position of the all specified columns.

# In[110]:


emp.iloc[[0,4], emp.columns.get_indexer(['base_salary', 'gender' ])]


# #### Boolean Indexing

# Tip : Use () to seperate the comparisons.

# In[111]:


mask = (emp['base_salary'] > 100000) | (emp['gender'] == 'Female') & (emp['employment_status'] == 'Active')
emp[mask]


# A little bit more complicated example.

# In[112]:


occupations = ['POLICE OFFICER', 'SENIOR POLICE OFFICER']
mask = ((emp['position_title'].map(lambda x: x in occupations)) & (emp['base_salary'] > 50000))
emp[mask].head(2)


# In[113]:


# Write above using isin

mask = ((emp['position_title'].isin(occupations)) & (emp['base_salary'] > 50000))
emp[mask].head(2)


# #### Where

# In[114]:


emp.where(emp['gender'] == 'Female', False)


# #### Query

# In[115]:


emp.query('base_salary > 100000 and employment_status == "Active" and gender == "Female"')


# ### MultiIndexing and Advanced Indexing

# ```{csv-table}
# :header-rows: 1
# :delim: ;
# 
# Code; Description
# `pd.MultiIndex.from_*`; Set of methods which create multiindex from various sources such as tuples, arrays ...
# ```

# Setting multiple indexes on a dataframe.

# In[116]:


import pandas as pd

emp = pd.read_csv('data/employee.csv')
emp = emp.set_index(['gender','unique_id'])
emp


# In[117]:


emp.loc['Female']


# In[118]:


emp.loc['Female'].loc[10]


# ## Setting options

# You can set options for pandas using `set_option` method e.g. `pd.set_option('display.width', None)`

# ```{csv-table}
# :header-rows: 1
# :delim: ;
# 
# Option; Description
# `display.width`; Use full width of terminal
# `display.max_columns`; Set as ``None`` to display all cols
# ```

# ## Text

# Refer to the following [link](https://pandas.pydata.org/docs/user_guide/text.html#method-summary) to get various string related methods and their uses.

# String methods are used as follows `Series.str.method()`, to chain follow the pattern  `Series.str.method().str.method()`

# ### Snippets

# In[119]:


emp[emp['department'].str.contains('Lib')]


# In[120]:


emp['department'].str.lower().str.split()


# ## Merge & Joins

# ## Grouping & Aggregations

# ```{csv-table}
# :header-rows: 1
# :delim: ;
# 
# Code; Description
# ``df.groupby('colname')``; Groupby a single column
# ``df.groupby(['colname', 'colname'])``; Groupby multiple columns in order of listing
# `df.groupby(colname)[col].agg(agg_function)`; Aggregate on a column after group by
# ``df.groupby([col, col])[[col, col]].agg([func1, func2])``; Aggregate multiple funcs on multi column after group by on multi cols.
# ``df.groupby([col, col])[[col, col]].agg({col:[func1, func2], col[func3, func4]})``; Aggregate multiple funcs on multi column after group by on multi cols. (Seperate aggregation for seperate cols.)
# ``df.groupby(colname)[col].agg(agg_function).rename(columns = {})``; rename cols
# ``df.groupby(colname).agg(final_col_name = pd.NamedAgg(column=aggregate_on_col, aggfunc=func_name))``; Named Aggregation
# ```

# ### Snippets

# In[121]:


flights = pd.read_csv('data/flights.csv')
flights


# In[122]:


flights.groupby('AIRLINE').describe()


# In[123]:


flights.groupby('AIRLINE')['DEP_DELAY'].mean()


# In[124]:


flights.groupby(['AIRLINE', 'WEEKDAY'])[['CANCELLED', 'DIVERTED']].agg([np.sum, np.mean, np.std])


# In[125]:


flights.groupby(['AIRLINE'])[['AIRLINE','CANCELLED', 'DEP_DELAY']]    .agg({'AIRLINE':'count','CANCELLED':[np.sum], 'DEP_DELAY':[np.mean, np.std]})    .rename(columns={'count':'Total Flights', 'sum':'Total Cancelled','std':'Standard Deviation', 'mean':'Average Delay'})


# #### Named Aggregation

# In[126]:


flights.groupby(['AIRLINE'])    .agg(
         **{
             "Total Flights":pd.NamedAgg(column='AIRLINE',aggfunc='count'),
             "Total Cancelled":pd.NamedAgg(column='CANCELLED',aggfunc=np.sum),
             "Average_Delay":pd.NamedAgg(column='DEP_DELAY',aggfunc=np.mean),
             "Std Dev on Departure Delay":pd.NamedAgg(column='DEP_DELAY',aggfunc=np.std),
             "Funny Val":pd.NamedAgg(column='DEP_DELAY',aggfunc=lambda x: (np.std(x) + 2))  # Can supply lambda as well.
         }
)


# In[127]:


flights


# ## TimeSeries

# Working with dates and times is a complex topic, only a small subset of functionality is covered here.

# While working with pandas timeseries you can use the following time related concepts
# 
# - Date time - A specific date and time with timezone support 
# - Time deltas - absolute time duration
# - Time Spans -  A span of time defined by a point in time and its associated frequency.
# - Date Offsets - A relative time duration that respects calendar arithmetic.
# 
# For details on the methods refer to the following [link](https://pandas.pydata.org/docs/user_guide/timeseries.html#overview)

# ```{csv-table}
# :header-rows: 1
# :delim: ;
# 
# Code; Description
# ``pd.date_range('2020-01-01', periods=10,freq='H')``; Creating dates
# ``pd.Timedelta``; Used for arithmetic of date and time
# ``df['col'].astype('datetime64')``; Convert to datetype. For timezone use ``'datetime64[ns, US/Eastern]'`` Supports from nanosec to weeks.
# ``pd.to_datetime(df['col'])``; Converts to datetime from various formats.
# ```

# TimeDelta for calculations

# In[128]:


day1 = pd.Timestamp('2020-01-01')
day1 + pd.Timedelta(1, 'D')


# Convert objects to datetime

# In[129]:


emp['hire_date'] = emp.hire_date.astype('datetime64')
emp['job_date'] = emp.job_date.astype('datetime64')

