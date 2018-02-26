In this simple Project, I'm going to learn & try to understand SVM better. First a bit of a discussion about SVM.

What is SVM?

Support Vector Machine( SVM ) is a binary classifier that is used to find out whether something belongs to one class
 or other but being a binary classifier doesn't mean it can only be used in cases where there are only two classes. 
 How it does that is a bit intuitive & more complex than the other supervised learning algorithms that we have come so far.
 
 Linear Regression was pretty simple & could be solved using eqn. of a straight line y = mx +b.
 
 K-nearest neigbours was also simple in that we used Euclidean distance to classify the point was closer to neighbouring classes.
 
 In Support-Vector Machines, we try to divide the dataset into repsective classes with the help of a decision boundary. In a 2-d plane,
 this decision boundary will appear as a straight line whereas in a normal n-dimensional plane, it is a hyper plane. How we get this decision boundary is 
 logically simple but mathematically tough as it requires a lot of optimizations to get the best line.
 
 Logic wise, what we do is first find support vectors ( these satisfy the eqn. yi(xi.w+b) = 1 ) Through these support vectors we 
 draw two hyper planes such that points to the right of + class & points to left of - class will be part of the respective classes. 
 
 The hyperplanes passing through the support vectors should be such that the width between them is the maximum, then we draw a hyperplane between these two
 planes which is at half the width.   
 
 SVM has some assertions which become constraints later on.
 
 SVM's training is actually an optimization problem to find the best separating line aka
 decision boundary.
 
 Each dimension is a feature & the whole collection is a featureset.
 We take a vector w that is perpendicular to the decision boundary, and then project vector u on w add some bias b to it & check to see if it is greater than  
 or less than 0 for a given class.
 
 
 
  