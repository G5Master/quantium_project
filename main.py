#Author KS Ngobeni
from file_handler import SoulFileHandler

#Create an instance of a SoulFoodFileHandler
handler=SoulFileHandler()

#Create the file paths to read from.
path0="./data/daily_sales_data_0.csv"
path1="./data/daily_sales_data_1.csv"
path2="./data/daily_sales_data_2.csv"

#read pink morsel data from the above given file paths
handler.read_pink_morsel(path0)
handler.read_pink_morsel(path1)
handler.read_pink_morsel(path2)

#Now write final pink morsel data to the following specified file
handler.write_pink_morsel("./data/output_file.csv")