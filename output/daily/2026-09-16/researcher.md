## Evidence overview

The supplied records contain a small core of directly relevant literature on protein-function prediction, surrounded by studies on protein structure prediction, protein–protein interaction, ligand binding, protein design, and clinical or biomedical prediction. Because only bibliographic metadata were supplied, the specific datasets, experimental splits, metrics, and quantitative results cannot be established reliably without examining the full texts.

### 1. Most directly relevant records

| Relevance | Record | What it appears to contribute | Dataset and metric information |
|---|---|---|---|
| **Very high** | **Kulmanov & Hoehndorf (2025), “Computational prediction of protein functional annotations.”** PMID 40728605 | Directly addresses computational prediction of protein functional annotations. It is likely the most important recent overview for methods, annotation schemes, and evaluation practice. | Not available from the record. Full text is needed to identify whether it covers Gene Ontology annotations, sequence or structure databases, benchmark datasets, and metrics such as precision, recall, F-score, AUROC, AUPRC, or ontology-aware measures. |
| **Very high** | **Gligorijević et al. (2021), “Structure-based protein function prediction using graph convolutional networks.”** DOI 10.1038/s41467-021-23303-9 | Direct methodological study using graph convolutional networks and structural information to predict protein function. This is the clearest primary research paper in the set on the requested topic. | The record does not specify the structural source, functional labels, train/test split, or metrics. The local PDF is available, so these details should be extracted directly. |
| **High** | **Yu, Wang & Teo (2022), “Machine Learning Approaches for Metalloproteins.”** PMID 35209064 | A focused review of machine-learning applications to metalloproteins, potentially including prediction of metal binding, catalytic activity, structural properties, or functional classes. | Dataset composition and evaluation measures are unknown. Full-text verification is essential because the title does not establish which tasks are treated as protein-function prediction. |
| **High** | **Bordin et al. (2023), “Novel machine learning approaches revolutionize protein knowledge.”** PMID 36504138 | Broad review of modern machine-learning approaches for protein analysis. It may discuss protein language models, large-scale sequence representations, structure prediction, and functional annotation. | Dataset and metric coverage cannot be inferred from the title. Full text is needed to distinguish function prediction from structure prediction and protein design. |
| **Moderate to high** | **Gao et al. (2023), “Hierarchical graph learning for protein-protein interaction.”** PMID 36841846 | Relevant to function inference when protein–protein interaction networks are used as functional evidence. The primary task, however, is interaction prediction rather than direct annotation of protein function. | The interaction dataset, negative-sampling strategy, and metrics are not reported in the supplied record. Full text is needed to assess relevance to function prediction. |
| **Moderate** | **Michalik & Kuder (2024), “Machine Learning Methods in Protein-Protein Docking.”** PMID 38987466 | Relevant to structure-based inference of molecular interactions, which can support functional characterization. It is not necessarily a direct protein-function prediction paper. | Datasets and metrics are unknown. Verify whether functional prediction is discussed or whether the review is restricted to docking accuracy. |
| **Moderate** | **Zhang et al. (2025), “Sequence-based virtual screening using transformers.”** PMID 40721411 | Demonstrates transformer-based sequence modelling in a protein-related prediction task. The likely endpoint is ligand or target prioritization rather than annotation of protein function. | Full text is required to determine the prediction target, training data, and evaluation metrics. |
| **Moderate** | **Odoemelam, Steuber & Schmuker (2025), “Computational modelling of olfactory receptors.”** PMID 40441539 | Potentially relevant as a specialised example of predicting receptor properties or ligand/function relationships using computational and machine-learning methods. | The role of machine learning and the functional endpoint are unclear from the title. Full-text verification is required. |

### 2. Relevant background for representations and structural evidence

These records are not direct evidence for protein-function prediction, but they help define the computational inputs increasingly used by function-prediction systems.

- **Jumper et al. (2021), “Highly accurate protein structure prediction with AlphaFold.”**  
  Provides the structural-prediction foundation from which structure-based function-prediction methods may obtain input features. It predicts structure, not protein function directly. A local PDF is available.

- **Abramson et al. (2024), “Accurate structure prediction of biomolecular interactions with AlphaFold 3.”**  
  Relevant to structural representations of protein–protein, protein–ligand, and other biomolecular interactions. It should not be treated as direct evidence of function annotation without full-text confirmation.

- **Váradi et al. (2023), “AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences.”**  
  Relevant as a potential source of predicted structures for large-scale function-prediction workflows. The supplied metadata do not show how the database was used for functional prediction.

- **Tran et al. (2026), “Rapid directed evolution guided by protein language models and epistatic interactions.”**  
  Relevant to protein language models and sequence representations, but its primary application appears to be sequence optimisation or directed evolution rather than prediction of naturally occurring protein functions.

- **Dauparas et al. (2022), “Robust deep learning–based protein sequence design using ProteinMPNN.”**  
  Focuses on protein design, not function prediction. It may be useful background for generative or structure-conditioned protein models.

- **Passaro et al. (2025), “Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction.”**  
  Addresses binding-affinity prediction, which is related to molecular function but is a distinct endpoint from protein functional annotation.

- **Schauperl & Denny (2022), “AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges.”**  
  Useful background on structure prediction and drug discovery, but not a direct study of protein-function annotation.

- **Chen et al. (2024), “AI-Driven Deep Learning Techniques in Protein Structure Prediction.”**  
  A structure-prediction review. It may discuss downstream functional applications, but this cannot be assumed from the title.

### 3. Indirect or low-relevance records

The following records should not be used as core evidence for the question unless full-text inspection reveals a specific protein-function prediction component:

- **Sahoo et al. (2021), “Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease.”**
- **Li et al. (2025), “Machine learning driven prediction of drug efficacy in lung cancer: based on protein biomarkers and clinical features.”**
- **Wu et al. (2025), “LCN2 drives ferroptosis-associated ischemia-reperfusion injury…”**
- **Zhang et al. (2025), “Machine Learning Prediction of 90-Day Mortality… Using Olink-Derived Inflammatory Protein Signatures.”**
- **Li et al. (2025), “Machine Learning-Based Predictive Modeling Maximizes the Efficacy of mTOR/p53 Co-Targeting Therapy Against AML.”**
- **Yoo et al. (2026), “Discovery of natural RORγt inhibitor using machine learning…”**
- **Wang et al. (2025), “Deciphering the mechanism of baicalein…”**
- **Pang et al. (2024), multi-omics integration for diabetic retinopathy.**
- **Tanabe et al. (2024), prediction of type 2 diabetes subtypes.**
- **Schade et al. (2024), AKT and EZH2 inhibitors in triple-negative breast cancer.**

These studies may use proteins as biomarkers, drug targets, or molecular features, but they are not evidently concerned with predicting the intrinsic function of uncharacterised proteins.

The following are general machine-learning or methodological reviews and are also secondary background rather than direct evidence:

- **Greener et al. (2021), “A guide to machine learning for biologists.”**
- **Alzubaidi et al. (2021), deep-learning review.**
- **Ponce Bobadilla et al. (2024), SHAP analysis.**
- **Kapoor & Narayanan (2023), “Leakage and the reproducibility crisis in machine-learning-based science.”**
- **von Rueden et al. (2021), informed machine learning.**
- **Ganaie et al. (2022), ensemble deep learning.**
- **Reel et al. (2021), machine learning for multi-omics.**
- **Other records on agriculture, kidney disease, digital twins, materials science, and clinical swarm learning.**

Kapoor and Narayanan are particularly relevant to methodological limitations, because data leakage and irreproducible evaluation are important risks in protein benchmarks. However, the record alone does not show whether the paper analyses protein-function studies specifically.

## Provisional synthesis

### How machine learning is being used

Based on the titles, the evidence set supports several main uses:

1. **Sequence-based prediction**  
   Transformer and protein-language-model approaches can learn representations from amino-acid sequences. These representations may be used for functional annotation, classification, interaction prediction, or related molecular tasks. The direct evidence for annotation is represented primarily by Kulmanov and Hoehndorf, while Zhang et al. and Tran et al. provide adjacent sequence-modelling examples.

2. **Structure-based prediction**  
   Graph convolutional networks can represent residues, atoms, or structural neighbourhoods as graphs and use this information to predict functional labels. Gligorijević et al. is the strongest direct record for this approach.

3. **Network and interaction-based inference**  
   Protein–protein interaction prediction and docking can provide functional evidence, particularly when interactions are integrated with sequence, structure, or biological-network information. Gao et al. and Michalik and Kuder are relevant but indirect.

4. **Specialised biochemical prediction**  
   Metalloprotein-focused models may predict metal-binding or catalytic properties. These applications are likely closer to biochemical function than general structural prediction, but the exact tasks need verification.

5. **Integration of predicted structures and large databases**  
   AlphaFold-derived structures and large predicted-structure repositories may expand the availability of structural input for proteins lacking experimental structures. This is an enabling technology rather than direct evidence that function has been correctly predicted.

### Datasets and labels

The supplied records do not provide enough information to identify the datasets used in the direct studies. Full-text extraction should specifically record:

- the sequence source, such as UniProt, Swiss-Prot, or other curated protein databases;
- whether functional labels are Gene Ontology terms, enzyme classes, pathway memberships, domains, ligand-binding functions, or organism-specific annotations;
- the source of structures, such as experimentally determined structures, predicted structures, or both;
- protein–protein interaction databases and the treatment of uncertain or missing interactions;
- redundancy-reduction procedures and sequence-identity thresholds;
- the temporal cutoff used to prevent information leakage;
- whether homologous proteins occur across training and test sets;
- class balance and the handling of proteins with multiple functions;
- whether the task is single-label, multilabel, hierarchical, or open-set prediction.

### Evaluation metrics

No metric can be attributed confidently to a particular record from the supplied metadata. For the direct papers, full-text verification should determine whether they report:

- precision, recall, F1-score, accuracy, and balanced accuracy;
- AUROC and, particularly for imbalanced multilabel tasks, AUPRC;
- top-\(k\) accuracy or ranking-based measures;
- ontology-aware measures such as semantic similarity, \(F_{\max}\), or \(S_{\min}\);
- calibration, confidence estimates, and coverage–accuracy trade-offs;
- structure-specific measures where applicable, such as interaction or binding-site prediction accuracy;
- performance on distant-homology, low-similarity, or temporally held-out test sets;
- comparisons with homology-transfer methods and non-neural baselines.

### Remaining limitations

Several limitations are important, but most require confirmation in the primary papers:

- **Incomplete and noisy labels:** protein annotations are uneven across taxa and often more complete for well-studied proteins than for poorly characterised proteins.
- **Class imbalance and multilabel complexity:** proteins can have several functions, while many functional categories have few positive examples.
- **Homology leakage:** random protein-level splits may place close homologues in both training and test sets, producing overly optimistic performance.
- **Limited generalisation:** models may perform poorly on remote homologues, unusual protein families, new organisms, or functions absent from the training data.
- **Dependence on predicted structures:** structure-based models may inherit errors or low confidence from predicted structures, especially for disordered or flexible regions.
- **Confounding by database and annotation biases:** models may learn taxonomic, sequence-length, or curation patterns rather than biochemical function.
- **Interpretability:** high predictive performance does not necessarily identify the residues, domains, interactions, or mechanisms responsible for a function.
- **Evaluation mismatch:** aggregate metrics can conceal poor performance for rare functions; ontology hierarchy and partial correctness also complicate interpretation.
- **Reproducibility and leakage:** preprocessing, redundancy filtering, benchmark construction, and temporal data separation need to be reported transparently.

## Full-text verification priorities

**Highest priority**

1. Kulmanov & Hoehndorf (2025) — direct review of functional annotation prediction.
2. Gligorijević et al. (2021) — direct structure-based graph-learning study; local PDF available.
3. Yu et al. (2022) — focused review of machine learning for metalloproteins.
4. Bordin et al. (2023) — broad review of modern protein machine learning.
5. Gao et al. (2023) — interaction prediction with possible functional relevance.

**Second priority**

6. Michalik & Kuder (2024) — docking and interaction modelling.
7. Zhang et al. (2025) — transformer-based sequence prediction.
8. Odoemelam et al. (2025) — olfactory-receptor modelling.
9. Jumper et al. (2021), Abramson et al. (2024), and Váradi et al. (2023) — structural resources and inputs.
10. Kapoor & Narayanan (2023) — leakage and reproducibility guidance.

All substantive claims about datasets, model architectures, baselines, metrics, and reported performance should be treated as **requiring full-text verification**.