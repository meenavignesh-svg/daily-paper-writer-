## Scope of the evidence

The supplied bibliography contains only a small number of papers directly concerned with protein-function prediction. The clearest primary study is Gligorijević et al. (2021), *Structure-based protein function prediction using graph convolutional networks*. Kulmanov and Hoehndorf (2025), *Computational prediction of protein functional annotations*, appears to be a directly relevant review. Bordin et al. (2023) and Yu et al. (2022) provide broader or specialised context.

Several other records concern adjacent problems rather than function prediction itself: AlphaFold and AlphaFold 3 predict structures or biomolecular interactions; protein–protein docking and interaction papers model molecular association; ProteinMPNN and protein-language-model studies address sequence design or directed evolution; and many of the clinical and cancer papers use proteins as biomarkers or therapeutic targets rather than predicting protein function. These distinctions matter because performance in structure prediction, docking, biomarker classification, or drug-response prediction cannot be treated as evidence of accurate functional annotation.

The bibliographic records alone do not establish the exact datasets, data-splitting procedures, baselines, or metrics used in the relevant studies. Those details require full-text verification [VERIFY].

## How machine learning is being used

### Sequence-based prediction

A major class of methods learns relationships between amino-acid sequences and functional labels. Traditional systems generally use engineered sequence features, such as composition, motifs, conservation, physicochemical properties, or similarity-derived profiles. More recent methods use learned representations from protein language models, in which large neural networks are pretrained on protein sequences and then adapted to downstream tasks such as functional classification [VERIFY].

The supplied evidence points to this broader transition through the review by Bordin et al. (2023), the sequence-based transformer paper by Zhang et al. (2025), and the protein-language-model work of Tran et al. (2026). However, the latter two papers appear to address virtual screening and directed evolution rather than standard functional annotation. Their relevance is therefore methodological rather than direct evidence for Gene Ontology or biochemical-function prediction [VERIFY].

Sequence models are attractive because they can be applied to proteins without experimentally determined structures. They may also capture remote evolutionary relationships that are difficult to identify using simple sequence similarity. Nevertheless, a model trained on densely annotated protein families may perform well partly because it recognises family membership, rather than because it has learned a mechanistic basis for function [VERIFY].

### Structure-based prediction

Gligorijević et al. (2021) provide the strongest direct evidence for a structure-based approach. Their method uses graph convolutional networks, representing proteins or their structural environments as graphs whose nodes and edges encode spatial relationships and molecular features. Such models can learn from three-dimensional arrangements of residues, potentially capturing active sites, binding pockets, interfaces, and other structural determinants of function.

The exact structural inputs—experimental structures, predicted structures, or both—are not identifiable from the supplied metadata and must be checked in the article [VERIFY]. The AlphaFold papers and the AlphaFold Protein Structure Database are relevant because they increase the availability of predicted structures. The database paper reports coverage of more than 214 million protein sequences, but that figure describes structural coverage, not the availability or reliability of functional labels. The confidence and suitability of these predicted structures for downstream functional inference also require verification [VERIFY].

Structure-based methods may be particularly useful for proteins whose sequences are divergent but whose folds or active-site geometries are conserved. Their limitations include dependence on structure quality, difficulty representing conformational flexibility, and the possibility that a correct global fold does not reveal the specific biochemical activity of a protein [VERIFY].

### Interaction- and network-informed prediction

Protein–protein interaction prediction and graph learning can provide indirect functional evidence. Gao et al. (2023), for example, use hierarchical graph learning for protein–protein interaction prediction. Interaction partners, complexes, and network neighbourhoods can be informative about cellular roles, pathway membership, or biological processes. However, an interaction prediction is not itself a functional annotation. It becomes evidence for function only when combined with an explicit downstream annotation task or a validated biological interpretation [VERIFY].

Similarly, the docking and AlphaFold 3 papers may support inference about binding interfaces or molecular interactions, but their primary outputs are structural or interaction-related. They should not be presented as direct benchmarks of protein-function prediction.

### Domain-specific and multimodal models

The review on metalloproteins suggests a specialised application in which models may predict metal-binding, coordination environments, catalytic properties, or metalloprotein classes. These tasks illustrate the value of incorporating domain knowledge and chemically meaningful structural features, but they may involve narrower labels and datasets than general protein-function annotation [VERIFY].

A broader direction is multimodal learning, combining sequence, structure, evolutionary profiles, protein–protein interactions, genomic context, expression data, and biochemical information. The supplied bibliography supports the general relevance of multi-omics machine learning, but the cited clinical multi-omics papers do not demonstrate multimodal protein-function prediction. The extent to which such integration improves functional annotation remains [VERIFY].

## Datasets and labels

The evidence does not identify the precise datasets used by the direct protein-function studies. A typical functional-annotation system would draw on some combination of:

- protein sequences from UniProt or related sequence repositories;
- Gene Ontology annotations for molecular function, biological process, and cellular component;
- experimentally determined or predicted structures from the Protein Data Bank and AlphaFold Database;
- evolutionary profiles and homologous sequences;
- protein–protein interaction databases;
- enzyme or ligand-binding databases; and
- specialised resources for metalloproteins or other protein classes.

These are plausible data sources for the field, but their use in the specific papers supplied here cannot be confirmed from the records and should be marked [VERIFY].

The choice and quality of labels are central. Protein-function annotations are often incomplete, unevenly distributed across species and protein families, and supported by different levels of experimental evidence. Gene Ontology terms are hierarchical and multilabel: a protein may have several molecular functions and biological processes, and some labels are much more specific than others. A model can therefore appear successful by predicting broad parent terms while failing on the precise function of biological interest [VERIFY].

A further concern is redundancy. Closely related proteins may occur in both training and test sets, allowing a model to exploit homology rather than generalise to genuinely novel proteins. The supplied paper on leakage and reproducibility is not protein-specific, but it highlights why sequence clustering, family-level splits, and temporally separated test sets are important. Whether the direct studies used these safeguards must be checked [VERIFY].

## Evaluation metrics

The bibliography does not report the evaluation metrics for the function-prediction studies. For multilabel protein annotation, appropriate evaluation commonly includes precision, recall, F1 score, and area under the precision–recall curve, often calculated per protein, per functional term, or across ontology levels [VERIFY]. Because functional labels are highly imbalanced, precision–recall measures are generally more informative than accuracy alone [VERIFY].

Other measures that may be relevant include:

- ROC-AUC, although it can be misleading under severe class imbalance;
- maximum F-measure, often used to summarise threshold-dependent annotation performance;
- coverage or the proportion of proteins receiving useful predictions;
- performance stratified by Gene Ontology depth or annotation frequency;
- performance on proteins with low sequence identity to the training data;
- calibration and confidence estimates; and
- top-\(k\) accuracy or ranking metrics where the model returns a prioritised list of functions.

For structure-based models, evaluation may also include comparisons against sequence-only baselines, homology-based annotation, existing annotation tools, or ablation tests that remove structural features. Whether Gligorijević et al. used these comparisons, and which metrics they reported, requires full-text verification [VERIFY].

A convincing evaluation should therefore report more than a single aggregate score. It should test performance under homology-reduced splits, distinguish experimentally supported from computationally inferred labels, and assess whether predictions remain reliable for underrepresented protein families. The supplied evidence does not show that all of these requirements were met [VERIFY].

## Persistent limitations

Several limitations are likely to remain important across the field.

First, the labels are not a complete ground truth. Unannotated proteins are not necessarily non-functional, and missing or incorrect annotations can make a correct prediction appear to be a false positive. Annotation bias toward well-studied organisms and protein families can also make benchmark results optimistic [VERIFY].

Second, data leakage and homologous-sequence overlap can inflate performance. Random splits are particularly problematic when close relatives are distributed across training and test sets. The general leakage literature supports this concern, but its magnitude in each protein-function paper must be assessed directly [VERIFY].

Third, class imbalance and ontology structure complicate interpretation. Common broad terms have abundant examples, whereas rare, specific functions may have too few labels for reliable supervised learning. A model may consequently favour frequent annotations and provide limited help for genuinely novel proteins [VERIFY].

Fourth, generalisation remains uncertain. A model trained on proteins from common model organisms, well-characterised families, or particular experimental conditions may perform poorly on proteins from distant taxa, disordered proteins, membrane proteins, or proteins with context-dependent functions [VERIFY]. Performance on a held-out random test set therefore does not necessarily indicate readiness for discovery use.

Fifth, structural information is not equivalent to functional information. AlphaFold-scale structure prediction makes structural features available, but function can depend on dynamics, ligand state, post-translational modification, cellular localisation, oligomerisation, and environmental conditions. Predicted structures may also contain local errors in exactly the regions—active sites, interfaces, or flexible loops—that matter most for function [VERIFY].

Finally, many high-capacity models remain difficult to interpret. Attention maps, saliency scores, or SHAP-like explanations can identify influential residues, but they do not by themselves establish a causal mechanism. Experimental validation is still needed to determine whether a predicted active site, interaction, or annotation is biologically correct.

## Overall assessment

Machine learning is being used in protein-function prediction mainly through sequence representation learning, structure-based graph models, and, increasingly, combinations of sequence, structure, evolutionary, and interaction information. The direct evidence in this bibliography most clearly supports graph-based structural prediction and the broader movement toward learned protein representations. Large structure databases and protein language models are expanding the available inputs, but several cited papers concern neighbouring tasks rather than function prediction itself.

The most important unresolved issues are not simply model architecture. They are the quality and completeness of functional labels, prevention of homology leakage, evaluation on genuinely novel proteins, treatment of multilabel and hierarchical annotations, calibration of confidence, and experimental validation. Exact claims about datasets and reported scores cannot be made responsibly from the supplied bibliographic records alone [VERIFY].