# Title

**Artificial Intelligence and Machine Learning in Protein Function Prediction: Methods, Data Resources, Evaluation, and Remaining Limitations**

## Abstract

Machine learning is increasingly used to infer protein function from amino-acid sequence, three-dimensional structure, molecular interactions, and related biological measurements. The supplied literature indicates several complementary directions: structure-based function prediction with graph convolutional networks, sequence-based modelling with transformers and protein language models, prediction of protein–protein interactions, and annotation of specialised protein classes such as metalloproteins [6,14,15,26]. Structure-prediction systems, particularly AlphaFold and AlphaFold 3, have also expanded the structural information available for downstream functional inference [1,10,21,22]. However, the evidence supplied here is insufficient to establish a consistent set of datasets, benchmark partitions, or evaluation metrics across studies. The AlphaFold Protein Structure Database is identified as providing structural coverage for more than 214 million protein sequences, but the role of this resource in specific function-prediction benchmarks is not documented in the available records [29]. Important limitations remain, including incomplete and uneven functional annotations, dependence on predicted rather than experimentally determined structures, possible information leakage between training and test data, limited interpretability, and uncertain transfer to evolutionarily distant proteins. More systematic and biologically realistic evaluation will be needed before high predictive performance can be equated with reliable functional knowledge.

## Introduction

Protein function prediction seeks to infer what a protein does from available molecular information. Depending on the task, this may involve assigning functional annotations, identifying catalytic or binding properties, predicting interaction partners, or distinguishing members of a specialised protein family. Machine-learning methods are attractive because proteins can be represented in several high-dimensional forms: as amino-acid sequences, structural graphs, molecular interaction networks, or combinations of these data types.

The literature supplied for this review reflects a field that is broader than annotation alone. General discussions of machine learning in protein science include structure prediction, protein design, molecular docking, virtual screening, and protein engineering [1,10,11,17]. Among the records, the most directly relevant studies concern computational prediction of protein functional annotations [20] and structure-based prediction using graph convolutional networks [26]. Other records address protein–protein interactions [14], sequence-based screening with transformers [15], metalloproteins [6], and the use of protein language models to guide directed evolution [3]. These examples suggest that function prediction is increasingly treated as a multimodal problem rather than as a task based solely on sequence similarity.

At the same time, structural prediction has become an important enabling technology. AlphaFold demonstrated highly accurate protein structure prediction [21], while AlphaFold 3 extended the scope of structure prediction to biomolecular interactions [22]. The resulting structural resources may support functional inference, although a predicted structure does not by itself establish a biological function. The distinction between structural plausibility and functional evidence is therefore central to interpreting machine-learning predictions.

## Evidence Synthesis

The supplied records indicate three principal ways in which machine learning is being applied to protein function prediction.

First, models are trained directly on protein sequences. Transformer-based methods are explicitly represented by the record on sequence-based virtual screening [15], while protein language models are discussed in relation to rapid directed evolution and epistatic interactions [3]. Protein language models learn statistical regularities from large collections of sequences and can provide representations for downstream prediction. These representations may capture evolutionary constraints or sequence patterns associated with activity, binding, localisation, or family membership. However, the supplied evidence does not specify which functional labels were predicted in these studies, how the sequence data were partitioned, or which metrics were used [VERIFY].

Second, proteins can be represented through their structures. The study titled *Structure-based protein function prediction using graph convolutional networks* indicates the use of graph-based deep learning to associate structural information with functional annotations [26]. In this setting, residues or atoms may be represented as nodes and their spatial relationships as edges, allowing a model to learn local and global structural patterns. The record establishes the broad methodological direction, but the supplied evidence does not provide the graph construction procedure, annotation ontology, benchmark dataset, or reported performance [VERIFY].

Third, machine learning is being applied to interaction and network-level problems. Hierarchical graph learning has been used for protein–protein interaction prediction [14], and machine-learning methods for protein–protein docking are reviewed elsewhere in the supplied literature [11]. Such approaches are relevant to function because interaction partners can provide contextual evidence about biological roles. Nevertheless, interaction prediction and function annotation are not interchangeable tasks. A model may identify a likely interaction without establishing the biochemical or cellular consequence of that interaction.

Specialised predictors also appear in the evidence. Metalloproteins present distinctive challenges because their function depends partly on metal identity, coordination geometry, and local chemical environment; a dedicated review discusses machine-learning approaches for this class of proteins [6]. More general reviews of computational functional annotation place these specialised applications within a wider annotation framework [20]. The available information does not allow comparison between specialised models and general-purpose sequence or structure models.

Structure-prediction systems provide an important source of input rather than a complete solution. AlphaFold and AlphaFold 3 are represented as major developments in protein and biomolecular structure prediction [21,22]. The AlphaFold Protein Structure Database is reported to provide structural coverage for over 214 million protein sequences [29]. This scale creates opportunities for structure-based annotation of proteins lacking experimentally determined structures. However, the presence of a predicted structure does not guarantee that the corresponding functional annotation is correct. Structural similarity may support a functional hypothesis, but function can also depend on dynamics, cofactors, cellular context, post-translational modification, oligomeric state, and interaction partners. These factors are not shown to be resolved by the supplied records [VERIFY].

The literature also points to a growing role for models that combine machine learning with experimental or computational workflows. Protein language models have been used to guide directed evolution [3], and related approaches include sequence design with ProteinMPNN [25] and computational screening for molecular discovery [7,8,12]. These applications are adjacent to function prediction: they use learned representations to identify or design proteins with desired properties. They should not, however, be treated as direct evidence that a model has correctly assigned a biological function.

## Methods and Datasets Observed

The evidence set contains several types of input data:

1. **Protein sequences.** Sequence-based transformers and protein language models are represented by records on virtual screening and directed evolution [3,15]. The specific sequence repositories, sequence lengths, taxonomic composition, and annotation sources are not reported in the supplied evidence [VERIFY].

2. **Predicted and experimental structures.** AlphaFold and AlphaFold 3 provide the structural-prediction context [21,22]. The AlphaFold Protein Structure Database is reported to contain structural coverage for more than 214 million protein sequences [29]. The evidence does not establish whether the function-prediction studies used this database directly, nor how confidence scores or unresolved regions were handled [VERIFY].

3. **Structure-derived graphs.** Graph convolutional networks have been used for structure-based protein function prediction [26]. A separate record describes hierarchical graph learning for protein–protein interaction prediction [14]. Details of nodes, edges, graph pooling, and model architecture are not available in the supplied summary [VERIFY].

4. **Interaction and docking data.** Protein–protein interaction prediction and docking are covered by the records on hierarchical graph learning and machine-learning docking methods [11,14]. The source databases, negative-sample construction, and treatment of experimentally unobserved interactions are not specified [VERIFY].

5. **Specialised protein datasets.** Metalloproteins are the subject of a dedicated review [6]. The supplied evidence does not identify the metal classes, functional labels, or benchmark datasets considered [VERIFY].

The records indicate the use of deep learning, graph neural networks, transformers, protein language models, and more general machine-learning approaches [3,6,14,15,17,26]. However, the supplied evidence does not provide enough information to identify a common evaluation framework. Accuracy values, precision, recall, F1 scores, receiver-operating-characteristic areas, precision–recall areas, ranking metrics, calibration measures, and structure-specific scores are not documented in the material provided [VERIFY]. Nor is it possible to determine whether studies used random, sequence-identity-reduced, family-level, or taxonomically separated test sets. This omission is consequential because closely related proteins can appear in both training and test sets, producing overly optimistic estimates.

## Research Gaps

Several gaps emerge from the available evidence.

**Standardised, biologically realistic benchmarks are needed.** Function prediction should be evaluated on test proteins that are sufficiently separated from the training data in sequence, structure, and evolutionary context. The supplied record on leakage and reproducibility in machine-learning science highlights the broader importance of preventing information leakage [30]. Whether the protein-function studies applied such safeguards is not reported [VERIFY].

**The relationship between structure prediction and function prediction requires clearer evaluation.** Large structure databases may make structural representations available for many proteins [29], but it remains necessary to determine when a predicted structure improves annotation over sequence-only models. Comparisons should distinguish experimentally determined structures from predicted structures and should account for uncertainty in the latter.

**Functional labels remain heterogeneous.** “Protein function” may refer to molecular activity, biological process, cellular location, interaction, ligand binding, or membership in an ontology class. These tasks have different levels of ambiguity and different appropriate evaluation procedures. The supplied evidence does not show that existing studies use a unified definition [VERIFY].

**Interpretability and biological validation remain underdeveloped.** A model may perform well while relying on sequence or structural correlates that are not causally related to function. Model explanations, mutational analysis, biochemical assays, and independent experimental validation are therefore important. The records supplied do not provide enough information to assess how often such validation was performed [VERIFY].

**Generalisation to underrepresented proteins is uncertain.** Large sequence resources do not necessarily provide balanced representation across taxa, protein families, cellular environments, or functional classes. Rare functions and proteins with few homologues are likely to remain difficult, although the extent of this problem cannot be quantified from the supplied evidence [VERIFY].

## Limitations

This review is constrained by the nature of the supplied material. Most records are bibliographic entries or titles rather than detailed study summaries. Consequently, it is possible to identify broad methodological themes but not to reconstruct training procedures, dataset composition, label definitions, model hyperparameters, or performance results reliably.

The evidence set also includes studies that are adjacent to, rather than directly about, protein function prediction. Papers on protein structure prediction, docking, virtual screening, drug discovery, disease modelling, and clinical prediction provide relevant context but should not be interpreted as direct benchmarks of functional annotation [1,4,5,7,8,9,10,11,12,13,18,19]. In addition, the available records do not support a quantitative comparison between model classes. Specific evaluation metrics and numerical results are absent [VERIFY].

Finally, the presence of a large structural database or a sophisticated model architecture should not be taken as evidence of biological validity. The available information does not establish how predictions were experimentally confirmed, how uncertainty was communicated, or whether models were tested on genuinely novel protein families.

## Conclusion

Machine learning is being used to predict protein function through sequence models, protein language models, structure-based graph networks, interaction predictors, and specialised systems for protein classes such as metalloproteins [3,6,14,15,20,26]. Large-scale structure-prediction resources, including the AlphaFold Protein Structure Database, provide additional representations that may support annotation at a scale previously difficult to achieve [21,29]. Nevertheless, structure prediction, interaction prediction, and functional annotation remain distinct tasks.

The supplied evidence does not permit a reliable account of the datasets or evaluation metrics used across the literature. This lack of detail is itself important: without transparent dataset construction, leakage-resistant test sets, explicit label definitions, and consistent reporting of metrics, apparent improvements in predictive performance are difficult to interpret. Future progress will depend not only on larger models and broader databases, but also on rigorous evaluation, uncertainty estimation, interpretability, and experimental validation of predictions.

## References

[1] Chen L, Li Q, Nasif KFA, et al. *AI-Driven Deep Learning Techniques in Protein Structure Prediction.* 2024. PMID: 39125995.

[3] Tran VQ, Nemeth M, Bartie LJ, et al. *Rapid directed evolution guided by protein language models and epistatic interactions.* 2026. PMID: 41712694.

[6] Yu Y, Wang R, Teo RD. *Machine Learning Approaches for Metalloproteins.* 2022. PMID: 35209064.

[10] Schauperl M, Denny RA. *AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges.* 2022. PMID: 35727311.

[11] Michalik I, Kuder KJ. *Machine Learning Methods in Protein-Protein Docking.* 2024. PMID: 38987466.

[14] Gao Z, Jiang C, Zhang J, et al. *Hierarchical graph learning for protein-protein interaction.* 2023. PMID: 36841846.

[15] Zhang S, Huo D, Horne RI, et al. *Sequence-based virtual screening using transformers.* 2025. PMID: 40721411.

[20] Kulmanov M, Hoehndorf M. *Computational prediction of protein functional annotations.* 2025. PMID: 40728605.

[21] Jumper J, Evans R, Pritzel A, et al. *Highly accurate protein structure prediction with AlphaFold.* Nature. 2021. doi:10.1038/s41586-021-03819-2.

[22] Abramson J, Adler J, Dunger J, et al. *Accurate structure prediction of biomolecular interactions with AlphaFold 3.* Nature. 2024. doi:10.1038/s41586-024-07487-w.

[26] Gligorijević V, Renfrew PD, Kościółek T, et al. *Structure-based protein function prediction using graph convolutional networks.* 2021. doi:10.1038/s41467-021-23303-9.

[29] Váradi M, Bertoni D, Magaña P, et al. *AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences.* 2023. doi:10.1093/nar/gkad1011.

[30] Kapoor S, Narayanan A. *Leakage and the reproducibility crisis in machine-learning-based science.* 2023. doi:10.1016/j.patter.2023.100804.