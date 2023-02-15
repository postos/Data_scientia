import pandas as pd
import matplotlib.pyplot as plt 

class Runner():
    def run(args):
        # print certification 
        print('I certify that this program is my own work\n'
            'and is not the work of others. I agree not\n'
            'to share my solution with others.\n'
            '-Paul Ostos') 

        # read in the Stock01.csv file and set the column index 
        test_data = pd.read_csv(args[0], index_col= (args[1]))

        # create a new dataframe with the data from "test_data" and set
        test_data01 = pd.DataFrame(test_data)

        # the perameters to be observed 
        test_data02 = test_data01.loc[:, args[4]: args[5]] #slice it like pizza
        date_range = test_data02.loc[args[2]: args[3]]
        
        # plot the grid with the specified labels  
        date_range.plot(figsize=(7,3), grid =  True,
                                title = 'Paul Ostos',
                                xlabel = 'Date',
                                ylabel = 'PRICE');

        plt.locator_params(axis = 'x', nbins = 5) 
        plt.tight_layout()
        plt.savefig('Proj09.jpg')
        plt.show()

    # end run function
# end class Runner


