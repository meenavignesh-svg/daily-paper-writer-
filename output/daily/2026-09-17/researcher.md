## Relevance-ranked evidence overview

### Overall assessment

The supplied records contain only a small number of papers directly focused on **machine-learning prediction of protein function**. The strongest direct evidence is:

1. **Structure-based protein function prediction using graph convolutional networks** (Gligorijević et al., 2021).
2. **Machine Learning Approaches for Metalloproteins** (Yu et al., 2022).
3. **Novel machine learning approaches revolutionize protein knowledge** (Bordin et al., 2023), a broad review likely covering sequence, structure, language-model and annotation-based approaches.

Several other records are highly relevant to the technical infrastructure of protein-function prediction—particularly protein structure prediction, protein–protein interaction modelling, protein language models and protein databases—but they do not necessarily predict molecular function directly. Most claims about datasets, splits and evaluation metrics require full-text verification because these details are not available from the bibliographic metadata.

---

## 1. Directly relevant records

| Rank | Record | Contribution to the question | Verification status |
|---|---|---|---|
| **1** | **Structure-based protein function prediction using graph convolutional networks** (Gligorijević et al., 2021; DOI: 10.1038/s41467-021-23303-9) | The most directly relevant record. It concerns the use of **graph convolutional networks** to infer protein function from structural representations. It is likely to address how residues, structural contacts or protein surfaces are represented and how these representations are linked to functional annotations. | **Full-text verification essential.** A local PDF is listed, so the methods, datasets and metrics should be extractable. |
| **2** | **Machine Learning Approaches for Metalloproteins** (Yu et al., 2022; PMID: 35209064) | Directly relevant to function prediction in a biologically important protein class. It likely reviews prediction of metalloprotein properties such as metal-binding sites, metal-ion identity, catalytic activity or related functional classes. | **Full-text verification essential.** The record is a review; its scope should be checked to distinguish function prediction from structure, ligand-binding or property prediction. |
| **3** | **Novel machine learning approaches revolutionize protein knowledge** (Bordin et al., 2023; PMID: 36504138) | Broad review of machine learning in protein science. It is likely to cover protein language models, sequence representations, structure prediction, annotation and possibly function prediction. It should provide useful context on how large pretrained models are used for protein classification and annotation. | **Full-text verification essential.** The title is broad, so the extent of coverage of functional prediction is uncertain. |
| **4** | **AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences** (Váradi et al., 2023; DOI: 10.1093/nar/gkad1011) | Relevant as a source of predicted structural features that can be used in downstream function-prediction models. It is a database/resource paper rather than a direct evaluation of a function-prediction model. | **Full-text verification needed.** The supplied PDF was inaccessible, although the resource description is clear from the title. |
| **5** | **Sequence-based virtual screening using transformers** (Zhang et al., 2025; PMID: 40721411) | Relevant to transformer-based protein sequence representations and prediction of sequence–ligand or sequence–function relationships. However, virtual screening is not equivalent to general protein-function annotation. | **Full-text verification essential** to establish the prediction target, labels, datasets and evaluation metrics. |
| **6** | **Hierarchical graph learning for protein-protein interaction** (Gao et al., 2023; PMID: 36841846) | Relevant to prediction of a specific aspect of protein function—whether proteins interact—using hierarchical graph-learning methods. It should be treated as interaction prediction rather than broad Gene Ontology or enzymatic-function prediction. | **Full-text verification needed.** The record does not reveal whether the model uses sequence, structure, interaction networks or multimodal inputs. |

### Likely methodological themes from these records

The directly relevant literature appears to involve several complementary modelling strategies:

- **Sequence-based models:** amino-acid sequences are encoded using conventional features, recurrent or convolutional models, or transformer/protein-language-model embeddings.
- **Structure-based models:** protein structures are represented as graphs, with residues or atoms as nodes and spatial proximity or chemical contacts as edges.
- **Interaction-network models:** known protein–protein interaction networks can be treated as graphs to infer interaction partners or functional associations.
- **Specialised classifiers:** models may predict metal-binding, catalytic or ligand-binding properties for particular protein families.
- **Hybrid approaches:** sequence, structure, evolutionary information and network context may be combined.

The precise architectures, training procedures and prediction targets should not be inferred from the titles alone.

---

## 2. Important supporting records

These papers are not necessarily direct studies of protein-function prediction, but they provide methods, representations or resources commonly used by function-prediction systems.

### Protein structure prediction and structural representations

- **Highly accurate protein structure prediction with AlphaFold** (Jumper et al., 2021; DOI: 10.1038/s41586-021-03819-2)  
  Provides a major source of predicted structures for downstream structural annotation. Its principal task is structure prediction, not direct functional prediction.

- **Accurate structure prediction of biomolecular interactions with AlphaFold 3** (Abramson et al., 2024; DOI: 10.1038/s41586-024-07487-w)  
  Relevant to modelling protein–protein, protein–nucleic-acid and protein–ligand interactions. It may support functional inference, but the primary task is interaction-structure prediction.

- **AI-Driven Deep Learning Techniques in Protein Structure Prediction** (Chen et al., 2024; PMID: 39125995)  
  A review of deep learning for structure prediction. Useful for understanding structural inputs to function-prediction pipelines, but not direct evidence about functional annotation.

- **AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges** (Schauperl and Denny, 2022; PMID: 35727311)  
  Contextual evidence concerning the use and limitations of predicted structures. It should not be treated as a study of protein-function prediction unless the full text demonstrates otherwise.

- **Machine Learning Methods in Protein-Protein Docking** (Michalik and Kuder, 2024; PMID: 38987466)  
  Relevant to interaction modelling and structural hypotheses about function, but docking performance is distinct from function-prediction performance.

### Protein language models and protein design

- **Rapid directed evolution guided by protein language models and epistatic interactions** (Tran et al., 2026; PMID: 41712694)  
  Shows a use of protein language models for guiding sequence optimisation and directed evolution. This is related to predicting sequence effects or fitness, not necessarily annotating natural protein function.

- **Robust deep learning–based protein sequence design using ProteinMPNN** (Dauparas et al., 2022; DOI: 10.1126/science.add2187)  
  Primarily a protein-design paper. It may inform sequence representations and generative modelling but does not directly answer how existing proteins are assigned functions.

- **Computational modelling of olfactory receptors** (Odoemelam et al., 2025; PMID: 40441539)  
  Potentially relevant to predicting receptor structure, ligand interactions or receptor activity. The specific prediction task must be confirmed.

- **Machine learning and classical MD simulation to identify inhibitors against the P37 envelope protein of monkeypox virus** (Rout et al., 2024; PMID: 37221882)  
  Concerns inhibitor discovery against a particular protein rather than prediction of protein function.

- **Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction** (Passaro et al., 2025; DOI: 10.1101/2025.06.14.659707)  
  Relevant to binding-affinity prediction and structural modelling, but not broad protein-function prediction.

---

## 3. Methodological and reporting guidance

These records are useful for interpreting model development and assessing limitations, but they are not protein-function studies themselves.

- **A guide to machine learning for biologists** (Greener et al., 2021)  
  General guidance on model construction, validation, feature representation and interpretation. Relevant to evaluating protein-prediction studies.

- **Leakage and the reproducibility crisis in machine-learning-based science** (Kapoor and Narayanan, 2023)  
  Particularly important for protein-function prediction, where highly similar sequences can occur across training and test sets. It supports scrutiny of homology-aware data splitting, duplicate removal and external validation.

- **Practical guide to SHAP analysis** (Ponce Bobadilla et al., 2024)  
  Relevant to interpretability, although it is focused on drug-development models rather than protein-function prediction.

- **Informed Machine Learning – A Taxonomy and Survey of Integrating Prior Knowledge into Learning Systems** (von Rueden et al., 2021)  
  Relevant to incorporating biochemical constraints, structural knowledge, evolutionary information or interaction networks into predictive models.

- **Review of deep learning: concepts, CNN architectures, challenges, applications, future directions** (Alzubaidi et al., 2021)  
  General deep-learning background; only indirectly relevant.

- **Ensemble deep learning: A review** (Ganaie et al., 2022) and **A review on extreme learning machine** (Wang et al., 2021)  
  General methodological context with limited protein-specific relevance.

- **Small data machine learning in materials science** (Xu et al., 2023)  
  Indirectly relevant to the small-data problem in experimentally characterised proteins, but not protein-specific evidence.

---

## 4. Records that are largely outside the question

The following records apply machine learning to clinical outcomes, cancer biology, drug response or other biomedical tasks. They may use protein or omics measurements as predictors, but they do not primarily predict protein molecular function:

- **Machine learning-based reproducible prediction of type 2 diabetes subtypes** (Tanabe et al., 2024).
- **AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution** (Schade et al., 2024).
- **LCN2 drives ferroptosis-associated ischemia-reperfusion injury after renal transplantation** (Wu et al., 2025).
- **Discovery of natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation** (Yoo et al., 2026).
- **Deciphering the mechanism of baicalein in cervical cancer via bioinformatics, machine learning and computational simulations** (Wang et al., 2025).
- **Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF Using Olink-Derived Inflammatory Protein Signatures** (Zhang et al., 2025).
- **Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease** (Sahoo et al., 2021).
- **Machine learning driven prediction of drug efficacy in lung cancer** (Li et al., 2025).
- **Multi-Omics Integration With Machine Learning Identified Early Diabetic Retinopathy...** (Pang et al., 2024).
- **Machine Learning-Based Predictive Modeling Maximizes the Efficacy of mTOR/p53 Co-Targeting Therapy Against AML** (Li et al., 2025).
- **Using machine learning approaches for multi-omics data analysis: A review** (Reel et al., 2021).
- **Swarm Learning for decentralized and confidential clinical machine learning** (Warnat-Herresthal et al., 2021).
- **Prediction of Chronic Kidney Disease - A Machine Learning Perspective** (Chittora et al., 2021).

Other records are general AI reviews or concern agriculture, digital twins or generative AI and provide little direct evidence for the present question.

---

## Datasets and labels

The supplied metadata do not specify the datasets used by the direct protein-function papers. Full-text verification should extract the following information:

1. **Sequence databases**
   - UniProtKB/Swiss-Prot or TrEMBL
   - Pfam, InterPro or other domain databases
   - Experimentally annotated protein families

2. **Functional labels**
   - Gene Ontology biological-process, molecular-function and cellular-component terms
   - Enzyme Commission classes
   - Protein family or domain labels
   - Metal-binding, catalytic-site or ligand-binding annotations
   - Protein–protein interaction labels

3. **Structural datasets**
   - Experimentally determined structures from the Protein Data Bank
   - Predicted structures from AlphaFold or related resources
   - Structural graphs based on residue contacts, distances, surfaces or geometric features

4. **Interaction datasets**
   - Curated protein–protein interaction databases
   - Positive and negative interaction pairs
   - Organism-specific interaction networks

5. **Data-splitting strategy**
   - Random protein-level split
   - Sequence-identity or homology-cluster split
   - Family-level or superfamily-level split
   - Temporal or external validation split

The splitting strategy is especially important. Random splits can substantially overestimate generalisation when homologous proteins occur in both training and test sets.

---

## Evaluation metrics

The supplied records do not provide enough information to state which metrics were actually used in each study. The full texts should be checked for the following, depending on the task:

- **Multilabel function annotation:** precision, recall, F1 score, area under the precision–recall curve, area under the ROC curve and maximum F-measure.
- **Hierarchical Gene Ontology prediction:** ontology-aware precision and recall, semantic similarity and metrics that account for parent–child relationships.
- **Protein-family or functional-class classification:** accuracy, balanced accuracy, macro-F1, Matthews correlation coefficient and per-class precision/recall.
- **Interaction prediction:** AUROC, AUPR, F1 score, precision at a specified ranking threshold and calibration.
- **Residue-level site prediction:** residue-level precision, recall, F1, MCC, intersection-over-union and distance-based localisation accuracy.
- **Structure-dependent downstream prediction:** performance should be separated according to whether the input structure is experimental or predicted, since structural uncertainty can affect functional inference.

Metrics such as **TM-score, RMSD or lDDT** are appropriate for evaluating structure prediction, not for directly evaluating protein-function prediction. They should not be substituted for functional metrics.

---

## Remaining limitations

The records collectively point to several important limitations, although the protein-specific papers must be read to determine which limitations they explicitly report:

1. **Annotation incompleteness and noise**  
   Protein-function labels are incomplete, unevenly distributed across taxa and sometimes inferred computationally rather than experimentally.

2. **Homology and data leakage**  
   Similar sequences or protein families across training and test sets can inflate performance. Homology-aware splitting and independent evaluation are essential.

3. **Class imbalance and long-tailed functions**  
   Common functions have many examples, whereas rare functions may have very few labelled proteins. Aggregate accuracy can therefore be misleading.

4. **Limited experimental ground truth**  
   Many predictions are evaluated against existing annotations rather than new experimental measurements.

5. **Poor transfer to distant proteins**  
   Models may perform well on proteins related to the training data but poorly on remote homologues, novel folds, unusual organisms or proteins with multifunctionality.

6. **Dependence on structural quality**  
   Structure-based methods may be affected by incorrect folds, disordered regions, missing cofactors, ligand-state differences and uncertainty in predicted structures.

7. **Multifunctionality and context dependence**  
   Protein function can depend on cellular compartment, expression state, post-translational modification, oligomeric state, binding partners and environmental conditions. A single sequence or structure may not determine one fixed function.

8. **Interpretability and causal validity**  
   Saliency maps, attention weights or feature-attribution methods may identify correlated regions without demonstrating that those regions cause the function.

9. **Reproducibility and benchmarking**  
   Differences in database versions, label propagation, negative-example construction and preprocessing can make results difficult to compare.

10. **Validation beyond benchmark scores**  
    Strong computational performance does not establish biological usefulness without prospective experimental validation.

---

## Records requiring priority full-text verification

### Highest priority

1. **Gligorijević et al. (2021), Structure-based protein function prediction using graph convolutional networks**  
   Verify architecture, structural representation, functional ontology, dataset construction, homology split and metrics.

2. **Yu et al. (2022), Machine Learning Approaches for Metalloproteins**  
   Verify which metalloprotein functions are covered and whether the evidence concerns prediction, classification, site identification or screening.

3. **Bordin et al. (2023), Novel machine learning approaches revolutionize protein knowledge**  
   Verify the review’s coverage of protein language models, functional annotation and evaluation practices.

### High priority supporting verification

4. **Váradi et al. (2023), AlphaFold Protein Structure Database in 2024**  
   Verify how the database is intended to support downstream functional analysis and how confidence measures should be interpreted.

5. **Gao et al. (2023), Hierarchical graph learning for protein-protein interaction**  
   Verify its relevance to functional inference and the treatment of positive and negative interactions.

6. **Zhang et al. (2025), Sequence-based virtual screening using transformers**  
   Verify whether the predicted output is binding, activity, function or another sequence-associated property.

7. **Tran et al. (2026), Rapid directed evolution guided by protein language models and epistatic interactions**  
   Verify whether the model predicts functional fitness, mutational effects or only guides experimental optimisation.

8. **Jumper et al. (2021) and Abramson et al. (2024), AlphaFold papers**  
   Use primarily to document structural inputs and their limitations, not as direct evidence of function-prediction performance.

### Lower priority or not needed for the main synthesis

The clinical prediction, cancer, drug-response, general AI, agriculture and unrelated biomedical records do not need detailed full-text review unless the scope is expanded to include machine learning using protein measurements as clinical predictors.

## Bottom line

The evidence supports a framework in which protein function is predicted from **sequence embeddings, structural graphs, interaction networks and specialised biochemical features**. However, the supplied records do not yet provide verifiable details about the exact datasets, label definitions, data splits or metrics. The Gligorijević, Yu and Bordin papers should therefore anchor the review, with AlphaFold and protein-language-model papers treated as enabling or adjacent technologies. Full-text extraction is necessary before making comparative claims about model performance or deciding which approaches generalise best to uncharacterised proteins.