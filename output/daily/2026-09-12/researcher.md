# Evidence overview

## Scope and relevance

The supplied records contain a small number of studies directly concerned with protein-function prediction, alongside a larger group on protein structure prediction, protein–protein interactions, ligand discovery, clinical biomarkers, and general machine learning. The strongest evidence for the question comes from:

1. **Direct structure- or sequence-based protein-function prediction**
2. **Reviews of machine learning for protein knowledge or metalloproteins**
3. **Protein structure and interaction models that provide inputs for function prediction**
4. **General machine-learning guidance relevant to evaluation and reproducibility**

The bibliographic metadata alone do not establish which datasets, label definitions, train/test splits, or evaluation metrics were used. These details require full-text verification.

---

## 1. Highest-relevance records

### 1.1 Structure-based protein-function prediction

**Gligorijević et al. (2021), “Structure-based protein function prediction using graph convolutional networks.”**  
DOI: 10.1038/s41467-021-23303-9

This is the most directly relevant primary study in the set. It addresses prediction of protein function from structural information using graph convolutional networks. The likely conceptual workflow is:

- represent a protein structure as a graph;
- encode residues, contacts, or geometric relationships as graph features;
- use graph convolutions to propagate information across the structure;
- predict one or more functional labels.

The record should be examined to determine:

- whether the task is Gene Ontology prediction, enzyme classification, ligand/function prediction, or another endpoint;
- whether experimentally determined structures, predicted structures, or both were used;
- how structural graphs and node/edge features were defined;
- whether the problem was single-label or multilabel;
- how homologous proteins were separated between training and test sets;
- which metrics were reported.

**Full-text verification: high priority.** The title establishes direct relevance, but not the dataset, model architecture, baselines, or quantitative performance.

---

### 1.2 Broad review of protein language models and machine learning

**Bordin et al. (2023), “Novel machine learning approaches revolutionize protein knowledge.”**  
PMID: 36504138

This review is likely to provide the broadest overview of modern protein representation learning, including protein language models (PLMs), self-supervised learning, sequence embeddings, and their applications to protein annotation. It is particularly relevant for understanding how models learn from large unlabeled sequence databases and are subsequently adapted to supervised tasks such as:

- protein-function classification;
- enzyme or substrate prediction;
- subcellular localization;
- interaction prediction;
- mutation-effect prediction;
- annotation transfer or retrieval.

The full text is needed to identify which specific function-prediction studies, databases, benchmarks, and metrics the review discusses. It may also help distinguish general protein “knowledge” tasks from experimentally validated function prediction.

**Full-text verification: high priority.**

---

### 1.3 Machine learning for metalloproteins

**Yu, Wang, and Teo (2022), “Machine Learning Approaches for Metalloproteins.”**  
PMID: 35209064

This review is relevant to a specialized but important class of function-prediction problems. Metalloprotein models may use sequence, structure, physicochemical descriptors, metal-binding-site features, or combinations of these inputs to predict:

- metal-binding proteins;
- metal-binding residues;
- metal identity or coordination;
- metalloprotein function or activity.

The main value of this record is likely its discussion of domain-specific feature engineering and the difficulty of predicting function when metal coordination, structure, and cellular context all matter.

**Full-text verification: high priority.** The title does not show whether the review focuses mainly on function prediction, binding-site prediction, or broader metalloprotein analysis.

---

## 2. Important supporting records

### 2.1 Protein structure prediction as an upstream source of functional information

**Jumper et al. (2021), “Highly accurate protein structure prediction with AlphaFold.”**  
DOI: 10.1038/s41586-021-03819-2

**Chen et al. (2024), “AI-Driven Deep Learning Techniques in Protein Structure Prediction.”**  
PMID: 39125995

**Schauperl and Denny (2022), “AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges.”**  
PMID: 35727311

These records concern structure prediction rather than protein-function prediction itself. They are nevertheless relevant because predicted structures can be used as inputs to structure-based function models, including graph neural networks and geometric deep-learning methods.

Their relevance to the question is therefore indirect:

- structure prediction can expand the number of proteins for which structural features are available;
- predicted structures may support function inference for proteins lacking experimental structures;
- structural confidence and local errors can affect downstream function predictions.

The AlphaFold paper should not be treated as evidence that AlphaFold directly predicts molecular function. It primarily supports the availability of predicted structural representations.

**Full-text verification: useful but secondary.** The key issue is whether the record explicitly discusses downstream function inference, rather than only structural accuracy.

---

### 2.2 Structural database coverage

**Váradi et al. (2023), “AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences.”**  
DOI: 10.1093/nar/gkad1011

This record is relevant to dataset construction. Large predicted-structure repositories make it possible to develop function-prediction systems using structural inputs at a much larger scale than would be possible with experimentally solved structures alone.

However, broad structural coverage does not guarantee broad functional coverage. Many proteins have incomplete, uncertain, or computationally transferred annotations. A full-text review should determine:

- how structure coverage is defined;
- whether confidence scores are included;
- what sequence databases and taxonomic groups are represented;
- whether the database is intended for function annotation or primarily structural access.

**Full-text verification: moderate to high priority.**

---

### 2.3 Protein–protein interaction prediction

**Gao et al. (2023), “Hierarchical graph learning for protein-protein interaction.”**  
PMID: 36841846

**Michalik and Kuder (2024), “Machine Learning Methods in Protein-Protein Docking.”**  
PMID: 38987466

These records address interaction prediction or docking rather than general protein-function prediction. They are relevant because interaction partners and interaction interfaces are functional evidence. Models may use:

- protein sequences;
- predicted or experimental structures;
- residue-contact graphs;
- interface geometry;
- experimentally reported interaction networks.

Interaction prediction can therefore support functional annotation, but it should not be equated with direct prediction of biochemical or cellular function. The full texts are needed to determine whether the studies evaluate functional consequences or only interaction/docking accuracy.

**Full-text verification: moderate priority.**

---

### 2.4 Sequence-based transformers and protein language models

**Zhang et al. (2025), “Sequence-based virtual screening using transformers.”**  
PMID: 40721411

This paper is primarily about virtual screening, not protein-function annotation. It may nevertheless be relevant if it uses protein sequence representations to infer ligand-binding or activity-related properties. Its inclusion should be conditional on the full text confirming that protein function or activity prediction is an evaluated task.

**Full-text verification: moderate priority.**

**Tran et al. (2026), “Rapid directed evolution guided by protein language models and epistatic interactions.”**  
PMID: 41712694

This record concerns the use of protein language models to guide sequence optimization and directed evolution. It is not necessarily a function-prediction study. It may provide evidence that PLMs can rank or model sequence variants associated with a desired phenotype, but that is distinct from predicting the natural function of an uncharacterized protein.

**Full-text verification: moderate priority, but likely peripheral.**

---

### 2.5 Computational modelling of specific protein families

**Odoemelam, Steuber, and Schmuker (2025), “Computational modelling of olfactory receptors.”**  
PMID: 40441539

This review may include machine-learning approaches for predicting receptor structure, ligand interactions, or receptor function. It is relevant only if it discusses generalizable function-prediction methods rather than receptor modelling alone.

**Full-text verification: moderate priority.**

---

## 3. Methodological and evaluation context

### 3.1 General guidance for machine learning in biology

**Greener et al. (2021), “A guide to machine learning for biologists.”**  
DOI: 10.1038/s41580-021-00407-0

This is not protein-function-specific, but it is useful for interpreting model-development choices. It may help assess:

- feature representation;
- supervised versus unsupervised learning;
- overfitting;
- validation design;
- class imbalance;
- model interpretation;
- appropriate performance reporting.

**Full-text verification: useful for methodological context.**

### 3.2 Leakage and reproducibility

**Kapoor and Narayanan (2023), “Leakage and the reproducibility crisis in machine-learning-based science.”**  
DOI: 10.1016/j.patter.2023.100804

This record is directly relevant to limitations in protein-function prediction, even though it is not protein-specific. Sequence datasets commonly contain homologous or near-duplicate proteins. Randomly splitting such data can place highly similar sequences in both training and test sets, producing overly optimistic estimates of generalization.

Important issues to check in protein-function studies include:

- sequence-identity clustering before splitting;
- separation of protein families across partitions;
- temporal or taxonomic holdouts;
- duplicate and near-duplicate removal;
- leakage through annotation databases or structural templates;
- reuse of benchmark data during model development.

**Full-text verification: high priority for the limitations section.**

### 3.3 Explainability

**Ponce Bobadilla et al. (2024), “Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development.”**  
DOI: 10.1111/cts.70056

This is not specific to protein function, but it is relevant to interpretation. Feature-attribution methods such as SHAP can help identify influential residues, sequence regions, structural contacts, or molecular descriptors. However, an attribution is not automatically a mechanistic explanation and should be validated experimentally or with independent structural evidence.

**Full-text verification: secondary priority.**

---

## 4. Records that are largely outside the question

The following records concern clinical prediction, cancer biology, disease biomarkers, drug-response prediction, general drug discovery, agriculture, materials science, digital twins, or generic deep learning. They do not provide direct evidence about machine-learning prediction of protein function:

- Tanabe et al. (2024), type 2 diabetes subtypes
- Schade et al. (2024), AKT and EZH2 inhibitors in TNBC
- Wu et al. (2025), LCN2 and renal injury
- Yoo et al. (2026), RORγt inhibitor discovery
- Wang et al. (2025), baicalein and cancer targets
- Zhang et al. (2025), HBV-related ACLF mortality
- Sahoo et al. (2021), inflammatory bowel disease therapy
- Li et al. (2025), lung-cancer drug efficacy
- Arulraj et al. (2024), PD-1 blockade biomarkers
- Pang et al. (2024), diabetic retinopathy and treatment response
- Li et al. (2025), mTOR/p53 therapy in AML
- Reel et al. (2021), multi-omics machine learning
- Benos et al. (2021), machine learning in agriculture
- Xu et al. (2023), small-data machine learning in materials science
- Feuerriegel et al. (2023), generative AI
- Rathore et al. (2021), AI and digital twinning
- Ganaie et al. (2022), ensemble deep learning
- Chittora et al. (2021), chronic kidney disease prediction
- Ahmed et al. (2022), diabetes prediction
- Warnat-Herresthal et al. (2021), decentralized clinical machine learning
- von Rueden et al. (2021), informed machine learning
- Alzubaidi et al. (2021), general deep-learning review
- Dauparas et al. (2022), ProteinMPNN sequence design
- Passaro et al. (2025), binding-affinity prediction

These records may offer general methodological concepts, but they should not be used as primary evidence for protein-function prediction unless full-text inspection reveals a relevant protein-function benchmark or analysis.

---

# Synthesis of the available evidence

## How machine-learning methods are being used

The records support three main modelling strategies.

### 1. Sequence-based models

Protein sequences can be represented using:

- hand-crafted physicochemical or composition features;
- k-mers or profile-based features;
- embeddings from protein language models;
- transformer representations learned from large sequence collections.

These representations can then be used for classification or multilabel prediction of functional annotations. PLMs are particularly attractive because they can be pretrained without complete functional labels and later adapted to smaller labelled datasets. The supplied records suggest this area is covered by Bordin et al. and possibly by the transformer and directed-evolution papers, but the exact prediction tasks require full-text confirmation.

### 2. Structure-based models

A protein structure can be represented as:

- a residue-contact graph;
- a geometric graph with spatial coordinates;
- a surface or pocket representation;
- a three-dimensional neural-network input.

The Gligorijević et al. paper provides the clearest direct example: graph convolutional networks are used to learn from structural relationships for function prediction. Predicted structures, including AlphaFold-derived structures, may extend this approach to proteins without experimental structures.

### 3. Integrated sequence–structure and interaction models

More recent systems may combine:

- sequence embeddings;
- predicted or experimental structures;
- residue-level contacts;
- protein–protein interaction networks;
- ligand or metal-binding information;
- evolutionary profiles and annotations.

Such integration can improve biological coverage, but it also creates additional risks of data leakage and makes it harder to determine which information drives a prediction.

---

## Datasets likely to be important

The supplied records do not provide enough information to identify the exact datasets used in the direct studies. Full-text review should specifically extract whether models use:

- **Gene Ontology annotations**, especially molecular function, biological process, and cellular component;
- **UniProt or Swiss-Prot** reviewed annotations;
- **Protein Data Bank** structures;
- **AlphaFold Protein Structure Database** structures;
- **sequence-similarity or profile databases**;
- **enzyme classification datasets**, such as EC-number labels;
- **protein–protein interaction databases**;
- **metalloprotein and metal-binding-site datasets**;
- **ligand-binding or activity datasets**;
- **temporal, taxonomic, or experimentally curated benchmark sets**.

A crucial distinction is whether annotations are experimentally supported or computationally propagated. Propagated labels can make a benchmark appear large while reducing independence between examples.

---

## Evaluation metrics

The supplied metadata do not state which metrics were used. For protein-function prediction, the most appropriate metrics depend on the task.

### Multilabel function annotation

Because proteins can have multiple functions and labels are often imbalanced, relevant metrics include:

- precision, recall, and F1 score;
- micro- and macro-averaged F1;
- area under the precision–recall curve;
- area under the ROC curve;
- precision at \(k\);
- recall at \(k\);
- coverage or annotation-completeness measures;
- Gene Ontology semantic-similarity metrics.

Accuracy alone is generally inadequate for sparse multilabel annotation.

### Hierarchical ontology prediction

For Gene Ontology or other hierarchical labels, evaluation should account for parent–child relationships. A prediction of a specific term may imply its ancestors, and errors at different levels should not necessarily be treated as equivalent.

### Enzyme or protein-family classification

Typical measures may include:

- balanced accuracy;
- macro-F1;
- Matthews correlation coefficient;
- per-class precision and recall;
- top-\(k\) accuracy;
- calibration and confidence-based coverage.

### Structural or interaction tasks

For structural interaction or binding predictions, likely metrics include:

- precision–recall and ROC curves;
- contact or interface precision;
- docking success rates;
- ranking metrics;
- affinity-prediction errors such as RMSE or correlation.

These should not be conflated with function-prediction performance.

**All metric claims require full-text verification.**

---

# Remaining limitations

## 1. Incomplete and noisy functional labels

Protein function is multidimensional and incompletely observed. A protein may have a known molecular activity but an unknown biological process or cellular location. Negative labels are also difficult: absence of an annotation does not necessarily mean absence of a function.

## 2. Homology and data leakage

Sequence similarity between training and test proteins can substantially inflate performance. This is especially important for function prediction because models may succeed by recognizing family membership rather than learning transferable biochemical principles. Cluster-based, family-level, temporal, or taxonomic holdouts are therefore more informative than random splits.

## 3. Annotation bias

Well-studied organisms and protein families are overrepresented in curated databases. Models may perform well on familiar proteins but poorly on proteins from underrepresented taxa, divergent families, or unusual cellular environments.

## 4. Dependence on predicted structures

Structure-based models using predicted structures inherit errors from the structure predictor. Local uncertainty may be especially consequential for active sites, flexible regions, interfaces, and ligand-binding pockets.

## 5. Limited functional ground truth

Many benchmarks measure agreement with existing annotations rather than experimentally testing a new prediction. High benchmark scores therefore do not necessarily demonstrate discovery of previously unknown function.

## 6. Class imbalance and ontology complexity

Protein-function labels are highly unevenly distributed. Common broad terms have many examples, whereas specific functions may have very few. Hierarchical and multilabel structure further complicate both training and evaluation.

## 7. Poor mechanistic interpretability

A model may identify a useful sequence or structural pattern without revealing why it is biologically important. Attribution methods can generate hypotheses, but causal or mechanistic interpretation generally requires independent structural, biochemical, or cellular validation.

## 8. Reproducibility and benchmark instability

Results can depend strongly on database release, annotation version, redundancy filtering, split strategy, and hyperparameter selection. Studies should report dataset versions, preprocessing, similarity thresholds, code, model checkpoints, and independent test sets.

---

# Overall assessment

The evidence set contains one clearly direct primary study—**structure-based protein-function prediction using graph convolutional networks**—and several useful reviews and supporting papers on protein language models, metalloproteins, predicted structures, and protein interactions. The central methodological trend is a shift from hand-crafted sequence features toward learned sequence embeddings, graph-based structural representations, and combined sequence–structure models.

However, the supplied records are insufficient to answer the dataset and metric portions of the question definitively. The **Gligorijević et al. paper**, **Bordin et al. review**, **Yu et al. review**, and the **Kapoor and Narayanan reproducibility paper** should receive priority full-text verification. The AlphaFold and AlphaFold Database papers are important for understanding structural inputs and data availability, but they should be treated as indirect evidence rather than direct demonstrations of protein-function prediction.