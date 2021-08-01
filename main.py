# Program by Carson Bring 7.31.21
""" After spending too much time shitposting on /biz/'s Stock Market general, I decided that it would benefit me to get
my stock information from a program so that I would stop wasting some time.

This program gets all of the messages from the current Stock Market General thread on /biz/ and updates with new tickers
whenever a thread hits post limit. If you are just curious as to what tickers are being talked about the most at a
moment in time, just run the program and stop it, otherwise it will continue to update if you just leave it on.

Had to make a couple of edits to the basc_py4chan library (what I used to get the message and thread info from /biz/) to
get it working with Python 3.9, so I've included the updated file that would need to be replaced after pip installing
py4chan.

Organization might not be perfect. I'll try to make up for it with comments
"""
import time
import stocksClass
import basc_py4chan


# This function makes it easier to read the information that is found in the 4chan messages that are read in

def reformatMessage(chanmessage):
    newmessage = ''
    if chanmessage != '':
        if chanmessage[0] == '>' and chanmessage[1] == '>':
            newmessage = chanmessage[10:]
        else:
            newmessage = ' ' + chanmessage
    newmessage = newmessage + ' '
    return newmessage


# setting up all of my lists and variables for the program

FullTickerList = []
FullNumberList = [0]
sortedFullTickerList = []
sortedFullNumberList = []
threadtickers = []
numOfTimesMentioned = []
sortedNumberList = []
sortedTickerList = []
counter = 0
previoussmg = ''

"""
This is a list of common words that happen to be capitalized but aren't usually tickers except for BABA and POWW, 
currently those tickers cause a bug for some reason, will probably fix in future. Add and remove from this list to your
heart's content """
nottickers = ['YOU', 'AM', 'TA', 'A', 'IS', 'NOW', 'OUT', 'SO', 'ON', 'G', 'M', 'NYC', 'FOR', 'ALL', 'SAFE', 'MSM',
              'TECH', 'BE', 'SON', 'ATH', 'MA', 'DIS', 'WIT', 'BABA', 'POWW', 'TQQQ']
FirstRun = False


# This function does all of the heavy lifting when it comes to finding the tickers from the thread
def find_tickers():

    # for this section i'm using all of the of the py4chan stuff ot get the messages from smg
    biz = basc_py4chan.Board('biz')
    allthreads = biz.get_all_threads()
    global previoussmg, FirstRun, FullTickerList, FullNumberList, sortedFullNumberList, sortedFullTickerList
    for thread in allthreads:

        if 'smg' in str(thread.topic.subject):
            smgthread = thread
            break

    smgposts = smgthread.all_posts

    # deciding on each call whether the program should grab new tickers from the messages or not
    if smgthread.bumplimit == True and smgthread != previoussmg or smgthread.bumplimit == True and FirstRun == True or counter == 0:

        """since the program runs the first time even if the thread is not at post limit, the program needs to make sure
        to clear out the existing values in the lists to make room for the accurate ones. After the first run this
        is fine though because the program will only grab new tickers and enter this part of the code when the thread
        is at post limit."""
        if FirstRun:
            FullTickerList = []
            FullNumberList = []
            sortedFullNumberList = []
            sortedFullTickerList = []

        # sets the a variable to true so that on next run it will activate the last block of code
        if counter == 0:
            FirstRun = True

        # this for loop gets the strings from each message and finds out if there is a ticker in each one.
        for post in smgposts:
            message = post.text_comment
            message = str(message)
            message = reformatMessage(message)
            for index, symbol in enumerate(stocksClass.Stocks.Symbols):
                isTicker = True
                capitalSymbol = str(symbol)
                capitalSymbol = capitalSymbol.upper()
                if f' {capitalSymbol} ' in message or message.endswith(capitalSymbol) is True or message.startswith(
                        capitalSymbol) is True or message.startswith(f'>{capitalSymbol} ') is True or message.endswith(
                    f' {capitalSymbol}.') is True:

                    for notticker in nottickers:
                        if notticker == capitalSymbol:
                            isTicker = False

                    if isTicker is True:
                        isExisting = False
                        for index, ticker in enumerate(threadtickers):
                            if ticker == symbol:
                                numOfTimesMentioned[index] = numOfTimesMentioned[index] + 1
                                isExisting = True
                        if isExisting is False:
                            threadtickers.append(symbol)
                            numOfTimesMentioned.append(1)

        # sorting the tickers in the temporary list (not the full one)
        largest = 0
        indexoflargest = 0
        tickeroflargest = ''

        for j in range(len(numOfTimesMentioned)):
            largest = 0
            for i in range(len(numOfTimesMentioned)):
                if numOfTimesMentioned[i] > largest:
                    largest = numOfTimesMentioned[i]
                    indexoflargest = i
                    tickeroflargest = threadtickers[i]
                    if i == len(numOfTimesMentioned) - 1:
                        indexoflargest = 0

            numOfTimesMentioned.pop(indexoflargest)
            threadtickers.pop(indexoflargest)
            sortedNumberList.append(largest)
            sortedTickerList.append(tickeroflargest)
        previoussmg = smgthread

    print('-----------------------------------< /smg/ ticker mentions >------------------------------------------')

# this is the part of the program that makes it so that the program will run over and over again.
inList = False
indexoffullticker = ''
if __name__ == '__main__':
    while True:

        find_tickers()

        counter = counter + 1
        # checking to see if the full ticker list has any of the tickers in the temporary list and adds to the full one
        if len(FullTickerList) != 0:
            for indx, ticker in enumerate(sortedTickerList):

                inList = False
                for index3, fullticker in enumerate(FullTickerList):
                    if ticker == fullticker:
                        indexoffullticker = index3

                        inList = True

                if inList:

                    FullNumberList[indexoffullticker] = FullNumberList[indexoffullticker] + sortedNumberList[indx]
                    inList = False
                else:
                    FullTickerList.append(ticker)
                    FullNumberList.append(sortedNumberList[indx])



        else:

            FullTickerList = sortedTickerList
            FullNumberList = sortedNumberList
            sortedTickerList = []
            sortedNumberList = []

        # sorting again
        largest = 0
        indexoflargest = 0
        tickeroflargest = 'hi'
        largest = 0
        isSorted = False
        for j in range(0, len(FullNumberList)):

            largest = 0

            for i in range(0, len(FullNumberList)):
                if FullNumberList[i] > largest:
                    largest = FullNumberList[i]
                    indexoflargest = i
                    tickeroflargest = FullTickerList[i]



            FullNumberList.pop(indexoflargest)
            FullTickerList.pop(indexoflargest)
            sortedFullNumberList.append(largest)
            sortedFullTickerList.append(tickeroflargest)

            tickeroflargest = ''

        stockname = ''
        stocknumber = ''
        for index, ticker in enumerate(sortedFullTickerList):
            if sortedFullNumberList[index] < sortedFullNumberList[-1]:
                stocknumber = sortedFullNumberList[-1]
                stockname = sortedFullTickerList[-1]
                sortedFullTickerList.pop(-1)
                sortedFullNumberList.pop(-1)
                sortedFullTickerList.insert(index, stockname)
                sortedFullNumberList.insert(index, stocknumber)

        sortedNumberList = []
        sortedTickerList = []


        FullNumberList = sortedFullNumberList
        FullTickerList = sortedFullTickerList

        for index, number in enumerate(sortedFullNumberList):
            print(f'{sortedFullTickerList[index]}: {number}')
        print(counter)
        # this can be changed here to what you want it to be.
        print(f'Waiting 1 minute...')
        time.sleep(60)
