title: Visualizing every job in the world
date: 02-10-2022 09:00
description: A visualization of every single job in the world (or at least in the EU)
status: published
slug: every-job-world
thumbnail: images/36/every-job-world.png


<a href="https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/duarteocarmo/esco-visualizations/master/projector_config.json">
<img src="{static}/images/36/every-job-world.png" alt="Embeddings" style="max-width:100%;">
</a>

Imagine you have to classify _every single job title_ in the world into 10 categories, how would you go about it? 

This is a  *fairly hard* problem to solve. However, the European Union has actually taken it on. They named it: [the ESCO project.](https://ec.europa.eu/esco/portal/occupation) (ESCO stands for European Skills, Competences, Qualifications and Occupations) 

Damn I love the EU. 

What if we scraped their database of 3001 occupations and ran them through the famous [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) model? We could look at all the [alternative names](https://ec.europa.eu/esco/portal/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Fisco%2FC821&conceptLanguage=en&full=true#&uri=http://data.europa.eu/esco/isco/C821) for each title/occupation, and build a network of jobs.

The result is [this projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/duarteocarmo/esco-visualizations/master/projector_config.json): a network of every job in the world, that clusters titles by similarity.

You can also run the PCA or t-SNE algorithms through it. These will cluster the jobs in slightly different ways. Go ahead and look for your job title on the right pane, and see the most similar jobs out there (at least according to BERT).
