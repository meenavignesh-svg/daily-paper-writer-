# Title

**Artificial Intelligence and Machine Learning for Protein Function Prediction: Methods, Data, Evaluation, and Remaining Challenges**

## Abstract

Machine-learning approaches to protein function prediction increasingly combine amino-acid sequence information, structural representations, molecular interactions, and experimentally measured phenotypes. The supplied literature indicates three principal strategies: sequence-based models, including transformer and protein-language-model representations; structure-based models, particularly graph neural networks; and interaction- or ligand-informed approaches that infer function from molecular context. Among the records reviewed, only one paper is explicitly focused on protein-function prediction: a graph-convolutional framework using structural representations [1]. Other studies address closely related problems, including protein structure prediction, protein–protein interactions, ligand affinity, mutation effects, protein design, and drug response. These studies demonstrate the expanding methodological landscape but cannot be treated as direct evidence of performance on general functional annotation. Likely data sources include annotated protein sequences, experimentally determined or predicted structures, interaction networks, ligand-binding measurements, and specialized metalloprotein datasets. However, the supplied records do not consistently identify the datasets, labels, train–test splits, or evaluation metrics used. Important unresolved issues include incomplete and biased annotations, homology leakage, class imbalance, uncertain structural inputs, limited interpretability, and weak validation on evolutionarily distant proteins. More rigorous reporting should include homology-controlled evaluation, external experimental testing, label-frequency-stratified performance, calibration, and uncertainty estimates.

## Introduction

Protein function prediction seeks to infer what a protein does from available biological information. Depending on the application, “function” may refer to molecular activity, ligand binding, catalytic class, interaction partners, subcellular role, biological process, or a combination of these properties. This breadth makes the problem substantially more complicated than ordinary single-label classification. A single protein may have several functions, and functional annotations are often hierarchical, incomplete, and unevenly distributed across protein families.

Machine learning is being used to address this problem by converting protein information into representations that can be associated with known functional labels or experimentally measured properties. Sequence models learn from amino-acid patterns; structural models represent residues and their spatial relationships; and network-based methods exploit interactions among proteins. More specialized models predict properties such as ligand affinity, metal coordination, mutation effects, or activity. These predictions can support functional inference, but they are not interchangeable with general protein-function annotation.

The supplied evidence must therefore be interpreted carefully. The bibliography contains one clearly relevant primary study, *Structure-based protein function prediction using graph convolutional networks* [1]. It also contains several reviews and studies of related computational tasks, including AlphaFold-based structure prediction [2], the AlphaFold Protein Structure Database [3], protein–protein interaction learning [4], sequence-based virtual screening [5], metalloprotein modelling [6], and protein-language-model-guided evolution [7]. The latter studies help describe available methods and data modalities, but they do not by themselves establish how accurately machine learning predicts protein function in the broad sense.

## Evidence Synthesis

### Sequence representations and protein language models

Sequence-based machine learning uses amino-acid sequences as the primary source of information. Earlier approaches commonly relied on manually designed features or sequence similarity, whereas contemporary systems increasingly use learned representations from deep neural networks and transformers. The supplied record on sequence-based virtual screening illustrates the use of transformer models for extracting information from protein sequences [5]. The study of protein-language-model-guided directed evolution similarly indicates that learned sequence representations can help estimate properties of variants and guide experimental selection [7].

These approaches are attractive because sequence data are abundant and can be used when no reliable three-dimensional structure is available. A sequence model may function as a classifier, rank candidate functional annotations, or provide embeddings that are subsequently combined with structural, evolutionary, or experimental features. Nevertheless, the cited records do not establish whether the models predict Gene Ontology terms, enzyme classes, binding sites, or another formal definition of protein function [VERIFY]. In particular, sequence-based virtual screening and directed evolution generally concern narrower endpoints—such as binding, activity, stability, or variant performance—rather than comprehensive functional annotation.

Sequence representations also face biological limitations. Similar sequences may have different functions, while paralogues can retain substantial sequence similarity but diverge in substrate specificity, interaction partners, or cellular role. Conversely, proteins with limited sequence identity may adopt related folds or perform analogous functions. Models trained on randomly divided sequence collections may therefore appear successful partly because related proteins occur in both training and test sets.

### Structure-based models

Structural information provides a second major route to function prediction. The directly relevant study by Gligorijević and colleagues uses graph convolutional networks to predict protein function from structural representations [1]. In this formulation, a protein is represented as a graph, with nodes and edges encoding molecular entities and their relationships. Graph-based models can capture local structural environments as well as longer-range relationships that are difficult to express in a linear sequence.

The supplied evidence does not specify the precise functional labels used in [1], nor whether the input structures were experimentally determined, computationally predicted, or a mixture of both [VERIFY]. These details are important because structural quality can vary substantially, especially in flexible regions, disordered segments, multidomain proteins, and proteins lacking close structural templates.

AlphaFold has expanded the availability of predicted protein structures and is therefore relevant as an enabling technology for downstream functional analysis [2]. The AlphaFold Protein Structure Database provides predicted structures for a very large number of protein sequences [3]. Such coverage could allow structure-based methods to be applied to proteins for which no experimentally solved structure exists. However, the supplied records do not show that the graph-convolutional function-prediction study specifically used AlphaFold-derived structures [VERIFY]. Predicted structures should not be treated as equivalent to experimentally validated conformations: uncertainty in the input may propagate into the functional prediction.

The development of models for biomolecular interactions, including AlphaFold 3, further illustrates the movement toward integrated structural representations [8]. These systems are relevant to function-related questions involving complexes, ligands, and other molecular partners, but structural prediction remains distinct from functional annotation.

### Interaction and network-based approaches

Protein–protein interactions provide contextual evidence about biological role. A protein’s interaction partners, network position, or residue-level contact patterns may help identify pathways and functional categories. The hierarchical graph-learning study on protein–protein interaction prediction is therefore methodologically relevant [4]. It demonstrates how graph-based learning can model biological relationships at multiple levels.

Interaction prediction should nevertheless be distinguished from protein-function prediction. A predicted interaction may support a functional hypothesis, but it does not necessarily identify the biochemical activity or cellular role of a protein. Interaction data are also affected by incomplete experimental coverage, species-specific biology, assay bias, and false positives or false negatives. The supplied evidence does not provide sufficient detail about the interaction datasets, label definitions, or evaluation design used in [4] [VERIFY].

### Ligand, metal, and mutation-related properties

A number of records address narrower molecular properties that can contribute to function inference. These include protein–ligand affinity ranking, virtual screening, metalloprotein modelling, drug-resistance mutations, and protein design [6, 9–12]. A model that predicts ligand binding, metal coordination, catalytic environments, or the effect of a mutation may reveal a specific aspect of protein function. Such predictions can be especially informative when experimental annotations are sparse.

These endpoints should not, however, be conflated with general function prediction. Binding affinity is not identical to biological activity, and a mutation associated with drug resistance does not necessarily define the complete function of the affected protein. The metalloprotein review is particularly relevant to specialized functional inference involving metal-binding proteins, although the exact datasets and metrics discussed there cannot be recovered from the supplied evidence [VERIFY].

### Functional labels and the meaning of prediction

General protein-function prediction is commonly framed as a multi-label problem because proteins may receive several annotations at different levels of specificity. Ontology-based labels are plausible in this context, but the evidence supplied does not confirm that the directly relevant study used Gene Ontology terms [VERIFY]. Other possible targets include enzyme classifications, protein families, binding-site categories, cellular localizations, or experimentally measured activities.

This distinction matters for both modelling and evaluation. Predicting a broad functional category is easier than predicting a specific molecular activity. Similarly, a model may achieve high performance on proteins from well-represented families while performing poorly on remote homologues or poorly annotated organisms. A single aggregate score cannot adequately describe this variation.

## Methods and Datasets Observed

The records indicate several methodological families:

1. **Graph convolutional and graph-learning models.** These represent proteins or molecular interaction systems as graphs and learn from structural or relational information [1, 4].  
2. **Transformer and protein-language-model approaches.** These learn sequence representations and can be applied to virtual screening, variant prioritization, or related property-prediction tasks [5, 7].  
3. **Structure-prediction systems.** AlphaFold and related methods generate structural inputs that may subsequently be used for function-related modelling [2, 8].  
4. **Integrated molecular modelling.** Other studies combine machine learning with molecular dynamics, virtual screening, docking, or biological validation to predict ligand interactions, resistance-associated variants, or therapeutic targets [9–12].  
5. **Specialized predictors.** Metalloprotein-focused methods address restricted classes of proteins and functional properties [6].

The likely datasets span several categories:

- annotated protein sequence databases;
- experimentally determined protein structures;
- predicted structural models, including AlphaFold-derived structures;
- protein–protein interaction databases;
- protein–ligand and affinity measurements;
- mutation and activity datasets;
- specialized collections of metalloproteins; and
- ontology-based functional annotations.

For most records, the exact dataset names, sample sizes, inclusion criteria, preprocessing steps, and label definitions are not provided. These details therefore require verification from the full texts [VERIFY]. The same applies to the use of experimentally validated labels versus computationally transferred annotations.

The supplied evidence also does not report the evaluation metrics used in the directly relevant function-prediction paper [VERIFY]. For multi-label functional prediction, relevant measures may include precision, recall, F1 score, receiver-operating-characteristic area under the curve, and precision–recall area under the curve. Ranking metrics may be appropriate when models return an ordered list of candidate functions, while ontology-aware measures may be needed when predictions at different levels of the functional hierarchy are considered.

Metric selection is particularly important under severe class imbalance. ROC-AUC can remain high when positive labels are rare, whereas precision–recall measures may provide a more informative view of performance for infrequent functions. Reporting only a global average can also hide poor performance on rare terms or on proteins from evolutionarily distant families. A robust evaluation should therefore report results by label frequency, functional category, sequence-similarity regime, and taxonomic or family-level holdout where possible [VERIFY].

## Research Gaps

Several gaps remain evident.

First, the distinction between general function prediction and related molecular-property prediction is not always made clearly. Binding, interaction, stability, drug response, and mutation-effect models may support functional inference, but they should be evaluated against the specific biological question being asked.

Second, the datasets and labels used by many studies are insufficiently characterized in the supplied evidence. Reproducibility requires explicit reporting of annotation sources, release dates, redundancy filtering, label propagation, missing-label treatment, and the definitions of positive and negative examples.

Third, evaluation should better reflect the intended use case. Random protein-level splits can place highly similar sequences in both training and test sets, producing optimistic estimates. Homology-controlled splits, species-level holdouts, family-level holdouts, and temporal validation would provide stronger evidence of generalization. The broader literature on leakage and reproducibility in machine learning emphasizes the importance of preventing information from crossing the training–test boundary [13].

Fourth, external experimental validation remains important. A computational prediction may be internally consistent yet biologically incorrect, particularly when annotations are noisy or structures are uncertain. The supplied records include examples of integrated computational and in vivo or experimental workflows, but they do not establish how frequently such validation is used for general function prediction [VERIFY].

Fifth, uncertainty and calibration require greater attention. A ranked prediction without a confidence estimate is difficult to interpret when proteins fall outside the training distribution. Structural uncertainty, annotation uncertainty, and evolutionary novelty should be considered explicitly.

Finally, interpretability remains unresolved. Feature-attribution tools such as SHAP can help examine model outputs in supervised learning [14], but an interpretable score does not necessarily provide a mechanistic explanation. Functional models should ideally identify sequence residues, structural regions, interaction partners, or molecular environments that support the prediction and should distinguish correlation from causation.

## Limitations

This review is constrained by the supplied evidence rather than by a systematic examination of the full literature. The bibliography contains only one clearly identified primary study devoted specifically to structure-based protein-function prediction [1]. Many other records concern adjacent applications, and their relevance to general function prediction is inferential.

The supplied material does not consistently provide full-text methodological details. Consequently, the exact datasets, labels, model architectures, train–test partitions, hyperparameter procedures, evaluation metrics, and validation experiments cannot be stated reliably for most studies. Where such information is absent, it has been marked [VERIFY] rather than inferred as fact.

The evidence base is also heterogeneous. It includes primary research articles, reviews, broad methodological papers, and studies in clinical or drug-discovery settings. These records should not be compared as though they evaluated the same prediction task. In addition, the citation list may not represent the full range of protein-function prediction methods, including classical homology-based approaches, profile methods, and other deep-learning systems not included here.

## Conclusion

Machine learning is being used to predict protein function through several complementary representations. Sequence models and protein language models learn information from amino-acid order; graph-based methods encode structural relationships or interaction networks; and integrated approaches predict more specific properties such as ligand binding, metal coordination, mutation effects, and molecular activity. Structure-prediction systems such as AlphaFold can provide useful inputs for downstream analysis, although structure prediction itself is not function prediction.

The strongest directly relevant evidence in the supplied records concerns a graph-convolutional approach to structure-based function prediction [1]. The wider set of studies demonstrates the expanding computational infrastructure around the problem but does not establish a common benchmark or a unified definition of function. Progress is therefore limited not only by model design but also by the quality of annotations, the incompleteness of biological datasets, and the difficulty of evaluating genuinely novel proteins.

Future studies should report datasets and labels in detail, use homology-aware splits, evaluate rare and hierarchical functions explicitly, quantify uncertainty, and validate predictions experimentally where possible. Without these safeguards, apparently strong performance may reflect annotation bias, data leakage, or recognition of familiar protein families rather than reliable prediction of function for uncharacterized proteins.

## References

[1] Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.

[2] Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. 2021. doi:10.1038/s41586-021-03819-2.

[3] Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.

[4] Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein–protein interaction. 2023. PMID:36841846.

[5] Zhang S, Huo D, Horne RI, et al. Sequence-based virtual screening using transformers. 2025. PMID:40721411.

[6] Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID:35209064.

[7] Tran VQ, Nemeth M, Bartie LJ, et al. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID:41712694.

[8] Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. 2024. doi:10.1038/s41586-024-07487-w.

[9] Brown BP. A generalizable deep learning framework for structure-based protein–ligand affinity ranking. 2025. PMID:41100673.

[10] Xie L, Lockhart C, Klimov DK, Jafri MS. Combining molecular dynamics and machine learning to predict drug resistance causing variants of BRAF in colorectal cancer. 2025. PMID:40942081.

[11] Schauperl M, Denny RA. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges. 2022. PMID:35727311.

[12] Michalik I, Kuder KJ. Machine Learning Methods in Protein–Protein Docking. 2024. PMID:38987466.

[13] Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.

[14] Ponce Bobadilla AV, Schmitt V, Maier CS, et al. Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development. 2024. doi:10.1111/cts.70056.