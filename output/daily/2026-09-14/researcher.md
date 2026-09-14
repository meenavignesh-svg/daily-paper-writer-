## Relevance-ranked evidence overview

This screening set contains a small number of records directly addressing **protein-function prediction**, alongside many papers on protein structure prediction, protein–protein interactions, drug discovery, clinical prediction, or general machine learning. The direct evidence is therefore narrower than the full record set suggests. Because abstracts or full texts were not supplied for most PubMed records, specific datasets, metrics, and comparative results should be verified in the full papers.

### Tier 1: Directly relevant to protein-function prediction

#### 1. Structure-based protein function prediction using graph convolutional networks  
**Gligorijević et al. (2021), Nature Communications**  
This is the most directly relevant primary study in the set. It represents proteins as structural graphs and applies graph convolutional learning to predict functional annotations. This addresses a central use of machine learning in the field: learning relationships between residue-level structural context, protein topology, and functional labels such as Gene Ontology terms.

- **Likely input:** protein structures or residue-contact graphs, possibly combined with sequence-derived features.
- **Prediction task:** assigning molecular-function, biological-process, or cellular-component annotations.
- **Datasets:** likely experimentally determined and/or predicted protein structures linked to functional annotations. The exact sources, homology-reduction procedure, and train/test split require verification.
- **Metrics:** function-prediction studies commonly report precision–recall measures, F-measure or maximum F-measure, area under the precision–recall curve, and sometimes per-term or per-protein coverage. The exact metrics used by this paper must be checked.
- **Importance:** demonstrates how structural information can complement sequence-based annotation, particularly for proteins with weak sequence similarity.
- **Limitations requiring examination:** dependence on structural quality, incomplete or noisy functional annotations, class imbalance across Gene Ontology terms, and possible information leakage between homologous proteins.

**Full-text verification: essential.** This record should be the first paper examined for concrete evidence on datasets, architecture, baselines, and evaluation.

#### 2. Novel machine learning approaches revolutionize protein knowledge  
**Bordin et al. (2023), review**  
This review is likely useful for mapping the wider field. Its title suggests coverage of protein language models, sequence annotation, structure prediction, protein embeddings, and possibly interaction or function inference.

- **Likely contribution:** overview of how machine learning is used to expand or interpret protein knowledge rather than a single new prediction model.
- **Potential relevance:** sequence-based function prediction, large-scale annotation of uncharacterized proteins, protein language models, and integration of sequence, structure, and evolutionary information.
- **Datasets and metrics:** likely discussed across multiple studies rather than as one standardized benchmark.
- **Limitations:** annotation bias, limited experimental validation, homology leakage, interpretability, and the difficulty of predicting functions that are poorly represented in existing databases.

**Full-text verification: essential.** The title alone does not establish which methods, datasets, or metrics are covered.

#### 3. Machine Learning Approaches for Metalloproteins  
**Yu et al. (2022), review**  
This review is relevant to a specialized form of protein-function prediction: predicting metal-binding proteins, metal-binding residues, metalloprotein classes, or catalytic properties.

- **Methods potentially covered:** support-vector machines, random forests, neural networks, sequence-derived descriptors, structural features, and possibly ensemble methods.
- **Datasets:** likely curated metalloprotein and non-metalloprotein sets, sequence databases, structural databases, and residue-level metal-binding annotations.
- **Metrics:** likely sensitivity, specificity, accuracy, Matthews correlation coefficient, precision, recall, F1 score, and area under the ROC curve. These must not be assumed without checking the review.
- **Limitations:** small and imbalanced datasets, redundancy among homologous proteins, incomplete metal-binding annotations, and the difficulty of distinguishing catalytic metal binding from non-functional or structural metal association.

**Full-text verification: essential.**

---

### Tier 2: Relevant methodological or enabling evidence

#### 4. Highly accurate protein structure prediction with AlphaFold  
**Jumper et al. (2021)**

This is not a protein-function prediction paper, but it is highly relevant because predicted structures are increasingly used as inputs to structure-based function-prediction models. AlphaFold can expand structural coverage for proteins lacking experimentally determined structures.

Its relevance is therefore indirect:

- predicted structures can support graph-based function prediction;
- structural similarity can suggest functional relationships;
- confidence estimates may help identify predictions that are more or less reliable.

Important limitations include uncertainty in low-confidence or disordered regions, problems with alternative conformations and complexes, and the fact that structural prediction does not by itself establish biochemical function.

**Full-text verification: recommended**, particularly if discussing how AlphaFold-derived structures are used as training or inference inputs.

#### 5. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences  
**Váradi et al. (2023)**

This paper documents a major enabling resource. Large-scale predicted-structure databases provide broad coverage for proteins that previously lacked structural information. They may facilitate structural annotation and training of models using protein structure.

However, database coverage should not be confused with functional validation. The database contains predicted structures, not experimentally confirmed functional assignments for every protein.

**Full-text verification: recommended** for database scope, confidence filtering, provenance, and possible links to functional annotations.

#### 6. AI-Driven Deep Learning Techniques in Protein Structure Prediction  
**Chen et al. (2024), review**

Relevant mainly as background on deep-learning representations of proteins. It may discuss convolutional, attention-based, transformer, and structure-prediction architectures. Its direct contribution to function prediction is likely limited unless it explicitly covers downstream functional annotation.

**Full-text verification: recommended.**

#### 7. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges  
**Schauperl and Denny (2022), review**

This is primarily a structure-prediction and drug-discovery review. It may help explain how predicted structures are used in downstream tasks, but it should not be treated as direct evidence for protein-function prediction without checking the text.

**Full-text verification: recommended if cited for functional annotation.**

#### 8. Hierarchical graph learning for protein–protein interaction  
**Gao et al. (2023)**

Protein–protein interaction prediction is adjacent to function prediction. Interaction partners and interaction networks can be used as functional evidence, and graph-learning models may infer protein roles from network context. Nevertheless, predicting an interaction is not the same as predicting a Gene Ontology function.

Potentially relevant data include protein-interaction databases and structural or sequence features. Typical metrics for interaction prediction include AUROC, AUPRC, precision, recall, and F1 score, but the exact datasets and metrics require verification.

**Full-text verification: recommended.**

#### 9. Machine Learning Methods in Protein–Protein Docking  
**Michalik and Kuder (2024), review**

This concerns docking and interaction modeling rather than function prediction. It is useful for understanding structure-based representations and interaction scoring, but it provides indirect evidence only.

**Full-text verification: optional for the main question; necessary for any detailed citation.**

#### 10. Sequence-based virtual screening using transformers  
**Zhang et al. (2025)**

This appears focused on identifying ligand–protein or compound–target relationships from sequence information. It may use protein language models or transformer representations, but virtual screening and binding prediction are distinct from broad protein-function annotation.

**Full-text verification: recommended only if the review is expanded to molecular-property or binding prediction.**

#### 11. Rapid directed evolution guided by protein language models and epistatic interactions  
**Tran et al. (2026)**

This record is relevant to the use of protein language models for predicting mutational effects and guiding protein engineering. Such models may capture sequence constraints associated with function, stability, or activity, but directed evolution is not equivalent to assigning a protein’s biological function.

**Full-text verification: recommended for mutation-effect prediction, not essential for the core review.**

#### 12. Robust deep-learning-based protein sequence design using ProteinMPNN  
**Dauparas et al. (2022)**

This concerns sequence design rather than function prediction. It may be relevant to generative protein modeling and sequence–structure relationships, but it does not directly answer how existing protein functions are annotated.

**Full-text verification: low priority.**

---

## How machine learning is being used

The records support four broad approaches, although the supplied bibliography does not provide enough information to quantify their relative use.

### 1. Sequence-based prediction

Models learn from amino-acid sequences using:

- manually designed descriptors such as composition, motifs, physicochemical properties, and evolutionary profiles;
- convolutional or recurrent neural networks;
- transformer-based protein language models;
- embeddings learned from large unlabeled protein sequence databases.

These representations can be used to predict enzyme classes, subcellular localization, binding properties, domains, residue-level functions, or Gene Ontology terms. Protein language models are particularly useful when labeled functional data are limited because they can be pretrained on very large sequence collections and then fine-tuned for specific tasks.

The supplied records on protein knowledge, transformers, and language-model-guided evolution are relevant, but their precise function-prediction tasks require full-text confirmation.

### 2. Structure-based prediction

Structural models represent a protein as:

- a three-dimensional coordinate set;
- a residue-contact graph;
- a surface or geometric representation;
- a residue-level graph with edges defined by spatial proximity.

Graph neural networks and graph convolutional networks can then learn patterns associated with functional sites or functional labels. The Gligorijević et al. paper is the clearest example in this set.

Predicted structures, including AlphaFold models, can make this approach applicable to proteins without experimentally determined structures. However, structural confidence and errors can affect downstream predictions.

### 3. Network and interaction-based inference

Protein–protein interaction networks, functional association networks, and hierarchical graph models can be used to infer function from a protein’s network neighborhood. This follows the principle that interacting or functionally associated proteins often participate in related biological processes.

Such methods are vulnerable to incomplete, biased, and context-dependent interaction data. An interaction prediction should therefore be distinguished from a direct functional annotation.

### 4. Integrated and multimodal models

Current systems increasingly combine:

- sequence embeddings;
- predicted or experimental structures;
- evolutionary profiles;
- protein–protein interaction networks;
- domain and motif annotations;
- expression or other omics data.

The advantage is that different data types provide complementary information. The disadvantages are greater computational cost, inconsistent data quality, missing modalities, and increased opportunities for train/test leakage.

---

## Datasets used or likely to be used

The supplied records do not identify a single common benchmark. Protein-function prediction commonly draws on the following resources:

- **UniProt/Swiss-Prot:** curated protein sequences and functional annotations;
- **Gene Ontology:** molecular-function, biological-process, and cellular-component labels;
- **InterPro, Pfam, and related domain databases:** domain and family annotations;
- **Protein Data Bank:** experimentally determined structures;
- **AlphaFold Protein Structure Database:** predicted structures;
- **CAFA benchmarks:** time-separated evaluations of automated function annotation;
- **STRING and BioGRID:** functional association and protein–protein interaction data;
- **specialized datasets:** for example, metalloprotein or metal-binding annotations.

Important dataset issues include:

1. **Class imbalance:** some functions have many examples, whereas rare functions have very few.
2. **Annotation incompleteness:** absence of an annotation does not necessarily mean absence of the function.
3. **Redundant homologues:** highly similar proteins in both training and test sets can inflate performance.
4. **Temporal leakage:** annotations added after model training may make retrospective evaluation unrealistic.
5. **Evidence heterogeneity:** experimentally supported and computationally inferred annotations may be mixed.
6. **Species and taxonomic bias:** many datasets overrepresent model organisms and well-studied proteins.
7. **Structure-quality variation:** experimental and predicted structures have different error profiles.

The exact dataset composition, sequence-identity thresholds, temporal splits, and label-filtering procedures should be extracted from the full texts, especially for Gligorijević et al. and Yu et al.

---

## Evaluation metrics

Common metrics for protein-function prediction include:

- **precision and recall**, especially when positive labels are sparse;
- **F1 score**;
- **area under the precision–recall curve (AUPRC)**;
- **area under the ROC curve (AUROC)**;
- **maximum F-measure**, often used in Gene Ontology prediction;
- **coverage**, measuring how many proteins or terms receive predictions;
- **per-term or per-protein averages**, which help distinguish performance on common versus rare functions;
- **ranking-based metrics**, such as precision at a specified cutoff;
- **calibration and confidence measures**, which are important when predictions are used for annotation prioritization.

Accuracy alone is generally inadequate because functional labels are highly imbalanced and because unannotated proteins cannot automatically be treated as negative examples. Robust evaluation should use non-redundant, homology-aware, or time-split test sets and should report performance separately for different ontology branches and annotation frequencies.

The present records do not reliably establish which of these metrics were used in each study. **Full-text verification is required before attributing any specific metric or numerical result to a paper.**

---

## Remaining limitations

The evidence set points to several persistent limitations:

1. **Training-label quality**  
   Functional annotations are incomplete, unevenly supported, and often propagated from homologues. Models may learn database-curation patterns rather than biochemical function.

2. **Generalization to novel proteins**  
   Performance is usually strongest for proteins similar to those seen during training. It is less clear how well models perform on remote homologues, orphan proteins, new protein families, or new taxa.

3. **Data leakage and inflated benchmarks**  
   Sequence similarity between training and test proteins can produce overly optimistic results. The record on leakage and reproducibility is directly relevant as a methodological warning, although it is not protein-specific.

4. **Rare and multilabel functions**  
   Proteins often have several functions, while many function classes contain few examples. This makes both training and evaluation difficult.

5. **Dependence on predicted structures**  
   Structure-based methods can inherit errors from predicted structures, especially for disordered regions, flexible loops, membrane proteins, complexes, and alternate conformations.

6. **Limited interpretability**  
   A high-performing model may not reveal which residues, motifs, structural contacts, or network relationships support its prediction. Explainability methods such as SHAP may help, but explanations themselves require biological validation.

7. **Confusing correlation with mechanism**  
   A model can accurately associate a protein with a functional label without identifying the causal biochemical mechanism. Experimental validation remains necessary.

8. **Distribution shift**  
   Models trained on curated databases may perform poorly on proteins from underrepresented organisms, unusual environments, or clinically relevant contexts.

9. **Evaluation mismatch**  
   Standard metrics may reward prediction of frequent, broad terms while obscuring poor performance on specific or biologically important functions. Time-split and experimentally validated evaluations are more informative.

---

## Records that are low relevance or should not be used as core evidence

The following papers primarily concern clinical prediction, cancer biology, drug efficacy, biomarker discovery, or other applications and do not directly answer the question:

- Tanabe et al. (2024), diabetes subtypes  
- Schade et al. (2024), TNBC inhibitors  
- Wu et al. (2025), renal transplantation injury  
- Yoo et al. (2026), RORγt inhibitor discovery  
- Wang et al. (2025), baicalein and cervical cancer  
- Zhang et al. (2025), HBV-related mortality  
- Sahoo et al. (2021), inflammatory bowel disease therapy  
- Li et al. (2025), lung-cancer drug efficacy  
- Vu et al. (2026), urinary proteomics and Parkinson’s disease  
- Pang et al. (2024), diabetic retinopathy  
- Li et al. (2025), AML therapy  
- Odoemelam et al. (2025), olfactory-receptor modeling  

General machine-learning reviews, including Greener et al. (2021), Alzubaidi et al. (2021), Ganaie et al. (2022), and von Rueden et al. (2021), may provide methodological background but should not be presented as protein-function evidence without relevant sections being confirmed.

## Overall assessment

The strongest evidence in this collection supports a field moving from sequence-only annotation toward **multimodal prediction**, combining protein language models, structural graphs, predicted structures, and interaction networks. The clearest direct record is the graph-convolutional study of structure-based protein-function prediction, supplemented by reviews of protein knowledge and metalloprotein modeling. AlphaFold and large predicted-structure databases are important enablers rather than function-prediction methods themselves.

The main unresolved issues are not simply model architecture. They are the quality and independence of functional labels, leakage-resistant evaluation, prediction of rare or novel functions, uncertainty estimation, interpretability, and experimental validation. Full-text review of the direct studies is essential before making specific claims about datasets, metrics, or performance.