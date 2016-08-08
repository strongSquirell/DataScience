# DataScience
This repository will contain systematization of my knowledge about Data Science.

__Steps__:  
Of course these may vary slightly depending on the type of problem, data, tools available etc.
1.	__Problem definition__  The first step is to of course understand the business problem. What is the problem you are trying to solve aˆ“ what is the business context? Very often however your client may also just give you a whole lot of data and ask you to do something with it. In such a case you would need to take a more exploratory look at the data. Nevertheless if the client has a specific problem that needs to be tackled, then then first step is to clearly define and understand the problem. You will then need to convert the business problem into an analytics problem. I other words you need to understand exactly what you are going to predict with the model you build. There is no point in building a fabulous model, only to realise later that what it is predicting is not exactly what the business needs.  
2.	__Data Exploration__ Once you have the problem defined, the next step is to explore the data and become more familiar with it. This is especially important when dealing with a completely new data set.    
3.	__Data Preparation__ Now that you have a good understanding of the data, you will need to prepare it for modelling. You will identify and treat missing values, detect outliers, transform variables, create binary variables if required and so on. This stage is very influenced by the modelling technique you will use at the next stage. For example, regression involves a fair amount of data preparation, but decision trees may need less prep whereas clustering requires a whole different kind of prep as compared to other techniques.  
4.	__Modelling__ Once the data is prepared, you can begin modelling. This is usually an iterative process where you run a model, evaluate the results, tweak your approach, run another model, evaluate the results, re-tweak and so onaˆ¦.. You go on doing this until you come up with a model you are satisfied with or what you feel is the best possible result with the given data.  
5.	__Validation__ The final model (or maybe the best 2-3 models) should then be put through the validation process. In this process, you test the model using completely new data set i.e. data that was not used to build the model. This process ensures that your model is a good model in general and not just a very good model for the specific data earlier used (Technically, this is called avoiding over fitting)  
6.	__Implementation and tracking__ The final model is chosen after the validation. Then you start implementing the model and tracking the results. You need to track results to see the performance of the model over time. In general, the accuracy of a model goes down over time. How much time will really depend on the variables aˆ“ how dynamic or static they are, and the general environment aˆ“ how static or dynamic that is.  

__Learning algorithms__:
  * supervised learning - labeled output (regression, classification)
  * unsupervised learning - unlabeled output (clustering(organize computing clusters, social network analysis, market segmentation, astronomical data analysis))

   training set  
        |  
learning algorithm   
        |    
input -> h -> output
