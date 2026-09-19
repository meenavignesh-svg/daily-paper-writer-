# Title

**Artificial Intelligence and Machine Learning in Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations**

## Abstract

Machine-learning methods are increasingly used to infer protein function from amino-acid sequence, three-dimensional structure, molecular interactions, and related biological data. The supplied literature indicates three particularly important directions: sequence-based representation learning, structure-based graph learning, and the use of interaction or network information as an additional source of functional evidence. Structure-based protein-function prediction using graph convolutional networks provides the clearest direct example in this set [1], while broader reviews describe the expanding role of machine learning across protein science [2,3]. Protein structure predictors such as AlphaFold and AlphaFold 3 are relevant because they can provide structural inputs for downstream functional inference, although structure prediction is not itself equivalent to function prediction [4,5].  

The evidence base is insufficient to establish which datasets, annotation schemes, model configurations, or performance values were used in most of the cited studies. Functional prediction is generally a multilabel and hierarchical problem, for which precision, recall, F1 score, precision–recall analysis, ranking measures, and ontology-aware metrics may be appropriate; the exact metrics reported in the directly relevant studies require verification. Major unresolved issues include annotation incompleteness, homology and data leakage, limited experimental validation, uncertainty in predicted structures, class imbalance, and poor evaluation on genuinely novel protein families.

## Introduction

Protein function prediction seeks to infer what a protein does from available molecular evidence. Depending on the task, this may involve assigning functional ontology terms, identifying enzyme activities, predicting binding or metal-coordination properties, inferring cellular roles, or estimating the consequences of sequence variation. These tasks differ in their inputs and labels, and they should not be treated as interchangeable.

Machine learning is attractive in this setting because proteins can be represented in several complementary ways. A sequence can be treated as an ordered string of amino acids; a structure can be represented as a spatial graph; and interaction partners can be modelled as part of a biological network. Recent work also uses large-scale representation learning, including protein language models, to extract patterns from sequence collections before supervised functional annotation is attempted [2,6]. The field therefore encompasses both conventional supervised learning and newer deep-learning approaches.

The evidence supplied for this review is heterogeneous. Only a small subset of the records directly concerns protein-function prediction. The most directly relevant primary study is Gligorijević et al., which uses graph convolutional networks for structure-based function prediction [1]. Bordin et al. provide a broader account of machine learning in protein science [2], and Yu et al. discuss machine-learning approaches for metalloproteins [3]. Other records address protein structure prediction, protein–protein interaction modelling, sequence design, virtual screening, or disease-related prediction. These studies help define the surrounding technical landscape, but they do not by themselves establish performance for protein-function annotation.

## Evidence Synthesis

### Sequence-based learning

Sequence-based prediction uses amino-acid sequences as the principal input. Earlier approaches may rely on motifs, physicochemical descriptors, evolutionary profiles, or similarity-derived features. More recent methods use protein language models, which learn distributed sequence representations from large collections of proteins. The supplied literature identifies protein language models as an important direction in protein engineering and protein science, including their use in modelling epistatic interactions [6]. Bordin et al. likewise describe the broader expansion of machine learning in protein-related analysis [2].

These representations can support several forms of functional inference. A model may predict functional labels directly, classify enzyme or binding properties, identify sequence features associated with localization, or transfer information from annotated proteins to less-characterized sequences. However, the supplied records do not specify which protein language models, training corpora, annotation databases, or downstream classifiers were used in the relevant studies [VERIFY].

A central advantage of sequence-based methods is their applicability to proteins for which no experimentally determined structure is available. Their limitation is that sequence similarity and learned statistical associations do not necessarily establish biochemical mechanism. Closely related proteins can have different substrate preferences or regulatory roles, while remote homologues may retain a common function despite substantial sequence divergence. These issues make the definition of appropriate test sets particularly important.

### Structure-based learning

Structure-based prediction represents a protein using spatial information. In graph-based formulations, residues or atoms may be represented as nodes, with edges encoding physical proximity, chemical contacts, or other relationships. Graph convolutional networks can then learn associations between structural patterns and functional annotations. This is the central approach described by Gligorijević et al. [1].

Structure-based learning is useful because proteins with limited sequence similarity may nevertheless share folds, active-site arrangements, or interaction surfaces. In principle, these structural similarities can provide functional evidence that sequence-only models miss. The success of such methods depends on the quality of the structural representation and on whether the available structure reflects the biologically relevant conformation. The supplied evidence does not provide sufficient detail to determine which structural datasets, graph definitions, functional labels, or comparative baselines were used in [1].

AlphaFold and AlphaFold 3 are important enabling technologies in this context [4,5]. Their primary outputs are predicted structures or biomolecular complexes, not functional annotations. The AlphaFold Protein Structure Database further increases the availability of predicted structural representations for proteins lacking experimentally determined structures [7]. These resources may therefore expand the scope of structure-based functional prediction, but predicted structures should not be assumed to have the same evidential status as experimentally observed structures.

### Interaction and network-based inference

Protein–protein interaction models provide another possible route to function prediction. A protein’s interaction partners, complex membership, or position within a network may contain information about its cellular role. Hierarchical graph learning and machine-learning approaches to protein–protein docking illustrate the broader development of models for molecular interactions [8,9].

Interaction prediction and function prediction remain distinct tasks. An interaction model may provide features for downstream annotation, but the supplied evidence does not demonstrate that the cited interaction studies evaluated functional prediction as an endpoint [VERIFY]. Interaction databases are also incomplete and context-dependent. Experimental conditions, tissue or cell type, subcellular localization, and molecular state can all influence whether an interaction is observed. Functional models that depend on interaction information may therefore inherit errors or biases from the underlying network.

### Integrated and application-specific approaches

A broader trend is the integration of sequence, structure, interaction, evolutionary, biochemical, and omics information. Informed machine learning provides a general framework for incorporating prior biological knowledge into predictive systems [10], while reviews of multi-omics machine learning describe strategies for combining heterogeneous molecular measurements [11]. Such approaches are potentially relevant to protein-function inference, particularly where function depends on cellular context.

Nevertheless, several records in the supplied bibliography use machine learning to predict disease subtypes, treatment response, mortality, or therapeutic efficacy rather than protein function [12–15]. They should not be treated as direct evidence for the question considered here. Their relevance is methodological: they illustrate the broader use of supervised learning with biological measurements, but they do not establish how well a model predicts molecular function.

## Methods and Datasets Observed

The evidence set consists primarily of bibliographic records from PubMed and OpenAlex, supplemented by an analytical summary of the directly relevant literature. It does not provide a systematic extraction of experimental methods from every full text. Accordingly, the following account distinguishes between datasets and metrics identified directly in the supplied evidence and those that are plausible for this research area but require verification.

The clearest directly relevant methodological record is the structure-based graph convolutional network study by Gligorijević et al. [1]. The title establishes the use of structural information and graph convolutional networks, but the supplied material does not report the precise source of structures, the functional annotation scheme, the train–test split, or the evaluation results [VERIFY].

Potential data sources for protein-function prediction include:

- **Protein sequences**, used either directly by sequence classifiers or as pretraining material for protein language models [2,6].
- **Curated functional annotations**, including Gene Ontology terms or other biochemical and cellular labels [VERIFY].
- **Experimental structures**, for example structures deposited in structural repositories [VERIFY].
- **Predicted structures**, including those available through the AlphaFold Protein Structure Database [7].
- **Interaction and network data**, which may be used as input features or as a separate prediction target [8,9].
- **Evolutionary information**, such as alignments, profiles, or coevolutionary features [VERIFY].
- **Biochemical and multi-omics measurements**, potentially used in multimodal models, although their use for direct protein-function prediction is not established by the supplied records [VERIFY].

Functional annotation is commonly a multilabel problem: a single protein can possess several molecular functions, participate in multiple biological processes, and occupy more than one cellular context. It is also hierarchical when ontology terms are used, because broad terms and more specific descendants are related. These properties make evaluation more complicated than ordinary binary classification.

Relevant metrics include precision, recall, and F1 score; area under the precision–recall curve; area under the receiver-operating-characteristic curve; threshold-dependent maximum F-measure; and ranking-based measures. Ontology-aware metrics, including semantic-distance or Smin-type measures, may also be appropriate [VERIFY]. For rare functional categories, precision–recall analysis is generally more informative than a metric that can remain high under severe class imbalance [VERIFY]. Exact metric selection should reflect whether the model is being used for binary annotation, multilabel classification, ranking of candidate functions, or hierarchical ontology completion.

A credible evaluation should also report how related proteins were separated between training and testing. Random splits can produce optimistic results when homologous sequences occur in both partitions. Kapoor and Narayanan’s discussion of leakage and reproducibility is not specific to protein prediction, but it highlights why apparently strong machine-learning performance may not generalize to independent data [16]. Family-disjoint, sequence-disjoint, or temporally separated evaluations may therefore be more informative than random partitioning alone [VERIFY].

## Research Gaps

Several gaps remain evident from the supplied literature.

First, the connection between predicted structure and predicted function requires more careful validation. Structural coverage has expanded substantially through resources such as the AlphaFold Protein Structure Database [7], but a predicted fold does not guarantee that active sites, conformational states, disorder, or interaction interfaces are represented accurately enough for functional inference.

Second, evaluation protocols need to distinguish interpolation from genuine discovery. A model may perform well when test proteins are close homologues of training proteins but fail on new families, unusual domains, or proteins with sparse annotation. The field would benefit from more consistent use of family-disjoint and temporally controlled benchmarks [VERIFY].

Third, functional labels themselves are incomplete, unevenly distributed, and partly dependent on prior computational annotation. This creates uncertainty about what constitutes a correct prediction and may reinforce existing annotation biases. The supplied evidence does not allow the extent of these problems to be quantified for the cited studies [VERIFY].

Fourth, model interpretability remains an important practical issue. A prediction is more useful to experimental biologists when it is accompanied by evidence about the residues, structural regions, motifs, or interactions driving the result. General work on explaining machine-learning predictions, including SHAP-based approaches, is relevant in principle [17], but the supplied records do not show how interpretability was implemented in the protein-function studies [VERIFY].

Finally, prediction should be connected more consistently to experimental testing. The distinction between a statistically plausible annotation and a demonstrated biochemical function remains fundamental. The available bibliography contains evidence of machine learning in protein engineering, structure prediction, and molecular modelling, but it does not establish a uniform standard for prospective experimental validation.

## Limitations

The main limitation of this review is the restricted and uneven evidence base. The bibliography contains only a small number of records directly addressing protein-function prediction, and much of the available information consists of titles, abstracts-level metadata, and broad analytical summaries rather than extracted full-text methods and results. Exact datasets, model architectures, preprocessing steps, baselines, and performance values therefore cannot be reported reliably for most studies.

The review also draws on adjacent topics, including protein structure prediction, protein–protein interaction modelling, protein design, virtual screening, and clinical machine learning. These areas are relevant to the technological context but are not equivalent to protein-function prediction. Their inclusion should not be interpreted as evidence that they solved the target task.

Several statements about commonly used datasets and metrics are presented as methodological possibilities rather than observations from the cited papers. They are marked [VERIFY] where the supplied evidence does not establish that a particular dataset, label system, or metric was used. The review also does not provide a formal systematic-search protocol, risk-of-bias assessment, or quantitative meta-analysis.

## Conclusion

Machine learning is being used to predict protein function through sequence representations, structural graphs, interaction networks, and, increasingly, combinations of these information sources. The strongest direct evidence in the supplied set concerns structure-based graph convolutional networks [1], while broader reviews place this work within a rapidly developing protein-machine-learning landscape [2,3]. Protein language models may improve sequence representation, and predicted structures from AlphaFold-related resources may make structure-based inference possible for proteins without experimental structures [4,5,7].

The central methodological challenge is not simply choosing a more powerful model. It is constructing reliable labels, preventing homology and annotation leakage, evaluating rare and hierarchical functions appropriately, and testing performance on proteins that are genuinely novel. The supplied evidence does not support firm conclusions about comparative accuracy or the superiority of any particular architecture. Progress will depend on transparent datasets, family-aware benchmarks, calibrated uncertainty, interpretable predictions, and experimental validation of proposed functions.

## References

1. Gligorijević V, Renfrew PD, Kościółek T, et al. Structure-based protein function prediction using graph convolutional networks. 2021. doi:10.1038/s41467-021-23303-9.

2. Bordin N, Dallago C, Heinzinger M, et al. Novel machine learning approaches revolutionize protein knowledge. 2023. PMID:36504138.

3. Yu Y, Wang R, Teo RD. Machine Learning Approaches for Metalloproteins. 2022. PMID:35209064.

4. Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. 2021. doi:10.1038/s41586-021-03819-2.

5. Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. 2024. doi:10.1038/s41586-024-07487-w.

6. Tran VQ, Nemeth M, Bartie LJ, et al. Rapid directed evolution guided by protein language models and epistatic interactions. 2026. PMID:41712694.

7. Váradi M, Bertoni D, Magaña P, et al. AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences. 2023. doi:10.1093/nar/gkad1011.

8. Gao Z, Jiang C, Zhang J, et al. Hierarchical graph learning for protein-protein interaction. 2023. PMID:36841846.

9. Michalik I, Kuder KJ. Machine Learning Methods in Protein-Protein Docking. 2024. PMID:38987466.

10. von Rueden L, Mayer S, Beckh K, et al. Informed Machine Learning—A Taxonomy and Survey of Integrating Prior Knowledge into Learning Systems. 2021. doi:10.1109/TKDE.2021.3079836.

11. Reel PS, Reel S, Pearson ER, et al. Using machine learning approaches for multi-omics data analysis: A review. 2021. doi:10.1016/j.biotechadv.2021.107739.

12. Zhang Y, Sun L, Liu H, et al. Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF Using Olink-Derived Inflammatory Protein Signatures. 2025. PMID:41255250.

13. Li J, Chen A, Liu Z, et al. Machine learning driven prediction of drug efficacy in lung cancer: based on protein biomarkers and clinical features. 2025. PMID:40355026.

14. Li J, Sugimoto E, Yamamoto K, et al. Machine Learning-Based Predictive Modeling Maximizes the Efficacy of mTOR/p53 Co-Targeting Therapy Against AML. 2025. PMID:40785506.

15. Pang Y, Luo C, Zhang Q, et al. Multi-Omics Integration With Machine Learning Identified Early Diabetic Retinopathy, Diabetic Macula Edema and Anti-VEGF Treatment Response. 2024. PMID:39671223.

16. Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. 2023. doi:10.1016/j.patter.2023.100804.

17. Ponce Bobadilla AV, Schmitt V, Maier CS, et al. Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development. 2024. doi:10.1111/cts.70056.