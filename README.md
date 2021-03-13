# Toy-Model-Checking
<<<<<<< HEAD
*My mad diary*
=======

>>>>>>> origin/feature/new/experimental




<br/><br/>


<<<<<<< HEAD
## Analyze
=======
## 1. Analyze
>>>>>>> origin/feature/new/experimental


We have 17 min training video, with 20 frames per second. It's 20400 frames, where we have speed on each frame. From the initial description, we can start with some basics on it a) Features taken from Images b) Features elapsed over time. We will include all work we had, and other possible thoughts.

Start with checking training video, we will see highway varience 70% of the video, and street about 30 %. We do have some noises, like low distance between cars, and few turns with very smoothed rotation. Some examples of the frames, you can see below. Nothing special at all. 

<br/> <br/> <br/>
<br/><br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/car-normal-ex1-0.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/car-normal-ex2-0.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/car-normal-ex3-0.gif" width="280" height="170" /> 

<<<<<<< HEAD
Examples of Working Areas in the train set.
=======
1.1.1. Examples of Working Areas in the train set.
>>>>>>> origin/feature/new/experimental
<br/> <br/> <br/> 
<br/><br/>



However, we have existing video for testing. Test video have 9 min video with the same framerate, and will be used for the next model evaluation. As you will see, it's not just usual task, where you need to keep in mind a regularization objective. But think about alternatives for the feature extraction. 

So lets describe test set, and what we have. Only 30% of varience from the highway. We have a lot of noises, which completely new comparing to the training set. Few of them are - Sharp turns - Car stop - Road steep descent and ascent.

<br/> <br/> <br/>
<br/><br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/car-turning-ex1-0.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/car-stop-ex1-0.gif" width="280" height="170" />  <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/car-turning-ex2-0.gif" width="280" height="170" /> 

<<<<<<< HEAD
Examples of Working Areas in the test set. LTR Car turning Ex.1 - Car stop - Car turning Ex.2
=======
1.1.2. Examples of Working Areas in the test set. LTR Car turning Ex.1 - Car stop - Car turning Ex.2
>>>>>>> origin/feature/new/experimental
<br/> <br/> <br/>
<br/><br/>



We will start with check training data and it's changes over time. Most useful information, it's changes speed over time. You can see, where speed changes very swift, and we can use it for tracking anomaly detection for the next validation phase (when ever your predictions meet near to unexpected result). 


<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/speed-changes-with-frame.png" width="900" height="250" /> 

<<<<<<< HEAD
Speed value at Frame index from initial training Video. 
=======
1.1.3. Speed value at Frame index from initial training Video. 
>>>>>>> origin/feature/new/experimental
<br/> <br/>

<br/> 

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/speed-changes-with-previous.png" width="900" height="250" /> 

<<<<<<< HEAD
Delta Speed changes over Previous frame. 
=======
1.1.4. Delta Speed changes over Previous frame. 
>>>>>>> origin/feature/new/experimental
<br/> <br/> 


Above Image explains how Speed may change from the previous. Even one Video is not enough to relay on this value, we can assume this parameter is good for validation and checking anomalies in a prediction. One more sample, of avarage rate of changing Speed, over previous 20 frames (1 second in time). 

<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/0/speed-changes-delta-20-frame.png" width="900" height="250" /> 

<<<<<<< HEAD
Delta Speed changes over Previous 20 frames.
=======
1.1.5. Delta Speed changes over Previous 20 frames.
>>>>>>> origin/feature/new/experimental
<br/> <br/>



<<<<<<< HEAD
## Feature Extraction

This is the most important step to solve this task. The way for creation model, regularization and preprocessing make no sense, unless we know what features are going to work! All examples below will consider the next way. Take frame at time T and next to it frame T+1. Use this two frames for feature extraction. 

### Optical Flow Gunnar Farneback

### Optical Flow Gunnar Farneback

### Optical Flow Lucas-Kanade
=======
>>>>>>> origin/feature/new/experimental








<br/> <br/>

<<<<<<< HEAD
## Preprocessing


### Working Area
=======
## 2. Preprocessing


### 2.1 Working Area
>>>>>>> origin/feature/new/experimental
From each frame, we can decide working area, which includes most of the features, depending on our task. And reduce number of the Inputs. Even we did some feature area investigation, it's easy to manually retrive most useful part.

<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.1/source-image.jpg" width="400" height="300" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.1/source-feature-area.png" width="400" height="300" /> 

<<<<<<< HEAD
Source Image and Source Image Areas. Red Box represents Working Area, for the next steps. 
=======
2.1.1. Source Image and Source Image Areas. Red Box represents Working Area, for the next steps. 
>>>>>>> origin/feature/new/experimental
<br/> <br/>

But we have another interesting question here. As you can see, we have Working Area, which consist from some Sub Areas, Close and Far. First one, has more features about road changes (has more changes over time, due of camera angle). And Second one with more noise like side objects, other cars and less road changes. 

<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.1/car-angle-variants.jpg" width="800" height="200" /> 

<<<<<<< HEAD
Frame changes updates in different way, based on Angle of a Camera. 
=======
2.1.2. Frame changes updates in different way, based on Angle of a Camera. 
>>>>>>> origin/feature/new/experimental
<br/> <br/>

At this point, we have few variants, for next preprocessing steps. We will use this options in the next phases. - Using Far Sub Area. - Using Close Sub Area, and so on.

*Note. It's very important to reduce number of Inputs, especialy in such cases, where we working with Video, and features elapsed over time. One wrong step will cause your model to have the Curse of Dimensionality. That is why we suppose to avoid last variant with using complete Working Area.*


Below animation, how we can estimate it, with changes over time. Note, this sample only for visualizing and deciding about next steps. because correct Area we can choose, only after using some Model and testing feature extraction on each frame. 

<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.1/image-mov-top-0.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.1/image-mov-mid-0.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.1/image-mov-bot-0.gif" width="280" height="170" /> 

<<<<<<< HEAD
Sub Area features changing over time. LTR Far - Mid - Close Areas.
=======
2.1.3. Sub Area features changing over time. LTR Far - Mid - Close Areas.
>>>>>>> origin/feature/new/experimental
<br/> <br/>

As a result, we come with few options for next work **a) Check Model velocity using several Sub Areas Types. b) Check Model velocity over all possible Sub Areas, with momentum over some shifting.**



<br/>

<<<<<<< HEAD
### Scaling and Normalization
=======
### 2.2 Scaling and Normalization
>>>>>>> origin/feature/new/experimental

Scaling takes some part in preprocessing, even we can simplify and avoid it's usage. Scale working in two directions, and for some cases might reduce a Dimensionality in two different ways. We will not talk about simple scaling down Image, to reduce it's size, but in some resources, you can find opossite usage of scaling, by increasing Image size.

<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.2/scale-source.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.2/scale-image.gif" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.2/scale-compressed.gif" width="280" height="170" />

<<<<<<< HEAD
Feature changing over time. LTR Source - Scaled - Compressed Images.
=======
2.2.1. Feature changing over time. LTR Source - Scaled - Compressed Images.
>>>>>>> origin/feature/new/experimental
<br/><br/>

For some cases, very simple process of scaling up small Image helps to make some kind of preprocessing and retaint most important features and their changes over time. We can compare this process, to some N Compressing, but requires substantially less resources to compute. 

For the normalization, we don't have something new. In case we working with Images, we can just normilize features, over maximum value of colors. Mean of RBG values at pixel divided by Max possible color value (255) (or even simpler for an Image, loaded in the Grey filter). As a another point, we can think about normalization with `Scikit-Learn` Scalers, however first variant is good enough. 

<<<<<<< HEAD
At this stage, we will play with Scaling in two different ways. After choosing some Sub Area from Working, we will **c) Apply some Scalling up and down based on Working Area size.*
=======
At this stage, we will play with Scaling in two different ways. After choosing some Sub Area from Working, we will **a) Apply some Scalling up and down based on Working Area size.*
>>>>>>> origin/feature/new/experimental


<br/>

<<<<<<< HEAD
### Frames Timeline 
=======
### 2.3 Frames Timeline 
>>>>>>> origin/feature/new/experimental

As we mentioned before, we will work on features elapsed over time. And for the single training sample, we should have few frames before the focus one. This Timeline of single training sample, might be configured in very different way. And not only previous frame, before the focused.

<br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/1.3/frames-elapsed-over-time.jpg" width="800" height="160" /> 

<<<<<<< HEAD
Single training sample consist from several frames
=======
2.3.1. Single training sample consist from several frames
>>>>>>> origin/feature/new/experimental
<br/><br/>

For testing purpose, we created Preprocessor objects, which can retrive Timelines in different format, and not only previous frame. We can represent it, as indexes '(0, 1, 2)', where '(0)' it's current frame, where we now the right Y value (and looking back to the previous '(1)', and next to it '(2)' frames). 

<<<<<<< HEAD
In out testing, we might check dependencies between frames '(0, 1)' or '(0, 1, 2, 3, 4)' and some variations in this range.   And even more complicated behavior, Timeline with different steps (ex. with step 2, we will have '(0, 2, 4)'), where frame changes will be more visible. So action items for this mapping is **d) Check different Frame Timelines.**
=======
In out testing, we might check dependencies between frames '(0, 1)' or '(0, 1, 2, 3, 4)' and some variations in this range.   And even more complicated behavior, Timeline with different steps (ex. with step 2, we will have '(0, 2, 4)'), where frame changes will be more visible. So action items for this mapping is **a) Check different Frame Timelines.**
>>>>>>> origin/feature/new/experimental




<br/>

<<<<<<< HEAD
### Regularization

After coming with different tests we see that regularization is very specific for task/model, and feature params/extraction which we have. Hence we suppose to skip this session and describe just agnostic points of it. 

- Floating area in the working frames. Descents and ascents might effect Camera angle and cause different frame representation. To cover such cases we added few functions, which produce floating area, during training phase. 

- Other.


<br/>

### Summary


In general it's very simple process, where we just shared all thoughts during Preprocessing. For some model, we should take Frames Timeline on Working Area and Normilize inputs. However we came up with several different options: Preprocessor combinations (marked above) which we should investigate. Keep in mind it might be quite specific for particular model and feature extraction purpose. 

Well known other algorithms might be used for feature extraction on Images. Some of them like `SIFT`, `ORB`, `HOG` and other, could work very well, but they don't. During validation and testing, patterns between their changes, doesn't work for speed. And other reasons related to the performance of a model, and such actions require huge time for computing.







<br/> <br/>


## Model

Same with preprocessing, we will describe just all investigation and work for choosing Model. We will start from simple implementations. In first phases, we suppose to keep everything as simple, as possible. Because you can increase complexity in any time and every part of the Model. 

Below you will find some graphics and Model structures. No Models (or it's structure) has the goal of being correct and used in dirty examples for general evaluation. Check sub branches, for the detailed implementation for each of them. They might have mistakes.  


<br/>

### MLP and 2D-CNN

Even from the initial sentence of the task (with processing video), which gives us hint to move in RNN directions, we had few examples of MLP. In our examples, we might represent features as delta changes between frames, where tried to achive some kind of Compressing during Timeline.

After some minor updates in Preprocessing behavior, we used different types of MLP, with different structure. However, this work, didn't effect model learning, and it was hard to resolve pattern in delta changes over time. Even with no Regularization, model didn't fit training samples. As for 2D-CNN, Convolution over Delta changes might work too. For the testing, it find correct Windows for patterns in delta changes over time, and not so good for a validation.


<br/>

### RNN and LSTM

Back to initial thoughts, RNN should have enough velocity on data over time. One more pros here, it's number of the inputs. Comparing to the previous methods, where we Flatten few frames (based on Timeline) into one blob features, here we can consume frames one by one. But for validation this model doesn't suite at all, even Plot below seems to be fine. 



<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.1-2.3/lstm-sample-over-iteration.png" width="600" height="300" /> 

Velocity of RNN model on some Preprocessor Combinations. TYPO. By `Number of Iter(I)` there is Number of Samples, during minibatch learning. 
<br/><br/>



<br/>

### 2D-CNN with LSTM

Combination of 2D-CNN windows, and tracking frames changes over time might work very well. Back to model strucutre, we continue some updates, slowly increasing model complexity, but validation results still not enough to work in this direction. 


<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.1-2.3/lstm-cnn-sample-over-iteration.png" width="600" height="300" /> 

Velocity of 2D-CNN with LSTM Model on some Preprocessor Combinations. TYPO. By `Number of Iter(I)` there is Number of Samples, during minibatch learning. 
=======
### 2.4 Regularization

As you can see from the Analyze above, we should care enough about Regularization. And model should be well rounded to cover most cases. We seperate all regularization objective into several points. 

- We have model above with Frames Augmentation and `CoarseDropout` and `GammaContrast` work for our cases. Only few layers enough for the retaining most of the usefull features in the video, without overfitting. Some of examples, you can see below. 

<br/><br/>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/aug-image-1.jpg" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/aug-image-2.jpg" width="280" height="170" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/aug-image-3.jpg" width="280" height="170" /> 

1.1.1. Examples of Working Areas in the train set.
<br/> <br/>

- Floating area in the working frames. We steep descent and ascent, which effect Camera angle and cause different frame representation. To cover such cases we added few functions, which produce floating area, during training phase. 

- Model. 





<br/>

### 2.5 Features Extraction


And of course we have to resolve the change from frame to frame to understand how speed was changed. There are few ways, how we can extract features over two frames. And besides most effective solution with Optical Flow, I think it was also possible to delta changes over two frames.  

* [Source frame from the Test Video, just for representation]

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/change-gif-delta.gif" width="620" height="300" /> 
<br/>

* Delta changes. With Threshold and Sharpens. 

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/change-gif-delta.gif" width="620" height="300" /> 
<br/>

* Lucas-Kanade Optical Flow based on "good features to track". Result converted to vector changes in moving direction.

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/change-gif-optical-vector.gif" width="620" height="300" /> 
<br/>

* Dense Optical Flow. 

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.4-2/change-gif-optical.gif" width="620" height="300" /> 
<br/>

* ....
<br/>

Above examples, it's just a small part of all possible variations between changes of two frames. For ex. we tried different Threshold and invertion level between delta changes of Gray/RGB frames. Or for Dense flow we might use current frame and frame two steps back, or Optical Flow between two Dense flow frames. <b> In general, simple Dense optical flow was quite enough to extract everything we need from the frame. </b>


<br/> <br/>




## 3. Model.

Same with preprocessing, we will describe just all investigation and work for choosing Model. We will start from simple implementations. In first phases, we suppose to keep everything as simple, as possible. Because you can increase complexity in any time and every part of the Model. 

Below you will find some graphics and Model structures. No Models (or it's structure) has the goal of being correct and used in dirty examples for general evaluation. Check sub branches, for the detailed implementation for each of them. They might have mistakes.  


<br/> <br/>

### 3.2 RNN and LSTM

I usually don't like idea to jump directly to complex solution. And try to evaluate everything step by step. The idea here was to use delta changes over time in frame and represent it in large MLP model. In theory it could work because weight can find patterns on speed changes while remembering previous result. Hence FC layers were used on flatten image delta changes and consumed by LSTM. Even it was fitting on training data, I didn't receive further good result on validation.  


<br/>

### 3.3 2D-CNN

Another straight forward idea it's to use CNN to resolve this changes. Window pattern could work very well, and it was proven on validation data. We tried different levels of CNN, including window size, strides, etc. Most of them could come up with good evaluation. <i> Current master branch is based on 2D CNN solution. </i>

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/2.1-2.3/lstm-cnn-sample-over-iteration.png" width="600" height="300" /> 

3.3.1. Velocity of 2D-CNN with LSTM Model on some Preprocessor Combinations. TYPO. By `Number of Iter(I)` there is Number of Samples, during minibatch learning. 
>>>>>>> origin/feature/new/experimental
<br/><br/>


<br/>

<<<<<<< HEAD
### 3D-CNN

Obviously 3D-CNN takes places in this list. Even this is most recommended types for the features elapsed over time, we came to this Model in last examples. And this Model works noticeably well on validation data. Starting from very simple Model we can see very good results, and continue work on Model complexity and Preprocessor Combinations. You can see how well this Model fit, comparing to other types. 


TBD

Velocity of 3D-CNN Model.Note. Comparing to previous Plots, this X direction represents epoches over all samples. Since this model was better, we continue training. 
<br/><br/>

=======
### 3.4 2D-CNN + LSTM & 3D-CNN

Even 2D CNN was enough, I think you could achieve much better with LSTM. The reason here, it's very important to value previous frames to understand acceleration over time. And next feature extraction changes (in our cases Optical Dense Flow) I started with 2D CNN + LSTM and update it to 3D CNN with all power of Keras lib. This Model was one the best on the validation data and speed of learning.  <i> Branch with 3D CNN usage TBD </i>


[TBD]

3.4.1. Velocity of 3D-CNN Model.Note. Comparing to previous Plots, this X direction represents epoches over all samples. Since this model was better, we continue training. 
<br/><br/>


## One interesting question
There is one interesting question to answer. And this question is about splitting data for next validation. Let me explain you, why> 

- From the task we have 20400 frames of given video. And we need to have at least 2 frames, as one data point to create Optical Flow. So to create training and validation data, we can take two consecutive frames as one data point, shuffle all pairs, and split (for ex. 50% for training and 50% for validation). This approach was used in models above, and I was able to achieve perfect result on validation data. 

- In case we change the validation to be and continues range on given video. Let's say last 15% of the video (~3000 frames). <b> Neither of above solution will work. </b> The main reason it's because we didn't shuffle pair of image, and this validation data will be completely new to the model. 

Seems like right approach for splitting data will be the last one. We want to get some unique range of video, to be used for validation. Because using pairs of frames within shuffled data still gives some chance for model to get a somewhat similar frame.

However, it's still question for me, how to solve this task, considering we use continues video range for validation. Because of lack of training data, how we can solve this problem in this case?



## Conclusion

Even I had a very good result on my validation data, this work was more like self education challenge. That's why I don't have actual test result from Comma AI challenge. Moreover, there is still complex question to answer (see above). But in any case, it was a very valuable task. 
>>>>>>> origin/feature/new/experimental
