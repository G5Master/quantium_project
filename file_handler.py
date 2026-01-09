#Author KS Ngobeni

import os.path
import re


#Class which deals with file handling for the SoulFood restaurant
class SoulFileHandler:

      #Default Constructor
      def __init__(self):
          #Initialize instance variables
          self.pinkMorsels=[]
          self.soulArray=[]

      #Method which processes pink morsel lines into the pinkMorsel list
      def read_pink_morsel(self,path):

         try:
            #Create a file reader
            with open(path,'r') as file_reader:
                  print("Processing pink morsels")
                  #Traverse the given file
                  for line in file_reader:
                        #Tokenize each line
                        tokenizer=line.split(",")
                        token1=tokenizer[0]
                        if token1.__eq__("pink morsel"):
                            print(line)
                            self.pinkMorsels.append(line)

         except Exception as e:
                print(e)

         print("Processing pink morsels complete.")

      #Method to write pink morsel content to a specified file
      def write_pink_morsel(self,path):
            try:
              print("Writing pink morsel content.")

              with open(path,"w") as file_writer:
                  # Write the column fields if the file to write to is empty
                    if os.path.getsize(path) == 0:
                        file_writer.write("sales,date,region\n")

                      #Traverse the pink morsel array
                    for i in range(len(self.pinkMorsels)):

                        #Tokenize each pink morsel row
                        tokenizer=re.split(r'[$,]+',self.pinkMorsels[i])
                        print(tokenizer)
                        #Process the price which is the second token
                        print(tokenizer[1])
                        price_str=tokenizer[1]
                        price=float(price_str)
                        print("Works3")

                        #Process the quantity which is the third token
                        quantity_str=tokenizer[2]
                        quantity=int(quantity_str)

                        #compute total sales for each pink morsel
                        sales=price*quantity

                        #Convert sales into a string
                        sales_str="$"+str(sales)

                        #Save the date of the current pink morsel into a local variable
                        date=tokenizer[3]

                        #Now process the region of the current pink morsel into a local variable
                        region=tokenizer[4]

                        #Process a line
                        delim=","
                        line=sales_str+delim+date+delim+region

                        #write each line into the desired file
                        file_writer.write(line)
                        print(line)

            except Exception as e:
                    print(e)

            print("Writing pink morsel data complete.")