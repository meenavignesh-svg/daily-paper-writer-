## Relevance-ranked evidence overview

The records contain a small number of papers directly concerned with machine-learning prediction of protein function, alongside many papers on protein structure prediction, molecular interaction prediction, drug discovery, or clinical biomarker modelling. The latter are relevant background but should not be treated as direct evidence for protein-function annotation.

### Tier 1: Directly relevant to protein-function prediction

| Record | Relevance and likely contribution | Dataset and metric information available from the record | Full-text verification |
|---|---|---|---|
| **Kulmanov & Hoehndorf, “Computational prediction of protein functional annotations” (2025)** | Most directly aligned with the question. The title indicates a review of computational methods for assigning functional annotations, presumably including machine learning and ontology-based prediction. | Not available from the citation. The review should be checked for task definitions, benchmark datasets, Gene Ontology (GO) categories, label hierarchies, and evaluation practices. | **Required.** No PDF supplied. |
| **Gligorijević et al., “Structure-based protein function prediction using graph convolutional networks” (2021)** | Direct methodological evidence for using graph convolutional networks (GCNs) to infer protein function from three-dimensional structure. It is likely important for understanding how structural residues, contacts, or surface features are represented for functional prediction. | The citation does not identify the protein set, structural source, functional labels, train/test split, or metrics. These must be extracted from the paper. | **Required, although a local PDF is supplied.** |
| **Bordin et al., “Novel machine learning approaches revolutionize protein knowledge” (2023)** | Broad review of machine learning in protein science. It may provide coverage of protein language models, representation learning, structure prediction, and annotation, and may help place function prediction within the wider protein-knowledge ecosystem. | No dataset or metric information can be established from the title alone. | **Required.** No PDF supplied. |
| **Yu et al., “Machine Learning Approaches for Metalloproteins” (2022)** | Relevant specialist review. It may discuss prediction of metal-binding sites, metalloprotein classes, catalytic functions, or metal-associated properties. This is a narrower form of protein-function prediction. | The record does not specify whether the evidence concerns classification, site prediction, affinity prediction, or functional annotation, nor which datasets and metrics were used. | **Required.** No PDF supplied. |

### Tier 2: Closely related methods or applications

| Record | Relevance |
|---|---|
| **Tran et al., “Rapid directed evolution guided by protein language models and epistatic interactions” (2026)** | Relevant to protein language models and prediction of sequence-function relationships. However, directed evolution generally predicts or optimizes an experimentally measured property rather than assigning a standardized functional annotation. The paper should be checked for the assay labels, training data, validation design, and whether predictions were experimentally tested. **Full text required; no PDF supplied.** |
| **Gao et al., “Hierarchical graph learning for protein-protein interaction” (2023)** | Relevant to graph-based modelling of protein relationships. Interaction prediction can support functional inference, but the title indicates PPI prediction rather than direct function annotation. **Full text required; no PDF supplied.** |
| **Zhang et al., “Sequence-based virtual screening using transformers” (2025)** | Relevant to transformer models applied to protein sequences and ligand-related prediction. It addresses molecular recognition or screening more directly than general protein-function prediction. **Full text required; no PDF supplied.** |
| **Abramson et al., “Accurate structure prediction of biomolecular interactions with AlphaFold 3” (2024)** | Important as structural input for downstream function inference, particularly where function depends on protein–ligand, protein–protein, or protein–nucleic-acid interactions. It is not itself a general protein-function annotation method. **Full text required; no PDF supplied.** |
| **Jumper et al., “Highly accurate protein structure prediction with AlphaFold” (2021)** | Foundational for structure-based functional inference, but the primary task is structure prediction rather than function prediction. Its relevance is indirect: predicted structures can provide features for function-prediction models. **Local PDF supplied, but full-text verification remains necessary.** |
| **Váradi et al., “AlphaFold Protein Structure Database in 2024” (2023)** | Provides an important potential source of predicted structures for large-scale structure-based function prediction. The supplied record states that the database covers more than 214 million sequences, but this figure should still be checked against the full text if used quantitatively. **Full text required; supplied PDF access failed.** |
| **Chen et al., “AI-Driven Deep Learning Techniques in Protein Structure Prediction” (2024)** and **Schauperl & Denny, “AI-Based Protein Structure Prediction in Drug Discovery” (2022)** | Background reviews on structural prediction. They may help explain the origin of structural features, but they do not directly answer how function labels are predicted. **Full texts required.** |
| **Michalik & Kuder, “Machine Learning Methods in Protein-Protein Docking” (2024)** | Relevant to interaction modelling and structural context, but not direct functional annotation. **Full text required.** |
| **Odoemelam et al., “Computational modelling of olfactory receptors” (2025)** | May involve prediction of receptor structure or ligand recognition. It is a domain-specific application rather than general function prediction. **Full text required.** |

## What the evidence suggests about current approaches

Based on the titles, the literature represented here spans several complementary modelling strategies:

1. **Sequence-based models.**  
   Protein sequences can be represented using conventional descriptors, learned embeddings, or protein language models. The directed-evolution and transformer records are particularly relevant to this category. Such models may predict functional classes, biochemical properties, ligand recognition, or experimentally measured activities.

2. **Structure-based models.**  
   The GCN paper is the clearest direct example. Proteins can be represented as graphs in which residues or atoms are nodes and spatial proximity, chemical contacts, or structural relationships are edges. These representations can support prediction of functional labels or sites. Predicted structures from AlphaFold-scale resources may make this approach applicable to proteins lacking experimentally determined structures.

3. **Interaction- and context-based models.**  
   Protein–protein interaction, protein–ligand, and protein–nucleic-acid models can provide indirect evidence about function. However, interaction prediction and function annotation are related but distinct tasks and should be evaluated separately.

4. **Domain-specific prediction.**  
   Metalloprotein modelling illustrates how machine learning can target a restricted functional domain, such as metal binding, catalytic activity, or metalloprotein classification. Such models may perform well within a domain but may not generalize to unrelated protein families.

## Datasets and evaluation metrics

The supplied bibliographic information does **not** provide enough evidence to identify the datasets or metrics used in the direct function-prediction studies. Full-text extraction should specifically record:

- the source of protein sequences and structures;
- functional label systems, especially Gene Ontology terms, enzyme classes, binding-site labels, or experimentally measured activities;
- redundancy-reduction procedures and sequence-similarity thresholds;
- whether test proteins are homologous or remote from training proteins;
- treatment of class imbalance and missing or incomplete annotations;
- temporal or species-based separation of training and test data;
- use of experimentally determined versus predicted structures;
- independent external validation and experimental validation.

Likely metric categories to verify include:

- precision, recall, F1 score, and accuracy for classification;
- area under the ROC or precision–recall curve;
- average precision or ranking metrics for multilabel annotation;
- coverage and semantic similarity for hierarchical Gene Ontology prediction;
- residue- or site-level precision, recall, and overlap measures for functional-site prediction;
- correlation or error measures for continuous activity or affinity prediction.

These should not be attributed to a particular paper until confirmed in the full text. In protein-function prediction, accuracy alone can be misleading because labels are often multilabel, hierarchical, incomplete, and highly imbalanced.

## Remaining limitations

The records support several limitations as important issues for verification, although they do not establish the magnitude of each problem:

- **Annotation incompleteness and noise:** databases contain missing, uncertain, or unevenly curated functional labels.
- **Homology leakage:** random sequence splitting can place highly similar proteins in both training and test sets, producing overly optimistic performance.
- **Limited generalization:** models trained on well-studied protein families may perform poorly on remote homologues, novel folds, unusual organisms, or proteins with few annotations.
- **Structure uncertainty:** predicted structures are valuable but may be unreliable in disordered regions, flexible complexes, alternative conformations, or weakly modelled domains.
- **Class imbalance and label hierarchy:** rare functions are difficult to evaluate, and errors between related ontology terms may not be equivalent to errors between unrelated terms.
- **Interpretability:** learned sequence or structural features may not clearly identify the residues or mechanisms responsible for a prediction.
- **Benchmark-to-experiment gap:** computationally plausible annotations do not necessarily establish biochemical activity; experimental validation remains important.
- **Reproducibility and leakage risks:** the general machine-learning records on leakage and reproducibility are relevant methodological warnings, but they are not protein-specific evidence.

## Overall assessment

The strongest direct evidence in this collection comprises the 2021 GCN study, the 2022 metalloprotein review, the 2023 protein-knowledge review, and the 2025 review of computational functional annotation. Together, they indicate that machine learning is being used primarily to learn relationships between protein sequence, structure, interaction context, and functional labels or biochemical properties. However, the supplied metadata contain almost no verifiable information about the actual datasets, train/test designs, or evaluation metrics. Those details require full-text review, particularly for the GCN study and the 2025 functional-annotation review.