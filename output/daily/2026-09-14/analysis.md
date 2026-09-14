The supplied evidence supports a relatively focused conclusion: machine learning is being used for protein-function prediction mainly by learning relationships between protein sequence or structure and functional annotations, but the directly relevant evidence in this set is limited. Many of the records concern protein structure prediction, protein–protein interactions, drug discovery, or clinical biomarkers rather than protein-function prediction itself.

### Main uses of machine learning

The clearest direct example is **structure-based function prediction** in Gligorijević et al. (2021), which represents proteins as structural graphs and applies graph convolutional networks. In this setting, residues or structural elements form graph nodes, while spatial contacts or other structural relationships form edges. The model then predicts functional annotations, most plausibly Gene Ontology terms covering molecular function, biological process, or cellular component [VERIFY]. This approach is intended to capture functional information that may not be apparent from primary-sequence similarity alone.

A second major direction is **sequence-based prediction using learned protein representations**. The review by Bordin et al. (2023) appears to cover protein language models, protein embeddings, and large-scale annotation. Such models learn statistical patterns from large protein-sequence corpora and can provide representations for downstream classification or multilabel prediction of function. The supplied record does not establish which specific language models, training corpora, or functional benchmarks that review discusses, so those details require verification.

Machine learning is also applied to **specialized functional categories**, such as metalloproteins. Yu et al. (2022) review methods for predicting metalloprotein classes, metal-binding residues, or related properties. These applications may use sequence descriptors, structural features, or conventional classifiers such as support-vector machines and random forests, alongside neural networks [VERIFY]. They illustrate that protein-function prediction is often decomposed into narrower tasks rather than treated as a single universal prediction problem.

A related but distinct use is **inference from protein interactions and networks**. Graph-learning studies such as Gao et al. (2023) predict protein–protein interactions, potentially providing indirect functional information through interaction partners or network context. However, interaction prediction should not be equated with direct Gene Ontology or biochemical-function prediction. Similarly, the protein–protein docking review by Michalik and Kuder (2024) is relevant to structural representations and interaction scoring but is not, on the supplied evidence, a direct function-prediction study.

Predicted structures are an important enabling technology. AlphaFold (Jumper et al., 2021) and the AlphaFold Protein Structure Database (Váradi et al., 2023) expand the number of proteins for which structural information is available. These structures can be supplied to downstream graph-based or structure-similarity models. They do not, however, constitute functional validation: a plausible predicted fold does not by itself establish catalytic activity, ligand specificity, cellular role, or biological process.

### Datasets and labels

The direct evidence suggests that function-prediction models are trained on proteins for which structural or sequence information can be linked to functional annotations. For the graph-convolutional study, the relevant data probably include experimentally determined and/or predicted structures paired with Gene Ontology labels, but the exact databases, filtering procedures, and split strategy are not provided in the supplied material [VERIFY].

Likewise, the metalloprotein literature probably uses curated positive and negative protein sets, structural databases, and residue-level metal-binding annotations [VERIFY]. The quality of these datasets is especially important because metal association can be structural, catalytic, or incidental, and these categories may not be consistently annotated.

Protein language-model approaches can use very large unlabeled sequence collections for pretraining and smaller labeled functional datasets for supervised prediction. The supplied evidence does not identify the precise sequence databases or annotation releases used by the relevant papers [VERIFY]. The AlphaFold database provides extensive predicted-structure coverage—reported in its title as more than 214 million protein sequences—but this is a structural resource, not a uniformly experimentally validated functional dataset.

An important issue is that functional labels are usually incomplete and unevenly distributed. Well-studied proteins and common Gene Ontology terms are more likely to be annotated than proteins from poorly characterized organisms or rare functional classes [VERIFY]. Functional prediction is also commonly multilabel: one protein may have several molecular functions, biological processes, and cellular localizations. This makes the construction of negative examples difficult, since an unannotated function is not necessarily an absent function.

### Evaluation metrics

The supplied records do not provide enough information to state which metrics were actually used in the principal function-prediction studies. Function-prediction work commonly reports precision, recall, F1 score or maximum F1, and precision–recall area under the curve, sometimes at the level of individual functions and sometimes at the protein level [VERIFY]. Coverage or the number of correctly recovered annotations may also be reported [VERIFY].

For specialized binary tasks such as metalloprotein or metal-binding prediction, studies may additionally report sensitivity, specificity, accuracy, Matthews correlation coefficient, and ROC-AUC [VERIFY]. ROC-AUC can be misleading when positive examples are rare, so precision–recall measures are often more informative for imbalanced annotation problems [VERIFY]. Exact comparisons between papers are difficult because they may use different ontology terms, annotation versions, thresholds, taxonomic groups, and definitions of a negative example.

A particularly important evaluation requirement is **homology-aware splitting**. Randomly dividing closely related proteins between training and test sets can make performance appear stronger because the model may recognize family or sequence similarity rather than infer function for genuinely novel proteins. The evidence identifies homology leakage and reproducibility as general machine-learning concerns, including in Kapoor and Narayanan (2023), but whether each protein-function study avoided this problem must be checked in the full texts [VERIFY].

### Remaining limitations

Several limitations recur across the relevant evidence:

- **Incomplete and noisy annotations:** database annotations do not provide an exhaustive account of protein function, and errors or differences in annotation practice can become training-label errors [VERIFY].
- **Class imbalance:** common functions have many examples, whereas rare functions may have too few examples for reliable learning [VERIFY].
- **Homology leakage:** inadequate separation of related proteins can inflate reported test performance [VERIFY].
- **Dependence on structural quality:** structure-based methods may be affected by errors in experimental structures, predicted structures, flexible regions, disorder, alternate conformations, or complexes.
- **Limited extrapolation:** models trained on known protein families may perform poorly on remote homologues, novel folds, unusual organisms, or functions that are weakly represented in training data [VERIFY].
- **Function is context-dependent:** a protein’s activity can depend on cofactors, cellular location, complexes, post-translational modifications, environmental conditions, or substrate availability—information that sequence or static structure alone may not capture [VERIFY].
- **Interpretability and validation:** residue-level explanations or high prediction scores do not necessarily demonstrate mechanism. Experimental assays remain necessary, particularly for new catalytic functions or therapeutic targets.

Overall, the field is moving from sequence-only classifiers toward protein language models, structural graphs, interaction networks, and combinations of sequence and structure. The major unresolved issue is not simply whether these models achieve high benchmark scores, but whether those scores survive homology-controlled testing and translate into experimentally confirmed function for proteins outside well-characterized families.