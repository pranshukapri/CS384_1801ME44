import math
# All decimal 3 places

# Function to compute mean
def mean(first_list):
    # mean Logic 
    count = 0
    for i in first_list:
        count = count + 1
    mean_value = summation(first_list) / count
    return round(mean_value,3)


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    rmse_value = math.sqrt(mse(first_list, second_list))
    return round(rmse_value,3)


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    count = 0
    mse_value = 0
    for i in first_list:
        mse_value = mse_value + (first_list[count] - second_list[count])*(first_list[count] - second_list[count])
        count = count + 1
    mse_value = mse_value / count
    return round(mse_value,3)


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for i in first_list:
        summation_value = summation_value + i
    return round(summation_value,3)
