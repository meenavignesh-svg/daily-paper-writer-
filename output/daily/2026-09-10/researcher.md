# Evidence overview: AI and machine learning in protein function prediction

## Overall assessment

The supplied records contain **only a small number of directly relevant studies** on protein-function prediction. Most records concern adjacent tasks—structure prediction, protein design, docking, virtual screening, biomarker prediction, or clinical machine learning. The strongest direct evidence is the study on **structure-based protein-function prediction using graph convolutional networks** and the broader review **Novel machine learning approaches revolutionize protein knowledge**. The records suggest that machine learning is being applied mainly by learning from **protein sequence, three-dimensional structure, interaction networks, or protein-language-model representations**, but the supplied metadata do not establish which datasets or evaluation metrics were used in most individual studies.

Consequently, the central details requested—benchmark datasets, train/test construction, metrics, and quantitative performance—require full-text verification.

---

## 1. Highest-relevance records

### 1.1 Structure-based protein function prediction using graph convolutional networks  
**Gligorijević et al., 2021**  
DOI: 10.1038/s41467-021-23303-9

**Relevance: very high**

This is the most directly relevant record. Its title indicates that a **graph convolutional network (GCN)** was used to predict protein function from structural information. A likely representation is a protein structure expressed as a graph, with residues or atoms as nodes and spatial or structural relationships as edges; however, the exact representation must be confirmed from the article.

This study should be used to extract:

- the functional prediction task, such as Gene Ontology or another annotation system;
- the source and quality of protein structures;
- whether experimentally determined structures, predicted structures, or both were used;
- how homologous proteins were separated between training and test sets;
- the number and balance of functional classes;
- the evaluation metrics and whether performance was measured per protein, per function, or per residue/domain;
- comparisons with sequence-based or similarity-based baselines.

**Full-text verification: required.** A local PDF is listed, so this appears to be one of the records most suitable for immediate verification.

---

### 1.2 Novel machine learning approaches revolutionize protein knowledge  
**Bordin et al., 2023**  
PMID: 36504138

**Relevance: high**

This review appears to cover recent machine-learning methods for protein representation and annotation. It is likely useful for organizing the field into sequence-based models, protein language models, structure-based methods, and approaches using interaction or other biological information. The title alone does not establish which methods, datasets, or metrics are discussed in detail.

This record may provide:

- an overview of protein language models and learned sequence embeddings;
- the relationship between structure prediction and functional annotation;
- examples of supervised, self-supervised, and transfer-learning approaches;
- discussion of large protein databases and annotation resources;
- limitations associated with sparse or uncertain functional labels.

**Full-text verification: required.** This is a review rather than a primary benchmark study and should be used for conceptual synthesis, not as a substitute for extracting quantitative results from original studies.

---

### 1.3 Machine Learning Approaches for Metalloproteins  
**Yu, Wang and Teo, 2022**  
PMID: 35209064

**Relevance: moderate to high**

This is a focused review of machine learning applied to metalloproteins. It is relevant because metal binding and metal-dependent activity are important components of protein function prediction. The review may cover prediction of metal-binding residues, metal-binding sites, metalloprotein classification, catalytic activity, or related structural properties. These distinctions cannot be resolved from the title alone.

It may be particularly useful for assessing:

- specialized datasets for metalloprotein sequences and structures;
- the effects of class imbalance and limited positive examples;
- sequence, structural, and physicochemical features;
- whether models generalize across metal types or protein families.

**Full-text verification: required.**

---

### 1.4 A guide to machine learning for biologists  
**Greener et al., 2021**  
DOI: 10.1038/s41580-021-00407-0

**Relevance: moderate**

This is a general methodological guide rather than a protein-function study. It can support interpretation of:

- supervised versus unsupervised learning;
- representation learning and transfer learning;
- data splitting and validation;
- overfitting and hyperparameter selection;
- appropriate evaluation metrics and model interpretation.

It should not be treated as direct evidence about protein-function benchmarks unless the full text contains relevant protein examples.

**Full-text verification: useful but not essential for the topic-specific evidence.** A local PDF is listed.

---

## 2. Adjacent records that inform the field but do not directly answer the question

### 2.1 Protein structure prediction and structure resources

- **Highly accurate protein structure prediction with AlphaFold** — Jumper et al., 2021  
- **Accurate structure prediction of biomolecular interactions with AlphaFold 3** — Abramson et al., 2024  
- **AI-Driven Deep Learning Techniques in Protein Structure Prediction** — Chen et al., 2024  
- **AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges** — Schauperl and Denny, 2022  
- **AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences** — Varadi et al., 2023

These records are important because predicted structures can serve as inputs or auxiliary information for downstream function prediction. However, their primary topic is **structure prediction or structural coverage**, not prediction of molecular function. The AlphaFold Database record indicates very large-scale structural coverage, but it does not demonstrate that those structures were used in a function-prediction benchmark.

**Use in the review:** background on the availability of structural representations and the opportunity to apply structure-based models to proteins lacking experimental structures.

**Full-text verification:** required before making claims about structural accuracy, confidence thresholds, or downstream functional use.

---

### 2.2 Protein-language models, sequence models, and protein design

- **Rapid directed evolution guided by protein language models and epistatic interactions** — Tran et al., 2026  
- **Sequence-based virtual screening using transformers** — Zhang et al., 2025  
- **Robust deep learning–based protein sequence design using ProteinMPNN** — Dauparas et al., 2022

These studies concern protein-language-model representations, sequence-based prediction, or sequence design. They are relevant to the broader methodological landscape, but they do not necessarily predict naturally occurring protein functions. Directed evolution and sequence design may optimize a measured phenotype or activity, whereas protein-function prediction generally refers to assigning or predicting biological annotations.

**Use in the review:** evidence that learned sequence representations and transformer-based models are being used for protein-related prediction and design.

**Full-text verification:** required to determine whether any experiments include explicit functional annotation prediction.

---

### 2.3 Protein interactions, docking, and ligand-related prediction

- **Hierarchical graph learning for protein-protein interaction** — Gao et al., 2023  
- **Machine Learning Methods in Protein-Protein Docking** — Michalik and Kuder, 2024  
- **Machine Learning Approaches for Metalloproteins** — Yu et al., 2022  
- **Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction** — Passaro et al., 2025  
- **Computational modelling of olfactory receptors** — Odoemelam et al., 2025

Interaction prediction and binding-affinity prediction can provide functional information, but they are distinct prediction tasks. A model predicting whether two proteins interact, or how strongly a ligand binds, should not automatically be classified as a protein-function predictor.

**Use in the review:** discuss neighbouring tasks and the distinction between predicting function, interaction, structure, and biochemical activity.

**Full-text verification:** needed to determine whether these papers include explicit functional annotation outcomes.

---

## 3. Records with little or no direct relevance

The following records primarily concern disease prediction, clinical biomarkers, cancer biology, multi-omics, or general machine learning:

- **AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution**
- **Machine learning-based reproducible prediction of type 2 diabetes subtypes**
- **LCN2 drives ferroptosis-associated ischemia-reperfusion injury**
- **Discovery of natural RORγt inhibitor using machine learning**
- **Multi-cohort, cross-species urinary proteomics reveals signatures of LRRK2 dysfunction**
- **Deciphering the mechanism of baicalein in cervical cancer**
- **Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF**
- **Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease**
- **Machine learning driven prediction of drug efficacy in lung cancer**
- **Virtual patient analysis identifies strategies to improve predictive biomarkers for PD-1 blockade**
- **Multi-Omics Integration With Machine Learning Identified Early Diabetic Retinopathy**
- **Using machine learning approaches for multi-omics data analysis: A review**
- **Swarm Learning for decentralized and confidential clinical machine learning**
- **Prediction of Chronic Kidney Disease**
- **Machine Learning in Agriculture**
- **Small data machine learning in materials science**
- **Review of deep learning**
- **Ensemble deep learning**
- **A review on extreme learning machine**
- **Generative AI**
- **Informed Machine Learning**
- **The Role of AI, Machine Learning, and Big Data in Digital Twinning**
- **Practical guide to SHAP analysis**

These may offer general lessons about validation, interpretability, data integration, or reproducibility, but they should not be used as evidence for how protein functions are predicted unless full-text screening identifies a specific protein-function component.

---

## 4. How machine learning is being used for protein-function prediction

Based on the directly relevant and adjacent records, the field can be organized into several methodological strategies.

### 4.1 Sequence-based prediction

Models learn from amino-acid sequences, either using manually engineered features or embeddings produced by protein-language models. Transformer models and other language-model architectures can represent sequence context and may support classification, annotation transfer, or prediction of biochemical properties.

The supplied records provide evidence that protein-language models and transformers are active areas of protein modelling, but they do not establish which of these studies performed standard function annotation.

### 4.2 Structure-based prediction

The GCN study provides direct evidence for using protein structure as a graph representation for function prediction. Structural information may capture:

- spatially neighbouring residues;
- folds and domains;
- active-site geometry;
- interfaces and pockets;
- relationships that are not obvious from sequence alone.

Predicted structures, particularly from AlphaFold-related resources, may expand the number of proteins for which structure-based functional inference is possible. Whether this improves function prediction, and under what confidence thresholds, requires direct study-level evidence.

### 4.3 Interaction- and network-based prediction

Protein-protein interaction and biological-network models can infer function from a protein’s relationships to other proteins. The hierarchical graph-learning and protein-protein interaction records are relevant to this direction, although they do not demonstrate function annotation prediction from the metadata supplied.

### 4.4 Multimodal and transfer-learning approaches

The broader literature represented here points toward combining sequence, structure, interaction, and biochemical information. Protein-language models and predicted structural databases make transfer learning possible even where experimentally labelled function data are limited. This is a plausible direction supported by the composition of the evidence set, but the specific datasets and gains of multimodal models require full-text verification.

---

## 5. Datasets and evaluation metrics

### What can be established from the supplied records

The supplied bibliographic records do **not provide enough information to identify the exact datasets or metrics used** in the primary protein-function studies. In particular, the metadata do not specify:

- whether functional labels came from Gene Ontology, enzyme classifications, curated databases, or experimental assays;
- whether sequences came from UniProt, Pfam, PDB, or another resource;
- whether structures were experimental or predicted;
- the number of proteins, labels, or species;
- whether the task was single-label, multilabel, hierarchical, or ranking-based;
- how sequence or structural homology was controlled during splitting;
- which evaluation metrics were reported.

The GCN paper and the metalloprotein review are the priority records for recovering these details.

### Metrics that should be extracted during full-text review

For each study, the review should record whether it reports:

- accuracy;
- precision, recall, and F1 score;
- area under the ROC curve;
- area under the precision–recall curve;
- Matthews correlation coefficient;
- top-\(k\) accuracy or ranking measures;
- per-class or macro/micro-averaged performance;
- calibration or confidence measures;
- performance across sequence-identity or structural-distance strata;
- external or experimentally validated performance.

For multilabel protein-function prediction, overall accuracy can be misleading. Macro-averaged measures, per-function recall, precision–recall curves, and ranking-based metrics are often more informative, especially when functional classes are imbalanced. This is a methodological recommendation, not a finding established by the supplied records.

### Dataset issues requiring particular attention

Full-text extraction should specifically check for:

1. **Homology-aware splitting:** whether close homologues occur in both training and test sets.  
2. **Temporal or database leakage:** whether annotations or structures became available after model development.  
3. **Label incompleteness:** whether unannotated proteins were incorrectly treated as negatives.  
4. **Class imbalance:** whether common functions dominate the results.  
5. **External validation:** whether predictions were tested on proteins from different families, organisms, or laboratories.  
6. **Experimental validation:** whether computational predictions were confirmed biochemically or biologically.

The record on **leakage and reproducibility in machine-learning-based science** is relevant to these concerns, but it is not protein-specific.

---

## 6. Remaining limitations

Several limitations are likely to remain important, although the supplied records do not quantify their effects for protein-function prediction.

### 6.1 Incomplete and noisy functional labels

Protein annotations are unevenly distributed across protein families and organisms. A missing annotation is not necessarily evidence that a protein lacks a function. This creates difficulties for both supervised learning and evaluation.

### 6.2 Homology and data leakage

Random splitting of related proteins can produce overly optimistic results because models may recognize family-level similarity rather than generalize to genuinely novel proteins. The leakage and reproducibility paper is relevant background for this issue. The protein-function papers should be checked for identity-based or structure-aware splits.

### 6.3 Class imbalance and hierarchical labels

Some functions are common whereas others have very few examples. Functional ontologies are also hierarchical, so an incorrect fine-grained prediction may still be biologically close to the correct parent term. Evaluation should therefore go beyond a single overall accuracy value.

### 6.4 Dependence on input quality

Structure-based prediction depends on the quality and coverage of structures. Predicted structures may be highly useful in some regions but uncertain in disordered segments, flexible regions, or complexes. The supplied AlphaFold records support the importance of structural resources but do not establish their effect on function-prediction accuracy.

### 6.5 Limited out-of-distribution generalization

A model trained on well-studied proteins may perform poorly on proteins from poorly sampled taxa, remote evolutionary families, novel folds, or unusual biochemical environments. Claims of general performance therefore require family-level, species-level, or temporal external validation.

### 6.6 Interpretability and biological validation

High predictive performance does not necessarily identify the causal residues, domains, interactions, or mechanisms underlying a function. Explainability methods such as SHAP may help inspect model behaviour, but explanations themselves require biological validation.

### 6.7 Reproducibility

Results can depend strongly on data curation, label definitions, split strategy, negative sampling, and preprocessing. The general machine-learning and leakage records support treating reproducibility as a central limitation, but protein-specific conclusions require inspection of the primary papers.

---

## Priority full-text verification list

### Essential

1. **Gligorijević et al. (2021), Structure-based protein function prediction using graph convolutional networks**  
2. **Bordin et al. (2023), Novel machine learning approaches revolutionize protein knowledge**  
3. **Yu et al. (2022), Machine Learning Approaches for Metalloproteins**

### Important contextual verification

4. **Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold**  
5. **Varadi et al. (2023), AlphaFold Protein Structure Database in 2024**  
6. **Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3**  
7. **Tran et al. (2026), Rapid directed evolution guided by protein language models and epistatic interactions**  
8. **Zhang et al. (2025), Sequence-based virtual screening using transformers**  
9. **Gao et al. (2023), Hierarchical graph learning for protein-protein interaction**  
10. **Kapoor and Narayanan (2023), Leakage and the reproducibility crisis in machine-learning-based science**

## Bottom line

The evidence set supports a view of protein-function prediction as moving from sequence similarity and handcrafted features toward **learned sequence representations, structure-aware graph models, and potentially multimodal systems**. However, the supplied records do not yet support a reliable comparative account of datasets, metrics, or quantitative performance. The structure-based GCN paper is the key primary study, while the protein-knowledge and metalloprotein reviews can provide field-level context. Exact claims about benchmark composition, evaluation, generalization, and biological validation should be deferred until these records undergo full-text verification.