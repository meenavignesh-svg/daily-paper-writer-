The supplied literature suggests that machine learning is being used for protein-function prediction through several related but distinct tasks. The strongest direct evidence comes from Gligorijević et al. (2021), which applies graph convolutional networks to structural representations of proteins, and from the review by Kulmanov and Hoehndorf (2025), which is explicitly concerned with computational prediction of functional annotations. The broader review by Bordin et al. (2023) and the specialist review on metalloproteins by Yu et al. (2022) provide relevant context, although their specific methods and benchmarks cannot be established from the bibliographic records alone.

## How machine-learning methods are being used

### Sequence-based prediction

Protein sequences may be analysed using hand-designed descriptors, conventional supervised-learning models, learned embeddings, or protein language models. Protein language models learn statistical representations from large sequence databases and can then be adapted to predict sequence–function relationships. The record for Tran et al. (2026), for example, indicates that language models are being used to guide directed evolution and model epistatic interactions. This is closely related to function prediction, but it appears to concern experimentally measured properties or improved variants rather than assignment of standardized functional annotations such as Gene Ontology terms [VERIFY].

Transformer-based sequence models are also represented by Zhang et al. (2025). However, that paper concerns sequence-based virtual screening, so it should not be treated as direct evidence for general protein-function annotation without examining the full text. More generally, sequence models are attractive because they can be applied to proteins without experimentally determined structures. Their predictions may nevertheless reflect homology and database composition rather than independently learned biochemical function, particularly when training and test proteins are closely related [VERIFY].

### Structure-based prediction

Structure-based models represent a protein as a spatial object rather than only as a residue string. In graph-based approaches, residues, atoms, or structural regions can serve as nodes, while edges encode spatial proximity, chemical contacts, or other structural relationships. Gligorijević et al. (2021) is the clearest direct example in the supplied evidence: it uses graph convolutional networks for structure-based protein-function prediction.

Predicted structures from AlphaFold and related systems can expand the amount of structural information available for proteins that lack experimentally determined structures. AlphaFold and AlphaFold 3 primarily predict structures or biomolecular interactions, not functional annotations themselves (Jumper et al., 2021; Abramson et al., 2024). Their contribution to function prediction is therefore indirect: predicted structures can be supplied as features to downstream classifiers or used to identify functional pockets, interfaces, or structural similarities. The existence of very broad structural coverage in the AlphaFold Protein Structure Database is potentially important for this purpose, although the quantitative coverage figure in the supplied record should be checked against the source before being cited [VERIFY].

### Interaction- and site-level prediction

Machine learning is also being applied to protein–protein interactions, protein–ligand recognition, docking, binding sites, and metal-associated properties. These tasks can support functional inference because interaction partners and binding sites often provide clues to biological role. Gao et al. (2023) addresses hierarchical graph learning for protein–protein interaction, while Michalik and Kuder (2024) review machine learning in protein–protein docking. Yu et al. (2022) focuses on metalloproteins, potentially including prediction of metal-binding sites, metalloprotein classes, or metal-dependent activity [VERIFY].

These tasks should not be conflated with general protein-function annotation. Predicting whether two proteins interact, whether a ligand binds, or whether a site coordinates a metal is a more specific prediction problem. A model may perform well on one of these tasks without correctly assigning broader biological functions.

## Datasets and labels

The supplied citations do not provide enough information to identify the exact datasets, data splits, or label definitions used by the direct studies. Those details require full-text examination, especially for Gligorijević et al. and Kulmanov and Hoehndorf. Relevant datasets and labels are likely to include:

- protein sequences from curated or large public sequence databases;
- experimentally determined or predicted three-dimensional structures;
- Gene Ontology annotations, including molecular function, biological process, and cellular component terms;
- enzyme or protein-family classifications;
- residue-level labels such as catalytic or ligand-binding sites;
- experimentally measured activities, binding affinities, or stability values in sequence-optimization studies.

The choice of label source is critical. Functional annotations are incomplete, unevenly distributed across species and protein families, and often propagated from homologues. Consequently, an apparent negative label may mean “not yet annotated” rather than “experimentally shown not to have this function.” This creates a distinction between predicting known annotations and discovering genuinely new functions.

Benchmark construction is another major issue. A useful analysis would need to establish whether studies remove highly similar sequences before splitting the data, whether homologous proteins occur in both training and test sets, and whether test proteins come from the same species or protein families as the training data. These details are not available in the supplied records [VERIFY]. The concern is particularly important because random sequence-level splits can produce highly optimistic estimates when near-duplicate or closely related proteins appear on both sides of the split. The literature on leakage and reproducibility in machine-learning science provides relevant methodological caution, although it is not specific to protein-function prediction (Kapoor and Narayanan, 2023).

## Evaluation metrics

The supplied evidence does not establish which metrics were used in the direct protein-function studies. For multi-label functional annotation, appropriate measures may include precision, recall, F1 score, area under the precision–recall curve, and ranking-based measures such as average precision or semantic similarity between predicted and reference Gene Ontology terms [VERIFY]. Because functional labels are hierarchical, evaluation may also need to account for partial correctness: predicting a parent ontology term may be less specific than predicting the correct child term but should not necessarily be treated as completely unrelated [VERIFY].

For residue- or site-level prediction, residue-level precision, recall, F1, area under the receiver-operating-characteristic curve, and spatial overlap measures may be relevant [VERIFY]. For binary interaction or binding prediction, researchers may report accuracy, AUROC, average precision, or Matthews correlation coefficient, but the appropriate metric depends on class balance. For continuous biochemical properties, correlation, mean absolute error, root-mean-square error, and calibration measures may be used [VERIFY].

Accuracy alone is often inadequate. Protein-function datasets can be highly imbalanced, with a small number of common functions and many rare labels. Precision–recall measures, per-class performance, macro-averaged scores, and performance on remote-homology test sets are therefore more informative than a single overall accuracy value [VERIFY]. Reported results should also be compared with simple baselines, such as sequence-similarity transfer or profile-based annotation, rather than only with other neural networks [VERIFY].

## Main limitations

Several limitations recur across this area.

First, **annotation quality limits the target itself**. Functional databases contain missing, noisy, and inconsistently curated annotations. A model trained against those labels may reproduce existing annotation practices rather than reveal function independently.

Second, **data leakage and homology bias can inflate performance**. Closely related proteins may share both sequence features and annotations. Unless data are clustered by sequence similarity or evaluated on remote homologues, a model may be learning family recognition rather than generalizable functional principles.

Third, **class imbalance and long-tailed function distributions** make rare functions difficult to predict. Strong average performance can conceal poor recall for uncommon but biologically important functions [VERIFY].

Fourth, **structure prediction does not guarantee function prediction**. AlphaFold-type systems can provide highly useful structural hypotheses, but functional discrimination may depend on ligand state, conformational dynamics, post-translational modifications, oligomeric context, cellular localization, or transient interactions. These factors are not necessarily captured by a single predicted structure. AlphaFold 3 extends structural modelling to biomolecular interactions, but it still does not by itself resolve the broader problem of assigning biological function.

Fifth, **domain transfer remains limited**. A model trained on well-studied enzymes or particular organisms may not generalize to poorly characterized protein families, membrane proteins, disordered proteins, or proteins with unusual architectures. Metalloprotein-specific models illustrate the value of specialization but also the risk that performance may be restricted to a narrow biochemical domain [VERIFY].

Sixth, **interpretability and experimental validation remain incomplete**. Learned embeddings and deep graph models may produce accurate predictions without identifying the residues or mechanisms responsible. Explainability tools can generate hypotheses, but their biological validity requires independent structural, biochemical, or cellular testing. The supplied evidence includes examples of experimental validation in adjacent drug-discovery and directed-evolution contexts, but it does not establish the extent of experimental validation for the direct function-prediction studies [VERIFY].

Overall, the evidence supports a view of protein-function prediction as an increasingly multimodal problem: sequence models capture evolutionary and biochemical patterns, structural and graph models capture spatial organization, and interaction or omics data provide biological context. The main unresolved question is not simply whether machine-learning models can achieve high benchmark scores, but whether those scores remain reliable for remote homologues, incompletely annotated proteins, rare functions, and experimentally testable new predictions. The supplied bibliography is sufficient to identify these methodological directions, but not to make a defensible comparison of datasets or numerical performance across studies without retrieving and examining the full texts.