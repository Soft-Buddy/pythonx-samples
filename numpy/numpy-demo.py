import numpy as np

def main():
    # Creating arrays
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([6, 7, 8, 9, 10])
    array3 = np.linspace(0, 1, 5)

    # Basic operations
    sum_array = np.sum(array1)
    mean_array = np.mean(array2)
    max_value = np.max(array3)

    # Reshaping arrays
    reshaped_array = np.reshape(array2, (1, 5))

    # Transposing arrays
    transposed_array = np.transpose(reshaped_array)

    # Element-wise operations
    squared_array = np.square(array1)
    sin_array = np.sin(array2)

    # Statistical operations
    std_deviation = np.std(array1)
    correlation_coefficient = np.corrcoef(array1, array2)[0, 1]

    # Random number generation
    random_array = np.random.rand(3, 3)

    # Linear algebra operations
    eigenvalues, eigenvectors = np.linalg.eig(random_array)

    # Indexing and slicing
    sliced_array = array2[2:6]

    # Masking
    mask = array1 > 2
    masked_array = array1[mask]

    # Concatenation
    concatenated_array = np.concatenate((array1, array2))

    # Stacking
    stacked_array = np.stack((array1, array2))

    # Save and load arrays
    np.save('saved_array.npy', array1)
    loaded_array = np.load('saved_array.npy')

    # Display results
    print("Original Array 1:", array1)
    print("Sum of Array 1:", sum_array)
    print("Mean of Array 2:", mean_array)
    print("Max value of Array 3:", max_value)
    print("Reshaped Array 2:", reshaped_array)
    print("Transposed Reshaped Array:", transposed_array)
    print("Squared Array 1:", squared_array)
    print("Sine of Array 2:", sin_array)
    print("Standard Deviation of Array 1:", std_deviation)
    print("Correlation Coefficient Matrix:", correlation_coefficient)
    print("Random Array:", random_array)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
    print("Sliced Array 2:", sliced_array)
    print("Masked Array 1:", masked_array)
    print("Concatenated Arrays:", concatenated_array)
    print("Stacked Arrays:", stacked_array)
    print("Loaded Array:", loaded_array)

if __name__ == "__main__":
    main()
