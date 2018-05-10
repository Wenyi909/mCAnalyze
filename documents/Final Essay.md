## Final Project Essay
##### 1. Now that you have seen many full research projects saved online as GitHub repositories do you plan to use GitHub for your future projects as a way to store code and data in the cloud and to share your progress with others?
Yes, I think Github is a good platform for developing tools and sharing with others. The master/branch structure enables users to always keep track of all the changes and updates, save individual versions without getting confused. The notes and comments sections help people to discuss problems and find solutions. In addition, Github has quite nice markdown display. Overall, it is a great place to develop future projects, store code and share data.

##### 2. Did you project accomplish the goals that you set out for yourself in your proposal? If not, why? What was the hardest problem in your project that were able to overcome? What, if any, was a problem that you were unable to overcome in your project within the given time?
I did accomplish my major goal, which is to try non-rigid motion correction and make motion correction comparison analysis. However, I haven't fully accomplished all the goals I set in my proposal. This is because I was stuck on how to integrate motion correction methods and optimize the results by changing various parameters. I spent too much time learning the motion correction and how the algorithm works, so I did not have enough time for optimization.

In my project, the hardest thing is to get the `NoRMCorre` non-rigid motion correction working on the data I have. The default parameters the package recommended did not work very well, and it took a long time to fugure out what parameters suit my data through trial and error. Now I still think the parameters need optimization, but in general the program is able to stablize the image smoothly. 

As for the problems that I was unable to tackle so far, professor recommended me to use machine learning to optimize the parameters I have. I think that's a really good idea, but so far I haven't figured out how to incorporate machine learning into the library that I have. I need to go through the machine learning tutorial again to have a sense of how to implement this strategy. In addition, I hope I can combine two motion corrections methods together to improve the results, but to do that I need to convert memory map file into tif file, which right now I haven't figured out how to do it.

##### 3. Do you feel that you've learned the skills necessary perform data analysis in Python, and to write your own program or pipeline for data analysis? What skills do you think you need to work on further, and where would you look to find more information about learning these skills?
Through this course, I have learnt a lot of the basic skills for developing my own program and performing data analysis. I need to further work on machine learning, and reading more into the imaging analysis tools. I will search for their documentations and tutorials online for help.



