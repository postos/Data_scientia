import pandas as pd
import matplotlib.pyplot as plt 

class Runner():
    def run(args):
        # print the certification
        print('I certify that this program is my own work')
        print('and is not the work of others. I agree not')
        print('to share my solution with others.')
        print('-Paul Ostos')
        
        # read the Stock01 file using pandas
        test_data = pd.read_csv(args[0], index_col= args[1])
        
        # set the parameters for the data to be analized
        test_data02 = test_data.loc[:,args[4]:args[5]]
        date_range = test_data02.loc[args[2]:args[3]]

        # transpose the data
        date_range02 = date_range.transpose()

        # plot the data with the desired specificatoins
        date_range02.plot(figsize = (7,3), xlabel='Category', 
                            ylabel = 'Value',
                            title = 'Paul Ostos');
        plt.legend(title = 'Date', loc = 'best')
        plt.tight_layout()
        plt.show()

    #end run function
#end class Runner