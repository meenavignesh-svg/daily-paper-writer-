# Title

**Artificial Intelligence and Machine Learning for Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations**

## Abstract

Machine-learning methods are increasingly used to infer protein function from amino-acid sequences, three-dimensional structures, protein–protein interactions, and biochemical or variant-associated data. The supplied evidence most directly supports structure-based prediction using graph convolutional networks, while related studies demonstrate the use of protein language models, transformers, interaction graphs, and structure-prediction systems for narrower tasks such as activity, binding, interaction, or variant-effect prediction [1–6]. Large predicted-structure resources, including the AlphaFold Protein Structure Database, may expand the structural information available for functional inference [7]. However, the supplied records do not consistently identify the precise datasets, annotation schemes, data splits, or evaluation metrics used in the relevant studies. Accordingly, claims about benchmark databases and comparative performance require verification. Important unresolved issues include annotation incompleteness, label imbalance, similarity leakage between training and test proteins, limited interpretability, uncertainty in predicted structures, and insufficient experimental validation.

## Introduction

Protein function prediction involves assigning one or more biological, molecular, or cellular roles to a protein. Depending on the task, the target may include enzyme activity, molecular function, biological process, cellular localization, ligand or metal binding, interaction partners, or the effects of sequence variation. These tasks are challenging because function is determined by interacting factors, including sequence, structure, dynamics, evolutionary history, cellular context, and post-translational regulation.

Machine learning provides several ways to integrate these sources of information. Conventional supervised models can use engineered sequence or structural features, whereas deep-learning systems can learn representations directly from sequences, contact maps, three-dimensional structures, or interaction networks. Protein-language models and transformer architectures provide another approach by learning statistical regularities from large collections of protein sequences [2,3]. Structure-based graph models represent residues or atoms as nodes connected according to spatial relationships; this approach is illustrated directly by the study of Gligorijević et al. on structure-based protein-function prediction [1].

The available evidence is heterogeneous. Some records address protein-function annotation directly, whereas others concern related predictions, including protein–protein interactions, docking, protein design, drug resistance, or molecular bioactivity [2–6]. These neighboring applications are informative but should not be treated as equivalent to general protein-function prediction without full-text verification.

## Evidence Synthesis

### 1. Sequence-based prediction and protein-language models

Amino-acid sequence is the most accessible representation of a protein and can encode information about evolutionary conservation, domains, motifs, localization signals, and physicochemical properties. Machine-learning systems may use one-hot or physicochemical encodings, profile-based features, embeddings from pretrained protein-language models, or transformer representations.

The supplied records indicate applications of protein-language models and transformers to protein-related prediction. Tran et al. describe the use of protein-language models and epistatic interactions to guide directed evolution [2]. Zhang et al. report sequence-based virtual screening using transformers [3]. These studies support the broader use of learned sequence representations for predicting protein-associated properties, but the supplied metadata does not establish that either study performs general ontology-based protein-function annotation. Their targets may instead be activity, ligand-related behavior, sequence fitness, or variant effects [VERIFY].

Protein-language models can be used in at least two ways:

1. **Feature extraction:** a pretrained model produces embeddings that are supplied to a downstream classifier or regressor.
2. **End-to-end or fine-tuned prediction:** model parameters are adapted to a labeled functional task.

The supplied evidence does not specify the pretraining corpora, fine-tuning procedures, annotation schemes, or family-level holdout strategies used in the listed studies [VERIFY]. These details are important because sequence similarity between training and test proteins can make a task substantially easier than prediction for genuinely novel protein families.

### 2. Structure-based function prediction

Protein structure provides spatial information that is not explicit in a linear sequence. Residues that are distant in sequence may be adjacent in three-dimensional space and jointly form an active site, binding interface, or structural motif. Graph neural networks are well suited to this representation because residues or atoms can be modeled as nodes, with edges representing spatial proximity, covalent bonds, or other structural relationships.

Gligorijević et al. provide the clearest direct evidence for this approach through a structure-based protein-function prediction model using graph convolutional networks [1]. The title supports the use of structural graphs and GCNs for functional prediction. However, the supplied evidence does not specify:

- whether the structures were experimentally determined or computationally predicted;
- whether nodes represented residues, atoms, or other structural elements;
- which functional labels were predicted;
- whether the task was single-label, multilabel, or hierarchical;
- what baselines and evaluation metrics were used; or
- how structural similarity between training and test proteins was controlled [VERIFY].

Predicted structures may increase the amount of structural information available for machine learning. The AlphaFold Protein Structure Database was reported as providing structural coverage for more than 214 million protein sequences [7]. This scale could facilitate structure-based annotation, particularly for proteins lacking experimentally determined structures. Nevertheless, structural availability does not imply accurate functional annotation. Predicted structures can contain uncertainty, and functional inference may depend on conformational states, ligand interactions, dynamics, or cellular context that are not fully represented by a single predicted structure.

AlphaFold and AlphaFold 3 primarily concern structure or biomolecular-interaction prediction rather than direct functional annotation [8,9]. Their outputs may nevertheless serve as inputs to downstream function-prediction systems. The extent to which this improves prediction for remote homologues or poorly characterized proteins remains [VERIFY].

### 3. Interaction- and network-based inference

Protein–protein interactions can provide indirect evidence about function. Proteins that interact may participate in the same complex, pathway, or biological process. Graph-learning methods can therefore use interaction networks to infer functional similarity or assign annotations.

Gao et al. describe hierarchical graph learning for protein–protein interaction prediction [4], while Michalik and Kuder review machine-learning methods for protein–protein docking [5]. These studies are relevant to interaction-informed functional inference, but interaction prediction is not identical to protein-function prediction. The former predicts relationships between proteins; the latter assigns properties or roles to individual proteins. A complete function-prediction pipeline may combine both tasks, but this distinction should be maintained.

Interaction data may also be noisy and incomplete. Experimentally observed interactions are influenced by assay type, cellular conditions, publication bias, and the degree to which particular proteins have been studied. Consequently, an interaction-based model can inherit biases from the underlying network [VERIFY].

### 4. Biochemical, metal-binding, and variant-related prediction

Some machine-learning applications focus on particular biochemical classes or functional mechanisms. Yu et al. review machine-learning approaches for metalloproteins [6]. Metalloprotein function may depend on metal identity, coordination geometry, local sequence context, and catalytic environment. The record confirms the relevance of machine learning to metalloprotein problems, but it does not identify whether the predicted outcome was metal-binding-site location, metal identity, catalytic activity, protein classification, or another property [VERIFY].

Variant-oriented methods provide another route to functional inference. Tran et al. combine protein-language models with epistatic interactions to guide directed evolution [2], and Xie et al. combine molecular dynamics and machine learning to predict drug-resistance-causing BRAF variants [10]. Such studies may predict changes in activity, stability, binding, or phenotype rather than assign broad functional annotations. They therefore represent a related but narrower category of protein-function prediction.

### 5. Generative and structure-enabled approaches

Recent systems also use machine learning to design sequences or predict structures and complexes. ProteinMPNN, for example, is presented as a deep-learning method for protein sequence design [11]. Sequence design is not itself function prediction, but design models can be used to identify sequences likely to adopt a desired fold or support a specified structural context. Similarly, AlphaFold 3 addresses biomolecular interactions and may provide structural hypotheses relevant to binding and function [9].

These approaches illustrate a shift from passive annotation toward integrated prediction and design. However, the evidence supplied does not demonstrate that generated sequences or predicted complexes reliably reproduce biological function in vivo. Experimental validation remains necessary [VERIFY].

## Methods and Datasets

### Data modalities

The supplied records indicate several data modalities relevant to protein-function prediction:

| Data modality | Potential use | Evidence |
|---|---|---|
| Protein sequences | Motif detection, evolutionary representation, embedding-based classification, variant-effect prediction | [2, 3, 10] |
| Protein structures | Active-site, fold, interface, and structure-based function prediction | [1, 7–9] |
| Protein–protein interaction networks | Network-context and interaction-informed functional inference | [4, 5] |
| Metalloprotein measurements | Metal-binding or metalloprotein-specific prediction | [6] |
| Variant and evolution data | Activity, resistance, fitness, or epistatic-effect prediction | [2, 10] |
| Ligand and bioactivity data | Binding, activity, or target-related prediction | [3, 12] |

The precise benchmark datasets used by the direct function-prediction study are not identified in the supplied evidence. In particular, the records do not establish the use of any specific protein-ontology database, sequence database, structural benchmark, interaction database, or challenge dataset [VERIFY]. Sample sizes, annotation-release dates, redundancy-reduction procedures, and class distributions are also unavailable.

### Learning paradigms

The evidence supports several methodological paradigms:

- **Supervised learning:** models are trained using proteins with known labels or measured properties.
- **Transfer learning:** pretrained sequence or structure models are adapted to a downstream task.
- **Graph learning:** residues, atoms, proteins, or interactions are represented as nodes and edges.
- **Multimodal learning:** sequence, structure, interaction, and biochemical information are combined.
- **Generative modeling:** models produce sequences or structural hypotheses that may be associated with desired functions.
- **Hybrid physics–machine-learning approaches:** molecular simulations or structural calculations are combined with learned predictors, as illustrated by the BRAF drug-resistance study [10].

General guidance on model selection, feature construction, validation, and interpretation is provided in broader machine-learning literature [13]. However, the supplied evidence does not permit a reliable comparison of the architectures or training procedures used in the protein-function studies.

### Evaluation metrics

The available records do not report, in the supplied metadata, the evaluation metrics used by the direct protein-function prediction study [1]. Therefore, no particular metric can be attributed confidently to that study without full-text inspection.

Appropriate metrics depend on the prediction target:

- **Multilabel functional annotation:** precision, recall, F1 score, average precision, or area under the precision–recall curve.
- **Hierarchical annotations:** metrics that account for partial correctness at different levels of the functional hierarchy.
- **Imbalanced labels:** precision–recall-based measures, macro-averaged scores, and per-class performance may be more informative than accuracy.
- **Ranking-based annotation:** precision at \(k\), recall at \(k\), mean average precision, or related ranking measures.
- **Interaction prediction:** AUROC, AUPRC, precision, recall, F1, and ranking metrics.
- **Residue- or site-level prediction:** residue-level precision, recall, F1, or overlap measures.
- **Continuous biochemical properties:** correlation, mean absolute error, root-mean-square error, and calibration-related measures.

These metrics are methodological possibilities rather than confirmed descriptions of the listed papers [VERIFY]. A central missing detail is the split strategy. Random splits can place closely related proteins, paralogues, or homologous domains in both training and test sets, potentially inflating apparent performance. Concerns about data leakage and reproducibility are discussed more generally by Kapoor and Narayanan [14]. Protein-function benchmarks should therefore report sequence-identity clustering, family-level holdouts, species separation, and, where possible, temporal validation [VERIFY].

## Research Gaps

1. **Incomplete reporting of datasets and labels.**  
   The available evidence does not identify the exact annotation sources, database versions, sample sizes, or label definitions used in the direct protein-function studies [VERIFY].

2. **Insufficiently stringent generalization tests.**  
   It remains important to determine whether models generalize to remote homologues, new protein families, new species, or newly characterized functions rather than merely interpolating among similar proteins [VERIFY].

3. **Integration of structure and sequence uncertainty.**  
   Predicted structures offer broad coverage, but models should account for confidence scores, alternative conformations, disorder, ligand dependence, and dynamic states [VERIFY].

4. **Functional context beyond isolated proteins.**  
   Many functions depend on complexes, cellular localization, expression, cofactors, post-translational modifications, and environmental conditions. Sequence- or structure-only models may not capture these factors [VERIFY].

5. **Better treatment of hierarchical and multilabel outputs.**  
   Protein functions are often overlapping and hierarchically organized. Evaluation should distinguish biologically meaningful partial predictions from completely incorrect assignments [VERIFY].

6. **Interpretability and mechanistic validation.**  
   Attention maps, residue attribution, or other explanation methods may identify influential features, but their correspondence to causal mechanisms requires experimental testing [VERIFY]. General approaches to explaining machine-learning predictions, including SHAP-based analysis, are available but are not specific evidence of validation for protein-function models [15].

7. **Experimental and prospective validation.**  
   Many computational predictions are evaluated against existing annotations. More prospective tests are needed to establish whether models can discover previously unrecognized functions and guide laboratory experiments [VERIFY].

8. **Reproducibility and benchmark standardization.**  
   Comparisons are difficult when studies use different data releases, splits, label policies, and metrics. Reproducible code, fixed benchmark protocols, and explicit leakage controls are needed [14].

## Limitations

This review is constrained by the supplied bibliography and accompanying analysis rather than a systematic search of the full literature. The evidence includes only a small number of records that directly address protein-function prediction; several others concern adjacent topics such as structure prediction, protein design, molecular bioactivity, drug resistance, or interaction prediction. These studies were included only as contextual evidence and should not be interpreted as direct demonstrations of general function annotation.

The supplied metadata generally consists of titles, authors, dates, and identifiers. It does not provide sufficient detail to verify the datasets, preprocessing procedures, model architectures, data splits, baselines, statistical tests, or evaluation metrics used in most studies. Statements about common benchmark databases and recommended metrics are therefore methodological context, not paper-specific findings, and are marked [VERIFY] where appropriate.

The evidence also does not support a quantitative comparison of model performance. In particular, no pooled accuracy estimate, meta-analysis, or ranking of architectures can be derived. Finally, publication and selection bias may favor successful applications and highly studied protein families, while poorly annotated proteins and negative results may be underrepresented [VERIFY].

## Conclusion

Machine learning is being applied to protein-function prediction through sequence models, protein-language models, structural graph networks, interaction graphs, biochemical-property predictors, and hybrid simulation–learning systems. The strongest direct evidence in the supplied records concerns structure-based function prediction with graph convolutional networks [1]. Other studies demonstrate related uses of protein-language models, transformers, interaction learning, metalloprotein modeling, and variant-effect prediction [2–6,10].

The principal data sources include protein sequences, predicted or experimental structures, interaction networks, biochemical measurements, and variant-associated observations. However, the supplied evidence does not identify the precise datasets or evaluation metrics used in most relevant studies. Reliable assessment therefore requires explicit reporting of annotation sources, label hierarchy, redundancy controls, family-level splits, class imbalance, calibration, and prospective validation.

The field’s central limitation is not simply model capacity. It is the difficulty of obtaining complete, unbiased, context-specific functional labels and evaluating generalization without sequence or structural leakage. Future progress will likely depend on integrating multimodal biological evidence while maintaining rigorous, leakage-resistant benchmarks and experimental validation.

## References

1. Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.

2. Tran VQ, Nemeth M, Bartie LJ, et al. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID:391? [VERIFY: supplied record lists PMID 41712694].

3. Zhang S, Huo D, Horne RI, et al. Sequence-based virtual screening using transformers. 2025. PMID:40721411.

4. Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein-protein interaction. 2023. PMID:36841846.

5. Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID:38987466.

6. Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID:35209064.

7. Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.

8. Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. *Nature*. 2021. doi:10.1038/s41586-021-03819-2.

9. Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*. 2024. doi:10.1038/s41586-024-07487-w.

10. Xie L, Lockhart C, Klimov DK, Jafri MS. Combining Molecular Dynamics and Machine Learning to Predict Drug Resistance Causing Variants of BRAF in Colorectal Cancer. 2025. PMID:40942081.

11. Dauparas J, Anishchenko I, Bennett NR, et al. Robust deep learning–based protein sequence design using ProteinMPNN. *Science*. 2022. doi:10.1126/science.add2187.

12. Bule M, Jalalimanesh N, Bayrami Z, et al. The rise of deep learning and transformations in bioactivity prediction power of molecular modeling tools. 2021. PMID:34532977.

13. Greener JG, Kandathil SM, Moffat L, Jones DT. A guide to machine learning for biologists. *Nature Reviews Molecular Cell Biology*. 2021. doi:10.1038/s41580-021-00407-0.

14. Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.

15. Ponce Bobadilla AV, Schmitt V, Maier CS, et al. Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development. 2024. doi:10.1111/cts.70056.