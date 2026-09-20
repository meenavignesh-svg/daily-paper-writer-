# Title

**Artificial Intelligence and Machine Learning for Protein Function Prediction: Methods, Data, Evaluation, and Remaining Limitations**

## Abstract

Machine learning is increasingly used to infer protein function from sequence, structure, interaction networks, and experimentally measured molecular phenotypes. The evidence considered here suggests three main directions: sequence-based representation learning with protein language models; structure-based prediction using graph neural networks; and specialized models for interactions, metal-binding proteins, ligand recognition, and activity-related properties. Among the supplied records, the most direct study of protein-function prediction is a structure-based graph convolutional network approach [1]. Broader reviews describe the use of learned protein representations and machine learning across protein science [2,3]. However, the available metadata do not establish the precise datasets, labels, train–test splits, or numerical evaluation results for most of these studies. Consequently, claims about the superiority of particular architectures or benchmark scores require full-text verification [VERIFY]. The principal limitations are noisy and incomplete annotations, class imbalance, homology-related information leakage, weak out-of-distribution generalization, and the difficulty of translating predictive performance into experimentally confirmed biological function.

## Introduction

Protein function prediction encompasses several related but distinct tasks. A model may assign a protein to a broad functional class, predict Gene Ontology or Enzyme Commission terms, identify a catalytic or ligand-binding site, infer a molecular interaction, or estimate biochemical activity. These endpoints should not be treated as interchangeable. Protein–protein interaction prediction, molecular docking, virtual screening, and structure prediction can support functional inference, but none is equivalent to direct functional annotation.

Machine learning is attractive in this setting because protein sequences and structures contain patterns that are difficult to capture with manually designed rules alone. Recent methods learn representations from large sequence collections, structural graphs, interaction networks, or combinations of these data types. Protein language models provide one route to sequence representation learning, while graph-based methods can model spatial relationships among residues. Structure prediction systems such as AlphaFold have further increased the availability of structural information, although predicted structure should be regarded as an input to functional analysis rather than a functional label in itself [4,5].

The supplied literature is heterogeneous. Only a limited subset directly addresses protein-function prediction. Other records concern protein structure prediction, protein design, drug discovery, disease biomarkers, clinical prediction, or therapeutic response. These studies are relevant as methodological context but cannot be used as direct evidence that a model predicts protein function.

## Evidence Synthesis

### Sequence-based representation learning

Protein language models and transformer-based methods learn numerical representations from amino-acid sequences. These representations can subsequently be used in supervised or semi-supervised models for tasks such as functional classification, activity prediction, ligand or substrate specificity, and variant prioritization. The review by Bordin and colleagues describes the broader use of machine learning to extract biological information from protein sequences and other molecular data [2].

The advantages of sequence-based models include their ability to use information from large sequence collections and to represent relationships that may not be evident from short sequence motifs. They may also be useful when experimentally determined structures are unavailable. However, the supplied evidence does not identify the exact pretraining datasets, model architectures, annotation resources, or downstream benchmark protocols used in the relevant studies [VERIFY].

Tran and colleagues describe protein language models in the context of rapid directed evolution and epistatic interactions [6]. This is closely related to functional prediction because the model may help identify variants likely to retain or improve a molecular phenotype. Nevertheless, the title alone does not establish whether the study performs conventional protein-function annotation, predicts experimentally measured activity, or ranks variants for experimental testing. That distinction requires verification from the full text [VERIFY].

Transformers are also being applied to sequence-based virtual screening [7]. Such approaches may predict ligand-related properties or prioritize candidate interactions. They should not automatically be described as models of protein function unless the predicted endpoint is explicitly functional, such as enzymatic activity or a validated binding phenotype.

### Structure-based prediction

The clearest direct example in the supplied records is the study by Gligorijević and colleagues, which uses graph convolutional networks for structure-based protein function prediction [1]. In this formulation, a protein is represented as a graph, enabling the model to learn from relationships among spatially related structural elements. This is potentially important because residues that are distant in sequence may be adjacent in three-dimensional space and may jointly form a functional site.

The available evidence does not specify whether the graph nodes represent residues, atoms, domains, or another structural unit. It also does not establish which node and edge features were used, whether structures were experimentally determined or computationally predicted, or which functional labels were assigned [VERIFY]. These details are central to interpreting the model and assessing whether it learns general structural principles or primarily exploits similarities among related proteins.

AlphaFold and AlphaFold 3 provide important structural resources and demonstrate the progress of deep learning for predicting protein structures and biomolecular interactions [4,5]. The AlphaFold Protein Structure Database has also expanded the amount of predicted structural information available for protein sequences [8]. Nevertheless, structure prediction and function prediction remain separate problems. A structurally plausible model does not by itself determine catalytic activity, cellular role, localization, substrate specificity, or interaction consequences.

### Specialized functional prediction

Machine learning is also used for narrower functional questions. Yu and colleagues review applications to metalloproteins, a category in which relevant tasks may include identifying metal-binding proteins, locating binding sites, predicting coordination properties, or classifying metal-dependent activities [3]. These examples illustrate that functional prediction can operate at different resolutions: the whole protein, a domain, an individual residue, a binding site, or a particular biochemical phenotype.

The supplied record does not identify the databases, label definitions, negative examples, or evaluation protocols used across the metalloprotein literature [VERIFY]. This uncertainty matters because specialized datasets may be substantially smaller and more biased than general protein sequence collections.

### Interaction-informed approaches

Graph-learning methods have also been applied to protein–protein interaction prediction [9]. Interaction information can contribute to functional inference because proteins participating in related complexes or pathways may share biological roles. However, interaction prediction is an intermediate task rather than a direct functional annotation problem. Similarly, machine-learning methods for protein–protein docking [10] may improve interaction modeling without necessarily predicting the biological function of either partner.

A careful review should therefore distinguish among:

- direct prediction of protein function or ontology terms;
- prediction of biochemical activity or binding;
- prediction of residue-level functional sites;
- protein–protein interaction prediction;
- docking or structural modeling; and
- prediction of variant effects or directed-evolution outcomes.

These tasks may be connected, but they require different labels, data splits, and evaluation metrics.

## Methods and Datasets Observed

The supplied evidence indicates several broad classes of input data:

1. **Protein sequences.** Large sequence collections are used to train protein language models or derive embeddings for downstream prediction [2,6].
2. **Protein structures.** Structural representations support graph-based function prediction and other structure-informed models [1]. Predicted structures may also be used as inputs, although the specific studies and sources require verification [VERIFY].
3. **Functional annotations.** Possible labels include protein-level functional categories, Gene Ontology terms, Enzyme Commission classes, binding-site annotations, and experimentally measured activities. The supplied records do not establish which of these labels were used in each direct study [VERIFY].
4. **Interaction networks.** Protein–protein interaction data are used in graph-learning approaches and may provide indirect evidence of function [9].
5. **Specialized biochemical datasets.** Metalloprotein and metal-binding datasets represent more focused resources for particular functional classes [3].
6. **Variant and phenotype measurements.** Directed-evolution studies may combine sequence models with epistatic information and experimental measurements of variant performance [6], although the precise data sources and endpoints require verification [VERIFY].

The bibliography does not provide sufficient evidence to name particular databases as having been used in the relevant experiments. UniProt, Gene Ontology, the Protein Data Bank, AlphaFold DB, CAFA benchmarks, enzyme databases, and specialized metalloprotein resources are plausible categories, but their use in the cited studies cannot be confirmed from the supplied records alone [VERIFY].

The choice of data split is especially important. Random sequence-level splits can place highly similar proteins in both training and test sets. In that situation, a model may appear to generalize while largely recognizing homology. More demanding alternatives include sequence-identity-controlled splits, protein-family splits, and temporal or structurally dissimilar test sets. The supplied metadata do not reveal which of these strategies were used in the direct prediction studies [VERIFY]. Information leakage is a broader reproducibility concern in machine-learning research and can lead to overestimated performance when related information crosses the boundary between training and evaluation data [11].

The available evidence also does not report the numerical evaluation metrics used by the relevant protein-function studies. Depending on the task, appropriate measures may include precision, recall, F1 score, area under the receiver-operating-characteristic curve, area under the precision–recall curve, and ranking measures such as precision at a defined cutoff. For multilabel ontology prediction, macro- and micro-averaged scores can behave differently in the presence of frequent and rare functions. Ontology-aware measures may also be appropriate, although their use in the cited studies requires verification [VERIFY].

Residue-level site prediction may require sensitivity, specificity, Matthews correlation coefficient, or site-level precision and recall. Activity prediction may use regression measures or classification metrics, while interaction and docking models may use ranking or structural-recovery measures. These scores should not be compared as though they evaluated the same biological task. Accuracy alone is potentially misleading when functional classes are highly imbalanced [VERIFY].

## Research Gaps

Several gaps remain evident from the supplied literature.

First, the field needs clearer separation of prediction targets. “Protein function” may refer to ontology annotation, enzymatic activity, ligand binding, cellular localization, interaction partners, or variant effects. Studies should state precisely which endpoint is being predicted and how it relates to experimentally testable biology.

Second, dataset construction requires greater transparency. Reports should specify the source of sequences, structures, annotations, and negative examples; the date of database retrieval; the treatment of conflicting annotations; and the extent of redundancy. This is particularly important for rare functions and poorly characterized protein families.

Third, evaluation should place greater emphasis on homology-aware and out-of-distribution testing. Performance on randomly split data may not reflect performance on novel protein families. Independent, family-held-out, temporal, or experimentally selected test sets would provide more informative evidence of generalization [VERIFY].

Fourth, direct experimental validation remains uneven. A high-confidence computational annotation is not necessarily a confirmed biological function. More studies should test predictions experimentally, especially for proteins outside the training distribution and for rare or weakly annotated functions.

Fifth, interpretability remains unresolved. Structure-based models may identify spatial regions associated with a prediction, but the supplied evidence does not establish whether these explanations are biologically faithful. General machine-learning guidance emphasizes the importance of linking model behavior to domain knowledge rather than treating post hoc explanations as definitive mechanisms [12].

Finally, multimodal integration requires careful assessment. Combining sequence, structure, interaction, and experimental data may improve prediction, but it can also introduce additional leakage, missing-data biases, and difficult-to-interpret dependencies. The benefit of each information source should be evaluated under controlled splits rather than inferred from performance on a single benchmark [VERIFY].

## Limitations

This review is constrained by the evidence supplied. The bibliography contains only a small number of papers directly focused on protein-function prediction, and the available records are primarily citation metadata rather than full study descriptions. Consequently, the exact datasets, preprocessing procedures, model architectures, train–test splits, baselines, metrics, and numerical results cannot be established for most cited studies.

Several records concern related but distinct topics, including clinical prediction, cancer biology, drug response, virtual screening, protein design, docking, and protein structure prediction. They have been used only as context where appropriate and not as direct evidence of protein-function annotation. In addition, some records are reviews, so their presence does not establish that every method or dataset discussed was evaluated in a primary protein-function prediction experiment.

Specific claims about the use of Gene Ontology, Enzyme Commission labels, UniProt, PDB, CAFA, AlphaFold DB, or particular evaluation protocols remain [VERIFY]. The supplied evidence also does not permit a quantitative comparison of sequence-based, structure-based, and interaction-based approaches.

## Conclusion

Machine learning is being used to predict protein function through several complementary representations. Protein language models convert sequence information into learned embeddings for downstream prediction; graph neural networks use spatial relationships in protein structures; and related models incorporate interactions, metal-binding information, ligand-related properties, or measured variant phenotypes. The most direct evidence in the supplied records concerns structure-based graph convolutional networks for protein-function prediction [1], supported by broader reviews of machine learning in protein science [2,3].

The central methodological challenge is not simply selecting a more complex model. Reliable evaluation depends on well-defined functional labels, carefully constructed datasets, homology-aware splits, appropriate metrics, and experimental validation. At present, the supplied evidence does not provide enough detail to determine which datasets or evaluation procedures dominate the field. The remaining limitations—annotation noise, class imbalance, information leakage, limited coverage of rare proteins, and uncertain generalization to novel families—mean that reported predictive performance should be interpreted cautiously. Progress will depend on transparent benchmarks and stronger links between computational predictions and experimentally demonstrated molecular function.

## References

[1] Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.

[2] Bordin N, Dallago C, Heinzinger M, et al. Novel machine learning approaches revolutionize protein knowledge. 2023. PMID: 36504138.

[3] Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID: 35209064.

[4] Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. 2021. doi:10.1038/s41586-021-03819-2.

[5] Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. 2024. doi:10.1038/s41586-024-07487-w.

[6] Tran VQ, Nemeth M, Bartie LJ, et al. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID: 41712694.

[7] Zhang S, Huo D, Horne RI, et al. Sequence-based virtual screening using transformers. 2025. PMID: 40721411.

[8] Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.

[9] Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein-protein interaction. 2023. PMID: 36841846.

[10] Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID: 38987466.

[11] Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.

[12] Greener JG, Kandathil SM, Moffat L, Jones DT. A guide to machine learning for biologists. 2021. doi:10.1038/s41580-021-00407-0.