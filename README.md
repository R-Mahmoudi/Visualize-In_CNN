# CNN Visualize 

This project aims to visualize filters, feature maps, guided backpropagation from any convolutional layers of all pre-trained models on ImageNet available in `tf.keras.applications` (TF 2.3). This will help you observe how filters and feature maps change through each convolution layer from input to output.

With any image uploaded, you can also make the classification with any of the above models and generate GradCAM, Guided-GradCAM to see the important features based on which the model makes its decision.

If "art" is in your blood, you can use any model to generate hallucination-like visuals from your original images. For this feature, personally, I highly recommend trying with "InceptionV3" model as the deep-dream images generated from this model are appealing.

With the current version, there are 26 pre-trained models.


## Briefs

| **Method**                | **Brief**                                                                                                                                                                                                                                                                                               | **Example** |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------:|
| Filter visualization      | Simply plot the learned filters.<br>* Step 1: Find a convolutional layer.<br>* Step 2: Get weights at a convolution layer, they are filters at this layer.<br>* Step 3: Plot filter with the values from step 2.<br>This method does not requre an input image.                                         |             |
| Feature map visualization | Plot the feature maps obtained when fitting an image to the network.<br>* Step 1: Find a convolutional layer.<br>* Step 2: Build a feature model from the input up to that convolutional layer.<br>* Step 3: Fit the image to the feature model to get feature maps.<br>* Step 4: Plot the feature map. |             |
| Guided Backpropagation    | Backpropagate from a particular convolution layer to input image with modificaton of the gradient of ReLU.                                                                                                                                                                                              |             |
## How to use
### Run with your resource
* Clone this repo:
```bash
git clone https://github.com/R-Mahmoudi/Visualize-In_CNN.git
cd Visualize-In_CNN
```
* Create virtualev:
```bash
conda create -n cnn-vis python=3.6
conda activate cnn-vs
bash requirements.txt
```
* Run demo with the file `Visualize_In_CNN.ipynb`

### Run on Google Colab
* Go to this link: https://github.com/R-Mahmoudi/Visualize-In_CNN/blob/main/Visualize_In_CNN.ipynb

* Change your runtime type to `Python3`
* Choose GPU as your hardware accelerator.
* Run the code.

Voila! You got it.

![](images/demo-1.gif)


## Briefs

<table style="border-collapse:collapse;border-spacing:0;table-layout: fixed; width: 717px" class="tg"><colgroup><col style="width: 191px"><col style="width: 526px"></colgroup><thead><tr><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal"><span style="font-weight:bold">Method</span></th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal"><span style="font-weight:bold">Brief</span></th></tr></thead><tbody><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Filter visualization</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Simply plot the learned filters.<br>* Step 1: Find a convolutional layer.<br>* Step 2: Get weights at a convolution layer, they are filters at this layer.<br>* Step 3: Plot filter with the values from step 2.<br>This method does not require an input image.<br><br><span style="font-weight:bold;font-style:italic">VGG-16, block1_conv1</span><br><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/filtervisVGG16_block1_conv1.png" alt="Image" width="500" height="178"></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Feature map visualization</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Plot the feature maps obtained when fitting an image to the network.<br>* Step 1: Find a convolutional layer.<br>* Step 2: Build a feature model from the input up to that convolutional layer.<br>* Step 3: Fit the image to the feature model to get feature maps.<br>* Step 4: Plot the feature map.<br><br><span style="font-weight:bold;font-style:italic">VGG-16, block1_conv1</span><br><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/featurevisVGG16_block1_conv1.png" alt="Image" width="500" height="394"><br><br><span style="font-weight:bold">VGG-16, block5_conv3</span><br><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/featurevisVGG16_block5_conv3.png" alt="Image" width="500" height="394"></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Guided Backpropagation</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Backpropagate from a particular convolution layer to input image with modificaton of the gradient of ReLU.<br><br><span style="font-weight:bold">VGG-16: block1_conv1 &amp; block5_conv3</span><br><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/guidedbackpropVGG16_block1_conv1.png" alt="Image" width="231" height="231"><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/backguidedVGG16_block5_conv3.png" alt="Image" width="231" height="231"></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">GradCAM</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">* Step 1: Determine the last convolutional layer<br>* Step 2: Perform gradient from `pre-softmax` layer to last convolutional layer and the apply global average pooling to obtain weights for neurons' importance.<br>* Step 3: Linearly combinate feature map of last convolutional layer and weights, then apply ReLu on that linear combination.<br><br><span style="font-weight:bold;font-style:italic">InceptionV3, explanation for "lakeside" class</span><br><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/lakesideInceptionV3.png" alt="Image" width="460" height="233"></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Guided-GradCAM</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">* Step 1: Calculate guided backpropagation from last convolutional layer to input.<br>* Step 2: Upsample GradCAM to the size of input<br>* Step 3: Apply element-wise multiplication of guided backpropagation and GradCAM<br><br><span style="font-weight:700;font-style:italic">InceptionV3, explanation for "boathouse" class</span><br><br><img src="https://raw.githubusercontent.com/nguyenhoa93/cnn-visualization-keras-tf2/master/images/boathouseInceptionv3.png" width="460" height="233"></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Deep Dream</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">See more in this excellent tutorial from François Chollet: <a href="https://keras.io/examples/generative/deep_dream/" target="_blank" rel="noopener noreferrer">https://keras.io/examples/generative/deep_dream/</a><br><br><span style="font-weight:bold;font-style:italic">InceptionV3</span><br><br><img src="https://raw.githubusercontent.com/R-Mahmoudi/Visualize-In_CNN/main/images/image.jpg" alt="Image" width="720" height="479"></td></tr></tbody></table>


## References
1. [How to Visualize Filters and Feature Maps in Convolutional Neural Networks](https://machinelearningmastery.com/how-to-visualize-filters-and-feature-maps-in-convolutional-neural-networks/) by Machine Learning Mastery
2. Pytorch CNN visualzaton by [utkuozbulak](https://github.com/utkuozbulak): https://github.com/utkuozbulak
3. CNN visualization with TF 1.3 by [conan7882](https://github.com/conan7882): https://github.com/conan7882/CNN-Visualization