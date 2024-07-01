# predicting_winners
So far, this repository is essetially functions a sandbox for me to learn the basics of machine learning, specificlly though the lens of tensorflow.
My first task was to model a sin function using a neural network. I realized very quickly that I didnt have a strong enough understanding of the topic to complete this task - so I turned to internet resorces to start learning. After around a day of watching youtube videos on everything from linear algebra to specific syntax of tensorflow, I was able to start building my model.
Building the model took a signifigantly smaller amount of time than I expected, and the code turned out to be less than 50 lines total - much shorter than I originally anticipated. Training the model took a little more time to figure out, but once again was fairly easy. Below are some of my main takeaways from the entire process:
1: Always enusre data is clean and formatted in a way that makes sense before importing. Many of my headaches came about from not having clean data - or not using the proper software to clean said data.
2: When training a model, messing around with the number of layers/nodes can be helpful in increasing accuracy, but the more effective way to do so is to increase the number of epochs, and properlly adjust batch size of each training set. 
3: Always have the "verbose" setting equal to 2 to get the most information about each training set.
4: The import statements are going to come up as errors for some reason, but they still work. Simply ignore the red squiggles. If you change the imports to try to fix the errors, the import statements do not work - and they become actual errors.

Some things I would like to learn more about:
1: I would like to understand loss functions better, specifficly why one would choose a certain loss function over another, and what the mathmatical differces between the two are.
2: I need to transition to using plotly for my graphs. Currently I am using matplotlib, which is fine, but produces ugly graphs.
3: I would like to understand better how to pick an effective number of layers and nodes for any given model.
