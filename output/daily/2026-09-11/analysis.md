## Current use of machine learning for protein-function prediction

The supplied literature suggests three main methodological directions, although only one listed primary study is directly focused on protein-function prediction.

### 1. Structure-based prediction

Gligorijević et al. (2021) directly address protein-function prediction with graph convolutional networks. In this setting, a protein can be represented as a graph whose nodes are residues or atoms and whose edges encode spatial proximity or structural contacts. Graph models can therefore use three-dimensional relationships that are unavailable from a simple sequence representation. This is particularly relevant when function depends on active-site geometry, residue contacts, domains, or binding interfaces.

The record does not establish whether the study used experimentally determined structures, predicted structures, or both; which functional labels were predicted; or how structural uncertainty was treated [VERIFY]. It also does not show whether the model was tested on proteins dissimilar to those in training, which is essential for assessing genuine functional generalization [VERIFY].

AlphaFold and AlphaFold 3 are relevant mainly as sources of structural information. Their primary contributions are structure or biomolecular-complex prediction, not direct functional annotation. The AlphaFold Protein Structure Database could enable large-scale structure-based function-prediction pipelines, but broad structural coverage should not be equated with experimentally validated functional predictions.

### 2. Sequence-based models and protein language models

The reviews by Bordin et al. (2023) and Yu et al. (2022), together with the transformer-related record by Zhang et al. (2025), indicate the importance of learned sequence representations. Protein language models are trained on large collections of amino-acid sequences and can produce embeddings that are subsequently used for classification, annotation, or prediction of sequence–function relationships. Transformer models may also be used directly for sequence-based prediction or for virtual screening.

The supplied evidence does not specify which language models, pretraining databases, downstream tasks, or baselines were used [VERIFY]. Tran et al. (2026) is relevant because it uses protein language models to guide directed evolution, but that is a sequence-design and experimental optimization task rather than conventional function annotation. Its relevance lies in treating sequence patterns and epistatic interactions as predictors of phenotypic or biochemical behavior, not in demonstrating a general-purpose function-prediction benchmark.

### 3. Specialised and multimodal models

Metalloproteins provide a specialised example in which function may depend simultaneously on sequence, fold, metal-binding residues, coordination geometry, and metal identity. Yu et al. (2022) review machine-learning approaches in this area, but the supplied record does not make clear whether the reviewed tasks are functional classification, metal-site prediction, ligand binding, or structure prediction [VERIFY].

Other listed studies concern related but distinct problems:

- hierarchical graph learning for protein–protein interaction prediction;
- machine learning for protein–protein docking;
- computational modelling of olfactory receptors;
- protein structure prediction;
- sequence-based virtual screening;
- protein design and directed evolution.

These tasks can provide evidence relevant to function—for example, interactions or ligand specificity—but they should not be treated as equivalent to predicting Gene Ontology function or experimentally defined biochemical activity. The clinical, cancer, diabetes, transplantation, and drug-response papers in the list primarily apply ML to patient or molecular phenotype prediction and are not direct evidence for protein-function annotation.

## Datasets and labels

The supplied bibliographic records do not report enough detail to identify the benchmark datasets used by the direct studies. In particular, they do not establish:

- whether labels came from Gene Ontology, enzyme classes, protein families, experimentally measured activities, or another annotation system;
- whether sequences were obtained from UniProt, Pfam, structural databases, or specialised metalloprotein collections;
- whether structures came from the Protein Data Bank, AlphaFold Database, or another source;
- how positive and negative examples were defined;
- whether homologous proteins were separated between training and test sets;
- whether evaluation was performed on temporally held-out proteins or newly characterised proteins.

These details are especially important because protein databases contain substantial redundancy and uneven annotation. Randomly splitting closely related sequences can make a model appear highly accurate while testing recognition of homologues rather than transfer to genuinely novel proteins. Such leakage and reproducibility concerns are highlighted by the supplied general ML literature, but their presence in each protein-function study requires paper-specific verification [VERIFY].

The AlphaFold Database is a potentially important data resource, with the cited database paper reporting structural coverage for more than 214 million protein sequences. That is a resource-scale figure, not evidence that all those proteins have reliable functional labels or that AlphaFold models are equally suitable for functional inference. Active sites, flexible regions, complexes, and ligand-bound conformations may remain uncertain [VERIFY].

## Evaluation metrics

No numerical evaluation metrics are provided in the supplied evidence. The records therefore do not support claims about which method performs best or about specific accuracy values.

For multilabel protein-function prediction, appropriate evaluation commonly includes precision, recall, F1 score, area under the precision–recall curve, and ranking-based measures such as precision at a specified cutoff or semantic distance between predicted and observed ontology terms [VERIFY]. Accuracy alone can be misleading when functions are imbalanced or when many proteins have multiple labels. For enzyme or family classification, balanced accuracy, Matthews correlation coefficient, and class-specific measures may be useful [VERIFY]. For interaction or binding-related tasks, AUROC, AUPRC, top-\(k\) retrieval, and calibration measures may be reported [VERIFY].

Metric choice must match the task. Structural accuracy measures such as RMSD, TM-score, or lDDT evaluate structure prediction, not protein-function prediction. Docking scores or binding-affinity errors likewise do not directly measure whether a model correctly identifies a protein’s biological role.

A meaningful comparison should also report performance on homology-reduced or remote-homology splits, independent external datasets, confidence calibration, and, where possible, experimental validation. Whether the listed studies do so is not established by the supplied metadata [VERIFY].

## Remaining limitations

Several limitations emerge from the evidence and from the methodological scope of the cited reviews, though their magnitude in individual studies requires verification.

1. **Incomplete and biased annotations.** Protein-function labels are sparse, uneven across species and protein families, and often propagated from homologues. An apparent negative example may simply be unannotated rather than genuinely lacking the function [VERIFY].

2. **Homology leakage.** Closely related proteins appearing in both training and test sets can inflate performance. This is a particular concern for sequence models and must be addressed through family-aware or similarity-controlled splitting.

3. **Limited transfer to novel proteins.** Models may perform well within well-characterised families but degrade on remote homologues, orphan proteins, novel folds, or proteins from underrepresented organisms [VERIFY].

4. **Dependence on structural quality.** Structure-based methods may be affected by errors in predicted structures, missing ligands, incorrect oligomeric states, flexible or disordered regions, and the absence of cellular context. A structurally plausible model does not by itself establish biochemical function.

5. **Multifunctionality and context dependence.** A single protein can have several molecular functions, participate in different complexes, or behave differently depending on tissue, organism, localization, modification state, or ligand environment. A single fixed label may not capture this biology.

6. **Class imbalance and hierarchical labels.** Rare functions are harder to predict, while broad parent terms may be easier than specific child terms. Reported scores can therefore depend strongly on ontology depth, label filtering, and the treatment of missing annotations [VERIFY].

7. **Interpretability and mechanistic validation.** Learned sequence or structure features may identify useful correlations without showing which residues, interfaces, or physicochemical mechanisms cause the function. Interpretability methods such as SHAP are relevant in general, but their reliability for protein-function models is not demonstrated by the supplied records [VERIFY].

8. **Reproducibility and experimental confirmation.** Large models can require substantial computational resources, specialised preprocessing, and proprietary or changing databases. More importantly, computational predictions require biochemical, cellular, or structural validation. The supplied evidence does not show that the directly relevant studies consistently performed prospective experimental testing [VERIFY].

## Overall assessment

The evidence supports a field moving toward sequence language models, structure-aware graph networks, and combinations of sequence, structure, interaction, and biochemical information. The clearest direct example is the use of graph convolutional networks for structure-based functional prediction. Protein language models and AlphaFold-derived structures are likely expanding the scale and scope of annotation, but the supplied records do not allow a reliable comparison of their predictive performance.

The principal evidentiary gap is not a lack of proposed architectures; it is insufficient information about dataset construction, homology-controlled evaluation, label quality, calibration, and experimental validation. Specific claims about datasets, metrics, or superiority of one method over another should therefore be checked against the full texts, especially Gligorijević et al. (2021), Bordin et al. (2023), and Yu et al. (2022) [VERIFY].