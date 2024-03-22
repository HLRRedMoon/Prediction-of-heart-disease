# import pandas as pd
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = {'Column1': [1, 2, 3, 4, 5],
#         'Column2': ['A', 'B', 'C', 'D', 'E']}
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Iterate through selected columns and delete random values
# columns_to_delete = ['Column1', 'Column2']

# for column in columns_to_delete:
#     # Calculate the number of values to delete
#     num_values_to_delete = int(len(df) * (percentage_to_delete / 100))
    
#     # Generate random indices to delete
#     indices_to_delete = random.sample(range(len(df)), num_values_to_delete)
    
#     # Set randomly selected values to None
#     df.loc[indices_to_delete, column] = None

# # Print the modified DataFrame
# print(df)


# import pandas as pd
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to None
# flat_values[indices_to_delete] = None

# # Reshape the modified array back to the original shape
# modified_data = flat_values.reshape(df.shape)

# # Create a new DataFrame with the modified data
# df_modified = pd.DataFrame(modified_data)

# # Print the modified DataFrame
# print(df_modified)


# import pandas as pd
# import numpy as np
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to numpy.nan
# flat_values[indices_to_delete] = np.nan

# # Reshape the modified array back to the original shape
# modified_data = flat_values.reshape(df.shape)

# # Create a new DataFrame with the modified data
# df_modified = pd.DataFrame(modified_data)

# # Convert the DataFrame to numeric type to handle nan values
# df_modified = df_modified.apply(pd.to_numeric, errors='coerce')

# # Print the modified DataFrame
# print(df_modified)


# import pandas as pd
# import numpy as np
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to numpy.nan
# flat_values[indices_to_delete] = np.nan

# # Reshape the modified array back to the original shape
# modified_data = flat_values.reshape(df.shape)

# # Create a new DataFrame with the modified data
# df_modified = pd.DataFrame(modified_data)

# # Convert NaN values back to integer type
# df_modified = df_modified.applymap(lambda x: int(x) if pd.notna(x) else x)

# # Print the modified DataFrame
# print(df_modified)


# import pandas as pd
# import numpy as np
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to numpy.nan
# flat_values[indices_to_delete] = np.nan

# # Reshape the modified array back to the original shape
# modified_data = flat_values.reshape(df.shape)

# # Create a new DataFrame with the modified data
# df_modified = pd.DataFrame(modified_data)

# # Fill NaN values with a specific integer (e.g., -1)
# df_modified = df_modified.fillna(-1).astype(int)

# # Print the modified DataFrame
# print(df_modified)


# import pandas as pd
# import numpy as np
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1.2, 2.3, 3.8], [4.1, 5.9, 6.7], [7.2, 8.6, 9.8]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to numpy.nan
# flat_values[indices_to_delete] = np.nan

# # Replace NaN values with a specific integer (e.g., -1) and convert to integer type
# df_modified = pd.DataFrame(np.nan_to_num(flat_values, nan=-1).astype(int).reshape(df.shape))

# # Print the modified DataFrame
# print(df_modified)


# import pandas as pd
# import numpy as np
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to numpy.nan
# flat_values[indices_to_delete] = np.nan

# # Fill NaN values with a specific integer (e.g., -1)
# flat_values = np.nan_to_num(flat_values, nan=-1).astype(int)

# # Reshape the modified array back to the original shape
# modified_data = flat_values.reshape(df.shape)

# # Create a new DataFrame with the modified data
# df_modified = pd.DataFrame(modified_data)

# # Print the modified DataFrame
# print(df_modified)


# import pandas as pd
# import numpy as np
# import random

# # Create a sample DataFrame (replace this with your actual DataFrame)
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# df = pd.DataFrame(data)

# # Specify the percentage of values to delete (e.g., 20%)
# percentage_to_delete = 20

# # Calculate the number of values to delete
# num_values_to_delete = int(df.size * (percentage_to_delete / 100))

# # Flatten the DataFrame to a 1D array
# flat_values = df.values.flatten()

# # Generate random indices to delete
# indices_to_delete = random.sample(range(len(flat_values)), num_values_to_delete)

# # Set randomly selected values to numpy.nan
# flat_values[indices_to_delete] = np.nan

# # Replace NaN values with a specific integer (e.g., -1)
# df_modified = pd.DataFrame(np.where(np.isnan(flat_values), -1, flat_values).reshape(df.shape).astype(int))

# # Print the modified DataFrame
# print(df_modified)


x=5
y= int(input("enter a number please : "))
result = x * y 
print(result)
