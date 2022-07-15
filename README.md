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
* <a href="#FutureDevelopment">Future Development</a>
* <a href="#References">References</a>

<h2 id="Idea">Idea</h2>
I was tired of working on projects for industry level with use cases. Sometimes there are times when you need to take a step back and relax, when you need to look back on why you chose this particular field. This was a different idea. Although it might not be something that has a use case but it is definitely something that you can look at and chuckle with you friends. It was fun creating this project and sometimes you do need to work on silly projects as well.

<h2 id="SampleResults">Sample Results</h2>
Here is a clip of realtime clip of the working of the application. 
<p align = "center"><img align = "center" src = "images/image.gif" /></p>

<h2 id="Dataset">Dataset</h2>
This project used <a href="https://github.com/schesa/ImgFlip575K_Dataset">ImgFlip scraped dataset</a>.

<h2 id="Setup">Setup</h2>
Clone the repository : <code>git clone https://github.com/Shreyz-max/Memes-Generator.git</code>

Video Caption Generator: <code>cd Memes-Generator</code>

Create environment: <code>conda create -n meme_generator python=3.8</code>

Activate environment: <code>conda activate meme_generator</code>

Install requirements: <code>pip install -r requirements.txt</code>

<h2 id="Usage">Usage</h2>
To use the models that have already been trained. Download the models from here and place them in models folder.
Change the model_weights_path in config file.

Run <code>python3 app.py</code>

If you want to train from scratch, you can run the following scripts in the sequence.

First we will clone the dataset library. <code> git clone https://github.com/schesa/ImgFlip575K_Dataset.git </code>
Here you can either scrape from scratch. The script for scraping from scratch is present in the repo itself.
I used the already existing dataset. I used the individual json files in dataset folder.
So the first step is to convert this into dataset for training.

Hence, run the code <code>python3 preprocess.py</code>

This is followed by <code> python3 preprocess_captions.py</code>

Now, for the training, run <code> python3 train.py</code>

<h2 id="Model">Model</h2>

DistillGPT2 is finetuned to generate captions. In here, the way this model is trained is such that, for each meme template a token 
has been assigned. You can check out the tokens in `special_tokens.py`. Now, the inference works just like any other transormer model.
Given the category token it has to predict the remaining words hence generating a caption. It also has two other tokens.
One signifies the end of the sentence and other signifies the end of the box. End of the box tells us the upper
and lower caption on the meme template.
This generated text along with the category is passed to `ImgFlip Api` to generate the meme. I added a bit
of front end to make it look a bit more interactive.
This is then deployed to AWS. The link to try this by yourself is <a href="http://54.148.195.21:8080/">here</a> .

<h2 id="FutureDevelopment">Future Development</h2>
<ul>
 <li> Using other transformers more advanced transformers</li> 
 <li> Working on a larger dataset</li>
</ul>

<h2 id="References">References</h2>
 
 [Dataset](https://github.com/schesa/ImgFlip575K_Dataset)
 
 [Keras implementation](https://github.com/apostaremczak/meme-generator)
