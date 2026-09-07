# Evidence overview: AI and machine learning for protein function prediction

## Scope and overall assessment

The supplied records contain **one directly focused study**, several **closely related reviews or methodological papers**, and many records that concern adjacent applications rather than protein-function prediction itself. On the information provided, the literature supports a broad view in which machine learning is used to infer protein function from:

- **sequence-derived representations**, including protein language-model embeddings;
- **three-dimensional structural representations**, including graph-based descriptions of residues, atoms, or contacts;
- **protein–protein interaction networks**;
- **protein–ligand or binding-related features**; and
- **integrated biological or omics data**.

However, the supplied bibliographic records do not provide enough information to establish which datasets, baselines, metrics, or limitations were used in most studies. These details require full-text verification.

---

## Relevance-ranked evidence

### Tier 1: Direct evidence on protein-function prediction

#### 1. Structure-based protein function prediction using graph convolutional networks  
**Gligorijević et al., 2021.** *Nature Communications.*  
DOI: 10.1038/s41467-021-23303-9

This is the most directly relevant record. Its title indicates a method that represents proteins structurally and applies **graph convolutional networks (GCNs)** to predict protein function. A likely conceptual workflow is:

1. represent a protein structure as a graph;
2. encode residue- or atom-level features and spatial relationships;
3. propagate information through graph-convolutional layers; and
4. predict one or more functional annotations.

The relevant functional labels may include ontology-based annotations, but this must not be assumed from the title alone. The record should be checked for:

- the exact functional prediction task;
- the source and composition of the protein structures;
- the annotation ontology and label hierarchy;
- whether experimentally solved structures, predicted structures, or both were used;
- train/test splitting, especially sequence- or structure-similarity separation;
- class imbalance handling;
- comparison with sequence-based methods; and
- evaluation metrics such as precision, recall, F1, ROC-AUC, precision–recall AUC, or ontology-specific measures.

**Full-text status:** **Priority full-text verification required.** A PDF is listed locally, but the bibliographic record alone does not establish the study’s detailed findings.

---

### Tier 2: Reviews and methodological sources directly informing the field

#### 2. Machine Learning Approaches for Metalloproteins  
**Yu, Wang and Teo, 2022.** *PubMed record, PMID 35209064.*

This review is relevant because metalloprotein function is strongly linked to metal binding, coordination geometry, catalytic activity, and structural context. It may cover machine-learning approaches for predicting properties such as:

- metal-binding sites;
- metal-ion specificity;
- coordination environments;
- catalytic or functional classes; and
- possibly metalloprotein structures or interactions.

The title does not establish which of these tasks are covered. It is especially useful for identifying domain-specific datasets, feature representations, and evaluation practices.

**Full-text status:** **Required.** The supplied record contains no full text.

#### 3. AI-Driven Deep Learning Techniques in Protein Structure Prediction  
**Chen et al., 2024.** *PubMed record, PMID 39125995.*

This appears to be a review of deep learning for **structure prediction**, rather than function prediction. It is relevant indirectly because structural predictions can provide inputs for structure-based function inference, especially for proteins lacking experimentally determined structures. It may discuss:

- deep-learning architectures;
- sequence-to-structure prediction;
- structural accuracy assessment; and
- challenges in using predicted structures downstream.

It should not be treated as direct evidence that a model predicts molecular or cellular function.

**Full-text status:** **Required.**

#### 4. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges  
**Schauperl and Denny, 2022.** *PubMed record, PMID 35727311.*

This is also adjacent rather than directly focused on function prediction. It may help establish how predicted structures are used in functional interpretation, binding analysis, or drug discovery, but the title does not indicate direct functional-label prediction.

**Full-text status:** **Required.**

#### 5. Highly accurate protein structure prediction with AlphaFold  
**Jumper et al., 2021.** *Nature.*

This is foundational for the use of predicted protein structures as inputs to downstream functional analysis. It is not itself a protein-function prediction study. Its importance is methodological: structural models can enable function inference for proteins without experimentally determined structures.

The relevant issues for this question are therefore indirect:

- how structural accuracy varies across proteins and regions;
- whether predicted structures are suitable for active-site or interaction inference; and
- how uncertainty in structure prediction propagates into function prediction.

**Full-text status:** **Available locally, but full-text verification is still required for any detailed claim.**

#### 6. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences  
**Váradi et al., 2023.** *Nucleic Acids Research.*

This record is relevant as a potential **resource or dataset source** for structure-based function prediction. It indicates very broad structure coverage, but the supplied metadata do not show whether the article evaluates functional prediction models. Full text is needed to verify:

- database contents and confidence measures;
- sequence and taxonomic coverage;
- update procedures;
- redundancy or homology issues; and
- appropriate uses and limitations for downstream machine learning.

**Full-text status:** **Required; the listed PDF download returned a 403 error.**

---

### Tier 3: Closely related protein-machine-learning applications

#### 7. Hierarchical graph learning for protein–protein interaction  
**Gao et al., 2023.** *PubMed record, PMID 36841846.*

Protein–protein interaction prediction is not identical to general protein-function prediction, but it is a closely related functional task. Graph learning may operate at several levels, potentially including residues, domains, proteins, or interaction networks. This record may inform:

- graph representations of protein relationships;
- hierarchical neural architectures;
- interaction datasets and negative sampling; and
- evaluation of binary or multi-label interaction predictions.

It should be included as supporting evidence rather than direct evidence unless the full text shows explicit functional annotation prediction.

**Full-text status:** **Required.**

#### 8. Sequence-based virtual screening using transformers  
**Zhang et al., 2025.** *PubMed record, PMID 40721411.*

This concerns transformer models and protein sequence information, but its stated application is **virtual screening**, not protein-function annotation. It may be informative about protein language models, sequence embeddings, and generalization across proteins, but it should not be used as direct evidence for function prediction without confirmation.

**Full-text status:** **Required.**

#### 9. Rapid directed evolution guided by protein language models and epistatic interactions  
**Tran et al., 2026.** *PubMed record, PMID 41712694.*

This appears to use protein language models to guide sequence optimization and account for epistatic interactions. The predicted target is likely an experimentally relevant protein property, but the title does not establish that the property is molecular function. It is relevant to the broader use of learned sequence representations and to the limitation that sequence-function relationships are affected by context and epistasis.

**Full-text status:** **Required.**

#### 10. Robust deep learning–based protein sequence design using ProteinMPNN  
**Dauparas et al., 2022.** *Science.*

This is primarily a **protein design** paper rather than a function-prediction paper. It may be useful for understanding inverse problems—designing sequences compatible with structural constraints—but should not be counted as evidence that machine learning predicts protein function.

**Full-text status:** **Required.**

#### 11. A generalizable deep learning framework for structure-based protein–ligand affinity ranking  
**Brown, 2025.** *PubMed record, PMID 41100673.*

Ligand-affinity prediction is a specific biochemical property and may be relevant to molecular function, binding specificity, and annotation. Nevertheless, it is narrower than general protein-function prediction. It may provide useful evidence on structure-based representations, generalization, and ranking metrics.

**Full-text status:** **Required.**

#### 12. Machine Learning Methods in Protein–Protein Docking  
**Michalik and Kuder, 2024.** *PubMed record, PMID 38987466.*

This review is relevant to structural interaction prediction and therefore to one component of protein function. It is not necessarily about functional annotation. Full text is needed to determine whether it discusses datasets, benchmarks, and metrics that transfer to function prediction.

**Full-text status:** **Required.**

#### 13. Computational modelling of olfactory receptors  
**Odoemelam, Steuber and Schmuker, 2025.** *PubMed record, PMID 40441539.*

This may include machine-learning-based structure or function modelling for a particular receptor family. The title alone does not indicate the methods or whether prediction was validated experimentally. It is a possible domain-specific example, but not currently strong evidence for the general question.

**Full-text status:** **Required.**

---

### Tier 4: General machine-learning, interpretability, and methodological context

#### 14. A guide to machine learning for biologists  
**Greener et al., 2021.** *Nature Reviews Molecular Cell Biology.*

Useful for general principles relevant to protein-function modelling, including feature construction, model selection, validation, and interpretation. It is not protein-function-specific and should support methodological discussion rather than serve as primary evidence.

**Full-text status:** **Available locally; verify before extracting specific recommendations.**

#### 15. Leakage and the reproducibility crisis in machine-learning-based science  
**Kapoor and Narayanan, 2023.** *Patterns.*

This is highly relevant to limitations. It may inform concerns about:

- information leakage between training and test sets;
- non-independent biological samples;
- overly optimistic benchmark results;
- inadequate external validation; and
- reproducibility of computational studies.

These concerns are especially important for protein datasets, where homologous sequences or related structures can occur across data partitions. The record is not protein-specific, so its implications need to be applied carefully.

**Full-text status:** **Required; the listed PDF returned a 403 error.**

#### 16. Practical guide to SHAP analysis  
**Ponce Bobadilla et al., 2024.**

Potentially relevant to interpretation of protein-function models if feature attribution is used. It does not provide direct evidence about protein prediction performance or biological validity.

**Full-text status:** **Required; the listed PDF returned a 403 error.**

#### 17. Informed Machine Learning  
**von Rueden et al., 2021.**

Potentially relevant to incorporating prior biological knowledge, physical constraints, structural information, or ontology relationships into models. This is methodological background rather than protein-specific evidence.

**Full-text status:** **Required; the listed PDF returned a 404 error.**

#### 18. Using machine learning approaches for multi-omics data analysis: A review  
**Reel et al., 2021.**

Could inform the use of integrated transcriptomic, proteomic, and other molecular data for functional inference. It is not specifically focused on protein-function prediction.

**Full-text status:** **Required; the listed full-text route returned a 403 error.**

---

## Records that should generally be excluded from the core synthesis

The following records appear unrelated to the question or concern clinical prediction rather than protein-function prediction:

- Machine-learning prediction of type 2 diabetes subtypes;
- AKT and EZH2 inhibitors in triple-negative breast cancer;
- dynamic prediction of non-neutral SARS-CoV-2 variants;
- LCN2 and renal-transplant injury;
- discovery of an RORγt inhibitor;
- baicalein mechanisms in cervical cancer;
- HBV-related acute-on-chronic liver failure mortality;
- BRAF drug-resistance variants;
- AI-guided therapy discovery in inflammatory bowel disease;
- machine-learning prediction of lung-cancer drug efficacy;
- virtual-patient analysis of PD-1 biomarkers;
- reviews of deep learning in general;
- swarm learning for clinical machine learning;
- generative AI in general;
- small-data machine learning in materials science;
- digital twinning;
- ensemble deep learning;
- chronic kidney disease prediction; and
- extreme learning machines.

Some of these papers may use proteins as biomarkers, targets, or molecular features, but that is not equivalent to predicting protein function. They should only be reconsidered if full-text screening shows a distinct protein-function prediction component.

---

## What can be concluded about methods?

Based on the titles, the relevant records indicate several major modelling strategies:

1. **Graph neural networks for structural prediction**  
   The Gligorijević et al. paper is the clearest example. Protein structures can be encoded as graphs, allowing models to learn local and long-range spatial relationships relevant to function.

2. **Protein language models and transformer representations**  
   The records on sequence-based virtual screening and directed evolution indicate the use of learned sequence representations. These models may capture evolutionary or contextual information without relying exclusively on manually engineered features.

3. **Structure-informed learning**  
   AlphaFold and related structure-prediction work provide predicted three-dimensional models that can be used when experimental structures are unavailable. This expands the possible coverage of structure-based function prediction but introduces uncertainty from predicted coordinates and confidence estimates.

4. **Interaction and network models**  
   Graph-learning and protein–protein interaction papers suggest that function can be inferred from relational information, including interaction partners and network context.

5. **Integrated and knowledge-informed models**  
   General methodological records point toward combining sequence, structure, interaction, omics, and prior biological knowledge. Whether the supplied protein-specific studies actually do this must be verified.

---

## Datasets and evaluation metrics

The supplied metadata do **not** identify the datasets or metrics used by the core studies. Full-text extraction should specifically look for the following.

### Likely dataset categories to verify

- experimentally annotated protein sequences;
- Gene Ontology or other curated functional annotations;
- protein structures from the Protein Data Bank;
- predicted structures from AlphaFold DB;
- protein–protein interaction databases;
- enzyme or metalloprotein specialist databases;
- sequence-similarity-reduced benchmark sets;
- domain or family-level datasets; and
- experimentally measured biochemical or binding datasets.

### Metrics to verify

For multi-label functional annotation, relevant metrics may include:

- precision, recall, and F1 score;
- micro- and macro-averaged scores;
- area under the ROC curve;
- area under the precision–recall curve;
- top-\(k\) precision or recall;
- coverage and ranking-based metrics;
- ontology-aware semantic similarity measures; and
- calibration or confidence metrics.

For interaction or affinity tasks, likely metrics include:

- AUROC and AUPRC;
- accuracy, precision, recall, and F1;
- correlation coefficients;
- root mean squared error or mean absolute error for regression; and
- ranking measures such as enrichment or top-\(k\) retrieval.

These are **candidate metrics to look for, not findings established by the supplied records**.

---

## Remaining limitations and risks

Several limitations are likely to be important, but their presence and magnitude must be confirmed in the primary papers.

1. **Annotation incompleteness and label noise**  
   Protein databases contain unevenly characterized proteins. An unannotated protein is not necessarily nonfunctional, and functional labels may be incomplete or too broad.

2. **Homology and data leakage**  
   Random sequence splitting can place highly similar proteins in both training and test sets, producing inflated performance. Evaluation should use identity-controlled or family-level splits where appropriate.

3. **Class imbalance and hierarchical labels**  
   Common functions are overrepresented, while rare functions may have very few examples. Gene Ontology labels are also hierarchical and non-independent, complicating both training and evaluation.

4. **Limited generalization to novel proteins**  
   Strong performance on proteins similar to the training set may not translate to remote homologues, new folds, unusual taxa, membrane proteins, disordered proteins, or multi-functional proteins.

5. **Dependence on structural quality**  
   Structure-based methods may be sensitive to missing regions, flexible conformations, ligand states, oligomerization, and errors in predicted structures.

6. **Function is context-dependent**  
   Protein activity can depend on cellular localization, expression, post-translational modification, cofactors, interaction partners, environmental conditions, and substrate availability. A static sequence or structure may not capture all of these factors.

7. **Interpretability does not guarantee biological explanation**  
   Attribution methods can identify influential inputs, but those signals still require experimental or mechanistic validation.

8. **Benchmark and reproducibility problems**  
   Inconsistent preprocessing, hidden overlap, incomplete reporting, and lack of external validation can make comparisons unreliable.

---

## Priority full-text verification list

The highest-priority records for full-text retrieval and structured extraction are:

1. **Gligorijević et al. (2021)** — direct structural function-prediction study.
2. **Yu et al. (2022)** — metalloprotein machine-learning review.
3. **Gao et al. (2023)** — graph learning for protein–protein interactions.
4. **Chen et al. (2024)** and **Schauperl & Denny (2022)** — structural prediction context.
5. **Jumper et al. (2021)** and **Váradi et al. (2023)** — structural resources relevant to downstream prediction.
6. **Tran et al. (2026)** and **Zhang et al. (2025)** — protein language-model applications.
7. **Kapoor & Narayanan (2023)** — leakage and reproducibility concerns.
8. **Gligorijević et al. and any interaction/affinity papers** — for exact datasets, split strategies, baselines, and metrics.

Overall, the supplied set supports a preliminary conclusion that protein-function prediction is moving toward **multimodal learning over sequence, structure, and biological networks**, with graph neural networks and protein language models as prominent approaches. It does not yet support a reliable comparison of model performance, datasets, or limitations because those details are absent from the bibliographic records and require full-text verification.