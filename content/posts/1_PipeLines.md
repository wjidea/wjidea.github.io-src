Title: Pan-Core Genome Pipeline (Part I)
Category: article
Tags: bioinformatics
Slug: bacpan1
Date: 03-08-2016
Template: article



Parallel  
- [How to use Parallel (video)](https://www.youtube.com/watch?v=OpaiGYxkSuQ)  
- [Tutorial Document](http://www.gnu.org/software/parallel/parallel_tutorial.html)

FASTQC
`
	#!/bin/bash
	#this file is to run fastqc
	
	#run paralell
	#-j indicates run as many jobs as possible
	#+0 indicates add 0 job to cpu core(s)
	ls *.gz | time parallel -j+0 --eta 'fastqc {}'`

Trimmomatic

	TRIM_PATH='/home/wjidea/apps/Trimmomatic-0.32/trimmomatic-0.32.jar'`

	RAW_SEQ='/home/wjidea/Files/Turf_bac_rawseq/20130608_DNASeq_PE/raw_seqs'
	ADAPTER='/home/wjidea/apps/Trimmomatic-0.32/adapters/TruSeq3-PE-2.fa'
	FWPE=${1%%.fastq.gz}.PE.fq.gz
	FWSE=${1%%.fastq.gz}.SE.fq.gz
	RVPE=${2%%.fastq.gz}.PE.fq.gz
	RVSE=${2%%.fastq.gz}.SE.fq.gz
	java -jar $TRIM_PATH PE $1 $2 $FWPE $FWSE $RVPE $RVSE ILLUMINACLIP:$ADAPTER:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`

FASTx trimmer

	fastx_trimmer -Q33 -l 70 -i combined.fq | fastq_quality_filter -Q33 -q 30 -p 50 > combined-trim.fq
	fastx_trimmer -Q33 -l 70 -i s1_se | fastq_quality_filter -Q33 -q 30 -p 50 > s1_se.filt
	
Assembly
	SPAdes 3.1.0
Assembly quality check
	QUAST: Quality Assessment Tool for Genome Assemblies

### Another way to make parallel
Split file into small chunks by lines for example, then run each file with the code below to run jobs in parallel, especially when some tasks are not compatible with GNU parallel:

    split -dl 304 big_file suffix

`for session in gene*;
 do screen -d -m -S $session ./ext_mFasta2.sh $session;
done;`

###Roary:

CAUTION: roary uses tons of intermediate files to process with the pangenome results data, therefore the parallel is not working for the query_pan_genome function.

###other useful codes

	rename 's/pan_genome_results_//' pan_genome_results_*.fa

	parallel -j+0 --eta 'muscle -in {} -out {.}.aln' ::: *.fa

	parallel -j+0 --eta 'trimal -in {} -out {.}.trim.aln -gt 0.8 -st 0.001 -cons 60' ::: *.aln

	parallel -j+0 --eta 'fasttree -quiet -nopr {} > {.}.tre' ::: *.aln

	rename 's/(.{2,}?)\.trim\.tre/$1.tre/' *.trim.tre       

	parallel -j+0 --eta 'coreGenome.R {} {.}.png' ::: *.Rtab 

#### TBD ...