Title: Build a bioinformatics lab server with a small budget in 2014 (Part1)
Date: 08-01-2014
Modified: 03-08-2016
Category: article
Tags: Bioinformatics
Slug: builtServer
Template: article
Status: published


A friend of mine is going to set up a plant pathology lab soon, and he is planning working with some bioinformatics work over there. I am helping him build a lab server with a reasonable price, which in this case was USD1.5k. I plan to use this opportunity to write a blog to document the whole process to share with the potential community.

Nowadays, next generation sequencing (NGS) is becoming affordable and approachable to most of the labs. Although many other options are out there for people who want to seek for data computing solutions. But the cheap way for a lab with limited fundings could be a lab-owned server. Now let’s see what we can get with this price, and what’s the performance is gonna be.

1. Consult for the scope of their research. 

At this step, I had a couple of conversation with my friend, who is a pure molecular bacteriologist with limited experience in bioinformatics. From the conversations, I understood the potential applications in his research, and the size of the potential computation loads. After a few rounds of conversation, his requirements and applications are listed below:

* Bacterial genome assembly
* Comparative genomics
* Transcriptomics with emphasis on genes DE analysis
* Genomic features annotations

Based on the requirement, I made a few suggestions on the configuration of the server. First, due to the small size of bacterial genome, the storage of the server is not the first of concern.