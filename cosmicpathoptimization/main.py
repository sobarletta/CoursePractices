def average_temperature(M, temperatures):
    average_temp = sum(temperatures) // M
    return average_temp

if __name__ == "__main__":
    # Get input only when this script is run directly
    M = int(input().strip())
    temperatures = list(map(int, input().strip().split()))
    # Print the result
    print(average_temperature(M, temperatures))
