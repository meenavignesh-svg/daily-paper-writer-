# Title

**Artificial Intelligence and Machine Learning in Protein Function Prediction: Methods, Datasets, Evaluation, and Remaining Limitations**

## Abstract

Machine-learning methods are increasingly used to infer protein properties from sequence, structure, interaction networks, and experimentally measured biological data. The supplied literature includes work on protein structure prediction, metalloproteins, protein–protein docking, interaction prediction, protein language models, sequence-based virtual screening, and computational modelling of olfactory receptors [1, 6, 10, 11, 14, 15, 17, 18]. It also contains several studies in which proteins serve as biomarkers, therapeutic targets, or features in disease-prediction models rather than as the direct object of function prediction [2, 4, 5, 7–9, 12, 13, 16, 19, 20]. Across the records provided, machine learning is therefore being applied across a broad continuum: from predicting structural or interaction-related properties to prioritising candidate proteins and compounds in biomedical settings. However, the supplied evidence does not provide sufficient information about the exact datasets, train–test designs, performance metrics, or validation procedures used in most studies. These details should be retrieved from the full texts [VERIFY]. The main limitations evident from the literature set are conceptual heterogeneity, incomplete reporting in the available records, potential dependence on biased biological databases, limited experimental validation, and uncertainty about how well models generalise to proteins, organisms, and functions that are poorly represented in training data.

## Introduction

Protein function prediction traditionally draws on sequence similarity, structural homology, evolutionary conservation, domain architecture, interaction data, and experimental annotation. Machine-learning methods extend these approaches by learning statistical relationships between protein representations and labelled functional outcomes. Depending on the task, the input may be an amino-acid sequence, a predicted or experimentally determined structure, a protein–protein interaction graph, a molecular descriptor, or a combination of omics measurements.

The supplied literature illustrates the breadth of this field but also its uneven boundaries. Some records address protein structure prediction directly [1, 10], while others focus on protein–protein interactions or docking [11, 14]. A separate group concerns metalloproteins, for which function is closely related to metal coordination and active-site context [6]. Protein language models and transformer-based methods appear in studies of protein knowledge, directed evolution, and sequence-based virtual screening [3, 15, 18]. These approaches are relevant to function prediction because they attempt to encode information from protein sequences or use learned representations to infer biochemical or interaction-related properties.

Other papers use machine learning in biomedical studies where proteins are predictors, biomarkers, or therapeutic targets. Examples include models involving inflammatory protein signatures, protein biomarkers and clinical features, disease-associated genes or proteins, and computationally prioritised drug targets [4, 5, 7–9, 12, 13, 16, 19, 20]. Such studies may contribute indirectly to functional interpretation, but their primary prediction targets are often disease outcomes, treatment response, drug efficacy, or candidate compounds rather than protein function itself. This distinction is important when synthesising the field.

## Evidence Synthesis

### Sequence and language-model-based prediction

Protein language models provide one route to learning representations directly from amino-acid sequences. The literature list includes a broad discussion of machine-learning approaches to protein knowledge [18], a study of rapid directed evolution guided by protein language models and epistatic interactions [3], and work on sequence-based virtual screening using transformers [15]. Together, these records suggest that sequence models are being used not only to assign functional labels but also to estimate sequence plausibility, capture evolutionary or epistatic relationships, and prioritise sequences or compounds for further testing.

The available evidence does not specify which language-model architectures, pretraining databases, downstream prediction tasks, or validation metrics were used in these studies [VERIFY]. It is therefore not possible to determine from the supplied material whether performance was assessed through sequence-level classification, regression, ranking, held-out mutational fitness, biochemical assays, or another framework. The distinction matters because a model that predicts evolutionary plausibility is not necessarily a model that predicts a particular molecular function.

### Structure-based and interaction-related prediction

Protein structure prediction is represented by a review of AI-driven deep-learning techniques [1] and a review of AI-based structure prediction in drug discovery [10]. Structural information can support function prediction by revealing folds, active-site geometry, ligand-binding pockets, oligomeric interfaces, or conformational features. Nevertheless, structure prediction and function prediction are related but distinct tasks. A highly accurate structural model does not automatically establish the biochemical activity of the corresponding protein.

Protein–protein docking and interaction prediction form another important area. The supplied records include a review of machine-learning methods in protein–protein docking [11] and a study describing hierarchical graph learning for protein–protein interaction [14]. These approaches indicate a shift from treating proteins as isolated sequences towards representing them as interacting entities in a network or three-dimensional interface. Interaction predictions may provide functional clues, particularly for poorly characterised proteins, but they remain dependent on the quality and coverage of interaction data. The supplied records do not state whether the interaction tasks were binary classification, affinity prediction, interface ranking, or pose selection [VERIFY].

Computational modelling of olfactory receptors [17] further illustrates the value of structure-informed approaches for protein families that are difficult to characterise experimentally. However, the available record does not indicate whether the study predicted receptor function, ligand specificity, structural conformation, or another property [VERIFY].

### Function-specific modelling

The review on machine-learning approaches for metalloproteins is directly relevant to function prediction because metal binding and coordination often form part of a protein’s catalytic or regulatory role [6]. Such models may integrate sequence, structural, and chemical information. The supplied evidence does not identify the specific metalloprotein classes, labels, feature representations, or evaluation procedures, so the scope and comparative performance of the methods cannot be assessed reliably [VERIFY].

Protein language models are also being used to guide directed evolution [3]. This is adjacent to function prediction rather than identical to it: the model may help identify mutations likely to improve a desired phenotype, while the phenotype itself could be enzymatic activity, binding, stability, or another experimentally measured property. The record title indicates that epistatic interactions are considered, suggesting attention to combinations of mutations rather than independent residue effects. The exact experimental design and outcome measures are not available in the supplied evidence [VERIFY].

### Biomedical applications involving proteins

Several records apply machine learning to biomedical prediction problems in which proteins are central but are not necessarily the prediction target. One study predicts mortality using Olink-derived inflammatory protein signatures [9]. Another predicts drug efficacy in lung cancer using protein biomarkers and clinical features [13]. Additional studies use machine learning to investigate disease mechanisms, identify candidate targets, or prioritise therapeutic interventions, including work on renal transplantation injury and LCN2 [5], RORγt inhibitor discovery [7], baicalein and the target proteins PIM1 and CDK2 [8], inflammatory bowel disease therapy [12], and mTOR/p53 co-targeting in acute myeloid leukaemia [20].

These studies demonstrate how machine learning can connect protein measurements or protein targets with clinically relevant outcomes. They should not, however, be interpreted automatically as general protein-function predictors. Their labels may represent mortality, treatment response, disease state, or drug efficacy. Similarly, the use of a protein as a therapeutic target does not by itself constitute a computational prediction of its molecular function. This distinction is particularly important in reviews that combine molecular bioinformatics with clinical machine learning.

The records on type 2 diabetes subtypes [2], diabetic retinopathy and treatment response [19], and predictive biomarkers for PD-1 blockade [16] are even further from direct protein-function prediction. They may involve molecular or multi-omics features, but the supplied evidence does not establish that protein function was modelled as the outcome [VERIFY].

## Methods and Datasets Observed

The available evidence consists primarily of PubMed bibliographic records, titles, author lists, publication years, PubMed identifiers, and links. The records span 2021–2026 and include reviews, methodological studies, protein-modelling applications, and clinical or translational machine-learning analyses. The supplied material does not provide a systematic-search protocol, inclusion criteria, database release versions, feature definitions, model hyperparameters, or full-text extraction table.

Several broad dataset categories can be inferred from the titles:

- protein sequences and sequence-derived representations, particularly in protein language-model and transformer studies [3, 15, 18];
- protein structures or predicted structures in structure-prediction and docking research [1, 10, 11, 17];
- protein–protein interaction data for graph-based interaction prediction [14];
- metalloprotein-related sequence, structural, or biochemical records [6];
- protein biomarkers and inflammatory protein measurements in clinical prediction studies [9, 13];
- multi-omics or clinical datasets in disease and treatment-response modelling [2, 16, 19, 20].

These categories should not be mistaken for confirmed dataset identities. The supplied records do not name the underlying repositories, experimental cohorts, annotation sources, or dataset sizes [VERIFY]. Likewise, no evaluation metrics are explicitly reported in the evidence provided. Depending on the task, relevant metrics might include accuracy, precision, recall, F1 score, area under the receiver-operating-characteristic curve, area under the precision–recall curve, mean squared error, correlation, ranking measures, docking or interface scores, or experimentally measured functional activity. Which of these were actually used in the cited studies cannot be established from the available material [VERIFY].

The same uncertainty applies to validation strategy. It is not possible to determine whether the studies used random splits, sequence-identity-clustered splits, family-level holdouts, temporal validation, external datasets, cross-validation, or prospective experimental testing [VERIFY]. These choices are especially consequential in protein prediction because closely related sequences can occur in both training and test sets, producing performance estimates that may not reflect prediction for genuinely novel proteins.

## Research Gaps

First, the field would benefit from clearer separation of prediction targets. Structure prediction, interaction prediction, ligand screening, disease biomarker prediction, and molecular function annotation are often discussed under the broad heading of AI in protein research, although they involve different labels, datasets, and standards of evidence. A useful comparative review should define whether “function” refers to molecular activity, biological process, cellular localisation, interaction partner, ligand specificity, phenotype, or therapeutic response.

Second, the supplied evidence does not allow a reliable comparison of datasets or metrics. Future studies should report dataset provenance, annotation quality, class balance, sequence redundancy, taxonomic coverage, and the extent of experimental confirmation. Performance should be measured using task-appropriate metrics and evaluated on splits that control for homology and information leakage.

Third, generalisation remains a central concern. Models trained on well-studied proteins and abundant annotations may perform poorly on under-represented protein families, divergent organisms, membrane proteins, disordered proteins, or proteins with context-dependent activity [VERIFY]. The records concerning protein language models, metalloproteins, olfactory receptors, and interaction prediction point to different forms of this challenge, but the supplied evidence does not provide enough detail to quantify it [3, 6, 14, 17, 18].

Fourth, interpretability requires further attention. A model may rank a protein or sequence accurately without revealing which residues, structural motifs, interactions, or biochemical constraints support the prediction. This is particularly important when machine learning is used to nominate therapeutic targets or guide directed evolution [3, 7, 8, 20].

Finally, prospective experimental validation is unevenly documented in the available records. Some titles explicitly mention in vivo validation or experimental discovery [5, 7, 12], whereas others are reviews or computational studies. The field needs evaluations that test predictions prospectively and report not only computational scores but also the proportion of predictions that are experimentally confirmed.

## Limitations

This synthesis is limited by the evidence supplied. It is based on bibliographic records and titles rather than verified extraction from the full texts. Consequently, statements about datasets, model architectures, evaluation metrics, and validation procedures are necessarily provisional. Where these details are required, they are marked [VERIFY].

The literature set is also heterogeneous. Several papers concern clinical prediction, drug discovery, disease mechanisms, or biomarkers rather than direct protein-function annotation [2, 4, 5, 7–9, 12, 13, 16, 19, 20]. Their inclusion is useful for describing the broader use of machine learning in protein-centred biomedical research, but it limits direct comparison with sequence- or structure-based function-prediction methods.

The supplied records do not establish whether the list was generated through a systematic search or whether relevant studies were omitted. Publication and indexing biases may therefore be present. In addition, the inclusion of records dated 2026 means that their status and full-text availability should be checked against the current bibliographic record [VERIFY]. Finally, without detailed methodological information, no conclusions can be drawn about which machine-learning family is most accurate or most suitable for protein function prediction.

## Conclusion

The supplied literature portrays machine learning in protein research as a set of related but distinct activities. Sequence models and protein language models are being used to represent protein knowledge, guide directed evolution, and support sequence-based screening [3, 15, 18]. Structure-based methods address protein folding, docking, receptor modelling, and interaction-related questions [1, 10, 11, 14, 17]. More specialised applications consider metalloproteins and other functionally constrained protein classes [6]. In parallel, protein measurements and protein targets are incorporated into clinical prediction, drug discovery, and disease-mechanism studies [5, 7–9, 12, 13, 16, 19, 20].

The main unresolved issue is not whether machine learning can produce useful predictions, but how reliably those predictions transfer to new proteins, functions, organisms, and experimental settings. The available evidence does not provide enough detail to compare datasets or evaluation metrics, and those omissions prevent a rigorous assessment of reported performance [VERIFY]. Progress will depend on transparent dataset construction, homology-aware validation, explicit definition of functional labels, calibrated uncertainty estimates, and prospective experimental testing. Until these standards are consistently applied, computational performance should be interpreted as evidence of predictive association rather than definitive evidence of protein function.

## References

[1] Chen L, Li Q, Nasif KFA, Xie Y, Deng B, Niu S, Pouriyeh S, Dai Z. *AI-Driven Deep Learning Techniques in Protein Structure Prediction*. 2024. PubMed PMID: 39125995.

[2] Tanabe H, Sato M, Miyake A, Shimajiri Y, Ojima T, Narita A, Saito H, Tanaka K. *Machine learning-based reproducible prediction of type 2 diabetes subtypes*. 2024. PubMed PMID: 39168869.

[3] Tran VQ, Nemeth M, Bartie LJ, Chandrasekaran SS, Fanton A, Moon HC, Hie BL, Konermann S. *Rapid directed evolution guided by protein language models and epistatic interactions*. 2026. PubMed PMID: 41712694.

[4] Schade AE, Perurena N, Yang Y, Rodriguez CL, Krishnan A, Gardner A, Loi P, Xu Y. *AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution*. 2024. PubMed PMID: 39385030.

[5] Wu Z, Yu B, He Q, Huang C. *LCN2 drives ferroptosis-associated ischemia-reperfusion injury after renal transplantation: integrated machine learning and in vivo validation*. 2025. PubMed PMID: 41205031.

[6] Yu Y, Wang R, Teo RD. *Machine Learning Approaches for Metalloproteins*. 2022. PubMed PMID: 35209064.

[7] Yoo H, Han SJ, Lee JE, Cho C, Hong D, Jeong B, Kim S, Jung GY. *Discovery of natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation*. 2026. PubMed PMID: 40915561.

[8] Wang S, Liu C, Ye D, Qi J, Xing Y, Wang J, Fan X, Li X. *Deciphering the mechanism of baicalein in cervical cancer via bioinformatics, machine learning and computational simulations: PIM1 and CDK2 are key target proteins*. 2025. PubMed PMID: 40339869.

[9] Zhang Y, Sun L, Liu H, Shi K, Lu Y, Feng Y, Wang X. *Machine Learning Prediction of 90-Day Mortality in HBV-Related ACLF Using Olink-Derived Inflammatory Protein Signatures*. 2025. PubMed PMID: 41255250.

[10] Schauperl M, Denny RA. *AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges*. 2022. PubMed PMID: 35727311.

[11] Michalik I, Kuder KJ. *Machine Learning Methods in Protein-Protein Docking*. 2024. PubMed PMID: 38987466.

[12] Sahoo D, Swanson L, Sayed IM, Katkar GD, Ibeawuchi SR, Mittal Y, Pranadinata RF, Tindle C. *Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease*. 2021. PubMed PMID: 34253728.

[13] Li J, Chen A, Liu Z, Wei S, Zhang J, Chen J, Shi C. *Machine learning driven prediction of drug efficacy in lung cancer: based on protein biomarkers and clinical features*. 2025. PubMed PMID: 40355026.

[14] Gao Z, Jiang C, Zhang J, Jiang X, Li L, Zhao P, Yang H, Huang Y. *Hierarchical graph learning for protein-protein interaction*. 2023. PubMed PMID: 36841846.

[15] Zhang S, Huo D, Horne RI, Qi Y, Pujalte Ojeda S, Yan A, Vendruscolo M. *Sequence-based virtual screening using transformers*. 2025. PubMed PMID: 40721411.

[16] Arulraj T, Wang H, Deshpande A, Varadhan R, Emens LA, Jaffee EM, Fertig EJ, Santa-Maria CA. *Virtual patient analysis identifies strategies to improve the performance of predictive biomarkers for PD-1 blockade*. 2024. PubMed PMID: 39467131.

[17] Odoemelam CS, Steuber V, Schmuker M. *Computational modelling of olfactory receptors*. 2025. PubMed PMID: 40441539.

[18] Bordin N, Dallago C, Heinzinger M, Kim S, Littmann M, Rauer C, Steinegger M, Rost B. *Novel machine learning approaches revolutionize protein knowledge*. 2023. PubMed PMID: 36504138.

[19] Pang Y, Luo C, Zhang Q, Zhang X, Liao N, Ji Y, Mi L, Gan Y. *Multi-Omics Integration With Machine Learning Identified Early Diabetic Retinopathy, Diabetic Macula Edema and Anti-VEGF Treatment Response*. 2024. PubMed PMID: 39671223.

[20] Li J, Sugimoto E, Yamamoto K, Dai Y, Zhang W, Chang YH, Nakahara J, Yabushita T. *Machine Learning-Based Predictive Modeling Maximizes the Efficacy of mTOR/p53 Co-Targeting Therapy Against AML*. 2025. PubMed PMID: 40785506.