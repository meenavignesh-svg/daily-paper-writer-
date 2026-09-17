# Title

**Artificial Intelligence and Machine Learning for Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations**

## Abstract

Machine learning is increasingly used to infer protein function from amino-acid sequence, predicted or experimental structure, interaction networks, and integrated biological measurements. The supplied literature illustrates several major directions: structure-based graph learning for functional annotation, protein language models for sequence representation and directed evolution, machine learning for metalloprotein analysis, and models of protein–protein interactions and biomolecular complexes [3, 6, 14, 26]. These approaches extend beyond conventional sequence similarity by learning relationships among residues, structural environments, interaction partners, and functional labels. Large structure resources, including the AlphaFold Protein Structure Database, provide an important source of predicted structural information and reportedly cover more than 214 million protein sequences [29]. However, the evidence supplied here does not provide a consistent account of the datasets, train–test partitioning strategies, or evaluation metrics used across studies. In particular, details such as species composition, label quality, class imbalance, external validation, and performance on remote homologues are frequently unavailable from the bibliographic records alone [VERIFY]. The principal limitations therefore remain not only model accuracy, but also annotation incompleteness, data leakage, structural uncertainty, limited interpretability, and weak comparability between studies. More reliable progress will require carefully separated benchmarks, experimentally supported labels, calibrated predictions, and evaluation schemes that test generalisation to genuinely novel proteins.

## Introduction

Protein function prediction concerns the inference of biological roles from information such as sequence, three-dimensional structure, molecular interactions, biochemical measurements, or cellular context. Traditional approaches have relied heavily on homology, conserved motifs, structural comparison, and manually curated annotation. Machine learning adds a different capability: it can learn statistical representations from large collections of proteins and use these representations to assign functional labels or rank candidate functions.

The supplied literature shows that this field is closely connected to, but not identical with, protein structure prediction and protein design. AlphaFold demonstrated highly accurate structure prediction for many proteins [21], while AlphaFold 3 extended structure prediction to biomolecular interactions [22]. These developments are relevant to function prediction because structural models can be used as input to downstream classifiers, even when experimental structures are unavailable. The distinction is important, however. Predicting a structure is not equivalent to predicting biological function, and a structurally plausible model does not by itself establish biochemical activity.

Recent work has also broadened the meaning of protein function prediction. Models may annotate molecular function, infer interaction partners, identify functional residues, predict ligand binding, or guide the discovery of proteins with desired activities. Reviews of machine learning in protein science describe this wider landscape, including sequence models, structure-based methods, protein–protein docking, and computational modelling of receptor families [1, 10, 11, 16, 18]. The central questions for this review are therefore: how are machine-learning methods being used, what datasets and evaluation metrics are apparent in the available literature, and which limitations remain consequential?

## Evidence Synthesis

### Sequence-based learning and protein language models

A major use of machine learning is to represent protein sequences in a form that captures evolutionary or biochemical regularities. Protein language models learn from large sequence collections, generally by training on patterns of amino-acid co-occurrence and sequence context. The supplied record on protein language models describes their use in rapid directed evolution and explicitly highlights epistatic interactions, or dependencies between mutations [3]. In this setting, the model is not simply assigning a pre-existing functional annotation. It is being used to identify promising sequence variants and to guide experimental optimisation.

Sequence-based transformers have also been applied to virtual screening [15]. This indicates that transformer representations can support prediction or ranking tasks involving protein sequences and candidate molecules, although the supplied evidence does not specify the precise prediction target, training set, or evaluation protocol [VERIFY]. Similarly, the review *Novel machine learning approaches revolutionize protein knowledge* places sequence-based learning within a broader effort to extract functional information from protein data [18].

Sequence models are attractive because sequence databases are much larger than collections of experimentally characterised proteins. They can also be applied to proteins for which no experimentally determined structure exists. Their principal weakness is that a sequence representation does not necessarily resolve context-dependent function. Closely related proteins can differ in substrate specificity, cellular localisation, oligomeric state, or regulation, while remote homologues may share a function that is difficult to recognise from sequence alone. The supplied records do not allow the relative performance of language models and conventional homology-based methods to be quantified [VERIFY].

### Structure-based and graph-based prediction

Structure provides a second major representation for function prediction. The clearest directly relevant example is the use of graph convolutional networks for structure-based protein function prediction [26]. In such models, a protein can be represented as a graph in which residues or atoms are nodes and spatial proximity, chemical relationships, or other structural relations define edges. Graph learning can therefore capture local structural environments and long-range contacts that are not explicit in a one-dimensional sequence.

This approach benefits from the expansion of predicted structural resources. The AlphaFold Protein Structure Database is described as providing structural coverage for more than 214 million protein sequences [29]. Such coverage creates the possibility of applying structure-based annotation to proteins without experimentally resolved structures. Nevertheless, database-scale structural coverage should not be confused with database-scale functional validation. A predicted structure may be useful for recognising a fold or identifying a possible active-site arrangement, but it may not reliably distinguish among related biochemical functions.

Protein–protein interaction prediction provides a related application. Hierarchical graph learning has been used for protein–protein interaction [14], and machine-learning methods have also been reviewed in the context of protein–protein docking [11]. These models can contribute to functional inference by identifying interaction partners or plausible complexes. AlphaFold 3 further demonstrates the importance of modelling biomolecular interactions rather than isolated protein structures [22]. Yet interaction prediction remains an indirect route to function: an interaction may be conditional on cell type, modification state, concentration, or experimental assay, and a predicted association does not necessarily establish physiological relevance.

### Functional inference for specialised protein classes

Some applications focus on protein families whose functions depend strongly on chemical context. Metalloproteins are an example. The review by Yu, Wang, and Teo concerns machine-learning approaches for metalloproteins [6], where metal coordination, ligand identity, geometry, and local structure may be central to activity. This class illustrates why generic sequence-only prediction may be inadequate. Functional classification may require features describing residues around a metal-binding site, structural geometry, or physicochemical properties.

Other supplied records concern computational modelling of olfactory receptors [16], a difficult receptor family in which sequence diversity and membrane-protein structure complicate annotation. Protein structure prediction and modelling are also discussed in the context of drug discovery [10]. These studies suggest that machine learning is often used as one component of a larger workflow rather than as a standalone function annotator. Typical workflows may combine prediction with virtual screening, molecular simulation, docking, or experimental validation. The supplied records do not provide enough methodological detail to determine how often these downstream predictions are experimentally confirmed [VERIFY].

### Integration with biological and clinical data

Several records use machine learning to connect proteins with disease phenotypes, biomarkers, or treatment response. Examples include inflammatory protein signatures for mortality prediction [9], protein biomarkers and clinical features for drug-efficacy prediction [13], and multi-omics integration for diabetic retinopathy and treatment response [19]. These studies are relevant to protein function in a broad translational sense, but they do not necessarily predict molecular function in the conventional annotation sense. They instead infer clinical outcomes or disease-associated roles from protein measurements and other patient-level variables.

This distinction matters when comparing evidence. A model that predicts a clinical endpoint from an Olink protein signature is solving a different problem from a model that assigns Gene Ontology molecular-function terms to an uncharacterised sequence. The datasets, labels, sources of variation, and appropriate metrics are correspondingly different. The supplied literature includes both kinds of work, but does not support a single unified performance comparison [VERIFY].

### Use of machine learning in discovery and design

Machine learning is also used to prioritise candidate proteins, mutations, ligands, and therapeutic targets. The record on directed evolution uses protein language models and epistatic interactions to accelerate sequence optimisation [3]. Other studies combine machine learning with virtual screening and in vivo validation to identify an inhibitor of RORγt [7], or with computational simulations to investigate candidate inhibitors against the monkeypox virus P37 envelope protein [17]. These applications use prediction to narrow a large search space.

Such systems should be viewed as decision-support methods rather than direct measurements of function. A model may rank candidates effectively while still providing an imperfect mechanistic explanation. In addition, discovery studies often report the success of selected candidates, whereas the performance of the full ranking system, including negative or unselected candidates, may be harder to assess. The supplied evidence does not specify whether these studies report standard ranking metrics, prospective validation rates, or calibration analyses [VERIFY].

## Methods and Datasets Observed

This review is based on the supplied bibliography and the information visible in the associated records. It is therefore an evidence mapping exercise rather than a reproducible systematic review. The records include primary research articles and reviews retrieved from PubMed and OpenAlex. The most directly relevant sources are the structure-based graph convolutional network study [26], the reviews of machine learning for metalloproteins and protein–protein docking [6, 11], the review of emerging approaches in protein knowledge [18], and studies involving protein language models, sequence transformers, and biomolecular structure prediction [3, 15, 21, 22].

The datasets observed in the supplied evidence fall into several broad categories:

1. **Protein sequence collections.** Protein language models and sequence-based transformers rely on large sequence corpora, although the specific databases, sequence counts, filtering procedures, and taxonomic composition are not reported in the supplied summaries [VERIFY].

2. **Predicted and experimentally determined structures.** AlphaFold and AlphaFold 3 provide structural predictions relevant to downstream function and interaction analysis [21, 22]. The AlphaFold Protein Structure Database is reported to provide coverage for more than 214 million protein sequences [29]. The precise subset used for functional prediction, confidence filtering, and removal of homologous sequences is not specified [VERIFY].

3. **Structure–function and interaction datasets.** The graph convolutional network study uses protein structures for functional prediction [26], while other records concern protein–protein interactions and docking [11, 14]. The supplied evidence does not identify the annotation ontologies, interaction databases, structural-resolution thresholds, or train–test split policies [VERIFY].

4. **Specialised biochemical datasets.** Metalloprotein studies are likely to require labels relating to metal binding or metalloprotein class [6], while receptor modelling and protein–ligand screening use family-specific or ligand-associated information [7, 16, 17]. The exact datasets and label definitions are not available in the supplied records [VERIFY].

5. **Clinical and multi-omics datasets.** Some studies use protein biomarkers together with clinical variables or other omics measurements [9, 13, 19]. These datasets are designed for disease or treatment-response prediction rather than general protein-function annotation.

The available evidence is notably sparse regarding evaluation metrics. Standard machine-learning practice distinguishes classification metrics such as accuracy, precision, recall, F1 score, area under the receiver-operating-characteristic curve, and area under the precision–recall curve; ranking tasks may use enrichment or ranking-based measures; and regression tasks may use correlation or error measures. However, the supplied records do not provide a reliable study-by-study account of which metrics were used. Accordingly, assigning particular metrics to individual papers would risk fabrication [VERIFY]. The same caution applies to claims about cross-validation, independent test sets, calibration, confidence intervals, or prospective experimental validation.

The general machine-learning literature emphasises the importance of appropriate model evaluation and awareness of leakage [23, 30]. These concerns are especially important in protein datasets because homologous sequences, related structures, and shared annotations can occur across nominally separate training and test sets. A random split may therefore produce an optimistic estimate if the test proteins are close relatives of proteins seen during training. The supplied evidence raises this methodological issue but does not establish how consistently it has been addressed in the protein studies listed here [VERIFY].

## Research Gaps

Several gaps remain evident.

First, there is no consistent benchmark framework spanning sequence-only, structure-based, interaction-based, and multimodal models. These approaches often address related but non-identical prediction tasks, use different label definitions, and report different metrics. Direct comparisons are consequently difficult.

Second, evaluation on genuinely novel proteins remains insufficiently documented. Performance should ideally be assessed using splits based on sequence similarity, structural similarity, protein family, or evolutionary lineage, rather than only random partitions. The available records do not establish whether such stringent splits were routinely used [VERIFY].

Third, functional labels are uneven in quality. Protein databases contain experimentally supported annotations, computational transfers, incomplete annotations, and potentially contradictory records. A model may learn annotation practices or database biases rather than biological function. The supplied literature does not provide enough detail to assess label provenance across the studies.

Fourth, the field needs stronger treatment of uncertainty. Functional prediction is often multi-label: a protein may participate in several processes, have multiple molecular activities, or act differently in different cellular contexts. A single top-ranked label can therefore be misleading. Confidence calibration, abstention, and explicit representation of alternative functions are important but not documented consistently in the available evidence [VERIFY].

Fifth, interpretability remains unresolved. Graph models and language models can identify residues or sequence regions associated with a prediction, but an association is not necessarily a causal biochemical explanation. General work on explaining supervised machine-learning predictions, including SHAP-based approaches, provides relevant methodological context [27], but the supplied records do not show how consistently such explanations are validated experimentally in protein-function studies.

Finally, experimental validation remains a bottleneck. Models can prioritise candidates for testing, but functional assignment ultimately depends on biochemical, cellular, or organismal evidence. The literature includes examples of in vivo validation in discovery workflows [7], yet the evidence provided does not indicate the proportion of predictions that receive independent experimental confirmation across the field.

## Limitations

This review has several limitations. The evidence set is heterogeneous and includes papers that are peripheral to molecular protein-function prediction, such as clinical outcome modelling, cancer treatment prediction, and general machine-learning reviews. These records were retained where they helped clarify how protein measurements or machine learning are used, but they should not be interpreted as direct evidence of performance in protein annotation.

The bibliographic records contain titles, authors, years, identifiers, and links, but not complete methodological descriptions. In particular, the supplied material does not consistently report training datasets, feature representations, label ontologies, split strategies, hyperparameters, baseline models, evaluation metrics, or experimental validation. Statements about those details have therefore been marked [VERIFY] rather than inferred.

A further limitation is that the evidence includes reviews alongside primary studies. Reviews can identify methodological trends, but they cannot substitute for inspection of the original experiments when comparing datasets or metrics. In addition, some linked articles were unavailable or associated with access errors, and the supplied analysis indicates that automated drafting failed because of a rate-limit error. The present synthesis consequently relies only on the evidence explicitly provided and does not claim exhaustive retrieval or independent verification of every article.

## Conclusion

Machine learning is being used for protein-function prediction through several complementary routes. Sequence models and protein language models learn representations from large protein corpora and can support annotation, mutation prioritisation, and directed evolution [3, 15, 18]. Structure-based graph models use spatial relationships among residues to predict functional labels [26]. Interaction and docking models extend inference to protein complexes [11, 14, 22], while specialised approaches address metalloproteins, receptors, protein–ligand interactions, and disease-associated protein signatures [6, 9, 13, 16]. Large predicted-structure resources, particularly the AlphaFold Protein Structure Database, make structure-informed analysis possible at unprecedented scale [21, 29].

The main weakness of the current evidence is not a lack of model diversity, but a lack of consistently documented and biologically demanding evaluation. The supplied records do not permit a reliable comparison of datasets or metrics across studies [VERIFY]. Future work should report annotation provenance, homology-aware data splits, independent test sets, calibration, uncertainty, and experimental confirmation in a standardised manner. Most importantly, performance should be measured on proteins and functions that are genuinely outside the model’s training distribution. Without that discipline, high predictive scores may reflect data redundancy or annotation leakage rather than robust functional understanding.

## References

[1] Chen L, Li Q, Nasif KFA, et al. AI-Driven Deep Learning Techniques in Protein Structure Prediction. 2024. PMID: 39125995.

[2] Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID: 35209064.

[3] Tran VQ, Nemeth M, Bartie LJ, et al. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID: 41712694.

[4] Schauperl M, Denny RA. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges. 2022. PMID: 35727311.

[5] Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID: 38987466.

[6] Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein-protein interaction. 2023. PMID: 36841846.

[7] Zhang S, Huo D, Horne RI, et al. Sequence-based virtual screening using transformers. 2025. PMID: 40721411.

[8] Odoemelam CS, Steuber V, Schmuker M. Computational modelling of olfactory receptors. 2025. PMID: 40441539.

[9] Rout M, Dey S, Mishra S, et al. Machine learning and classical MD simulation to identify inhibitors against the P37 envelope protein of monkeypox virus. 2024. PMID: 37221882.

[10] Bordin N, Dallago C, Heinzinger M, et al. Novel machine learning approaches revolutionize protein knowledge. 2023. PMID: 36504138.

[11] Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. *Nature*. 2021. doi:10.1038/s41586-021-03819-2.

[12] Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*. 2024. doi:10.1038/s41586-024-07487-w.

[13] Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. *Nature Communications*. 2021. doi:10.1038/s41467-021-23303-9.

[14] Greener JG, Kandathil SM, Moffat L, Jones DT. A guide to machine learning for biologists. *Nature Reviews Molecular Cell Biology*. 2021. doi:10.1038/s41580-021-00407-0.

[15] Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. *Nucleic Acids Research*. 2023. doi:10.1093/nar/gkad1011.

[16] Bobadilla AVP, Schmitt V, Maier CS, et al. Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development. 2024. doi:10.1111/cts.70056.

[17] Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.

[18] Yoo H, Han SJ, Lee JE, et al. Discovery of natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation. 2026. PMID: 40915561.

[19] Zhang Y, Sun L, Liu H, et al. Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF Using Olink-Derived Inflammatory Protein Signatures. 2025. PMID: 41255250.

[20] Pang Y, Luo C, Zhang Q, et al. Multi-Omics Integration With Machine Learning Identified Early Diabetic Retinopathy, Diabetic Macula Edema and Anti-VEGF Treatment Response. 2024. PMID: 39671223.

[21] Li J, Chen A, Liu Z, et al. Machine learning driven prediction of drug efficacy in lung cancer: based on protein biomarkers and clinical features. 2025. PMID: 40355026.