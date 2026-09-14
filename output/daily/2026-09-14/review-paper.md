# Title

**Artificial Intelligence and Machine Learning in Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations**

## Abstract

Machine-learning methods are increasingly used to infer protein function from amino-acid sequence, three-dimensional structure, interaction networks, and learned protein representations. The most directly relevant evidence in the supplied literature concerns structure-based prediction with graph convolutional networks, sequence-based representation learning, and specialized prediction tasks involving metalloproteins [1–3]. Protein structure-prediction systems, particularly AlphaFold, have also expanded the structural information available for downstream functional inference, although structural prediction should not be confused with functional validation [4,5]. Training data generally combine protein sequences or structures with functional annotations, but the precise databases, annotation versions, filtering procedures, and train–test splits are often not clear from the available records [VERIFY]. Evaluation commonly involves classification metrics such as precision, recall, F1 score, area under the precision–recall curve, and ROC-AUC, although the supplied evidence does not establish which metrics were used consistently across the main function-prediction studies [VERIFY]. Persistent limitations include incomplete annotations, class imbalance, homology leakage, dependence on structural quality, weak extrapolation to novel proteins, and the biological context-dependence of function. More rigorous homology-aware benchmarks and experimental validation remain essential.

## Introduction

Protein function prediction is a central problem in computational biology. Experimental characterization is slow and unevenly distributed across protein families, whereas sequence databases contain very large numbers of proteins with limited or no functional annotation. Machine learning offers a way to use existing sequence, structural, and interaction data to prioritize likely functions for uncharacterized proteins.

The problem is not a single prediction task. Depending on the application, a model may be asked to assign Gene Ontology terms, identify a protein family or functional class, locate metal-binding residues, predict interaction partners, or infer a biochemical property. These tasks differ in their labels, data requirements, and appropriate evaluation procedures. Protein–protein interaction prediction, for example, can provide indirect evidence about function but should not be treated as equivalent to direct prediction of a molecular function or biological process [6,7].

The supplied literature supports a focused account of several major approaches. These include graph-based models that represent proteins through structural relationships, sequence models that learn reusable representations from large protein corpora, and conventional or deep-learning methods developed for narrower functional categories such as metalloproteins [1–3]. Structure-prediction systems such as AlphaFold provide an important source of predicted structural information for these downstream models [4,5]. However, the evidence set also contains many studies focused on drug discovery, disease biomarkers, molecular docking, or clinical prediction rather than protein-function prediction itself. Conclusions about datasets and metrics must therefore remain cautious.

## Evidence Synthesis

### Sequence-based learning and protein representations

One important direction uses machine learning to learn relationships between protein sequences and functional annotations. Protein language models are trained on large collections of unlabeled sequences and learn statistical representations that can subsequently be used for supervised or semi-supervised prediction. These representations may support classification of protein families, functional categories, or multiple annotations per protein. The review by Bordin and colleagues describes the broader contribution of newer machine-learning approaches to protein knowledge, including protein language models and learned embeddings [2].

The supplied record does not identify the precise language models, sequence databases, annotation releases, or benchmark datasets discussed in that review. Specific claims about model architectures or comparative performance therefore require verification [VERIFY]. Nonetheless, the general strategy is clear: pretraining on sequence collections is used to extract information that can be transferred to downstream functional prediction, where labeled data are usually much smaller than the unlabeled sequence corpus.

Sequence-based models are attractive because sequences are widely available and do not require an experimentally determined structure. Their principal challenge is that sequence similarity may reflect evolutionary relatedness without resolving the precise biochemical activity of a protein. Closely related proteins can differ in substrate specificity, regulation, localization, or interaction partners. Conversely, proteins with similar functions may have diverged substantially at the sequence level.

### Structure-based prediction with graph neural networks

A particularly direct example is the structure-based protein-function prediction study by Gligorijević et al. [1]. The approach represents a protein as a graph and applies graph convolutional networks. In such a representation, residues or structural elements can serve as nodes, while spatial contacts or other structural relationships define edges. The model learns patterns in the three-dimensional arrangement of the protein that are associated with functional annotations.

Structure-based learning can capture information that is difficult to express through a linear sequence alone. Functional sites may depend on residues that are distant in primary sequence but close in three-dimensional space. A structural graph can also encode local environments, contact patterns, and the organization of a protein surface. The exact functional labels used in the study are not established by the supplied evidence, although Gene Ontology annotation is a plausible interpretation that must be checked against the full text [VERIFY].

Graph learning is also being applied to protein–protein interactions. Gao et al. describe hierarchical graph learning for interaction prediction [6], while Michalik and Kuder review machine-learning methods for protein–protein docking [7]. These methods may contribute to function inference because interaction partners and complex membership often provide functional context. Nevertheless, interaction prediction is a related but distinct endpoint. A model that predicts an interaction does not necessarily identify the biochemical function of either protein.

### Specialized functional prediction

Protein-function prediction is frequently divided into narrower biological questions. Metalloproteins provide one example. Yu, Wang, and Teo review machine-learning approaches for metalloproteins, including tasks that may involve classifying metalloproteins, identifying metal-binding residues, or predicting related structural and biochemical properties [3]. Such tasks can use sequence-derived descriptors, structural features, or learned representations. The supplied record does not establish which individual classifiers, feature sets, or benchmark datasets were used in the reviewed studies [VERIFY].

This specialization is biologically meaningful. Metal association can influence catalysis, folding, stability, and regulation, but not every metal-binding site has the same functional interpretation. Labels may therefore distinguish among protein-level classes, residue-level binding sites, and catalytic roles. These distinctions complicate both model training and evaluation.

### Predicted structures as an enabling resource

AlphaFold has substantially increased the availability of predicted protein structures [4]. The AlphaFold Protein Structure Database was reported as providing structural coverage for more than 214 million protein sequences in its 2024 description [5]. Such resources can support structure-based function prediction, structural comparison, and the construction of graph representations for proteins lacking experimentally determined structures.

A predicted structure, however, is not a functional assay. It may provide a useful fold or surface geometry while leaving catalytic activity, ligand specificity, cellular localization, regulation, and biological context unresolved. Structural confidence may also vary across domains, flexible regions, and disordered segments. AlphaFold 3 extends structure prediction to biomolecular interactions, but the existence of a predicted interaction structure should likewise not be interpreted as direct evidence that the interaction occurs in a particular biological context [8].

## Methods and Datasets Observed

The directly relevant studies indicate several broad data configurations.

First, structure-based models link protein structures to functional labels [1]. These structures may be experimentally determined or predicted, but the supplied evidence does not specify the proportion of each type, the structural databases involved, or the preprocessing and quality-control procedures [VERIFY]. Functional labels may be drawn from ontology-based annotation systems, although the precise ontology, release, and annotation filters are not available in the supplied records [VERIFY].

Second, sequence-based approaches use large unlabeled sequence collections for representation learning and smaller labeled datasets for downstream prediction [2]. The exact sequence repositories and training corpora are not identified here [VERIFY]. This distinction between pretraining data and supervised training data is important: a model can benefit from millions of unlabeled sequences while still having relatively few reliable examples for a particular function.

Third, specialized metalloprotein studies use curated protein or residue-level datasets [3]. The supplied evidence does not establish how positive and negative examples were defined, whether homologous sequences were removed, or how structural and biochemical labels were reconciled [VERIFY]. These choices can substantially affect apparent performance.

The AlphaFold Protein Structure Database represents a further category of resource: a very large predicted-structure repository rather than a uniformly experimentally validated functional dataset [5]. It can make structural methods applicable to proteins without solved structures, but it also introduces uncertainty associated with prediction quality and incomplete biological context.

Across these settings, the construction of negative examples is a major methodological issue. The absence of an annotation does not necessarily mean that a protein lacks the corresponding function. This is especially problematic for multilabel prediction, in which one protein may legitimately possess several molecular functions, biological processes, and cellular localizations. Annotation density is also likely to be uneven, with better-characterized proteins and common functions receiving more extensive curation than poorly studied proteins or rare functional categories [VERIFY].

### Evaluation metrics

The supplied records do not provide sufficient detail to identify a consistent set of metrics used by the principal protein-function prediction studies. In comparable multilabel classification settings, researchers may report precision, recall, F1 score, maximum F1, and area under the precision–recall curve, either per function or aggregated across proteins [VERIFY]. Coverage or the number of recovered annotations may also be relevant [VERIFY].

For binary or residue-level tasks, including some metalloprotein applications, sensitivity, specificity, accuracy, Matthews correlation coefficient, and ROC-AUC may be used [VERIFY]. Because functional datasets can be highly imbalanced, precision–recall measures are often more informative than ROC-AUC alone, particularly when positive examples are rare. This point should not be taken as evidence that every cited study used these metrics; the exact reporting must be verified from the full articles.

Comparisons across studies are difficult when they use different annotation releases, taxonomic groups, ontology terms, thresholds, or definitions of a negative example. A further concern is homology leakage. If closely related proteins occur in both training and test sets, a model may appear to predict function while largely recognizing family similarity. Kapoor and Narayanan discuss leakage and reproducibility as general problems in machine-learning research [9]. Whether the individual protein-function studies used appropriate homology-aware splits is not established by the supplied evidence [VERIFY].

## Research Gaps

Several gaps remain evident.

**More reliable benchmark design is needed.** Protein-function benchmarks should report the source and release of annotations, the treatment of unannotated proteins, the degree of sequence redundancy, and the taxonomic composition of each split. Homology-aware evaluation is particularly important for testing performance on genuinely novel proteins rather than close relatives.

**The field needs better assessment of generalization.** A model may perform well on common protein families but fail on remote homologues, proteins from underrepresented organisms, proteins with novel folds, or rare functional classes. Benchmark performance should therefore be separated from evidence of transfer to biologically distant proteins.

**Uncertainty should be reported more explicitly.** High-confidence predictions are not necessarily correct, and confidence scores may be poorly calibrated when the test distribution differs from the training distribution. Evaluation should distinguish confidence calibration, ranking quality, and classification accuracy [VERIFY].

**Sequence and structure should be integrated with biological context.** Static sequence or structure may not capture cofactors, post-translational modifications, cellular localization, complex membership, environmental conditions, or substrate availability. Models that combine structural information with interaction, expression, biochemical, or evolutionary data may offer a more realistic account of function, but the supplied evidence does not establish how often such integration has been achieved successfully [VERIFY].

**Interpretability requires stronger validation.** Residue-level attributions or salient graph features may suggest a functional site, but they do not by themselves demonstrate mechanism. Explanations should be assessed against mutagenesis, biochemical assays, structural experiments, or other independent evidence [VERIFY].

**Experimental validation remains underdeveloped.** Computational predictions are most useful when they guide targeted experiments. More studies are needed that prospectively test predictions rather than evaluating only against existing annotations, which may reproduce biases in the databases used for training.

## Limitations

This review is limited by the supplied evidence set. Only one cited record is clearly a direct study of structure-based protein-function prediction [1], while several others are reviews or address adjacent problems such as protein structure prediction, docking, interaction prediction, drug discovery, or clinical biomarker modeling [2–8]. The available records do not provide enough detail to reconstruct the datasets, preprocessing procedures, model configurations, or evaluation protocols of the main function-prediction studies.

Consequently, statements about specific databases, Gene Ontology usage, classifier types, metric selection, class imbalance, and annotation quality have been marked [VERIFY] where the evidence is insufficient. The cited literature also spans different tasks and cannot support direct performance comparisons. Finally, the evidence does not permit a systematic quantitative assessment of how sequence-based, structure-based, and graph-based methods compare under a common benchmark.

## Conclusion

Machine learning is being used to predict protein function by learning associations between protein sequence, three-dimensional structure, interaction context, and functional annotation. The clearest directly supported approach is structure-based graph convolutional learning, in which proteins are represented through structural relationships and classified according to functional labels [1]. Protein language models provide a complementary sequence-based strategy, while specialized methods address narrower problems such as metalloprotein classification and metal-binding prediction [2,3]. Large predicted-structure resources, particularly AlphaFold and its associated database, make structural approaches feasible at an unprecedented scale, but they do not replace functional experiments [4,5].

The principal methodological weaknesses are not confined to model architecture. They also arise from incomplete and noisy annotations, ambiguous negative examples, class imbalance, inconsistent benchmarks, and the risk of homology leakage. Evaluation metrics are likely to include precision, recall, F1, precision–recall area, and ROC-AUC, but the supplied evidence is insufficient to attribute particular metrics systematically to the central studies [VERIFY]. Progress will depend on transparent datasets, homology-aware splits, calibrated uncertainty, evaluation on remote and underrepresented proteins, and experimental testing of genuinely novel predictions.

## References

1. Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.

2. Bordin N, Dallago C, Heinzinger M, et al. Novel machine learning approaches revolutionize protein knowledge. 2023. PMID:36504138.

3. Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID:35209064.

4. Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. 2021. doi:10.1038/s41586-021-03819-2.

5. Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.

6. Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein-protein interaction. 2023. PMID:36841846.

7. Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID:38987466.

8. Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. 2024. doi:10.1038/s41586-024-07487-w.

9. Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.