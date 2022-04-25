# Financial_Ratio_Analysis
Analysis of a company and its relevant financial ratio's versus the industry averages and companies previous results.

Summary:

This program works with multiple functions starting with financial statements stored in CSV files with standardized tags, like Revenue and Net Income, and turns
them into multiple dictionaries containing computed financial ratios for 2020 and 2019. Dictionaries were super helpful, because of the key-value relationship 
that I used often in this code. Once the ratios are stored in a dictionary the 4 companies’ ratios in the chosen industry, big tech, are combined to make an 
industry average for 2020 and 2019. Now based on user input a company is chosen, financial ratios of the chosen companies are displayed and a firm score is 
developed with a recommendation on whether or not the company chosen is a good investment.

Functions in the Program & other commands: 

First, a function opens a CSV file and turns it into a list of lines, returning this list of lines. This function is called for each company. 
The function is called openRead(fileName), and takes in the file’s name.
Then all dictionaries and needed variables are initialized, and the above function is called for each firm.
Second, a new function takes the read file and splits each line into its own list. Taking each line and using it to create 2 dictionaries for each firm, 
with financial information for 2020 and 2019, ie. Revenue: $$$$. All firms are run with this function, called filetoDict(filename, dict, dict1), and the
dictionaries are returned. Ie.. Google2020 or Apple2019.
Now that each firm has a dictionary created for 2020 and 2019 financial information it was time to create a function to calculate the financial ratios for each 
company for each year. I used another function to complete this task giving it 2 inputs, an inDictionary made up of the financial information of the firm and 
an outDictionary to assign the newly created ratios to. Because I standardized the keys for the financial information of these companies, I was able to write 
one function to work for all 4 companies. All 4 companies were ran through this function for 2020 and 2019 with 8 new dictionaries created, ie. AppleRatio20 
and AppleRatio19. 
Now that all the dictionaries for each company were created, it was time to calculate the industry averages for each year, 2019 and 2020. I used a new function 
with a for loop to create this average by looping through a ratio dictionary and averaging each ratio by adding them together and dividing by 4. Two for loops 
were run in this function creating an industry average for each ratio in 2020 and 2019.
Now that I had my ratios for each company and an industry average for each year, I was ready for my final function, ratio analysis. This function takes in a 
company name and based on the chosen name imports the corresponding dictionaries for 2020 and 2019. Then it takes each key in the dictionary and compares 
ratios for 2020 to 2019, adding a point to firmscore for each ratio that improved from 2019 to 2020. Then it compares the chosen company’s ratios from 2020 to 
the industry average for 2020, adding a point to firmscore each time a companies ratio is greater than the industry average. 
It repeats this same process for 2019 ratios as well. 
Then this function prints the chosen companies financial ratios for 2020 and 2019 as well as quantifying the firmscore and giving a recommendation based on the firm score.

While loop and user input:

Now that all the functions are made and working well it was time to make this code interact with the user. To do this I created a while loop with professor 
Rosen’s patented done = false stating condition. 
This loop asks the user to input a company name out of the list of choices: Apple, Microsoft, Google, and IBM. If the user does not enter one of these names, 
they are prompted again with a nested while loop until one of the companies is chosen, it is not case sensitive. 
Then it runs the financialAnalysis function on the selected company. Then it askes the user if it wants to try another company, and ask the user to 
input Y or Yes for yes, and will continue to repeat until the user enters any other input than y or yes, also not case sensitive.
Finally, my code displays a goodbye message to thank the user.

Problems and Issues:

The problems I had with this project were mostly related to the input files having the Exact same keys, and changes in the keys would completely break the 
code because the dictionary keys need to be identical to run my financial analysis and create the relevant ratios. This is what stopped me from being able to
pull live data from the online, because companies use different tags for their information, like Net sales instead of Revenue, and a multitude of other 
examples. So, I had to go through the 4 files I chose and standardize them, as well as remove all commas as that is how python spits the data. Once the 
files where prepared it was just thinking critically about what I wanted to do and playing with the code till it worked as intended.

Conclusion:

Overall, I am happy with the outcome of this project. I can use and add to this code in the future to automate ration analysis for me. 
I can now take a group of any company’s financial statements, prepare the files, compute all the relevant ratios and compare them to each other
to make sound investment decisions. The ability to group any companies I chose into an industry and create industry averages will also prove useful 
in the future. As a graduating accounting major, this will be a useful program that I add to for years to come and will allow me to showcase 
my tech skills at my new job this june. 
