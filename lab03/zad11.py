import statistics

def basic_statistics(numbers):
    if not numbers:
        return None
    
    stats = {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0 
    }
    
    return stats

numbers = [10, 20, 30, 40, 50]
print(basic_statistics(numbers))
