## Relevance-ranked evidence overview

### Scope and evidentiary caution

The records include a mixture of direct studies of protein-function prediction, reviews, methods for related protein tasks, and papers in which machine learning is applied to clinical or drug-discovery questions. The bibliographic information alone is insufficient to establish the exact datasets, train/test procedures, or evaluation metrics used. The points below therefore distinguish what can be inferred from the titles and metadata from what requires full-text verification.

---

## Tier 1: Directly relevant to protein-function prediction

### 1. Structure-based protein function prediction using graph convolutional networks  
**Gligorijević et al., 2021** — DOI: 10.1038/s41467-021-23303-9

This is the most directly relevant empirical record. It explicitly describes the use of graph convolutional networks to predict protein function from structural information. The likely methodological contribution is the representation of proteins or structural neighbourhoods as graphs, followed by graph-based learning to assign functional annotations. However, the supplied record does not establish:

- which structural source was used;
- whether structures were experimental, predicted, or both;
- which functional ontology or annotation system was predicted;
- how homologous proteins were separated between training and test sets;
- which baselines were used; or
- which evaluation metrics were reported.

**Full-text verification: essential.** The record has an accessible article/PDF link, but the specific claims above must be checked in the paper.

### 2. Computational prediction of protein functional annotations  
**Kulmanov and Hoehndorf, 2025** — PMID: 40728605

This appears to be a recent review or overview focused specifically on computational protein-function annotation. It is potentially the most useful source for organising the field, including sequence-based, structure-based, ontology-aware, and possibly interaction-based approaches. It should help identify:

- major annotation datasets and databases;
- machine-learning model classes;
- benchmarking practices;
- the role of Gene Ontology and related ontologies; and
- limitations such as incomplete annotations, annotation bias, and poor generalisation to remote homologues.

These details cannot be confirmed from the title and metadata alone.

**Full-text verification: essential.**

### 3. Novel machine learning approaches revolutionize protein knowledge  
**Bordin et al., 2023** — PMID: 36504138

This record is likely a broad review of modern machine-learning approaches for protein sequence and structural analysis. It may provide important context on protein language models, representation learning, and large-scale protein databases. Its relevance is probably substantial, although the title is broader than function prediction.

**Full-text verification: required** to determine how much of the paper concerns functional annotation rather than structure, design, or other protein applications.

### 4. Machine Learning Approaches for Metalloproteins  
**Yu et al., 2022** — PMID: 35209064

This review is relevant to function prediction in a specialised protein class. Metalloprotein function can involve metal-binding sites, coordination geometry, catalytic residues, and sequence or structural signatures. The paper may illustrate how machine learning is used for classification or prediction of metalloprotein properties and functions.

Its relevance is narrower than the general protein-function records, and the title does not indicate whether the review evaluates predictive models systematically.

**Full-text verification: required**, especially for datasets, task definitions, and performance metrics.

---

## Tier 2: Relevant methods or closely related protein-prediction tasks

### 5. Sequence-based virtual screening using transformers  
**Zhang et al., 2025** — PMID: 40721411

This paper is relevant to transformer-based protein-sequence modelling, but virtual screening is not equivalent to predicting biological protein function. It may nevertheless provide evidence about sequence representations, pretrained protein language models, and evaluation of sequence-based predictions.

**Full-text verification: required** before using it as evidence for functional annotation.

### 6. Hierarchical graph learning for protein-protein interaction  
**Gao et al., 2023** — PMID: 36841846

Protein–protein interaction prediction is a related functional task because interaction partners can provide evidence about biological roles. However, interaction prediction should not be treated as direct prediction of Gene Ontology or biochemical function unless the paper explicitly performs that task.

**Full-text verification: required.**

### 7. Machine Learning Methods in Protein-Protein Docking  
**Michalik and Kuder, 2024** — PMID: 38987466

This review concerns docking and structural interaction modelling. It may be useful for the structural context of protein function, particularly molecular recognition and interaction interfaces, but docking performance is not a direct measure of protein-function prediction.

**Full-text verification: required**, and likely secondary relevance only.

### 8. AI-Driven Deep Learning Techniques in Protein Structure Prediction  
**Chen et al., 2024** — PMID: 39125995

This is relevant to the structural foundation of function prediction, but structure prediction and function prediction are distinct problems. Predicted structures may subsequently be used as inputs to function-prediction systems, but the title does not show that this paper evaluates functional annotation.

**Full-text verification: required.**

### 9. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges  
**Schauperl and Denny, 2022** — PMID: 35727311

This is primarily about structure prediction and its use in drug discovery. It is useful background for understanding how predicted structures may support functional inference, but it is not direct evidence about protein-function prediction.

**Full-text verification: required if cited for limitations of structure-derived function prediction.**

### 10. Highly accurate protein structure prediction with AlphaFold  
**Jumper et al., 2021** — DOI: 10.1038/s41586-021-03819-2

AlphaFold is foundational for structure-based biological inference, but this paper is not, on the basis of its title, a protein-function prediction study. It may be cited to explain the availability of predicted structural features, not as evidence that AlphaFold directly predicts protein function.

### 11. AlphaFold Protein Structure Database in 2024  
**Varadi et al., 2023** — DOI: 10.1093/nar/gkad1011

This record is relevant to data availability. The title indicates structure coverage for more than 214 million protein sequences, suggesting a major resource for structure-based function-prediction research. It does not itself establish the quality, annotation completeness, or suitability of those structures for supervised function prediction.

The figure of “over 214 million protein sequences” comes from the title and should be retained only as a description of database coverage, not as evidence of functional annotation quality.

**Full-text verification: recommended**, particularly for coverage, confidence measures, and database composition.

### 12. Accurate structure prediction of biomolecular interactions with AlphaFold 3  
**Abramson et al., 2024** — DOI: 10.1038/s41586-024-07487-w

This is relevant to interaction- and structure-informed functional inference, but it predicts biomolecular structures and interactions rather than protein function directly.

**Full-text verification: required for any stronger claim.**

### 13. Rapid directed evolution guided by protein language models and epistatic interactions  
**Tran et al., 2026** — PMID: 41712694

This paper appears to use protein language models to guide protein engineering and directed evolution. It may contain useful evidence about sequence representations and prediction of variant performance, but variant optimisation is different from predicting the native biological function of an uncharacterised protein.

**Full-text verification: required.**

### 14. Robust deep learning-based protein sequence design using ProteinMPNN  
**Dauparas et al., 2022** — DOI: 10.1126/science.add2187

Protein design is adjacent to function prediction but should not be conflated with it. The paper may be relevant to generative and structure-conditioned modelling, especially when discussing the boundary between predicting function and designing proteins with desired properties.

---

## Tier 3: General machine-learning or interpretability background

### 15. A guide to machine learning for biologists  
**Greener et al., 2021** — DOI: 10.1038/s41580-021-00407-0

Useful general background for model selection, validation, data leakage, overfitting, and interpretation. It is not protein-function-specific.

### 16. Leakage and the reproducibility crisis in machine-learning-based science  
**Kapoor and Narayanan, 2023** — DOI: 10.1016/j.patter.2023.100804

This is highly relevant to evaluating protein-function prediction studies, even though it is not protein-specific. It provides a framework for assessing whether reported performance may be inflated by:

- information leakage between training and test sets;
- duplicate or near-duplicate biological sequences;
- inappropriate random splitting;
- tuning on the test set; and
- poor reproducibility of data and code.

**Full-text verification: recommended.** It should support methodological criticism, but protein-specific examples should not be attributed to it without checking the text.

### 17. Practical guide to SHAP analysis  
**Ponce Bobadilla et al., 2024** — DOI: 10.1111/cts.70056

Potentially relevant to model interpretability, especially when functional predictions need to be linked to residues, domains, or structural features. It is not specific to proteins and does not establish that SHAP is biologically valid for any particular protein model.

**Full-text verification: required** before making claims about interpretation.

### 18. Informed Machine Learning  
**von Rueden et al., 2021** — DOI: 10.1109/TKDE.2021.3079836

Relevant to incorporating biological prior knowledge, physical constraints, ontologies, or structural information into learning systems. It is general methodological background rather than direct evidence.

---

## Records that are not materially relevant to the question

The following papers concern clinical prediction, disease mechanisms, therapeutic response, drug discovery, or unrelated applications. They should generally be excluded from a focused evidence synthesis on machine learning for protein-function prediction:

- **Machine learning-based reproducible prediction of type 2 diabetes subtypes** — Tanabe et al., 2024  
- **AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution** — Schade et al., 2024  
- **LCN2 drives ferroptosis-associated ischemia-reperfusion injury** — Wu et al., 2025  
- **Discovery of natural RORγt inhibitor** — Yoo et al., 2026  
- **Deciphering the mechanism of baicalein in cervical cancer** — Wang et al., 2025  
- **Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF** — Zhang et al., 2025  
- **Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease** — Sahoo et al., 2021  
- **Machine learning driven prediction of drug efficacy in lung cancer** — Li et al., 2025  
- **Multi-Omics Integration With Machine Learning** for diabetic retinopathy — Pang et al., 2024  
- **Machine Learning-Based Predictive Modeling** of mTOR/p53 therapy in AML — Li et al., 2025  
- **Computational modelling of olfactory receptors** — Odoemelam et al., 2025, unless the full text shows a specific function-prediction component  
- General reviews of agriculture, diabetes, clinical machine learning, generative AI, ensemble learning, extreme learning machines, digital twins, or materials science.

These papers might be relevant to general machine-learning methodology, but their biological prediction targets are not protein function.

---

## What the records suggest about current approaches

Taken together, the most relevant records point to several major uses of machine learning in protein-function prediction:

1. **Sequence-based prediction**  
   Protein sequences can be represented using handcrafted features, evolutionary profiles, or learned embeddings from protein language models. The transformer and protein-language-model records are relevant to this direction, although the supplied metadata does not confirm which functional labels were predicted.

2. **Structure-based prediction**  
   Protein structures can be represented as graphs in which residues or atoms are nodes and spatial contacts are edges. The graph-convolutional-network paper is direct evidence for this approach. AlphaFold and related structure databases increase the availability of structural inputs, including for proteins without experimentally determined structures.

3. **Interaction-informed prediction**  
   Protein–protein interaction and docking models may provide functional clues by predicting interaction partners, interfaces, or molecular complexes. These are generally intermediate tasks rather than direct functional annotation.

4. **Ontology- and knowledge-aware prediction**  
   The protein-annotation review and informed-machine-learning review are likely to address the use of structured biological knowledge, including functional ontologies and prior biological constraints. This can help exploit relationships among related functional terms rather than treating labels as independent classes.

5. **Specialised prediction**  
   Metalloproteins represent an example in which models may use sequence, structure, metal-binding motifs, or physicochemical features to predict a restricted class of functions or properties.

---

## Datasets and evaluation metrics

The supplied records do not provide enough information to state definitively which datasets or metrics were used in the direct studies. These details require full-text extraction, especially from:

- Gligorijević et al. (2021);
- Kulmanov and Hoehndorf (2025);
- Bordin et al. (2023); and
- Yu et al. (2022).

For a rigorous review, the following should be extracted from each paper:

### Dataset information

- protein sequence databases and release dates;
- experimentally characterised versus computationally annotated proteins;
- Gene Ontology or other functional-label sources;
- structural databases and structure-confidence thresholds;
- protein families or homology clusters;
- class balance and number of labels per protein;
- handling of obsolete, incomplete, or uncertain annotations;
- whether proteins sharing substantial sequence identity were grouped into the same split; and
- whether test proteins were drawn from a later database release or from the same annotation distribution as training proteins.

### Evaluation metrics

The metric choice should match the task. For multilabel functional annotation, relevant possibilities include:

- precision, recall, and F1 score;
- micro- and macro-averaged performance;
- area under the precision–recall curve;
- area under the receiver operating characteristic curve;
- ranking-based measures such as precision at *k* or recall at *k*;
- semantic similarity measures for Gene Ontology predictions;
- coverage and false-discovery measures;
- calibration of predicted probabilities; and
- performance stratified by protein family, sequence identity, or annotation depth.

These are methodological possibilities, not metrics confirmed for the listed papers. The full texts should be checked before attributing any particular metric to a study.

---

## Remaining limitations

The records support several important limitations, although the protein-specific evidence needs confirmation in the full texts.

### 1. Dependence on incomplete and biased labels

Protein-function datasets are usually built from existing annotations, which are unevenly distributed across species, protein families, and functions. Common or well-studied proteins are likely to be overrepresented, while rare functions and poorly characterised proteins are underrepresented. Models may therefore reproduce annotation availability rather than discover genuinely new biology.

### 2. Homology and data leakage

Random protein-level splitting can produce overly optimistic results when closely related sequences, domains, or structures occur in both training and test sets. The leakage paper is relevant to this concern. Protein-function studies should use homology-aware or family-aware splits and report performance at different sequence-similarity levels.

### 3. Incomplete transfer to remote homologues

A model can perform well on proteins similar to its training examples while failing on remote homologues or novel folds. Structure-based approaches may reduce some sequence-similarity limitations, but their performance can still depend on structure quality, domain boundaries, and the availability of informative structural neighbours.

### 4. Multifunctionality and context dependence

Proteins may have several molecular functions, participate in different complexes, or act differently across tissues, species, cellular compartments, or environmental conditions. A single static label may therefore inadequately represent the biological function being predicted.

### 5. Structural uncertainty

Predicted structures provide broad coverage, but confidence varies across domains, flexible regions, disordered segments, and protein complexes. Functional predictions based on uncertain regions or inaccurate interfaces may be unreliable. AlphaFold-derived structural availability should not be equated with experimentally validated functional information.

### 6. Class imbalance and annotation hierarchy

Functional labels are often highly imbalanced and hierarchically related. Generic terms may be easy to predict, whereas specific child terms are rare. Evaluation based only on aggregate accuracy or ROC-AUC can obscure poor performance on uncommon but biologically important functions.

### 7. Interpretability and biological validation

Feature-attribution methods may identify residues, contacts, or sequence regions associated with a prediction, but an explanation is not necessarily a mechanistic demonstration. Experimental validation remains important, particularly for predictions involving novel functions or therapeutic targets.

### 8. Reproducibility and changing databases

Protein databases, annotations, structures, and model checkpoints change rapidly. Results may depend strongly on database release, preprocessing, and split construction. Studies should report versions, filtering rules, code, model weights, and independent test sets.

---

## Overall assessment

The strongest direct evidence in this collection is the graph-convolutional-network study of structure-based function prediction and the recent review on computational functional annotation. The remaining protein-focused records mostly provide adjacent evidence on structure prediction, protein language models, interactions, docking, or specialised protein classes. The central methodological themes are the integration of sequence and structure representations, graph-based modelling of spatial relationships, transformer-derived protein embeddings, and use of biological knowledge or ontologies.

However, the supplied bibliographic records do not allow reliable conclusions about the exact datasets or metrics used. Full-text verification is essential before making study-level claims, particularly for benchmark composition, homology-aware splitting, annotation sources, and reported performance. The most important unresolved limitations are biased and incomplete functional labels, leakage through sequence or structural similarity, weak generalisation to remote or novel proteins, context-dependent multifunctionality, structural uncertainty, and insufficient experimental validation.