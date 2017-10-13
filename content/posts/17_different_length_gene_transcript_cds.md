Title: Length differences for gene, transcript, and CDS
Category: article
Tags: R
Slug: gene features biomart R 
Template: article
Status: published

The lengths of gene, transcript, and CDS can be quite different in their lengths.

First we need to understand all of these three terms:

- gene
Of these three, gene is a big concept, which contains both transcript and CDS.

- transcript
A gene can have multiple forms of transcripts (a.k.a. isoforms), of course with varied lengths

- CDS
Coding region composed of exon, but it does not include the 5' or 3' UTRs in the exon. A CDS always starts with a
AUG codon and ends with a stop codon (UAG, UAA, and UGA).

The job I need to do is to add gene function annotation (brief description) and CDS length with a list of gene in 
_Arabidopsis thaliana_. I found the `biomaRt` tool in BioConductor is quite helpful.

Below are my script to retrieve those information from biomart within R environment.

```R
library(biomaRt)

mart <- biomaRt::useMart(biomart = "plants_mart", dataset = "athaliana_eg_gene", host = 'plants.ensembl.org')
attrs <- listAttributes(mart)
attrs[grep("length", attrs$name),]

ath_attr <- biomaRt::getBM(attributes = c("ensembl_gene_id", "description"), mart = mart)
ath_attr_structure <- biomaRt::getBM(attributes =c("ensembl_gene_id", "cds_length"), mart = mart)
ath_attr_structure <- ath_attr_structure[!is.na(ath_attr_structure$cds_length), ]
ath_attr_extract <- data.frame(ensembl_gene_id = character(), cds_length = character())

counter = 0
for (gene_ath_id in ath_attr$ensembl_gene_id){
  counter <- counter + 1
  print(counter/length(ath_attr$ensembl_gene_id))
  if (gene_ath_id %in% ath_attr_structure$ensembl_gene_id){
    subDf <- ath_attr_structure[ath_attr_structure$ensembl_gene_id == gene_ath_id, ]
    if (dim(subDf)[1] > 1){
      longested_CDS_length <- max(subDf$cds_length)
      longested_CDS <- subDf[subDf$cds_length == longested_CDS_length, ]
      ath_attr_extract <- rbind(ath_attr_extract, longested_CDS)
    } else{
      ath_attr_extract <- rbind(ath_attr_extract, subDf)
    }
  }
  else {
    next
  }
}
ath_attr_merge <- merge(ath_attr, ath_attr_extract, by = "ensembl_gene_id")

save(ath_attr_merge, file="ath_description_longest_cds_length.Rdata")

x_rpkm_df_genL <- merge(x_rpkm_df, ath_attr_merge, by.x = "gene_id", by.y = "ensembl_gene_id", all.x = TRUE)

```

- References

[1]. [biomaRt](https://master.bioconductor.org/packages/release/bioc/html/biomaRt.html) 