# AI and Machine Learning in Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations

## Abstract

Machine learning is being applied to protein function prediction through several related strategies: learning from amino-acid sequences, representing proteins as structural graphs, modelling protein–protein interactions, and combining predicted structures with functional or biochemical information. The supplied literature includes work on structure-based graph convolutional networks, protein language models, transformer-based sequence screening, metalloprotein analysis, protein–protein docking, and large-scale structure prediction [1–7]. These studies indicate a gradual shift from manually engineered sequence descriptors towards representations learned from large sequence and structure collections. However, the evidence supplied here is primarily bibliographic rather than a detailed extraction of experimental results. Consequently, the precise training datasets, label definitions, data-splitting procedures, and evaluation metrics used by individual studies cannot be established reliably for most records. The literature also points to persistent concerns about annotation quality, evolutionary redundancy, limited experimental validation, interpretability, and leakage between training and test data. Protein structure databases and predicted-structure resources substantially extend the available input space, but increased coverage does not necessarily provide equally reliable functional labels. More rigorous benchmarking across remote homologues, protein families, organisms, and experimentally validated functions remains necessary.

## Introduction

Protein function prediction seeks to infer what a protein does from available molecular information, most commonly its amino-acid sequence, three-dimensional structure, evolutionary relationships, interaction partners, or biochemical context. Conventional computational annotation has often relied on sequence similarity, conserved motifs, domain assignments, and experimentally characterised homologues. Machine-learning methods extend this framework by learning statistical relationships between molecular representations and functional labels, rather than requiring every predictive rule to be specified in advance.

The recent literature spans several levels of biological description. Protein language models learn representations from large collections of sequences and can be used for annotation, variant analysis, or directed evolution [1, 2]. Structure-based models represent residues and their spatial relationships explicitly; one study applies graph convolutional networks to protein function prediction [3]. Other work addresses adjacent problems, including protein–protein docking [4], protein–protein interaction prediction [5], metalloprotein modelling [6], and sequence-based virtual screening with transformers [7]. These tasks are not identical to assigning a protein function, but they illustrate how machine learning is increasingly used to connect sequence, structure, molecular interactions, and phenotype.

The role of structure prediction has also expanded. AlphaFold demonstrated highly accurate protein structure prediction [8], while AlphaFold 3 extends structure modelling to biomolecular interactions [9]. The AlphaFold Protein Structure Database provides predicted structural coverage for more than 214 million protein sequences, according to the title and description of the cited database paper [10]. Such resources can provide structural inputs for function-prediction systems, especially for proteins lacking experimentally determined structures. They do not, however, remove the need for reliable functional annotations or experimental validation.

This review asks how machine-learning methods are being used to predict protein function, what datasets and evaluation metrics are used, and what limitations remain. The supplied evidence does not contain a systematic extraction of methods and results from every paper. Where a dataset, metric, or methodological detail cannot be supported directly, it is identified as [VERIFY].

## Evidence Synthesis

### Sequence-based learning and protein language models

A major direction in current protein machine learning is the use of sequence representations learned from large protein corpora. The review by Bordin and colleagues describes newer machine-learning approaches for extracting knowledge from protein sequences and related biological data [1]. Protein language models are also used in directed evolution. Tran and colleagues describe rapid directed evolution guided by protein language models and epistatic interactions [2]. In this setting, the model is not simply assigning an existing functional label. It is being used to identify or prioritise sequence changes in the context of interactions among mutations. This illustrates a broader trend in which learned sequence representations support both annotation and the design or optimisation of proteins.

Transformer architectures are likewise being applied to sequence-based virtual screening [7]. The immediate task is screening rather than general functional annotation, and the supplied record does not establish the exact target labels, training data, or performance measures [VERIFY]. Nevertheless, sequence-based screening is relevant to function prediction because ligand binding, substrate specificity, and biochemical activity are important components of protein function.

Sequence-only models can be attractive because protein sequences are abundant relative to experimentally resolved structures. Their limitation is that function is often determined by three-dimensional organisation, conformational dynamics, oligomerisation, post-translational modification, cellular localisation, and interactions with other molecules. Sequence representations may encode some of these properties indirectly, but the extent to which they do so for poorly represented protein families remains [VERIFY].

### Structure-based prediction

Structure-based machine learning treats the protein as a spatial object rather than a one-dimensional sequence. Gligorijević and colleagues explicitly describe structure-based protein function prediction using graph convolutional networks [3]. In this formulation, residues or atoms can be represented as graph nodes, while edges encode spatial proximity or other structural relationships. Graph learning is therefore well suited to identifying local structural motifs and long-range residue relationships that are difficult to express in a simple sequence representation.

Structure-based prediction is supported by advances in computational structure generation. AlphaFold produced highly accurate protein structure predictions [8], and AlphaFold 3 addresses interactions involving proteins and other biomolecules [9]. Predicted structures can extend structural annotation to proteins without experimentally determined coordinates. The AlphaFold Protein Structure Database further increases the practical availability of structural inputs [10].

However, the use of predicted structures introduces uncertainty that should be propagated into downstream function prediction. A predicted structure may be accurate in a well-folded domain but less reliable in disordered regions, flexible loops, alternative conformations, or interfaces. The supplied evidence does not provide a quantitative assessment of how structural uncertainty affects function-prediction accuracy [VERIFY].

### Interaction- and context-based prediction

Protein function is frequently expressed through interactions. The literature supplied includes machine-learning methods for protein–protein docking [4] and hierarchical graph learning for protein–protein interaction prediction [5]. These approaches model relationships between proteins rather than assigning function from an isolated sequence. Such methods may help infer complexes, interaction partners, or functional modules, which can in turn support functional annotation.

Interaction-based predictions are particularly important for proteins whose biochemical activity depends on complex formation. At the same time, interaction labels are often context dependent. An interaction observed in one tissue, cellular compartment, or experimental assay may not generalise to another biological setting. The supplied records do not provide sufficient information to determine how the cited studies handled tissue specificity, condition dependence, false negatives, or assay heterogeneity [VERIFY].

The review of machine-learning approaches for metalloproteins represents another specialised direction [6]. Metalloprotein function depends on coordination chemistry, metal identity, ligand geometry, and local structural environment. This domain illustrates why generic sequence-based prediction may be insufficient for some protein classes and why domain-specific representations or chemically informed features may be necessary.

### Integrated computational workflows

Several records describe broader workflows in which machine learning is combined with virtual screening, molecular modelling, or experimental validation. These include the discovery of a natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation [11], as well as a study of baicalein mechanisms involving computational analysis and candidate target proteins [12]. Such studies are not necessarily benchmarks of general protein-function prediction. Rather, they use machine learning to prioritise candidate proteins, ligands, or mechanisms within a biological discovery pipeline.

This distinction matters. A model that successfully prioritises a therapeutic target or compound is not automatically a general-purpose protein-function predictor. Its apparent performance may depend on the biological system, the candidate space, and the experimental validation strategy. The supplied evidence does not permit a direct comparison between these application-oriented studies and methods developed specifically for function annotation [VERIFY].

## Methods and Datasets Observed

The supplied corpus contains several classes of input data, although the precise datasets used by most individual studies are not specified in the available evidence.

**Protein sequences.** Protein language models and transformer-based methods use amino-acid sequences as their primary input [1, 2, 7]. The underlying sequence corpora, redundancy-reduction procedures, taxonomic composition, and train–test partitioning are not reported in the supplied records [VERIFY]. These details are essential because sequence similarity between training and test proteins can substantially inflate apparent performance.

**Protein structures.** Structure-based graph convolutional networks use structural information to predict protein function [3]. The exact source of the structures, the representation of nodes and edges, and the functional annotation database are not given here [VERIFY]. Predicted structures from AlphaFold and related resources provide a potentially large structural input set [8–10], but the distinction between experimentally determined and predicted structures should be retained during evaluation.

**Interaction networks and complexes.** Protein–protein interaction prediction and docking methods use pairwise or complex-level information [4, 5]. The evidence does not specify whether the interaction labels were drawn from curated databases, high-throughput assays, structural complexes, or combinations of these sources [VERIFY]. Differences among these sources can affect both class balance and biological interpretation.

**Specialised biochemical datasets.** Metalloprotein prediction requires information about metal-binding proteins and their coordination environments [6]. The exact labels and dataset size are not available in the supplied record [VERIFY]. Similarly, studies of ligand discovery and molecular targets may use compound–protein associations, docking scores, biochemical assays, or in vivo outcomes [11, 12], but these inputs cannot be reconstructed from the titles alone.

### Evaluation metrics

The evidence supplied does not report enough detail to identify a consistent set of evaluation metrics across the protein-function literature. Accuracy, precision, recall, F1 score, area under the receiver-operating-characteristic curve, area under the precision–recall curve, calibration, top-\(k\) accuracy, and ranking-based measures are all plausible in this area, but their use by particular cited studies cannot be asserted without examining the full texts [VERIFY].

Metric choice should reflect the task. For multilabel protein-function annotation, micro- and macro-averaged measures may answer different questions because common functions can dominate aggregate results. For highly imbalanced interaction or activity prediction, precision–recall analysis may be more informative than receiver-operating-characteristic analysis. Ranking metrics are relevant when a method prioritises candidate functions or proteins rather than making a single categorical prediction. For structure-based models, evaluation may also involve comparisons with experimentally assigned functions or performance across sequence-identity thresholds, but the supplied evidence does not specify such analyses [VERIFY].

A particularly important issue is the construction of independent test sets. Randomly splitting related proteins can produce optimistic estimates because homologous sequences occur in both training and test partitions. Kapoor and Narayanan’s discussion of leakage and reproducibility in machine-learning science provides a general warning that is directly relevant to protein benchmarks [13]. In protein-function prediction, leakage may arise through sequence similarity, shared domains, duplicated annotations, structural templates, or indirect reuse of the same experimental information. The presence or absence of leakage controls in the cited protein studies is [VERIFY].

## Research Gaps

Several gaps are apparent from the available evidence.

First, there is a need for more transparent dataset reporting. Protein-function studies should state the source of sequences, structures, interactions, and labels; the date of database retrieval; redundancy filtering; taxonomic composition; and the criteria used to define positive and negative examples. Without these details, results are difficult to compare.

Second, benchmarks should test generalisation beyond close homologues. Performance on remote homologues, proteins from underrepresented organisms, novel folds, disordered proteins, and proteins with weak or conflicting annotations would provide a more meaningful assessment of biological utility. The supplied evidence does not show that these categories are treated consistently across studies [VERIFY].

Third, predicted structures require uncertainty-aware evaluation. Large predicted-structure resources expand coverage [10], but downstream models should distinguish confident structural information from uncertain regions and alternative conformations. It remains unclear how often structure-based function predictors are robust to these differences [VERIFY].

Fourth, functional annotation is inherently multilabel and hierarchical. A protein may participate in several molecular functions, biological processes, or cellular locations, and annotations may exist at different levels of specificity. Evaluation frameworks should therefore distinguish exact-label recovery from biologically acceptable partial or hierarchical matches. The records supplied do not establish whether the cited methods use a common ontology or hierarchical scoring system [VERIFY].

Fifth, interpretability and experimental validation remain uneven. Learned representations can identify predictive sequence or structural patterns, but a predictive feature is not necessarily a mechanistic determinant. The cited discovery studies include experimental or in vivo validation in their titles [11, 12], yet this type of validation is not equivalent to systematic validation of a general annotation model.

Finally, there is scope for integrating prior biological knowledge more explicitly. Work on informed machine learning surveys approaches for incorporating prior knowledge into learning systems [14]. For protein function, such knowledge may include structural constraints, biochemical rules, interaction networks, evolutionary relationships, and ontology structure. The challenge is to use prior information without introducing circularity or obscuring how much of the prediction comes from independent evidence.

## Limitations

This review is constrained by the supplied evidence. The corpus includes reviews, primary research papers, database articles, and studies whose main focus is not protein-function prediction. Several records concern clinical prediction, cancer biology, proteomics, or drug discovery rather than direct functional annotation [15–19]. They provide context for machine-learning use in biology but should not be treated as equivalent evidence.

More importantly, the available material consists largely of titles, bibliographic metadata, and selected article descriptions. Full methodological details, datasets, label definitions, baseline models, train–test splits, and numerical results are absent for many records. Accordingly, this review cannot make a reliable quantitative comparison of models or report a verified list of evaluation metrics for each study. Those details are marked [VERIFY] rather than inferred.

The evidence also does not support conclusions about which architecture is universally superior. Sequence models, graph networks, interaction models, and integrated workflows address different tasks and may be evaluated under incompatible conditions. Apparent differences in performance could reflect dataset composition, annotation quality, or test-set design rather than architectural advantages.

## Conclusion

Machine learning is being used in protein-function prediction through sequence language models, transformer-based methods, structural graph networks, interaction models, and integrated structure–ligand or structure–biology workflows [1–7]. Advances in protein structure prediction and large predicted-structure databases provide an important foundation for structure-aware annotation [8–10]. The field is consequently moving towards models that combine sequence, structure, interactions, and biochemical context rather than treating protein function as a property of sequence alone.

The central methodological weakness is not a lack of model variety but insufficiently comparable evidence. The supplied records do not allow the datasets, evaluation metrics, or leakage controls of most studies to be established with confidence. Future work should prioritise transparent dataset construction, homology-aware and leakage-resistant splits, multilabel and hierarchical evaluation, uncertainty-aware use of predicted structures, and experimental validation on genuinely novel proteins. These measures would make reported performance more interpretable and clarify how well machine-learning systems predict function beyond the boundaries of the data on which they were trained.

## References

1. Bordin N, Dallago C, Heinzinger M, Kim S, Littmann M, Rauer C, Steinegger M, Rost B. Novel machine learning approaches revolutionize protein knowledge. 2023. PMID: 36504138.

2. Tran VQ, Nemeth M, Bartie LJ, Chandrasekaran SS, Fanton A, Moon HC, Hie BL, Konermann S. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID: 41712694.

3. Gligorijević V, Renfrew PD, Kościółek T, Leman JK, Berenberg D, Vatanen T, Chandler C, Taylor BC. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.

4. Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID: 38987466.

5. Gao Z, Jiang C, Zhang J, Jiang X, Li L, Zhao P, Yang H, Huang Y. Hierarchical graph learning for protein-protein interaction. 2023. PMID: 36841846.

6. Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID: 35209064.

7. Zhang S, Huo D, Horne RI, Qi Y, Pujalte Ojeda S, Yan A, Vendruscolo M. Sequence-based virtual screening using transformers. 2025. PMID: 40721411.

8. Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O, Tunyasuvunakool K, Bates R, et al. Highly accurate protein structure prediction with AlphaFold. 2021. doi:10.1038/s41586-021-03819-2.

9. Abramson J, Adler J, Dunger J, Evans R, Green T, Pritzel A, Ronneberger O, Willmore L, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. 2024. doi:10.1038/s41586-024-07487-w.

10. Váradi M, Bertoni D, Magaña P, Paramval U, Pidruchna I, Radhakrishnan M, Tsenkov M, Nair S, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.

11. Yoo H, Han SJ, Lee JE, Cho C, Hong D, Jeong B, Kim S, Jung GY. Discovery of natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation. 2026. PMID: 40915561.

12. Wang S, Liu C, Ye D, Qi J, Xing Y, Wang J, Fan X, Li X. Deciphering the mechanism of baicalein in cervical cancer via bioinformatics, machine learning and computational simulations: PIM1 and CDK2 are key target proteins. 2025. PMID: 40339869.

13. Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.

14. von Rueden L, Mayer S, Beckh K, Georgiev B, Giesselbach S, Heese R, Kirsch B, Walczak M, et al. Informed Machine Learning—A Taxonomy and Survey of Integrating Prior Knowledge into Learning Systems. 2021. doi:10.1109/TKDE.2021.3079836.

15. Chen L, Li Q, Nasif KFA, Xie Y, Deng B, Niu S, Pouriyeh S, Dai Z. AI-Driven Deep Learning Techniques in Protein Structure Prediction. 2024. PMID: 39125995.

16. Schauperl M, Denny RA. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges. 2022. PMID: 35727311.

17. Odoemelam CS, Steuber V, Schmuker M. Computational modelling of olfactory receptors. 2025. PMID: 40441539.

18. Wu Z, Yu B, He Q, Huang C. LCN2 drives ferroptosis-associated ischemia-reperfusion injury after renal transplantation: integrated machine learning and in vivo validation. 2025. PMID: 41205031.

19. Vu DT, Sibran W, Metousis A, Vandewynckel L, Eraslan B, Goveas L, Itang EC, Deldycke C, et al. Multi-cohort, cross-species urinary proteomics reveals signatures of LRRK2 dysfunction in Parkinson's disease. 2026. PMID: 41611872.