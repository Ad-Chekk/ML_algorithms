
# Input = [

# [1,1,-1],

# [1,-1,1],

# [-1,1,1],

# [-1,-1,-1]]

# W1 = []

# W2 = []

# b = []

# Input = [

# [1, 1, -1],

# [1, -1, 1],

# [-1, 1, 1],

# [-1, -1, -1]

# ]

# for x1, x2, y in Input:

#     W1.append(x1 * y)

#     W2.append(x2 * y)

#     b.append(y) # Update the bias

# import pandas as pd

# W1old=0

# W2old=0

# W1newl=[]

# W2newl=[]

# bnewl=[]

# for old in W1:

#     Wnew=W1old+old

#     W1newl.append(Wnew)

#     W1old=Wnew

# for old in W2:

#     Wnew=W1old+old

#     W2newl.append(Wnew)

#     W1old=Wnew

# for old in b:

#     Wnew=W1old+old

#     bnewl.append(Wnew)

#     W1old=Wnew

# data = {'W1': W1, 'W2': W2, 'b': b, 'W1new': W1newl, 'W2new': W2newl,

# 'bnew': bnewl}

# df=pd.DataFrame(data)

# print(df)



# import pandas as pd

# W1 = [1, 2, 3]

# W2 = [4, 5, 6]

# b = [7, 8, 9]

# W1newl = [10, 11, 12]

# W2newl = [13, 14, 15]

# bnewl = [16, 17, 18]

# # Creating a DataFrame

# data = {'W1': W1, 'W2': W2, 'b': b, 'W1new': W1newl, 'W2new': W2newl,

# 'bnew': bnewl}

# df = pd.DataFrame(data)

# # Displaying the DataFrame

# print("DataFrame:")

# print(df)