# Toy-Model-Checking

## 1. Preprocessing

This section will include all work we did, and other possible thoughts. We have 17 min training video, with 20 frames per second. It's 20400 frames, where we have speed on each frame. From the initial description, we can start with some basics on it. 1. Features taken from Images 2. Features elapsed over time. 

### 1.1  Working Area
From each frame, we can decide working area, which includes most of the features, depending on our task. And reduce number of the Inputs. Even we did some feature area investigation, it's easy to manually retrive most useful part.


<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/source-image.jpg" width="400" height="300" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/source-feature-area.png" width="400" height="300" /> 

But we have another interesting question here. As you can see, we have Working Area, which consist from `Close` and `Far` subareas. First one, has more features about road changes (has more changes over time, due of camera angle). And Second one with more noise like side objects, other cars and less road changes. 


<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/car-angle-variants.jpg" width="700" height="300" /> 

At this point, we have few variants, for next preprocessing steps. We will use this options in the next phases. - Using `Far` Sub Area. -Using `Mid` Sub Area. - Using `Close` Sub Area. - Using complete Working Area. 

<img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/image-mov-top-0.jpg" width="200" height="100" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/image-mov-mid-0.jpg" width="200" height="100" /> <img src="https://raw.githubusercontent.com/GensaGames/Toy-Model-Checking/master/files/image-mov-bot-0.jpg" width="200" height="100" /> 


**Note** It's very important to reduce number of Inputs, especialy in such cases, where we working with Video, and features elapsed over time. One wrong step will cause your model to have the Curse of Dimensionality. That is why we suppose to avoid last variant with using complete Working Area. 

Below correct way, how we can estimate it, with changes over time. Note, this sample only for visualizing and deciding about next steps. because correct Area we can choose, only after using some Model and testing feature extraction on each frame. 



