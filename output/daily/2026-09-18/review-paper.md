# Title

**Machine Learning for Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations**

## Abstract

Machine learning is increasingly used to infer protein function from amino-acid sequence, three-dimensional structure, evolutionary context, molecular interactions, and, in some settings, integrated biological data. The supplied literature indicates three main directions: sequence-based models, structure-based graph methods, and approaches that incorporate interaction or domain-specific information. Among the records reviewed, the clearest direct study is a graph-convolutional approach to structure-based protein-function prediction [1], complemented by a recent review of computational functional annotation [2]. Other papers address related but distinct problems, including protein structure prediction, protein–protein interaction prediction, sequence-based virtual screening, protein design, and directed evolution [3–8]. These studies are relevant to the development of representations and modelling strategies, but they should not be treated as direct evidence of functional-annotation performance.

The evidence supplied does not establish the precise datasets, label schemes, data-splitting procedures, baselines, or evaluation metrics used in the direct function-prediction studies. These details require full-text verification [VERIFY]. More generally, important limitations include incomplete and uneven functional annotations, class imbalance, redundancy between training and test proteins, dependence on structure quality, limited interpretability, and uncertain generalisation to evolutionarily distant proteins. Machine learning has therefore expanded the scale and sophistication of functional inference, but reliable evaluation still depends on carefully designed benchmarks and experimental validation.

## Introduction

Protein-function prediction is a central problem in computational biology. Experimental characterisation remains slower and more expensive than the accumulation of protein sequences, making computational annotation an important means of prioritising candidates for further study. Machine-learning methods are being applied not only to assign broad functional categories, but also to infer molecular activities, biological processes, cellular localisation, interactions, binding properties, and specialised biochemical features.

The field is heterogeneous, however. Protein structure prediction, protein–protein interaction prediction, molecular docking, drug-response prediction, and biomarker classification are adjacent tasks rather than interchangeable forms of protein-function prediction. For example, AlphaFold and AlphaFold 3 address structure and biomolecular interaction prediction [9,10], while other studies use proteins as biomarkers or therapeutic targets in clinical and cancer settings [11–14]. Their results may contribute useful inputs or biological context, but performance on these tasks cannot be interpreted as evidence that a model accurately assigns protein functional annotations.

The directly relevant evidence in the supplied bibliography is limited. Gligorijević et al. describe a structure-based graph convolutional approach [1], and Kulmanov and Hoehndorf review computational prediction of protein functional annotations [2]. Bordin et al. discuss broader developments in machine learning for protein science [15], while Yu et al. focus on metalloproteins [16]. Taken together, these records support a view of protein-function prediction as a developing area that combines learned representations with biological structure and prior knowledge. They do not, on their own, provide a complete comparison of contemporary methods.

## Evidence Synthesis

### Sequence-based prediction

Sequence-based methods learn associations between amino-acid sequences and functional labels. Earlier approaches commonly relied on engineered descriptors, motifs, residue composition, physicochemical properties, conservation, or similarity-derived profiles. More recent systems use neural representations learned from large collections of protein sequences. Protein language models are a prominent example: they are trained on sequences and subsequently adapted to downstream prediction tasks [15]. The supplied literature also includes a transformer-based study of sequence-based virtual screening [6] and a protein-language-model study of directed evolution [7]. These papers are methodologically relevant because they illustrate the use of learned sequence representations, but their primary objectives are not standard functional annotation [VERIFY].

Sequence models are attractive because they do not require an experimentally determined structure. They can also be applied to proteins for which structural information is unavailable or uncertain. In principle, learned representations may capture evolutionary relationships that are not apparent from simple sequence identity. A central concern, however, is whether a model has learned general biochemical principles or is primarily recognising membership in a protein family. If related proteins are present in both training and test sets, apparent performance may reflect homology rather than generalisation to novel proteins [VERIFY].

### Structure-based prediction

The strongest direct example in the supplied evidence is the structure-based graph convolutional network of Gligorijević et al. [1]. In this framework, protein structure is represented as a graph, allowing the model to use relationships between residues or structural environments. Graph-based representations are well suited to proteins because spatial proximity, residue neighbourhoods, and local molecular geometry can be encoded explicitly. Such information may help identify structural features associated with active sites, binding pockets, interfaces, or other determinants of function.

The precise structural inputs used in the study—whether experimental structures, predicted structures, or both—cannot be established from the supplied record [VERIFY]. The relevance of predicted structures has nevertheless increased substantially with the development of AlphaFold [9] and the expansion of the AlphaFold Protein Structure Database. The database record reports structural coverage for more than 214 million protein sequences [17]. This is important for the availability of structural representations, but it should not be confused with equivalent coverage of experimentally supported functional labels. Nor does a predicted structure guarantee that the relevant active site, conformational state, or interaction geometry is represented accurately [VERIFY].

Structure-based methods may be particularly useful when proteins have diverged in sequence while retaining similar folds or functional sites. Their limitations include dependence on structural quality, the representation of conformational flexibility, and the difficulty of distinguishing proteins with similar global folds but different biochemical activities. A structurally plausible model may therefore provide useful evidence without resolving function conclusively [VERIFY].

### Interaction- and network-informed prediction

Protein interactions provide another source of functional information. Hierarchical graph learning has been applied to protein–protein interaction prediction [18]. Interaction partners, complexes, and network neighbourhoods can be informative about cellular roles and pathway membership. Nonetheless, predicting an interaction is not equivalent to predicting protein function. It becomes functional evidence only when incorporated into an explicit annotation task or supported by a validated biological interpretation [VERIFY].

The same distinction applies to docking and biomolecular-complex modelling. Machine-learning approaches to protein–protein docking [19] and AlphaFold 3 [10] may improve predictions of molecular associations, but their outputs are not direct measures of Gene Ontology annotation or biochemical-function prediction. They are best understood as complementary sources of structural or relational evidence.

### Specialised and multimodal approaches

Specialised models may target narrower functional questions, such as metal binding, coordination environments, or catalytic properties in metalloproteins. The review by Yu et al. illustrates this domain-specific direction [16]. Such models can use chemically meaningful features and may benefit from focusing on a more constrained biological problem. Their results may not transfer directly to broad, multilabel annotation across the entire proteome [VERIFY].

A further direction is multimodal learning, in which sequence, structure, evolutionary profiles, interactions, genomic context, expression, and biochemical measurements are combined. The supplied bibliography supports the wider relevance of machine learning for multi-omics analysis [20], but the cited multi-omics studies largely concern clinical prediction rather than protein-function annotation. Consequently, the extent to which multimodal integration improves protein-function prediction remains [VERIFY].

## Methods and Datasets Observed

This review is based on the supplied bibliography and accompanying evidence synthesis. The records were assessed for direct relevance to protein-function prediction and separated from studies addressing neighbouring tasks. The most directly relevant records were the structure-based graph-convolutional study [1], the review of computational functional annotation [2], the broader protein-machine-learning review [15], and the metalloprotein review [16]. Records on structure prediction, interaction prediction, protein design, virtual screening, directed evolution, and clinical or cancer prediction were treated as contextual rather than direct evidence [3–14,18,19].

The bibliography does not provide sufficient information to identify the exact datasets used in the direct function-prediction studies. In this field, plausible data sources include protein sequence repositories, Gene Ontology annotations, structural databases such as the Protein Data Bank and AlphaFold Database, evolutionary profiles, protein–protein interaction resources, enzyme databases, ligand-binding resources, and specialised metalloprotein datasets. Their use in particular studies cannot be confirmed from the supplied records and should be checked in the full texts [VERIFY].

The labels themselves present a substantial methodological issue. Protein-function annotations are commonly multilabel and hierarchical: one protein may have several molecular functions, biological processes, and cellular components, while terms differ considerably in specificity. An evaluation that rewards prediction of broad parent terms may therefore obscure poor performance on specific functions of practical interest [VERIFY]. Functional annotations also vary in evidential support and are unevenly distributed across taxa and protein families.

The supplied evidence does not report the exact metrics used by the direct studies. For multilabel annotation, relevant measures commonly include precision, recall, F1 score, and area under the precision–recall curve, assessed per protein, per functional term, or across ontology levels [VERIFY]. Because functional labels are typically imbalanced, precision–recall-based measures are often more informative than accuracy alone [VERIFY]. Calibration, ranking quality, and performance on rare or previously unseen functions may also be important, although their use in the identified papers cannot be established here [VERIFY].

## Research Gaps

Several gaps emerge from the available evidence.

First, there is a need for clearer separation between functional annotation and related prediction tasks. Structure prediction, docking, interaction prediction, virtual screening, and protein design can support functional inference, but they should be evaluated with task-specific benchmarks rather than presented as direct evidence of annotation accuracy.

Second, benchmark design requires greater attention to biological redundancy. Random protein-level splits may place closely related sequences or members of the same family in both training and test sets. In that situation, performance can be inflated by homology leakage. Family-level clustering, remote-homology splits, and temporally separated test sets would provide more demanding tests of generalisation, although whether the direct studies used these procedures remains [VERIFY]. The broader literature on leakage and reproducibility underscores the importance of this issue [21].

Third, the field would benefit from better characterisation of label quality. Functional databases contain incomplete annotations, uneven experimental support, and hierarchical dependencies. Evaluation should distinguish performance on experimentally supported labels from performance on computationally transferred annotations, and should report how results vary with annotation specificity [VERIFY].

Fourth, the contribution of different information sources remains insufficiently resolved. Sequence, structure, interaction networks, and biochemical context may be complementary, but comparisons must determine whether additional modalities improve prediction beyond a strong sequence baseline. This is particularly important now that predicted structures are available at unprecedented scale [17].

Finally, successful computational predictions require biological validation. A high-scoring annotation is a hypothesis, not necessarily a demonstrated molecular mechanism. The supplied evidence does not allow the extent of experimental validation in the direct studies to be determined [VERIFY].

## Limitations

The principal limitation of this review is the restricted evidence base. Only a small subset of the supplied records directly addresses protein-function prediction, and the available information consists largely of bibliographic records and a high-level analysis rather than verified full-text extraction. Exact datasets, model architectures, baselines, split strategies, and evaluation metrics are therefore unavailable in several cases [VERIFY].

The evidence also spans different publication years and research objectives. Some records concern methods published up to 2026, while others provide earlier foundations. The resulting synthesis is descriptive rather than a formal quantitative comparison. It would be inappropriate to rank the methods or claim that one representation is superior on the basis of the supplied records alone.

A further limitation is that several potentially informative studies concern adjacent applications. Their inclusion provides context for sequence models, structural modelling, interactions, and machine learning more generally, but it cannot substitute for direct evidence on functional annotation. Finally, the review does not independently verify the quality, completeness, or experimental status of any functional labels or benchmark datasets.

## Conclusion

Machine learning is being used to predict protein function through several complementary strategies. Sequence-based models learn from amino-acid representations and increasingly draw on protein language models. Structure-based methods, including graph convolutional networks, represent spatial relationships between residues and structural environments [1]. Interaction- and network-informed approaches add relational context, while specialised models target narrower biochemical problems such as metalloprotein function [16]. Predicted structures from resources such as AlphaFold may make structure-aware inference more broadly applicable, but structural coverage should not be mistaken for functional certainty [9,17].

The available evidence does not establish a single standard dataset or evaluation protocol. Protein sequence repositories, ontology annotations, structural databases, interaction resources, and specialised biochemical datasets are plausible components of current workflows, but their use in individual studies requires verification. Likewise, commonly appropriate metrics for multilabel prediction include precision, recall, F1, and precision–recall area, yet the exact metrics used in the relevant papers are not documented in the supplied material [VERIFY].

The remaining challenge is not simply to build larger models. It is to evaluate them against biologically difficult and leakage-resistant benchmarks, account for incomplete and hierarchical labels, quantify uncertainty, and demonstrate that predictions transfer to experimentally novel proteins. Until those requirements are met consistently, machine learning should be viewed as a powerful system for prioritising functional hypotheses rather than a replacement for biological validation.

## References

1. Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.  
2. Kulmanov M, Hoehndorf R. Computational prediction of protein functional annotations. 2025. PMID:40728605.  
3. Chen L, Li Q, Nasif KFA, et al. AI-Driven Deep Learning Techniques in Protein Structure Prediction. 2024. PMID:39125995.  
4. Schauperl M, Denny RA. AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges. 2022. PMID:35727311.  
5. Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. 2024. doi:10.1038/s41586-024-07487-w.  
6. Zhang S, Huo D, Horne RI, et al. Sequence-based virtual screening using transformers. 2025. PMID:40721411.  
7. Tran VQ, Nemeth M, Bartie LJ, et al. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID:41712694.  
8. Dauparas J, Anishchenko I, Bennett NR, et al. Robust deep learning–based protein sequence design using ProteinMPNN. 2022. doi:10.1126/science.add2187.  
9. Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. 2021. doi:10.1038/s41586-021-03819-2.  
10. Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.  
11. Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID:35209064.  
12. Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein-protein interaction. 2023. PMID:36841846.  
13. Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID:38987466.  
14. Bordin N, Dallago C, Heinzinger M, et al. Novel machine learning approaches revolutionize protein knowledge. 2023. PMID:36504138.  
15. Reel PS, Reel S, Pearson ER, et al. Using machine learning approaches for multi-omics data analysis: A review. 2021. doi:10.1016/j.biotechadv.2021.107739.  
16. Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.