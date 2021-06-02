# Chapter 1

## The Machine Learning Landscape

### Exercises

1. **How would you define Machine Learning?**
 
   Machine Learning is the process of learning from data. Specifically, an ML
   process is any task where data used as an input to process improves the
   performance of said task.

2. **Can you name four types of problems where it shines?**

   1. Problems where existing solutions require a lot of fine tuning or lots of
      rules to encapsulate the logic
   2. Complex problems where tradtional approaches can't provide an adequate solution
   3. Fluctuating environments where the data is changing and must be adjusted to
   4. Gaining insights from large volumes of data that are otherwise intractable

3. **What is a labeled training set?**

   A labeled training set is one where each observation in the training set has
   a label or value that represents the known outcome for that observation
   where the outcome is the target variable that would serve as a dependent
   variable when creating a model based on the labeled training set.

4. **What are the two most common supervised tasks?**
 
   * Classification - aims to predict the category of an observation based on
     certain attributes or characterstics of previous obervations in a specific
     category
   * Regression - aims to predict a target value such as the sale price a house
     based attributes or characterstics of previously sold houses

5. **Can you name four common unsupervised tasks?**

   1. Clustering
      * K-Means
      * DBSCAN
      * Hierarchical Cluster Analysis (HCA)
   2. Anomaly detection and novelty detection
      * One-class Support Vector Machine (SVM)
      * Isolation Forest
   3. Visualization and dimensionality reduction
      * Principal Component Analysis (PCA)
      * Kernel PCA
      * Locally Linear Embedding (LLE)
      * t-Distributer Stochastic Neighbor Embedding (t-SNE)
   4. Association rule learning
      * Apriori
      * Eclat

6. **What type of Machine Learning algorithm would you use to allow a robot to
   walk in various unknown terrains?**

   A reinforcement learning algorithm would be a good choice to guide a robot
   over various unknown terrains. In reinforcement learning the learning system
   is rewarded when it does something correctly and as a result is capable of
   learning in various environments as long as the reward system is setup to
   reward actions that lead to a desired outcome more than actions that do not. 

7. **What type of algorithm would you use to segment customers into multiple
   groups?**

   There are a couple of algorithms you could use for this purpose. If you
   already know the segments you are trying group customers in you have
   historical data you could use a multi-label or group classification
   algorithm. However, if you do not know what groupings you're looking for and
   are instead looking to discover the segments, an unsupervised clustering
   algorithm would likely be the best place to start.

8. **Would you frame the problem of spam detection as a supervised or
   unsupervised learning problem?**

   I would frame the problem as a supervised learning problem first. Using a
   corpus of known spam emails, one should be able to train a model to identify
   spam that has used tactics similar to the examples that the model was
   trained on. However, spammers often change their tactics over time and the
   model would likely need to be frequently retrained, so adding in an online
   learning or semi-supervised learning component would likely imporove task
   performance when trying to deal with everchanging spam tactics.

9. **What is an online learning system?**

   An online learning system learns incrementally on small amounts of data,
   known as mini or micro batches. The system can learn on the fly and is low
   cost from a data infrastructure because it learns continuously using a
   smaller amount of computing resources than large batch models that need
   very large data volumes to train.

10. **What is out-of-core learning?**

    Out-of-core learning generally refers to systems that can learn on data
    incrementally in a fashion that does not require all the data to be in 
    a computer's memory at the same time. As a result it can be trained on
    enormous data sets or used in scenario's where computing resources are
    limited.
 
11. **What type of algorithm relies on a similarity measure to make
    predictions?**

    *Instance-based learning* relies on learing a known set of training
    examples and then generalizing to new examples based on applying a measure
    of similiarity between the new examples and the known examples.

12. **What do model-based learning algorithms search for? What is the most
    common strategy they use to succeed? How do they make predictions?**

    *Model-based learning* systems search for an optimal representation of the
    data they are trained on. The most common strategy is to define a utility
    or fitness function to judge how good model fits the data, or define cost
    function to judge how poorly the model fits the data, then train the model 
    through optimzation to maximize the utiltity function or minimize the cost
    funtion. Once the model is trained it is used to make predictions on new
    data by applying the model to the new data which is called inference.

13. **What is the difference between a model parameter and a learning
    algorithm's hyperparameter?**

    A model parameter is an output value that was tweaked during the model
    training or optimzation process and is applied to new data to make
    predictions durning the inference process. A hyperparameter is a parameter 
    of a specific learning algorithm that is used to tune or change how the
    algorithm performs during training but is not an data parameter of the
    model.

14. **Can you name the four main chanllenges of Machine Learning?**

    1. Insufficient quanity of training data
    2. Nonrepresentative training data
    3. Poor quality data
    4. Underfitting and overfitting training data

15. **If your model performs great on training data but generalizes poorly to
    new instances, what is happening? Can you name three possible solutions?**

    Most likely, the model is overfitted to the training data and has a very
    high variance vs bias ratio. Some common solutions are:

    1. Use a more simple model
    2. Constrain the model through regularization
    3. Obtain more representative training data by gathering more data or
       reducing the noise by correcting bad data and removing outliers

16. **What is a test set, and why would you want to use it?**

    The test set is holdout set that is never used during the model training and
    validation process it. It's purpose is to judge how well the model
    generalizes to completely unknown data by comparing it's training and
    validation performance against it's performance making preditions on the
    test set. The differnce in performance in training vs the test set is the
    model's generatization error.

17. **What is the purpose of a validation set?**

    The validation set is used to test the performance differences between
    different models and learning algorithm hyperparameter combinations trained
    using a base training set (total data set - (validation + testing) sets)
    to search for optimal model/hyperparameter combination before retraining
    the winner on the base training and validation sets combined, then
    assessing performance on the test set.
 
18. **What is the train-dev set, when do you need it, and how do you use it?**

    The train-dev set is an additional data set that can be held out in cases
    when you are not sure whether all the training data you're using will be
    representative of the data a model will see in it's intended purpose. The
    train-dev set is a smaller known representative dataset that can be used to
    test whether a model trained on the larger training set is overfitting the
    data before moving the model to the validation process.

19. **What can go wrong if you tune hyperparameters using the test set?**

    Both the model and hyperparameters may be overfit to the testing data and
    a model that performs extremely well in testing will not perform nearly as
    well on new data because it doesn't resemble the test set that the model is 
    tightly bound to.
