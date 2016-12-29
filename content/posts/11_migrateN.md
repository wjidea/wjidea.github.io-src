Title: Migration analysis using migrate-n
Category: article
Date: 05-20-2016
Tags: bioinformatics; population genetics; evolution
Slug: migrateN
Template: article
Status: draft

I have used migrate-n for my population migration analysis for quite a while.
During the time I was using migrat-n, parallel computation is of particular
important for such a computation intensive job. In addition, Bayesian sampling
based methods are generally sensitive to the amount of sample taken at each run.
Therefore, the default answer to numerous problems in migrate-n analysis was
please make longer runs in the migrate-n discussion group in google forum.

In this post, I will specifically emphasize two topics in migrate run: 1) parameter
file setup and 2) parallel computation.

1) parameter settings for migrate-N

The parameters that are subject to change include: migration model (matrix),
Bayesian sample serach strategies, input, and output file names

```

```

2) parallel computing

It is recommended to run migrate-n analysis in a cluster environment, since the
multilocus sampling requires high parallel computation power. Also, you can run
migrate-n in multi-core single processor machine, which you may need some trick
to figure that out.

I will place two submission files for the two environments

