"""
There are numerous methods that operate on python series objects. These can broadly be
categorized into the following categories:
1. Data Manipulation
2. Aggregation and Summary Statistics
3. Filtering and Selection
4. Missing Data Handling
5. Miscellaneous

Each of these categories can further be divided into sub categories. We will cover all the
methods listed under each of these sub categories. Few of these methods have already been
covered in the previous modules in details and will only get a mention in this module.
"""
import pandas as pd

#   DATA MANIPULATION:
# 1. Arithmetic Operations:
"""
The methods listed under arithmetic operations are as follows:
add(): Perform element-wise addition.
sub(): Perform element-wise subtraction.
mul(): Perform element-wise multiplication.
div(): Perform element-wise division.

Element wise operation means 2 series containing the same number of elements. The operations
are performed on the values at the same positions. Please refer to the below code:
"""
print("#" * 95)
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Perform element-wise addition
result_add = s1.add(s2)
print("Addition result:")
print(result_add)

# Perform element-wise subtraction
result_sub = s1.sub(s2)
print("\nSubtraction result:")
print(result_sub)

# Perform element-wise multiplication
result_mul = s1.mul(s2)
print("\nMultiplication result:")
print(result_mul)

# Perform element-wise division
result_div = s1.div(s2)
print("\nDivision result:")
print(result_div)

# 2. String Operations:
"""
The methods listed under string operations are as follows:
str.upper(): Convert strings to uppercase.
str.lower(): Convert strings to lowercase.
str.contains(): Check if strings contain a substring. Returns a series containing boolean 
                value for comparison with each element in the series.
str.replace(): Replace substrings in strings.

The above methods carry out their operations on each element in the series. Please refer to 
the below code illustrations:
"""
print("#" * 95)
s = pd.Series(['apple', 'banana', 'orange'])

# Convert strings to uppercase
result_upper = s.str.upper()
print("Uppercase strings:")
print(result_upper)

# Convert strings to lowercase
result_lower = s.str.lower()
print("\nLowercase strings:")
print(result_lower)

# Check if strings contain a substring
result_contains = s.str.contains('an')
print("\nStrings containing 'an':")
print(result_contains)

# Replace substrings in strings
result_replace = s.str.replace('a', 'x')
print("\nStrings with 'a' replaced by 'x':")
print(result_replace)

# 3. Element-wise Functions:
"""
These methods apply functions to each element in the series. The methods listed under this 
category are as follows:
apply(): Apply a function to each element. We have already used and discussed this function 
        in the previous module. Hence, we will be skipping it here.
map(): Map values of Series using input correspondence.
transform(): Call function producing a like-indexed Series on each group.
Please refer to the below code:
"""
print("#" * 95)
s = pd.Series([1, 2, 3])

# Map values of Series using input correspondence
result_map = s.map({1: 'one', 2: 'two', 3: 'three'})
print("\nMap values:")
print(result_map)


def double(x):
    return x * 2


# Using map() to double each element
doubled_series = s.map(double)
print("\nDoubled Series (using map()):")
print(doubled_series)

# Using transform() to double each element
doubled_series_transformed = s.transform(double)
print("\nDoubled Series (using transform()):")
print(doubled_series_transformed)

# 4. Sorting:
"""
The methods listed under this category are as follows:
sort_values(): Sort the Series by values.
sort_index(): Sort the Series by index.
The descriptions are pretty self explanatory. Lets delve into the code:
"""
print("#" * 95)
s = pd.Series([3, 1, 2], index=['b', 'a', 'c'])

# Sort the Series by values
result_sort_values = s.sort_values()
print("Sort by values:")
print(result_sort_values)

# Sort the Series by index
result_sort_index = s.sort_index()
print("\nSort by index:")
print(result_sort_index)

###############################################################################################
#   AGGREGATION AND SUMMARY STATISTICS:
# 1. Aggregation:
"""
The methods that come under this sub category are as follows:
sum(): Compute the sum of all elements.
product(): Compute the product of all elements.
mean(): Compute the mean of all elements.
median(): Compute the median of all elements.
min(): Compute the minimum value.
max(): Compute the maximum value.
count(): Count non-NA/null observations.
value_counts(): Counts the number of unique values in series. 'NaN' values are excluded by 
                default. This method is specific only for pandas Series objects.

The description of the individual methods mentioned above is pretty self explanatory. Lets 
use them in code. Please refer below:
"""
print("#" * 95)
s = pd.Series([1, 2, 3, 4, 5])

# Compute the sum
result_sum = s.sum()
print("Sum:", result_sum)

# Compute the product
result_product = s.product()
print("Product:", result_product)

# Compute the mean
result_mean = s.mean()
print("Mean:", result_mean)

# Compute the median
result_median = s.median()
print("Median:", result_median)

# Compute the minimum value
result_min = s.min()
print("Minimum value:", result_min)

# Compute the maximum value
result_max = s.max()
print("Maximum value:", result_max)

# Count non-NA/null observations
result_count = s.count()
print("Count:", result_count)

# Count occurence of individual values:
s = pd.Series([1, 2, 2, None, 4, 4, None])
value_freq = s.value_counts()
print(value_freq)
value_freq_percent = s.value_counts(normalize=True)
print(value_freq_percent)
value_freq_des = s.value_counts(ascending=True)
print(value_freq_des)
value_freq_na = s.value_counts(dropna=False)
print(value_freq_na)

# 2. Descriptive Statistics:
"""
The methods that fall under this sub category are as follows:
describe(): provides a summary of descriptive statistics for the data in a Series. 
            It computes various statistics such as count, mean, standard deviation, minimum, 
            maximum, and percentiles.
quantile(): calculates the specified quantile(s) of the data in the Series. A quantile is a 
            value below which a certain proportion of data falls.
value_counts(): Count unique values.
"""
print("#" * 95)
s = pd.Series([1, 2, 3, 4, 5])

# Generate descriptive statistics
result_describe = s.describe()
print("Descriptive statistics:")
print(result_describe)

# Compute the 25th percentile
result_quantile = s.quantile(0.25)
print("\n25th percentile:", result_quantile)

# Count unique values
result_value_counts = s.value_counts()
print("\nValue counts:")
print(result_value_counts)

###############################################################################################
#   FILTERING AND SELECTION:
# 1. Boolean Indexing:
"""
Boolean indexing deals with functions like '.loc[]', '.iloc[]', '.at[]' and '.iat[]'. The 
operations of these methods have been discussed extensively and in details in the previous 
module. Hence, it is skipped in this module.
"""

###############################################################################################
#   FILLING MISSING DATA:
# 1. Filling Missing Values:
"""
These methods replace NaN (Not a Number) values with specified values in a series. The 
methods listed under this category are:
fillna(): method used to fill missing values in a Series with a specified scalar value or 
        using interpolation methods.
ffill(): method used to fill missing values in a Series using forward fill, i.e., propagate 
        the last valid observation forward to fill missing values.
bfill():  method used to fill missing values in a Series using backward fill, i.e., propagate 
        the next valid observation backward to fill missing values.
Please refer to the below code illustrations.
"""
print("#" * 95)
s = pd.Series([1, None, 3, None, 5])

# Fill missing values with a specified value (0)
filled_values = s.fillna(0)
print("Filled with 0:\n", filled_values)

# Fill missing values using forward fill
ffill_values = s.ffill()
print("\nForward filled:\n", ffill_values)

# Fill missing values using backward fill
bfill_values = s.bfill()
print("\nBackward filled:\n", bfill_values)

# 2. Dropping Missing Values:
"""
Only one method exists in this category. That is the dropna() method. The dropna() method 
has been covered in the previous module and has been discussed detailly. Hence, we will skip
it here in order to avoid redundancy.
"""
###############################################################################################
#   MISCELLANEOUS:
# 1.  Append and Concatenate:
"""
These are methods for appending or concatenating multiple Series objects. Only one working 
method is listed under this category. The pd.concat() method has been discussed in the 
previous module in great details. Hence, we will skip it in this module to avoid redundancy.
"""
# 2. Data Type Conversion:
"""
Only one method is listed under this category. The astype() method is used to convert the 
data types of elements present in the series. Please refer to the following example:
"""
print("#" * 95)
s = pd.Series(['1', '2', '3'])

# Convert string values to integers
converted_series = s.astype(int)
print("Converted Series:")
print(converted_series)

# 3. Copying and Views:
"""
The methods listed under this category are as follows:
copy(): Create a deep copy of the Series.
view(): Create a view of the Series.
Please refer to the below code illustrations:
"""
print("#" * 95)
s = pd.Series([1, 2, 3])

# Create a deep copy of the Series
copied_series = s.copy()
print("Copied Series:")
print(copied_series)

# Create a view of the Series
viewed_series = s.view()
print("\nViewed Series:")
print(viewed_series)

# 4. Duplicates Handling:
"""
These methods aim to identify and remove duplicate values from a series. The methods listed 
under this category are:
drop_duplicates(): Remove duplicate values from the Series.
duplicated(): Indicates duplicate values in the Series.

Please refer to the below code illustrations:
"""
print("#" * 95)
s = pd.Series([1, 2, 2, 3, 3, 3])

# Check for duplicate values
duplicated_values = s.duplicated()
print("Duplicated Values:")
print(duplicated_values)

# Remove duplicate values
deduplicated_series = s.drop_duplicates()
print("Deduplicated Series:")
print(deduplicated_series)

###############################################################################################
"""
This concludes the module. We have managed to list most of the methods that can be used to 
carry out operations on pandas series.
"""
