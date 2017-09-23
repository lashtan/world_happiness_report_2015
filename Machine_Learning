#### MACHINE LEARNING ####
print("Happy Dimensions:\nLength, Columns\n", happy.shape)
print("Let's use", int(.75*158),"observations for the training set")
print("Let's use", int(.25*158+1), "observations for the test set") 

# new df with just the 6 explan variables and the response (score)
df=happy.iloc[:, 3:11]
del df['std_err']

train, test = train_test_split(df, test_size = 0.25, random_state = 7) #set random seed

# Create training test
x_train = train.loc[:, train.columns != 'score'] #explanatory variables training set
y_train = train.loc[:, train.columns == 'score'] #also called target, response, or classification set

# Create test set 
x_test = test.loc[:, test.columns != 'score']
y_test = test.loc[:, test.columns == 'score'] 

regr = linear_model.LinearRegression() # Create linear reg object
regr.fit(x_train, y_train) # Train the model 
y_pred = regr.predict(x_test) # Make predictions 

# turn everything into arrays
x_train_a=x_train.values
x_test_a=x_test.values
y_train_a=x_train.values
y_test_a=x_test.values

# re-fit
regr = linear_model.LinearRegression() # Create linear reg object
regr.fit(x_train_a, y_train_a) # Train the model 
y_pred_a = regr.predict(x_test_a) # Make predictions 

#coefficients, mean squared error, explained variance (r^2)
print('Coefficients: \n', regr.coef_)
print("MSE: %.2f" 
      % mean_squared_error(y_test_a, y_pred_a))
print('Variance score: %.2f' 
      % r2_score(y_test_a, y_pred_a))

# got a MSE of 0 and R^2 of 1, so clearly something failed...

#plot
plt.scatter(x_test_a, y_test_a,  color='black')
plt.plot(x_test_a, y_pred_a, color='blue', linewidth=3)
plt.show()  
