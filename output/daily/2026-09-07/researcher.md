## Relevance-ranked evidence table

**Assessment basis:** bibliographic metadata and titles supplied by the user. Findings, datasets, metrics, and limitations are **not assumed unless visible from the record**. Full-text verification is therefore required for detailed evidence extraction.

| Rank | Record | Relevance to protein-function prediction | Methods or role indicated by the record | Dataset / evaluation evidence available from record | Full-text verification |
|---:|---|---|---|---|---|
| **1** | **Structure-based protein function prediction using graph convolutional networks** (Gligorijević et al., 2021; DOI: 10.1038/s41467-021-23303-9) | **Direct, primary evidence** | Graph convolutional networks using protein structural information to predict function | Dataset identity, function ontology, train/test splitting, class imbalance handling, and metrics are not given in the record | **Highest priority. Local PDF available.** |
| **2** | **Machine Learning Approaches for Metalloproteins** (Yu et al., 2022; PMID: 35209064) | **Direct or near-direct review evidence** | Machine learning applied to metalloproteins; likely relevant to functional or biochemical property prediction, but scope cannot be confirmed from title alone | No datasets or metrics identifiable from metadata | **High priority.** PubMed record only; obtain full text. |
| **3** | **A guide to machine learning for biologists** (Greener et al., 2021; DOI: 10.1038/s41580-021-00407-0) | **High methodological relevance** | General guidance on supervised/unsupervised learning, model development, validation, and interpretation in biology | Likely useful for evaluation and workflow principles, but protein-function-specific datasets/metrics are not established from the record | **High priority for methodological context. Local PDF available.** |
| **4** | **Hierarchical graph learning for protein-protein interaction** (Gao et al., 2023; PMID: 36841846) | **Strong adjacent evidence** | Hierarchical graph learning for predicting protein–protein interactions, a functional relationship between proteins | Dataset construction, negative examples, protein-similarity leakage, and metrics are unknown | **High priority**, especially if “function” includes interaction-based annotation. |
| **5** | **Machine Learning Methods in Protein-Protein Docking** (Michalik & Kuder, 2024; PMID: 38987466) | **Strong adjacent review evidence** | ML methods for structural docking and interaction modeling; relevant to inferring molecular function through binding partners | No specific datasets or metrics available from metadata | **High priority** for interaction/function boundaries. |
| **6** | **AI-Driven Deep Learning Techniques in Protein Structure Prediction** (Chen et al., 2024; PMID: 39125995) | **Indirect but important supporting evidence** | Deep learning for protein structure prediction; structures can provide inputs for downstream function prediction | No datasets or metrics available from metadata | **Medium–high priority.** Verify whether function prediction is discussed or only structure prediction. |
| **7** | **AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges** (Schauperl & Denny, 2022; PMID: 35727311) | **Indirect supporting review** | AI-based structural prediction and its use in drug discovery | No dataset or metric information available from record | **Medium priority** for limitations, but not a core function-prediction source. |
| **8** | **Highly accurate protein structure prediction with AlphaFold** (Jumper et al., 2021; DOI: 10.1038/s41586-021-03819-2) | **Important enabling evidence, not direct function prediction** | Deep-learning protein structure prediction; structural representations may support function annotation | The record does not provide function-prediction datasets or metrics | **Medium priority. Local PDF available.** Use only for structural-model context. |
| **9** | **AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences** (Varadi et al., 2023; DOI: 10.1093/nar/gkad1011) | **Supporting dataset/resource evidence** | Large-scale predicted structural resource that may be used as input for structure-based function prediction | The title identifies scale—over 214 million sequences—but not a function-prediction benchmark or evaluation metric | **Medium priority.** Full text needed to establish coverage, confidence filtering, and appropriate use. |
| **10** | **Sequence-based virtual screening using transformers** (Zhang et al., 2025; PMID: 40721411) | **Adjacent sequence-model evidence** | Transformer models applied to protein sequences for virtual screening; may predict ligand-related properties rather than general protein function | Dataset type, labels, split strategy, and metrics unknown | **Medium priority**, only if ligand binding or biochemical activity is included in the review scope. |
| **11** | **Rapid directed evolution guided by protein language models and epistatic interactions** (Tran et al., 2026; PMID: 41712694) | **Adjacent protein-property prediction evidence** | Protein language models and epistatic modeling used to guide variant selection/evolution | The record does not establish that canonical protein functions were predicted; datasets and metrics unavailable | **Medium priority** if the review includes activity or variant-effect prediction. |
| **12** | **Robust deep learning–based protein sequence design using ProteinMPNN** (Dauparas et al., 2022; DOI: 10.1126/science.add2187) | **Adjacent, mainly protein design** | Deep learning for sequence design rather than direct functional annotation | No function-prediction datasets or metrics identifiable from metadata | **Lower priority.** Verify only if sequence design/function coupling is in scope. |
| **13** | **Accurate structure prediction of biomolecular interactions with AlphaFold 3** (Abramson et al., 2024; DOI: 10.1038/s41586-024-07487-w) | **Adjacent structural/interaction evidence** | Prediction of biomolecular interaction structures; potentially relevant to binding-function inference | No function-prediction datasets or metrics available from metadata | **Lower–medium priority.** Full text needed to determine relevance to functional annotation. |
| **14** | **The rise of deep learning and transformations in bioactivity prediction power of molecular modeling tools** (Bule et al., 2021; PMID: 34532977) | **Adjacent review evidence** | Deep learning for bioactivity prediction, which overlaps with prediction of protein–ligand activity but not necessarily protein function annotation | No specific dataset or metric information in record | **Medium priority** if bioactivity is included. |
| **15** | **Leakage and the reproducibility crisis in machine-learning-based science** (Kapoor & Narayanan, 2023; DOI: 10.1016/j.patter.2023.100804) | **Important cross-cutting limitations evidence** | Addresses data leakage and reproducibility in ML research | Protein-specific datasets/metrics not indicated | **High priority for limitations.** Full text required; PDF access was blocked in the supplied record. |
| **16** | **Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development** (Ponce Bobadilla et al., 2024; DOI: 10.1111/cts.70056) | **Methodological support** | Model explainability and feature attribution using SHAP | No protein-function datasets or metrics indicated | **Medium priority** if interpretability is a review objective; supplied PDF access failed. |
| **17** | **Informed Machine Learning—A Taxonomy and Survey of Integrating Prior Knowledge into Learning Systems** (von Rueden et al., 2021; DOI: 10.1109/TKDE.2021.3079836) | **General methodological support** | Incorporating prior knowledge into ML, potentially relevant to biological constraints and ontologies | No protein-specific evidence visible from metadata | **Lower priority**, unless discussing knowledge-guided protein-function prediction. |
| **18** | **Ensemble deep learning: A review** (Ganaie et al., 2022; DOI: 10.1016/j.engappai.2022.105151) | **General methodological support** | Ensemble deep-learning methods | No protein-specific datasets or metrics in record | **Low priority.** |
| **19** | **Review of deep learning: concepts, CNN architectures, challenges, applications, future directions** (Alzubaidi et al., 2021; DOI: 10.1186/s40537-021-00444-8) | **General background** | Deep-learning architectures and challenges | No protein-function-specific evidence from metadata | **Low priority. Local PDF available.** |

## Records likely outside the review scope

These records concern clinical prediction, cancer biomarkers, drug efficacy, molecular drug discovery, or unrelated applications rather than predicting the function of proteins:

- *Machine learning-based reproducible prediction of type 2 diabetes subtypes*
- *AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution*
- *A Risk-Tiered Validation Framework for Artificial Intelligence in Drug Discovery*
- *Dynamic Prediction of Non-Neutral SARS-CoV-2 Variants Using Incremental Machine Learning*
- *LCN2 drives ferroptosis-associated ischemia-reperfusion injury...*
- *Discovery of natural RORγt inhibitor using machine learning...*
- *Deciphering the mechanism of baicalein in cervical cancer...*
- *Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF...*
- *Combining Molecular Dynamics and Machine Learning to Predict Drug Resistance Causing Variants of BRAF...*
- *Artificial intelligence guided discovery of a barrier-protective therapy...*
- *Machine learning driven prediction of drug efficacy in lung cancer...*
- *Virtual patient analysis identifies strategies to improve... PD-1 blockade*
- *Swarm Learning for decentralized and confidential clinical machine learning*
- *Using machine learning approaches for multi-omics data analysis: A review*
- *Machine Learning in Agriculture*
- *Generative AI*
- *Small data machine learning in materials science*
- *The Role of AI, Machine Learning, and Big Data in Digital Twinning*
- *Prediction of Chronic Kidney Disease*
- *A review on extreme learning machine*

Some excluded records may still provide generic information about validation, explainability, or small-data problems, but they should not be treated as evidence about protein-function prediction itself.

## Evidence currently supported by the records

### How ML methods are being used

The records indicate several broad approaches, but only one record is explicitly titled as protein-function prediction:

1. **Structure-based prediction:**  
   Graph convolutional networks are explicitly used for protein-function prediction in Gligorijević et al. Structural prediction systems such as AlphaFold are relevant as enabling resources, but structure prediction should not be conflated with function prediction.

2. **Sequence-based modeling:**  
   Transformers and protein language models are represented by the sequence-based virtual-screening and directed-evolution records. Their exact targets—function labels, binding, activity, or variant effects—must be verified in full text.

3. **Interaction-based inference:**  
   Graph learning for protein–protein interaction and ML for protein docking may support functional inference through predicted interaction relationships.

4. **Domain- or chemistry-specific prediction:**  
   The metalloprotein review may cover prediction of metal-binding, catalytic, structural, or other metalloprotein properties, but the precise task needs verification.

5. **Interpretability and validation:**  
   SHAP, informed ML, and the leakage/reproducibility paper are relevant to explaining predictions and assessing whether reported performance is reliable.

### Datasets and evaluation metrics

**The supplied bibliographic records do not provide enough information to identify the datasets or metrics used.** Full-text extraction should specifically look for:

- Protein sequence databases and annotation sources, such as UniProt, Gene Ontology, Pfam, PDB, or specialized metalloprotein/interaction databases.
- Structural sources, including experimentally determined structures versus predicted structures.
- Protein–protein interaction databases and definitions of positive and negative interactions.
- Dataset size, label hierarchy, class imbalance, and annotation quality.
- Random versus sequence-, structure-, family-, or species-level splits.
- Independent or temporal test sets.
- Leakage controls, particularly homologous proteins appearing across training and test sets.
- Metrics such as accuracy, precision, recall, F1 score, ROC-AUC, PR-AUC, Matthews correlation coefficient, top-\(k\) accuracy, coverage, calibration, and ontology-aware measures such as semantic similarity.

### Limitations suggested by the evidence set

These should be treated as **issues to verify**, not established findings from the supplied metadata:

- **Data leakage and inflated performance**, directly flagged by the Kapoor and Narayanan record.
- **Dependence on structural-model quality**, relevant when predicted structures are used for function inference.
- **Limited or biased functional annotations**, likely important for protein-function benchmarks but not documented in the supplied records.
- **Class imbalance and incomplete negative examples**, especially for interaction and functional-label prediction.
- **Homology and distribution-shift problems**, where near-identical proteins occur across training and test sets or where models are applied to novel protein families.
- **Interpretability and biological validation**, motivating the SHAP and informed-ML records.
- **Reproducibility**, including unclear preprocessing, unavailable code or datasets, and inconsistent benchmark splits.

## Priority full-text verification set

For answering the stated question efficiently, verify these first:

1. Gligorijević et al. — direct structure-based function prediction.
2. Yu et al. — ML for metalloproteins.
3. Gao et al. — graph learning for protein–protein interactions.
4. Michalik & Kuder — ML for protein–protein docking.
5. Greener et al. — ML methodology for biologists.
6. Kapoor & Narayanan — leakage and reproducibility.
7. Chen et al. — deep learning for protein structures.
8. Jumper et al. and Varadi et al. — structural inputs and database coverage.
9. Zhang et al. and Tran et al. — sequence transformers and protein language models, if activity or variant-function prediction is included.

**Bottom line:** the strongest directly relevant record is the graph-convolutional-network study on structure-based protein-function prediction. The remaining useful records mainly address enabling representations—sequences, structures, and interactions—or methodological concerns. The supplied metadata are insufficient to report specific benchmark datasets, numerical performance, or validated limitations; those require full-text verification.