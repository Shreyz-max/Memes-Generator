# Meme Generator

This is an automated AI meme generator. On selecting a particular meme template a relating caption to that meme template gets generated.
Here, the mechanism is similar to a captioning model but no images were used for training. This is a fun project I created to test the sarcasm levels of a 
trained model. The application has then been deployed on AWS.

## Table of contents
* <a href="#Idea">Idea</a>
* <a href="#SampleResults">Sample Results</a>
* <a href="#Dataset">Dataset</a>
* <a href="#Setup">Setup</a>
* <a href="#Usage">Usage</a>
* <a href="#Model">Model</a>
  * <a href="#TrainingArchitecture">Training Architecture</a>
  * <a href="#InferenceArchitecture">Inference Architecture</a>
  * <a href="#Loss">Loss</a>
  * <a href="#Metric">Metric</a>
* <a href="#Features">Features</a>
* <a href="#Scripts">Scripts</a>
* <a href="#FutureDevelopment">Future Development</a>
* <a href="#References">References</a>

<h2 id="Idea">Inspirationdea</h2>
I was tired of working on projects for industry level with use cases. Sometimes there are times when you need to take a step back and relax, when you need to look back on why you chose this particular field. This was a different idea. Although it might not be something that has a use case but it is definitely something that you can look at and chuckle with you friends. It was fun creating this project and sometimes you do need to work on silly projects as well.

<h2 id="SampleResults">Sample Results</h2>
Here is a clip of realtime clip of the working of the application. 
<p align = "center"><img align = "center" src = "images/predict_realtime.gif" /></p>

<h2 id="Dataset">Dataset</h2>
This project used a href="https://github.com/schesa/ImgFlip575K_Dataset">ImgFlip scraped dataset</a>.
