## Relevance-ranked evidence overview

The records contain a small number of directly relevant studies and several papers that are relevant to protein representation, structure modelling, interaction prediction, or methodological evaluation. Many of the remaining records concern clinical prediction or drug discovery rather than prediction of protein function itself.

### Tier 1: Direct evidence on protein-function prediction

#### 1. Structure-based protein function prediction using graph convolutional networks  
**Gligorijević et al., 2021**  
DOI: 10.1038/s41467-021-23303-9

This is the most directly relevant primary study. Its title indicates a graph-convolutional approach that uses protein structural information to predict function. The likely prediction targets are functional labels such as Gene Ontology terms, but this must be confirmed in the full text. The paper should be examined for:

- structural representation: residue-contact graphs, 3-D coordinates, or predicted structures;
- graph-convolutional architecture and pooling strategy;
- functional annotation source and ontology;
- handling of proteins with multiple functions;
- train/test splitting, particularly whether homologous proteins occur in both sets;
- evaluation metrics, likely including precision–recall-based measures for multilabel prediction;
- comparison with sequence-based and homology-based baselines.

**Assessment:** central evidence for the question.  
**Full-text verification:** **high priority**. A local PDF is listed, but the study’s datasets, metrics, and limitations still require direct verification.

#### 2. Machine Learning Approaches for Metalloproteins  
**Yu, Wang & Teo, 2022**  
PMID: 35209064

This review is relevant because metalloprotein function prediction often involves identifying metal-binding proteins, metal-binding residues, catalytic sites, or metal-dependent activity from sequence and structural features. It may cover classical machine-learning methods as well as deep learning. The title alone does not establish which prediction tasks are included.

Important items to extract are:

- protein and residue-level prediction tasks;
- sequence, structural, physicochemical, and evolutionary features;
- datasets and sources of positive and negative examples;
- class-imbalance treatment;
- reported metrics, such as sensitivity, specificity, Matthews correlation coefficient, F1 score, AUROC, or AUPRC;
- whether evaluations are independent, nonredundant, or homology-reduced.

**Assessment:** relevant domain-specific review, especially for enzyme and catalytic-function prediction.  
**Full-text verification:** **high priority**.

#### 3. Novel machine learning approaches revolutionize protein knowledge  
**Bordin et al., 2023**  
PMID: 36504138

This appears to be a broad review of modern protein machine learning, likely including protein language models, representation learning, structure prediction, annotation, and design. It is useful for mapping how pretrained models are applied to function prediction, but it is unlikely to provide a single standardized evaluation framework.

It may help identify:

- sequence language models and embeddings used for annotation;
- transfer learning and fine-tuning for function prediction;
- zero-shot or few-shot prediction;
- links between sequence, structure, interaction, and function;
- relevant benchmark datasets and databases.

**Assessment:** high-value contextual review, but not necessarily a source of directly comparable experimental results.  
**Full-text verification:** **high priority**.

---

### Tier 2: Closely related evidence

#### 4. AI-Driven Deep Learning Techniques in Protein Structure Prediction  
**Chen et al., 2024**  
PMID: 39125995

This is primarily about structure prediction rather than function prediction. It is relevant because predicted structures are increasingly used as inputs to structure-based functional annotation. It can provide background on the reliability and limitations of structural representations, but it should not be treated as direct evidence that a model predicts biochemical or cellular function.

**Full-text verification:** useful for understanding structure-derived inputs; not central for function-prediction outcomes.

#### 5. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges  
**Schauperl & Denny, 2022**  
PMID: 35727311

This is another indirect source. It may discuss how predicted structures support target identification, binding analysis, and functional interpretation. It is more relevant to downstream use of protein structures than to formal protein-function classification.

**Full-text verification:** secondary priority.

#### 6. Highly accurate protein structure prediction with AlphaFold  
**Jumper et al., 2021**  
DOI: 10.1038/s41586-021-03819-2

AlphaFold predicts structure, not protein function. Its relevance is indirect: structural predictions can expand the set of proteins for which structure-based function-prediction methods can be applied. The paper may also clarify structural confidence measures and the distinction between accurate structural prediction and reliable functional inference.

**Full-text verification:** not essential for the core question, but useful background.

#### 7. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences  
**Varadi et al., 2023**  
DOI: 10.1093/nar/gkad1011

This record is relevant to dataset availability. Large predicted-structure repositories can supply inputs for structure-based function prediction, but database coverage should not be equated with experimentally validated functional annotation. The full text is needed to verify coverage, confidence filtering, provenance, and possible uses in annotation pipelines.

**Full-text verification:** useful, especially for discussing data scale and limitations.

#### 8. Hierarchical graph learning for protein-protein interaction  
**Gao et al., 2023**  
PMID: 36841846

Protein–protein interaction prediction is not identical to protein-function prediction, but interaction networks can serve as functional evidence. A graph model may predict interaction edges or learn representations that are subsequently used for functional annotation. The target variable and evaluation protocol must be confirmed before treating this as function-prediction evidence.

**Full-text verification:** required if included in the evidence synthesis.

#### 9. Machine Learning Methods in Protein-Protein Docking  
**Michalik & Kuder, 2024**  
PMID: 38987466

This is relevant to structural interaction modelling rather than direct function annotation. It may provide information on geometric learning, docking poses, interface prediction, and structural evaluation, but docking metrics should not be conflated with functional prediction metrics.

**Full-text verification:** secondary priority.

#### 10. Sequence-based virtual screening using transformers  
**Zhang et al., 2025**  
PMID: 40721411

This concerns sequence-based ligand or compound screening. It may use protein language models or transformer representations, which are also used in function prediction, but the primary outcome is likely binding or virtual-screening performance rather than functional annotation.

**Full-text verification:** required before drawing conclusions about protein-function prediction.

#### 11. Rapid directed evolution guided by protein language models and epistatic interactions  
**Tran et al., 2026**  
PMID: 41712694

This is relevant to protein language models and their ability to capture sequence constraints, epistasis, or activity-associated variation. However, guided protein engineering is distinct from predicting a protein’s function. The paper may provide useful evidence about representation quality and generalization to experimental activity, but this cannot be inferred from the title alone.

**Full-text verification:** required; likely useful as emerging, adjacent evidence.

#### 12. Robust deep learning–based protein sequence design using ProteinMPNN  
**Dauparas et al., 2022**  
DOI: 10.1126/science.add2187

ProteinMPNN is primarily a sequence-design model conditioned on structure. It is not a protein-function predictor, although designed sequences may be evaluated for foldability or experimentally measured activity. It should be cited only if the review discusses the boundary between function prediction, structure prediction, and protein design.

**Full-text verification:** optional for the core synthesis.

#### 13. Accurate structure prediction of biomolecular interactions with AlphaFold 3  
**Abramson et al., 2024**  
DOI: 10.1038/s41586-024-07487-w

This is relevant to modelling protein–protein, protein–nucleic-acid, and protein–ligand interactions. Such interaction structures may support functional inference, but the paper is not, on the supplied information, a direct study of protein-function classification.

**Full-text verification:** optional or secondary priority.

---

### Tier 3: General machine-learning methodology relevant to interpretation

#### 14. A guide to machine learning for biologists  
**Greener et al., 2021**  
DOI: 10.1038/s41580-021-00407-0

Useful for explaining supervised learning, feature representations, validation, overfitting, and interpretation in biological applications. It is not protein-function-specific, but it may help frame methodological standards.

#### 15. Leakage and the reproducibility crisis in machine-learning-based science  
**Kapoor & Narayanan, 2023**  
DOI: 10.1016/j.patter.2023.100804

This is highly relevant to limitations. Protein datasets are especially vulnerable to leakage because homologous sequences, related structures, and annotations can be shared between training and test sets. The paper can support a general discussion of leakage and reproducibility, although its examples may not be specific to protein annotation.

#### 16. Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development  
**Ponce Bobadilla et al., 2024**  
DOI: 10.1111/cts.70056

Potentially relevant to interpretability, particularly when models use sequence, structural, or physicochemical features. It is not specific to protein-function prediction, and SHAP explanations do not necessarily establish biological causality.

#### 17. Informed Machine Learning—A Taxonomy and Survey of Integrating Prior Knowledge into Learning Systems  
**von Rueden et al., 2021**  
DOI: 10.1109/TKDE.2021.3079836

Relevant to incorporating biological constraints, physical priors, ontologies, structural information, or interaction networks into learning systems. It is methodological rather than protein-specific.

#### 18. Review of deep learning: concepts, CNN architectures, challenges, applications, future directions  
**Alzubaidi et al., 2021**  
DOI: 10.1186/s40537-021-00444-8

General deep-learning background. It contributes little direct evidence on protein-function datasets or evaluation.

---

### Tier 4: Adjacent biomedical applications, not direct evidence

The following studies use machine learning with protein-related measurements or targets but do not appear, from their titles, to predict protein function:

- **Machine learning prediction of 90-day mortality in HBV-related ACLF using Olink-derived inflammatory protein signatures** — Zhang et al., 2025.
- **Machine learning-driven prediction of drug efficacy in lung cancer based on protein biomarkers and clinical features** — Li et al., 2025.
- **LCN2 drives ferroptosis-associated ischemia-reperfusion injury... integrated machine learning and in vivo validation** — Wu et al., 2025.
- **Discovery of natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation** — Yoo et al., 2026.
- **Deciphering the mechanism of baicalein... PIM1 and CDK2 are key target proteins** — Wang et al., 2025.
- **Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease** — Sahoo et al., 2021.
- **AKT and EZH2 inhibitors kill TNBCs...** — Schade et al., 2024.
- **Virtual patient analysis... predictive biomarkers for PD-1 blockade** — Arulraj et al., 2024.
- **Computational modelling of olfactory receptors** — Odoemelam et al., 2025.

These may contain examples of protein biomarkers, target identification, virtual screening, or mechanistic inference. They should not be used as evidence for general protein-function prediction unless full-text review confirms that the models explicitly predict molecular function, activity, binding, localization, or related protein-level labels.

The remaining records on diabetes subtypes, diabetic retinopathy, inflammatory bowel disease treatment response, chronic kidney disease, agriculture, digital twins, and general generative AI are outside the core scope.

## What the supplied evidence suggests about current uses of machine learning

Taken together, the most relevant records support several broad modes of use:

1. **Sequence-based prediction**  
   Protein sequences are converted into hand-engineered features, learned embeddings, or representations from protein language models. These representations can be used to predict functional classes, enzyme activity, binding properties, or residue-level annotations.

2. **Structure-based prediction**  
   Proteins are represented as three-dimensional coordinates, residue-contact graphs, geometric graphs, or surface features. Graph neural networks can then learn relationships between structural patterns and functional labels. The Gligorijević et al. paper is the clearest direct evidence for this category.

3. **Network-based prediction**  
   Protein–protein interaction networks and other biological graphs provide relational information. A model may infer function from a protein’s interaction partners, network position, or jointly learned sequence and network representations.

4. **Multimodal prediction**  
   Current methods increasingly combine sequence, predicted or experimental structure, interaction data, evolutionary information, ligand data, and functional annotations. AlphaFold-derived structures and protein-language-model embeddings are important enabling resources, although the supplied records do not establish how well any particular multimodal system performs for function prediction.

5. **Transfer learning and foundation models**  
   Large models trained on protein sequences or structures can be adapted to smaller labelled datasets. The records on protein language models, transformers, and broad protein machine learning are relevant to this trend, but their exact function-prediction tasks and benchmarks require full-text verification.

## Datasets and labels

The bibliographic metadata do not provide enough information to identify the exact datasets used in the direct studies. Full-text extraction should specifically look for:

- **Protein sequence databases:** UniProt/Swiss-Prot, UniProtKB/TrEMBL, Pfam, InterPro, or related resources.
- **Functional labels:** Gene Ontology molecular-function, biological-process, and cellular-component terms; enzyme commission numbers; protein families; catalytic residues; ligand- or metal-binding annotations.
- **Structural data:** PDB structures, AlphaFold-predicted structures, contact maps, residue graphs, and confidence-filtered predicted models.
- **Interaction data:** experimentally supported protein–protein interaction databases and functional association networks.
- **Benchmark datasets:** CAFA-style benchmarks, held-out proteins, temporal splits, or homology-reduced test sets.
- **Experimental activity datasets:** biochemical assays, binding measurements, mutational scans, or curated enzyme-function datasets.

The key issue is that protein-function labels are often incomplete, hierarchical, noisy, and unevenly distributed across organisms and protein families. A model can therefore appear accurate by learning annotation frequency, family similarity, or database-specific biases rather than generalizable biological function.

## Evaluation metrics

No exact metrics can be attributed confidently to the records from the metadata alone. For full-text verification, the review should distinguish:

- **Multilabel function prediction:** precision, recall, F1 score, AUROC, AUPRC, and maximum F-measure across thresholds;
- **Ranking quality:** precision@k, recall@k, mean average precision, or normalized discounted cumulative gain;
- **Residue-level prediction:** per-residue precision, recall, F1, MCC, and overlap or localization measures;
- **Calibration:** reliability, calibration error, and confidence stratification;
- **Structure-assisted prediction:** performance stratified by structural confidence and sequence homology;
- **Generalization:** performance on remote-homology, organism-held-out, temporal, or experimentally validated test sets.

Accuracy alone is generally inadequate for multilabel and highly imbalanced protein-function problems.

## Persistent limitations

The most important limitations to investigate across the full texts are:

1. **Annotation incompleteness and noise:** absence of an annotation does not necessarily mean absence of function.
2. **Homology and data leakage:** random sequence-level splitting can place near-identical proteins in both training and test sets, inflating performance.
3. **Class imbalance and long-tailed functions:** common Gene Ontology terms are easier to predict than rare or specific functions.
4. **Limited experimental validation:** computational predictions may not be tested using biochemical or cellular assays.
5. **Poor performance on novel proteins:** models often generalize less reliably to remote homologues, disordered proteins, unusual organisms, or proteins with multiple functions.
6. **Dependence on input quality:** predicted structures, interaction networks, and database annotations carry their own uncertainty and biases.
7. **Interpretability limits:** feature attribution or attention patterns do not by themselves demonstrate a causal mechanism.
8. **Benchmark inconsistency:** different ontologies, filtering rules, splits, thresholds, and evaluation metrics make comparisons difficult.
9. **Function is context-dependent:** activity can depend on cellular location, cofactors, partners, post-translational modifications, expression state, and environmental conditions.
10. **Reproducibility:** inaccessible training data, changing databases, undocumented preprocessing, and inadequate external validation can limit independent replication.

## Overall assessment

The strongest directly relevant record is the study on **structure-based protein-function prediction with graph convolutional networks**, supported by the reviews on **metalloprotein machine learning** and **modern protein machine learning**. The other protein-AI records mainly provide enabling technologies—structure prediction, interaction modelling, protein language models, or sequence design—rather than direct evidence of functional annotation performance.

A defensible final synthesis should therefore avoid claiming specific datasets, metrics, or performance values until the high-priority full texts have been checked. The records most in need of verification are:

1. Gligorijević et al. (2021), structure-based function prediction;
2. Yu et al. (2022), metalloprotein machine learning;
3. Bordin et al. (2023), modern protein machine learning;
4. Gao et al. (2023), graph learning for protein–protein interaction;
5. Tran et al. (2026), protein language models and directed evolution;
6. Zhang et al. (2025), sequence-based transformer screening;
7. AlphaFold Database review and AlphaFold/AlphaFold 3 papers, if predicted structures are discussed as function-prediction inputs;
8. Kapoor and Narayanan (2023), for leakage and reproducibility limitations.