import math
# All decimal 3 places

def check(listx):
    for i in listx:
        if isinstance(i, str):
            return 1
    return 0

# Function to compute mean
def mean(first_list):
    # mean Logic 
    if check(first_list):
        return 0
    count = 0
    for i in first_list:
        count = count + 1
    mean_value = summation(first_list) / count
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    if check(first_list):
        return 0
    # median Logic
    sorted_list = sorting(first_list)
    n = len(sorted_list)
    if n%2 == 0:
        median_value = (sorted_list[int(n/2)] + sorted_list[int(n/2)-1]) /2
    else:
        median_value = sorted_list[int(n/2)]
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    if check(first_list):
        return 0
    # Standard deviation Logic
    standard_deviation_value = math.sqrt(variance(first_list))
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    if check(first_list):
        return 0
    # variance Logic
    count = 0
    mean1 = mean(first_list)
    variance_value = 0
    for i in first_list:
        variance_value = variance_value + (i - mean1) * (i - mean1)
        count = count + 1
    variance_value = variance_value / count
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if check(first_list) | check(second_list):
        return 0
    rmse_value = math.sqrt(mse(first_list, second_list))
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if check(first_list) | check(second_list):
        return 0
    count = 0
    mse_value = 0
    for i in first_list:
        mse_value = mse_value + (first_list[count] - second_list[count])*(first_list[count] - second_list[count])
        count = count + 1
    mse_value = mse_value / count
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if check(first_list) | check(second_list):
        return 0
    mae_value = 0
    count = 0
    for i in first_list:
        mae_value = mae_value + abs(first_list[count] - second_list[count])
        count = count + 1
    mae_value = mae_value / count
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if check(first_list) | check(second_list):
        return 0
    mean1 = mean(first_list)
    den = 0
    count = 0
    for i in first_list:
        den = den + (i - mean1)*(i - mean1)
        count = count + 1
    num = count * mse(first_list, second_list)
    nse_value = 1 - (num/den)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if check(first_list) | check(second_list):
        return 0
    pcc_value = 0
    num = 0
    temp1 = 0
    temp2 = 0
    count = 0
    mean1 = mean(first_list)
    mean2 = mean(second_list)
    for i in first_list:
        num = num + (first_list[count] - mean1) * (second_list[count] - mean2)
        temp1 = temp1 + (first_list[count] - mean1) * (first_list[count] - mean1)
        temp2 = temp2 + (second_list[count] - mean2) * (second_list[count] - mean2)
        count = count + 1
    den = math.sqrt(temp1) * math.sqrt(temp2)
    pcc_value = num/den
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    if check(first_list):
        return 0
    # Skewness Logic
    skewness_value = 0
    return skewness_value
    
def sorting(first_list):
    if check(first_list):
        return 0
    # Sorting Logic
    count = 0
    sorted_list = []
    for i in first_list:
        sorted_list.append(i)
        count = count + 1
    n = len(sorted_list)
    for i in sorted_list:
        for j in range(0, n-1-1):
             if sorted_list[j] > sorted_list[j+1]:
                 sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    if check(first_list):
        return 0
    # Kurtosis Logic
    kurtosis_value = 0
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    if check(first_list):
        return 0
    # sum Logic
    summation_value = 0
    for i in first_list:
        summation_value = summation_value + i
    return summation_value
