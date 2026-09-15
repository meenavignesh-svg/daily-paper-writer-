# Evidence overview

## Scope and evidence strength

The supplied records contain a small number of papers directly addressing **protein-function prediction**, alongside many papers on protein structure prediction, protein–protein interactions, drug discovery, clinical prediction, and general machine learning. The strongest evidence for the question comes from:

1. **Structure-based protein-function prediction using graph convolutional networks** (Gligorijević et al., 2021).
2. **Computational prediction of protein functional annotations** (Kulmanov and Hoehndorf, 2025).
3. **Novel machine learning approaches revolutionize protein knowledge** (Bordin et al., 2023).
4. **Machine Learning Approaches for Metalloproteins** (Yu et al., 2022).

The records establish the relevance of these topics, but the supplied metadata do **not** provide enough information to report exact datasets, train/test procedures, or evaluation metrics. Those details require full-text verification.

---

## 1. Directly relevant evidence

### 1.1 Structure-based protein-function prediction using graph convolutional networks  
**Gligorijević V et al. (2021)**  
DOI: 10.1038/s41467-021-23303-9  
**Relevance: Very high**

This is the most directly relevant primary research article in the supplied set. Its title indicates that graph convolutional networks are applied to **three-dimensional protein structures** to predict functional annotations.

The study is likely relevant to the following methodological questions:

- How structural information is represented as a graph.
- Whether residues, structural contacts, or spatial neighborhoods form the graph nodes and edges.
- How graph convolutional networks are used to predict protein-function labels.
- Whether the targets are Gene Ontology or other functional annotations.
- How predictions are evaluated under multi-label classification.
- Whether structural models, including predicted structures, are used in addition to experimentally determined structures.

**Datasets and metrics:** The title alone does not establish the training datasets, annotation source, split strategy, or metrics. These should be extracted from the full text. In particular, verify whether the study uses PDB-derived structures, Gene Ontology annotations, sequence-homology-controlled splits, and metrics such as precision–recall, Fmax, AUROC, or AUPR.

**Limitations to verify:** likely issues include incomplete structural coverage, dependence on annotation quality, class imbalance among functional terms, and reduced performance for rare or poorly represented functions. These should not be attributed to the paper without checking its results and discussion.

**Full-text verification: Required.** A local PDF is listed, which should make this a priority for detailed extraction.

---

### 1.2 Computational prediction of protein functional annotations  
**Kulmanov M and Hoehndorf (2025)**  
PMID: 40728605  
**Relevance: Very high**

This record appears to be a recent review or methodological overview focused specifically on computational prediction of protein functional annotations. It is likely the best source in the set for synthesising:

- Sequence-based, structure-based, and network-based prediction.
- Supervised, semi-supervised, and representation-learning approaches.
- Ontology-aware prediction of Gene Ontology terms.
- Use of protein language-model embeddings.
- Problems caused by incomplete and biased annotations.
- Evaluation protocols for hierarchical, multi-label functional prediction.

**Datasets and metrics:** These cannot be determined from the citation. Full-text review is needed to identify which benchmark datasets and metrics are discussed and whether the authors distinguish between random, protein-family-aware, and temporal or homology-reduced evaluation.

**Limitations to verify:** likely topics include annotation propagation errors, label imbalance, dependence among ontology terms, homology leakage, and the difficulty of predicting functions absent from the training data. These are important issues for the review but should be linked to the article only after verification.

**Full-text verification: Required.** No PDF is supplied.

---

### 1.3 Novel machine learning approaches revolutionize protein knowledge  
**Bordin N et al. (2023)**  
PMID: 36504138  
**Relevance: High, but broad**

This appears to be a broad review of modern machine-learning methods in protein science. It is likely useful for placing function prediction within the wider development of:

- Protein sequence embeddings and protein language models.
- Structure prediction and structure-informed learning.
- Protein–protein interaction prediction.
- Functional annotation and knowledge-base construction.
- Large-scale prediction enabled by pretrained models.

It may help explain how machine learning is moving from manually designed sequence features toward learned representations derived from large protein databases.

**Datasets and metrics:** Not recoverable from the record. The full text should be checked for named resources such as UniProt, Pfam, InterPro, Gene Ontology, Protein Data Bank, CAFA benchmarks, and protein language-model training corpora.

**Limitations to verify:** broad reviews commonly discuss training-data bias, interpretability, computational cost, and the gap between predictive performance and experimentally validated function. The article must be checked before using it as evidence for any specific limitation.

**Full-text verification: Required.** No PDF is supplied.

---

### 1.4 Machine Learning Approaches for Metalloproteins  
**Yu Y, Wang R, Teo RD (2022)**  
PMID: 35209064  
**Relevance: High for a functional subdomain**

This review is focused on metalloproteins, for which machine learning may be used to predict properties such as:

- Metal-binding residues or sites.
- Metal-binding specificity.
- Protein or enzyme classes.
- Catalytic activity.
- Structure or ligand interactions related to function.

It is particularly relevant because metalloprotein function depends on sequence, structure, coordination geometry, and chemical context. These proteins therefore illustrate the limitations of generic sequence-only models and the potential value of incorporating structural and biochemical features.

**Datasets and metrics:** Full text is needed to identify the data sources, feature representations, task definitions, and evaluation metrics. These may differ substantially between residue-level site prediction, protein-level classification, and activity prediction.

**Limitations to verify:** likely concerns include limited experimentally characterised metalloproteins, uneven representation of metal classes, noisy labels, and the difficulty of modelling coordination chemistry. These should be confirmed in the review.

**Full-text verification: Required.** No PDF is supplied.

---

## 2. Relevant but indirect evidence

### 2.1 AI-driven deep learning techniques in protein structure prediction  
**Chen L et al. (2024)**  
PMID: 39125995  
**Relevance: Moderate**

This record concerns protein **structure** prediction rather than function prediction. It is relevant because predicted structures are increasingly used as inputs to structure-based functional annotation. However, it should not be treated as direct evidence that a model predicts biochemical or cellular function.

**Use in the review:** background on the availability of predicted structural features and the shift from sequence-only to structure-informed prediction.

**Full-text verification: Required** if discussing methods, benchmarks, or limitations.

---

### 2.2 Highly accurate protein structure prediction with AlphaFold  
**Jumper J et al. (2021)**  
DOI: 10.1038/s41586-021-03819-2  
**Relevance: Moderate**

This is foundational for modern structure-informed function prediction. AlphaFold provides structural models that can be used downstream for functional inference, but the paper itself primarily addresses structure prediction rather than functional annotation.

**Use in the review:** explain why structure-based machine learning became more feasible at proteome scale.

**Full-text verification: Recommended** for any detailed claim about training data, structural benchmarks, confidence measures, or performance.

---

### 2.3 AlphaFold Protein Structure Database in 2024  
**Váradi M et al. (2023)**  
DOI: 10.1093/nar/gkad1011  
**Relevance: Moderate**

This record is relevant to the dataset landscape. It documents the very large availability of predicted protein structures, which can support structure-based functional prediction. It does not itself establish that those structures yield accurate function predictions.

**Use in the review:** background on structural data availability and coverage.

**Full-text verification: Required** for the exact number of structures, coverage claims, confidence thresholds, and database construction.

---

### 2.4 Machine learning methods in protein–protein docking  
**Michalik I and Kuder KJ (2024)**  
PMID: 38987466  
**Relevance: Moderate to low**

Protein–protein docking is related to interaction prediction, which can provide functional evidence, but docking is not equivalent to general protein-function prediction.

**Use in the review:** only in a section on interaction-based or structure-based functional inference.

**Full-text verification: Required** before citing specific models or metrics.

---

### 2.5 Hierarchical graph learning for protein–protein interaction  
**Gao Z et al. (2023)**  
PMID: 36841846  
**Relevance: Moderate to low**

This paper appears to address prediction of protein–protein interactions. Interaction prediction can support functional annotation through network context, but the paper should not be presented as a direct protein-function prediction study unless the full text confirms that functional labels are also predicted.

**Full-text verification: Required.**

---

### 2.6 Sequence-based virtual screening using transformers  
**Zhang S et al. (2025)**  
PMID: 40721411  
**Relevance: Low to moderate**

This concerns sequence-based screening for molecular binding or related drug-discovery tasks. It may be methodologically relevant to protein representation learning, but it is not clearly a protein-function annotation study.

**Full-text verification: Required** before including it in the main evidence synthesis.

---

### 2.7 Rapid directed evolution guided by protein language models and epistatic interactions  
**Tran VQ et al. (2026)**  
PMID: 41712694  
**Relevance: Low to moderate**

Protein language models are relevant because the same sequence representations can be used for function prediction. However, directed evolution and variant selection are distinct from predicting the function of uncharacterised proteins.

**Use in the review:** possible example of protein language models being used to model sequence–function relationships, not as direct evidence for annotation prediction.

**Full-text verification: Required.**

---

### 2.8 Robust deep-learning-based protein sequence design using ProteinMPNN  
**Dauparas J et al. (2022)**  
DOI: 10.1126/science.add2187  
**Relevance: Low**

This concerns sequence design rather than function prediction. It may be mentioned only to distinguish generative protein design from predictive functional annotation.

**Full-text verification: Not necessary for the main question; required only if discussed.**

---

### 2.9 Accurate structure prediction of biomolecular interactions with AlphaFold 3  
**Abramson J et al. (2024)**  
DOI: 10.1038/s41586-024-07487-w  
**Relevance: Low to moderate**

AlphaFold 3 predicts structures of biomolecular complexes, which may inform interaction or functional inference. The record does not indicate direct functional annotation.

**Full-text verification: Required** for any use beyond brief background.

---

## 3. General methodological and limitation evidence

### 3.1 A guide to machine learning for biologists  
**Greener JG et al. (2021)**  
DOI: 10.1038/s41580-021-00407-0  
**Relevance: Supporting**

This is useful for explaining general concepts such as:

- Training, validation, and test sets.
- Overfitting and regularisation.
- Feature engineering versus learned representations.
- Model calibration and interpretability.
- Appropriate evaluation design.

It does not provide protein-function-specific evidence, but it can support methodological explanations.

**Full-text verification: Recommended.** A local PDF is listed.

---

### 3.2 Leakage and the reproducibility crisis in machine-learning-based science  
**Kapoor S and Narayanan A (2023)**  
DOI: 10.1016/j.patter.2023.100804  
**Relevance: High for limitations**

This is important supporting evidence for discussing data leakage and inflated performance estimates. Protein-function prediction is particularly vulnerable to leakage because closely related proteins may occur in both training and test sets, and annotations may be propagated through homology.

Relevant limitations to examine include:

- Homologous sequences appearing across data splits.
- Duplicate or near-duplicate structures.
- Annotation leakage from databases used both for training and evaluation.
- Benchmark results that do not reflect performance on genuinely novel protein families.

The supplied citation alone does not show whether the paper discusses protein applications specifically.

**Full-text verification: Required.**

---

### 3.3 Informed machine learning  
**von Rueden L et al. (2021)**  
DOI: 10.1109/TKDE.2021.3079836  
**Relevance: Supporting**

This may help frame methods that incorporate prior biological knowledge, including:

- Protein ontologies.
- Structural constraints.
- Evolutionary information.
- Interaction networks.
- Biochemical rules.

It is not protein-specific, so it should be used as methodological background rather than direct evidence.

**Full-text verification: Recommended.**

---

### 3.4 Ensemble deep learning: A review  
**Ganaie MA et al. (2022)**  
**Relevance: Low**

Potentially relevant to model-combination strategies, but not specifically to protein-function prediction.

---

### 3.5 Review of deep learning  
**Alzubaidi L et al. (2021)**  
**Relevance: Low**

General deep-learning background; not protein-specific.

---

### 3.6 Practical guide to SHAP analysis  
**Ponce Bobadilla AV et al. (2024)**  
**Relevance: Low to moderate**

Potentially useful for discussing interpretability of protein-function models, but not evidence that SHAP is appropriate or validated for a particular protein-function task.

**Full-text verification: Required** if used.

---

## 4. Records not relevant to the question

The following records concern clinical prediction, cancer biology, drug efficacy, disease biomarkers, or unrelated applications and should normally be excluded from the main review:

- Machine learning-based reproducible prediction of type 2 diabetes subtypes.
- AKT and EZH2 inhibitors in triple-negative breast cancer.
- LCN2 and renal transplantation injury.
- Discovery of an RORγt inhibitor.
- Baicalein mechanisms in cervical cancer.
- Mortality prediction in HBV-related acute-on-chronic liver failure.
- Artificial-intelligence-guided therapy for inflammatory bowel disease.
- Drug efficacy prediction in lung cancer.
- Multi-omics prediction of diabetic retinopathy and treatment response.
- mTOR/p53 co-targeting in acute myeloid leukaemia.
- Swarm learning for clinical machine learning.
- Multi-omics machine-learning review.
- Machine learning in agriculture.
- Small-data machine learning in materials science.
- Generative AI.
- Digital twinning.
- Chronic kidney disease prediction.
- Extreme learning machine.

These papers may discuss general machine-learning methods, but their prediction targets are not protein functions.

---

# Synthesis by methodological approach

## Sequence-based models

The supplied records suggest that protein sequences are increasingly represented using deep neural networks and protein language models rather than only handcrafted descriptors. These models can encode evolutionary and contextual information from large sequence databases and can then be fine-tuned or used as feature generators for functional classification.

The most relevant records are:

- Bordin et al. (2023).
- Kulmanov and Hoehndorf (2025).
- Tran et al. (2026), indirectly.
- Zhang et al. (2025), indirectly.

**What must be verified:** the exact model families, pretraining databases, sequence lengths, annotation targets, and whether evaluation is performed on proteins that are homologous or non-homologous to the training data.

## Structure-based models

Graph convolutional networks can represent proteins as residue-level or atom-level graphs, with edges describing spatial proximity, chemical contacts, or structural relationships. Such models are intended to capture functional information that may not be evident from sequence alone.

The central record is:

- Gligorijević et al. (2021).

Supporting records include AlphaFold and the AlphaFold Database papers, which concern the production and availability of structural inputs rather than function prediction itself.

## Network- and interaction-based models

Protein–protein interaction networks and graph-learning methods can provide functional context through a protein’s interaction partners and network neighbourhood. However, interaction prediction is a related task and should not be conflated with direct prediction of molecular function.

Relevant records include:

- Gao et al. (2023).
- Michalik and Kuder (2024).

## Domain- or chemistry-specific models

Metalloproteins illustrate the use of specialised machine-learning models for proteins whose functions depend on particular chemical properties, metal coordination, and catalytic environments.

Relevant record:

- Yu et al. (2022).

---

# Datasets and labels

The supplied metadata do not permit a definitive dataset inventory. Full-text extraction should specifically look for:

- **UniProt or Swiss-Prot** for curated protein sequences and functional annotations.
- **Gene Ontology** for molecular-function, biological-process, and cellular-component labels.
- **Protein Data Bank** for experimentally determined structures.
- **AlphaFold Database** for predicted structures.
- **Pfam, InterPro, and related domain databases** for family and domain labels.
- **CAFA benchmarks** for prospective or benchmarked protein-function prediction.
- **Protein–protein interaction databases** for network-based inference.
- **Metal-binding or enzyme-specific databases** for metalloprotein tasks.

Important dataset questions are:

1. Are annotations experimentally supported or electronically inferred?
2. Are proteins split randomly, by sequence identity, by family, or by time?
3. Are homologous proteins excluded from the test set?
4. Are rare Gene Ontology terms retained?
5. Are multiple labels allowed per protein?
6. Are predicted structures filtered by confidence?
7. Is the test set independent of the databases used for pretraining?

---

# Evaluation metrics

The records do not provide enough evidence to report which metrics were actually used in each study. For this topic, full-text verification should distinguish among:

- **Precision, recall, and F1 score:** useful for individual labels but sensitive to class imbalance.
- **AUROC:** common for binary or one-vs-rest classification, but potentially misleading for rare functional terms.
- **AUPR:** often more informative for highly imbalanced functional-label prediction.
- **Fmax:** commonly used when prediction confidence thresholds are varied.
- **Hierarchical semantic similarity:** important when Gene Ontology relationships are considered.
- **Coverage:** measures how many proteins receive predictions at a specified reliability.
- **Calibration and reliability measures:** important when predictions are used to prioritise experimental work.
- **Top-k accuracy or precision:** relevant when models return ranked candidate functions.
- **Residue-level precision/recall:** needed for active-site or binding-site prediction.
- **Protein-level accuracy:** appropriate for single-label tasks but insufficient for multi-functional proteins.

A major point for the review is that high aggregate scores may conceal poor performance on rare functions, novel protein families, or proteins with low similarity to the training data.

---

# Remaining limitations

Across the directly relevant literature, the main limitations to investigate are:

1. **Annotation incompleteness and noise**  
   Many proteins remain poorly characterised, and database annotations may be inferred, propagated, or inconsistent.

2. **Class imbalance and long-tailed functions**  
   Common functions have many examples, whereas rare functions may have too few labelled proteins for reliable learning.

3. **Homology and data leakage**  
   Random splits can place closely related proteins in both training and test sets, producing overoptimistic results.

4. **Limited generalisation to novel proteins**  
   Performance may decline for proteins from new families, unusual organisms, or underrepresented taxa.

5. **Dependence on input quality**  
   Structure-based methods depend on structural accuracy and coverage; sequence models depend on the quality and diversity of pretraining data.

6. **Multi-function and hierarchical labels**  
   Proteins often have several related functions, making flat classification inadequate and complicating evaluation.

7. **Interpretability**  
   A predicted label does not necessarily explain which residues, motifs, contacts, or evolutionary signals support the prediction.

8. **Limited experimental validation**  
   Computational predictions are not equivalent to demonstrated biochemical activity or cellular function.

9. **Distribution shift and biological context**  
   Function can depend on tissue, organism, cofactors, localisation, oligomeric state, post-translational modification, or environmental conditions that are absent from the input data.

10. **Reproducibility and benchmark inconsistency**  
    Results can vary with database versions, annotation cut-offs, sequence-similarity thresholds, and split procedures.

---

# Priority for full-text review

## Highest priority

1. Gligorijević et al. (2021), structure-based function prediction.
2. Kulmanov and Hoehndorf (2025), functional annotation prediction.
3. Bordin et al. (2023), machine learning in protein knowledge.
4. Yu et al. (2022), machine learning for metalloproteins.
5. Kapoor and Narayanan (2023), leakage and reproducibility.
6. Greener et al. (2021), machine learning methodology for biologists.

## Medium priority

7. Jumper et al. (2021), AlphaFold.
8. Váradi et al. (2023), AlphaFold Database.
9. Gao et al. (2023), graph learning for protein–protein interaction.
10. Michalik and Kuder (2024), machine learning in protein–protein docking.
11. Chen et al. (2024), deep learning for protein structure prediction.
12. Tran et al. (2026), protein language models and directed evolution.
13. von Rueden et al. (2021), informed machine learning.

## Low priority or exclude

The clinical, cancer, drug-efficacy, agriculture, and general-domain machine-learning records should be excluded from the core evidence synthesis unless the review has a separate section on transferable machine-learning methodology.

**Overall conclusion:** The supplied evidence supports a picture of protein-function prediction moving toward sequence language models, structure-aware graph networks, and biologically informed network models. However, the records provided here do not yet support a reliable account of the exact datasets or metrics used. Full-text verification of the four directly relevant protein-function papers is essential before making study-level claims.